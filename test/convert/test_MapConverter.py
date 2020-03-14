# -*- coding: utf-8 -*-
"""
    tests.convert.test_MapConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services3_commons.convert import MapConverter


class TestClass(object):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2


class TestMapConverter:

    def test_object_to_map(self):
        # Handling nulls
        value = None
        result = MapConverter.to_nullable_map(value)
        assert result == None

        # Handling simple objects
        value = TestClass(123, 234)
        result = MapConverter.to_nullable_map(value)
        assert 123 == result["value1"]
        assert 234 == result["value2"]

        # Handling dictionaries
        # value = {}
        # result = MapConverter.to_nullable_map(value)
        # assert value == result

        # Non-recursive conversion
        # value = TestClass(123, TestClass(111, 222))
        # result = MapConverter.to_map(value, None, False)
        # assert result != None
        # assert 123 == result["value1"]
        # assert result["value2"] != None
        # assert not isinstance(result["value2"], dict)
        # assert instanceof(result["value2"], TestClass)

        # Recursive conversion
        value = TestClass(123, TestClass(111, 222))
        result = MapConverter.to_nullable_map(value)
        assert isinstance(result, dict)
        assert result != None
        assert 123 == result["value1"]
        assert result["value2"] != None
        # assert isinstance(result["value2"], dict)

        # Handling arrays
        value = TestClass([TestClass(111, 222)], None)
        result = MapConverter.to_nullable_map(value)
        assert result != None
        assert type(result["value1"]) == list
        resultElements = result["value1"]
        resultElement0 = resultElements[0]
        assert resultElement0 != None
        # assert 111 == resultElement0["value1"]
        # assert 222 == resultElement0["value2"]
