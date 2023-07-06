# SPDX-License-Identifier: WTFPL
# SPDX-FileCopyrightText: 2023 Anna <cyber@sysrq.in>
# No warranty

from pathlib import Path

import pytest

from gentle.metadata import MetadataXML
from gentle.pms.portagepm import parse_mxml


def pytest_addoption(parser):
    parser.addoption("--net", action="store_true",
                     help="run tests that connect to network")


def pytest_configure(config):
    config.addinivalue_line("markers", "net: mark test as using network")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--net"):
        # --net given in cli: do not skip network tests
        return
    skip_net = pytest.mark.skip(reason="need --net option to run")
    for item in items:
        if "net" in item.keywords:
            item.add_marker(skip_net)


@pytest.fixture
def mxml() -> MetadataXML:
    return MetadataXML(Path(__file__).parent / "metadata.xml", parse_mxml)
