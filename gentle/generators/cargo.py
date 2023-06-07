# SPDX-License-Identifier: WTFPL
# SPDX-FileCopyrightText: 2022 Anna <cyber@sysrq.in>
# No warranty

"""
Metadata XML generator for Cargo.

The following attributes are supported:

* Upstream maintainer(s)
* Upstream documentation
* Remote ID
"""

import logging
from pathlib import Path

from gentle.generators import AbstractGenerator
from gentle.metadata import MetadataXML
from gentle.metadata.utils import extract_name_email, extract_remote_id

try:
    try:
        import tomllib
    except ModuleNotFoundError:
        import tomli as tomllib
    _HAS_TOMLLIB = True
except ModuleNotFoundError:
    _HAS_TOMLLIB = False

logger = logging.getLogger("cargo")


class CargoGenerator(AbstractGenerator):
    def __init__(self, srcdir: Path):
        self.srcdir = srcdir
        self.cargo_toml = srcdir / "Cargo.toml"
        self._active = all([_HAS_TOMLLIB,
                            self.cargo_toml.exists(),
                            self.cargo_toml.is_file()])

    def process_cargo_toml(self, cargo: dict, mxml: MetadataXML) -> None:
        if (package := cargo.get("package")) is None:
            return

        for author in map(extract_name_email, package.get("authors", [])):
            if author is None:
                continue
            mxml.add_upstream_maintainer(author)

        if (doc := package.get("documentation")) is not None:
            logger.info("Found documentation: %s", doc)
            mxml.set_upstream_doc(doc)

        if (homepage := package.get("homepage")) is not None:
            logger.info("Found homepage: %s", homepage)
            if (remote_id := extract_remote_id(homepage)) is not None:
                mxml.add_upstream_remote_id(remote_id)

        if (repo := package.get("repository")) is not None:
            logger.info("Found repository: %s", repo)
            if (remote_id := extract_remote_id(repo)) is not None:
                mxml.add_upstream_remote_id(remote_id)

    def update_metadata_xml(self, mxml: MetadataXML) -> None:
        if not self._active:
            return

        with open(self.cargo_toml, "rb") as file:
            cargo = tomllib.load(file)

        if "package" not in cargo and "workspace" in cargo:
            workspace = cargo["workspace"]
            members = set(workspace.get(members, []))
            members -= frozenset(workspace.get("exclude", []))
            for member in members:
                member_toml = self.srcdir / member / "Cargo.toml"
                with open(member_toml, "rb") as file:
                    self.process_cargo_toml(tomllib.load(file), mxml)
        else:
            self.process_cargo_toml(cargo, mxml)
