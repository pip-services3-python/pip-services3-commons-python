# -*- coding: utf-8 -*-
"""
    tests.config.test_NameResolver
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services_commons.config import ConfigParams
from pip_services_commons.config import NameResolver

class TestNameResolver:

    def test_read_config(self):
        config = ConfigParams.from_tuples("id", "ABC")
        name = NameResolver.resolve(config)
        assert "ABC" == name

        config = ConfigParams.from_tuples("name", "ABC")
        name = NameResolver.resolve(config)
        assert "ABC" == name

    def test_empty_name(self):
        config = ConfigParams.from_tuples()
        name = NameResolver.resolve(config)
        assert None == name
