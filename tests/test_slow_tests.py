# -*- coding: utf-8 -*-
import time

import pytest


@pytest.mark.slow
def test_slow_test():
    time.sleep(1)


@pytest.mark.slow
def test_very_slow_test():
    time.sleep(10)
