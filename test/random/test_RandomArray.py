# -*- coding: utf-8 -*-
"""
    tests.refer.test_RandomArray
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services3_commons.random import RandomArray


class TestRandomArray:

    def test_pick(self):
        listEmpty = []
        value = RandomArray.pick(listEmpty)
        assert None == value

        array = [1, 2]
        value = RandomArray.pick(array)
        assert value == 1 or value == 2
