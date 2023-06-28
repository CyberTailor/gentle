# SPDX-License-Identifier: WTFPL
# SPDX-FileCopyrightText: 2022-2023 Anna <cyber@sysrq.in>
# No warranty

import logging
import os
import re
from pathlib import Path

import portage
from portage.package.ebuild.doebuild import doebuild

logger = logging.getLogger("pm")


def src_unpack(ebuild: Path, tmpdir: str) -> Path:
    """
    Unpack the sources using Portage.

    :param ebuild: Path to the ebuild file
    :param tmpdir: Temporary directory
    :return: The value of ``${S}``
    """
    ebuild = ebuild.resolve()
    portdir = str(ebuild.parents[2])

    # pylint: disable=protected-access
    if portdir not in portage.portdb.porttrees:
        portdir_overlay = portage.settings.get("PORTDIR_OVERLAY", "")
        os.environ["PORTDIR_OVERLAY"] = (
            portdir_overlay + " " + portage._shell_quote(portdir)
        )

        logger.info("Appending %s to PORTDIR_OVERLAY", portdir)
        portage._reset_legacy_globals()

    tmpsettings: portage.config = portage.portdb.doebuild_settings
    tmpsettings["PORTAGE_USERNAME"] = os.getlogin()
    tmpsettings["PORTAGE_TMPDIR"] = tmpdir
    tmpsettings["DISTDIR"] = tmpdir
    tmpsettings.features._features.clear()  # pylint: disable=protected-access
    tmpsettings.features.add("unprivileged")
    settings = portage.config(clone=tmpsettings)

    status = doebuild(str(ebuild), "unpack",
                      tree="porttree",
                      settings=settings,
                      vartree=portage.db[portage.root]["vartree"])
    if status != 0:
        raise RuntimeError("Unpack failed")

    env = Path(settings.get("T")) / "environment"
    srcdir_re = re.compile(r'^declare -x S="(?P<val>.+)"$')
    with open(env) as file:
        for line in file:
            if (match := srcdir_re.match(line)) is not None:
                return Path(match.group("val"))
    raise RuntimeError("No ${S} value found")
