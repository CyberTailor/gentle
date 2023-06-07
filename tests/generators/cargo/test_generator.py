# SPDX-License-Identifier: WTFPL
# SPDX-FileCopyrightText: 2023 Anna <cyber@sysrq.in>
# No warranty

from pathlib import Path

from gentle.generators.cargo import CargoGenerator
from gentle.metadata import MetadataXML


def test_pkg_none(mxml: MetadataXML):
    gen = CargoGenerator(Path(__file__).parent / "pkg_none")
    assert not gen.active


def test_pkg_empty(mxml: MetadataXML):
    gen = CargoGenerator(Path(__file__).parent / "pkg_empty")
    assert gen.active

    mxml_old = mxml
    gen.update_metadata_xml(mxml)
    assert mxml_old == mxml
