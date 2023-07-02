# SPDX-License-Identifier: WTFPL
# SPDX-FileCopyrightText: 2022 Anna <cyber@sysrq.in>
# No warranty

"""
Metadata XML generator for PHP PEAR and PECL.

The following attributes are supported:

* Upstream maintainer(s)
"""

import logging
import xml.etree.ElementTree as ET
from pathlib import Path

from gentle.generators import AbstractGenerator
from gentle.metadata import MetadataXML
from gentle.metadata.types import MaintainerStatus, Person

logger = logging.getLogger("pear")


class PearGenerator(AbstractGenerator):
    def __init__(self, srcdir: Path):
        self.package_xmls = list(srcdir.glob("package*.xml"))

    def update_metadata_xml(self, mxml: MetadataXML) -> None:
        try:
            xml: ET.ElementTree = ET.parse(self.package_xmls[0])
        except ET.ParseError:
            return

        pear_ns = "http://pear.php.net/dtd/package-2.0"
        ns = {"pear": pear_ns}

        if xml.getroot().tag != f"{{{pear_ns}}}package":
            return

        for lead in xml.findall("pear:lead", ns):
            if (lead_name := lead.find("pear:name", ns)) is None:
                continue

            person = Person("".join(lead_name.itertext()))
            if (lead_email := lead.find("pear:email", ns)) is not None:
                person.email = "".join(lead_email.itertext())

            if (lead_active := lead.find("pear:active", ns)) is not None:
                match "".join(lead_active.itertext()):
                    case "yes":
                        person.status = MaintainerStatus.ACTIVE
                    case "no":
                        person.status = MaintainerStatus.INACTIVE

            logger.info("Found upstream maintainer: %s", person)
            mxml.add_upstream_maintainer(person)

    @property
    def active(self) -> bool:
        return len(self.package_xmls) == 1
