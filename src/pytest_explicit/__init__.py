# -*- coding: utf-8 -*-
from typing import List

from pytest import mark
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.nodes import Item


def pytest_addoption(parser: Parser):  # pragma: no cover
    parser.addini(
        'explicit-only',
        'markers to only be ran when explicitly specified',
        type='linelist',
        default=['slow']
    )


def pytest_load_initial_conftests(early_config: Config, parser: Parser):
    explicit_markers = early_config.getini('explicit-only')

    group = parser.getgroup(
        'explicit',
        'explicitly run marker tests'
    )

    group.addoption(
        '--run-all',
        action='store_true',
        help='Runs all tests that would otherwise require a --run-<marker> flag'
    )

    for marker in explicit_markers:
        group.addoption(
            f'--run-{marker}',
            action='store_true',
            help=f'Allows tests marked as "{marker}" to be run'
        )


def pytest_collection_modifyitems(config: Config, items: List[Item]):
    if config.getoption('--run-all'):
        return

    markers = config.getini('explicit-only')
    for marker in markers:
        mark_skipped(marker, config, items)


def mark_skipped(explicit_marker: str, config: Config, items: List[Item]):
    if config.getoption(f'--run-{explicit_marker}'):  # pragma: no cover
        return

    skip_marker = mark.skip(
        reason=f'Requires --run-{explicit_marker} to be executed'
    )

    for item in items:
        for marker in item.iter_markers():
            if marker.name == explicit_marker:
                item.add_marker(skip_marker)
