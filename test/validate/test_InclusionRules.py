# -*- coding: utf-8 -*-
"""
    tests.validate.test_InclusionRules
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services3_commons.validate import Schema
from pip_services3_commons.validate import IncludedRule
from pip_services3_commons.validate import ExcludedRule


class TestInclusionRules:

    def test_included_rule(self):
        schema = Schema().with_rule(IncludedRule("AAA", "BBB", "CCC", None))
        results = schema.validate("AAA")
        assert 0 == len(results)

        results = schema.validate("ABC")
        assert 1 == len(results)

    def test_excluded_rule(self):
        schema = Schema().with_rule(ExcludedRule("AAA", "BBB", "CCC", None))
        results = schema.validate("AAA")
        assert 1 == len(results)

        results = schema.validate("ABC")
        assert 0 == len(results)
