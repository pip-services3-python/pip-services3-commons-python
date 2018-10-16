# -*- coding: utf-8 -*-
"""
    tests.refer.test_TypeMatcher
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest
import datetime

from pip_services_commons.reflect import TypeMatcher

class TestTypeMatcher:

    def test_match_integer(self):
        assert True == TypeMatcher.match_value_by_name("int", 123)
        assert True == TypeMatcher.match_value_by_name("Integer", 123)
        assert True == TypeMatcher.match_value(int, 123)


    # def test_match_long(self):
    #     assert True == TypeMatcher.match_value_by_name("long", 123L)
    #     assert True == TypeMatcher.match_value(long, 123L)

    def test_match_boolean(self):
        assert True == TypeMatcher.match_value_by_name("bool", True)
        assert True == TypeMatcher.match_value_by_name("Boolean", True)
        assert True == TypeMatcher.match_value(bool, True)


    def test_match_float(self):
        assert True == TypeMatcher.match_value_by_name("float", 123.456)
        assert True == TypeMatcher.match_value_by_name("Float", 123.456)
        assert True == TypeMatcher.match_value(float, 123.456)


    def test_match_string(self):
        assert True == TypeMatcher.match_value_by_name("string", "ABC")
        assert True == TypeMatcher.match_value(str, "ABC")


    def test_match_datetime(self):
        now = datetime.datetime.now()
        today = datetime.date.today()
        assert True == TypeMatcher.match_value_by_name("date", now)
        assert True == TypeMatcher.match_value_by_name("date", today)
        assert True == TypeMatcher.match_value_by_name("DateTime", now)
        assert True == TypeMatcher.match_value(datetime.datetime, now)


    def test_match_duration(self):
        assert True == TypeMatcher.match_value_by_name("duration", 123)
        assert True == TypeMatcher.match_value_by_name("TimeSpan", 123)


    def test_match_map(self):
        map = {}
        assert True == TypeMatcher.match_value_by_name("map", map)
        assert True == TypeMatcher.match_value_by_name("dict", map)
        assert True == TypeMatcher.match_value_by_name("Dictionary", map)
        assert True == TypeMatcher.match_value(dict, map)


    def test_match_array(self):
        array = []
        assert True == TypeMatcher.match_value_by_name("list", array)
        assert True == TypeMatcher.match_value_by_name("array", array)
        assert True == TypeMatcher.match_value_by_name("object[]", array)
        assert True == TypeMatcher.match_value(list, array)

        array = ()
        assert True == TypeMatcher.match_value_by_name("list", array)
        assert True == TypeMatcher.match_value_by_name("array", array)
        assert True == TypeMatcher.match_value_by_name("object[]", array)
