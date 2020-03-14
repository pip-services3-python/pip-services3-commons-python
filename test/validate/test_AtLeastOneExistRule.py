# -*- coding: utf-8 -*-
"""
    tests.validate.test_AtLeastOneExistRule
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from .TestObject import TestObject
from pip_services3_commons.validate import Schema
from pip_services3_commons.validate import AtLeastOneExistRule


class TestAtLeastOneExistRule:

    def test_only_one_exist_rule(self):
        obj = TestObject()
        schema = Schema().with_rule(AtLeastOneExistRule("Missing_Property", "String_Property", "Null_Property"))
        results = schema.validate(obj)
        assert 0 == len(results)

        schema = Schema().with_rule(AtLeastOneExistRule("String_Property", "Null_Property", "int_Field"))
        results = schema.validate(obj)
        assert 0 == len(results)

        schema = Schema().with_rule(AtLeastOneExistRule("Missing_Property", "Null_Property"))
        results = schema.validate(obj)
        assert 1 == len(results)
