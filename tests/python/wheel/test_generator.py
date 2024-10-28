# SPDX-License-Identifier: WTFPL
# SPDX-FileCopyrightText: 2023-2024 Anna <cyber@sysrq.in>
# No warranty

from copy import deepcopy
from pathlib import Path

import build.env
import pytest

from gentle.generators.python.wheel import WheelGenerator
from gentle.metadata import MetadataXML

from tests.utils import compare_mxml


def test_pkg_none(mxml: MetadataXML):
    gen = WheelGenerator(Path(__file__).parent / "pkg_none")
    assert not gen.active


@pytest.mark.parametrize("dirname", ["pyproject.toml", "setup.cfg", "setup.py"])
def test_pkg_empty(monkeypatch: pytest.MonkeyPatch, mxml: MetadataXML, dirname: str):
    # subprocess calls can make this test fail
    def blackhole(*args, **kwargs):
        pass
    monkeypatch.setattr(build.env, "run_subprocess", blackhole)

    gen = WheelGenerator(Path(__file__).parent / "pkg_empty" / dirname)
    assert gen.active

    mxml_old = deepcopy(mxml)
    gen.update_metadata_xml(mxml)
    assert compare_mxml(mxml_old, mxml) == ""


@pytest.mark.net
@pytest.mark.parametrize("dirname", ["rich", "commonmark"])
def test_pkg(mxml: MetadataXML, dirname: str):
    gen = WheelGenerator(Path(__file__).parent / dirname)
    assert gen.active

    gen.update_metadata_xml(mxml)
    with open(Path(__file__).parent / dirname / "metadata.xml") as file:
        assert mxml.dumps() == file.read().rstrip()

    mxml_prev = deepcopy(mxml)
    gen.update_metadata_xml(mxml)
    assert compare_mxml(mxml_prev, mxml) == ""
