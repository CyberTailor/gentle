# SPDX-License-Identifier: WTFPL
# SPDX-FileCopyrightText: 2023 Anna <cyber@sysrq.in>
# No warranty

from pathlib import Path

import pytest

from gentle.metadata import MetadataXML
from gentle.pms.portagepm import parse_mxml


@pytest.fixture
def mxml() -> MetadataXML:
    return MetadataXML(Path(__file__).parent / "metadata.xml", parse_mxml)
