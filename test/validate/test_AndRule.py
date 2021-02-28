# -*- coding: utf-8 -*-
from pip_services3_commons.validate import Schema, AndRule, AtLeastOneExistRule

from validate.StubObject import StubObject


class TestAndRule:

    def test_and_rule(self):
        obj = StubObject()

        schema = Schema().with_rule(AndRule(AtLeastOneExistRule("missing_property", "string_property", "null_property"),
                                            AtLeastOneExistRule("string_property", "null_property", "int_field")))

        results = schema.validate(obj)
        assert len(results) == 0

        schema = Schema().with_rule(AndRule(AtLeastOneExistRule("missing_property", "string_property", "null_property"),
                                            AtLeastOneExistRule("missing_property", "null_property")))
        results = schema.validate(obj)
        assert len(results) == 1
