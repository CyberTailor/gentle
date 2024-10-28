# SPDX-License-Identifier: WTFPL
# SPDX-FileCopyrightText: 2023-2024 Anna <cyber@sysrq.in>
# No warranty

from pathlib import Path

import pytest

from gentle.generators.shards import ShardsGenerator
from gentle.metadata import MetadataXML
from tests.utils import BaseTestGenerator


class TestShardsGenerator(BaseTestGenerator):
    generator_cls = ShardsGenerator
    generator_data_dir = Path(__file__).parent

    @pytest.mark.parametrize("dirname", ["athena-spec", "exception_page"])
    def test_pkg(self, mxml: MetadataXML, dirname: str):
        self._test_pkg(mxml, dirname)
