# SPDX-License-Identifier: WTFPL
# SPDX-FileCopyrightText: 2023-2024 Anna <cyber@sysrq.in>
# No warranty

from pathlib import Path

import pytest

from gentle.generators.nuspec import NuspecGenerator
from gentle.metadata import MetadataXML
from tests.utils import BaseTestGenerator


class TestNuspecGenerator(BaseTestGenerator):
    generator_cls = NuspecGenerator
    generator_data_dir = Path(__file__).parent

    @pytest.mark.parametrize("dirname", ["pkg_none", "pkg_multiple"])
    def test_pkg_none(self, mxml: MetadataXML, dirname: str):
        self._test_pkg_none(mxml, dirname)
