# -*- coding: utf-8 -*-
from typing import List

from pytest import mark
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.nodes import Item


def pytest_addoption(parser: Parser):  # pragma: no cover
    parser.addoption(
        '--run-slow',
        action='store_true',
        help='Allows tests marked as "slow" to be run'
    )


def pytest_collection_modifyitems(config: Config, items: List[Item]):
    if config.getoption('--run-slow'):  # pragma: no cover
        return

    skip_marker = mark.skip(reason='Requires --run-slow to be executed')

    for item in items:
        for marker in item.iter_markers():
            if marker.name == 'slow':
                item.add_marker(skip_marker)
