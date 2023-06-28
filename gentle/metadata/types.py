# SPDX-License-Identifier: WTFPL
# SPDX-FileCopyrightText: 2023 Anna <cyber@sysrq.in>
# No warranty

""" Types for working with Gentoo package metadata """

import xml.etree.ElementTree as ET
from dataclasses import dataclass, field


@dataclass
class Person:
    """ Representation of a person"""

    name: str = field(default="", compare=False)
    email: str = ""

    def to_xml(self, attrib: dict | None = None) -> ET.Element:
        """
        :param attrib: attributes for the ``<maintainer>`` tag
        :return: :file:`metadata.xml` respresentation of a person
        """
        result = ET.Element("maintainer", attrib=attrib or {})
        if self.name:
            name_elem = ET.SubElement(result, "name")
            name_elem.text = self.name
        if self.email:
            email_elem = ET.SubElement(result, "email")
            email_elem.text = self.email

        return result


@dataclass
class RemoteID:
    """ Representation of a remote ID """

    attr: str
    value: str

    def to_xml(self) -> ET.Element:
        """
        :return: :file:`metadata.xml` respresentation of a remote id
        """
        remote_elem = ET.Element("remote-id", type=self.attr)
        remote_elem.text = self.value
        return remote_elem


@dataclass
class Upstream:
    """ Representation of upstream metadata """

    maintainers: list[Person] = field(default_factory=list)
    changelog: str | None = None
    doc: str | None = None
    bugs_to: str | None = None
    remote_ids: list[RemoteID] = field(default_factory=list)
