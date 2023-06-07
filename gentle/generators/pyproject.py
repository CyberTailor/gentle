# SPDX-License-Identifier: WTFPL
# SPDX-FileCopyrightText: 2023 Anna <cyber@sysrq.in>
# No warranty

"""
Metadata XML generator for Python PEP 621 (pyproject.toml).

The following attributes are supported:

* Upstream maintainer(s)
* Upstream documentation
* Remote ID
"""

import logging
from pathlib import Path

from gentle.generators import AbstractGenerator
from gentle.metadata import Person, MetadataXML
from gentle.metadata.utils import extract_remote_id

try:
    try:
        import tomllib
    except ModuleNotFoundError:
        import tomli as tomllib
    _HAS_TOMLLIB = True
except ModuleNotFoundError:
    _HAS_TOMLLIB = False

logger = logging.getLogger("pyproject")


class PyprojectGenerator(AbstractGenerator):
    def __init__(self, srcdir: Path):
        self.pyproject_toml = srcdir / "pyproject.toml"
        self._active = all([_HAS_TOMLLIB,
                            self.pyproject_toml.exists(),
                            self.pyproject_toml.is_file()])

    def update_metadata_xml(self, mxml: MetadataXML) -> None:
        if not self._active:
            return

        with open(self.pyproject_toml, "rb") as file:
            pyproject = tomllib.load(file)

        if (project := pyproject.get("project")) is None:
            return

        for maint in project.get("maintainers", {}):
            person = Person(name=maint.get("name", ""), email=maint.get("email", ""))
            logger.info("Found upstream maintainer: %s", person)
            mxml.add_upstream_maintainer(person)

        for name, value in project.get("urls").items():
            logger.info("Found %s: %s", name, value)
            match name.lower():
                case "bug tracker" | "bugtracker" | "bugs":
                    mxml.set_upstream_bugs_to(value)
                case "changelog" | "changes":
                    mxml.set_upstream_changelog(value)
                case "doc" | "docs" | "documentation":
                    mxml.set_upstream_doc(value)
                case "source" | "repo" | "repository" | "home" | "homepage":
                    if (remote_id := extract_remote_id(value)) is not None:
                        mxml.add_upstream_remote_id(remote_id)
