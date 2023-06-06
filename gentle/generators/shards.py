# SPDX-License-Identifier: WTFPL
# SPDX-FileCopyrightText: 2022 Anna <cyber@sysrq.in>
# No warranty

"""
Metadata XML generator for Crystal Shards.

The folliwing attributes are supported:

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
    import yaml
    from yaml import CLoader
    _HAS_PYYAML = True
except ModuleNotFoundError:
    _HAS_PYYAML = False

logger = logging.getLogger("shards")


class ShardsGenerator(AbstractGenerator):
    def __init__(self, srcdir: Path):
        self.shard_yml = srcdir / "shard.yml"
        self._active = all([_HAS_PYYAML,
                            self.shard_yml.exists(),
                            self.shard_yml.is_file()])

    def update_metadata_xml(self, mxml: MetadataXML) -> None:
        if not self._active:
            return

        with open(self.shard_yml) as file:
            shard = yaml.load(file, CLoader)

        for author in map(extract_name_email, shard.get("authors", [])):
            if author is None:
                continue
            mxml.add_upstream_maintainer(author)

        if (doc := shard.get("documentation")) is not None:
            logger.info("Found documentation: %s", doc)
            mxml.set_upstream_doc(doc)

        if (homepage := shard.get("homepage")) is not None:
            logger.info("Found homepage: %s", homepage)
            if (remote_id := extract_remote_id(homepage)) is not None:
                mxml.add_upstream_remote_id(remote_id)

        if (repo := shard.get("repository")) is not None:
            logger.info("Found repository: %s", repo)
            print(extract_remote_id(repo))
            if (remote_id := extract_remote_id(repo)) is not None:
                mxml.add_upstream_remote_id(remote_id)

        mxml.dump()
