# -*- coding: utf-8 -*-
"""
    tests.convert.test_JsonConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_commons.convert import JsonConverter

class TestJsonConverter:

    def test_json_to_map(self):
        # Handling simple objects
        value = '{ "value1":123, "value2":234 }'
        result = JsonConverter.to_nullable_map(value)
        assert 123 == result["value1"]
        assert 234 == result["value2"]

        # Recursive conversion
        value = '{ "value1":123, "value2": { "value1": 111, "value2": 222 } }'
        result = JsonConverter.to_nullable_map(value)
        assert result != None
        assert 123 == result["value1"]
        assert result["value2"] != None
        assert isinstance(result["value2"], dict)

        # Handling arrays
        value = '{ "value1": [{ "value1": 111, "value2": 222 }] }'
        result = JsonConverter.to_nullable_map(value)
        assert result != None
        assert type(result["value1"]) == list
        resultElements = result["value1"]
        resultElement0 = resultElements[0]
        assert resultElement0 != None
        assert 111 == resultElement0["value1"]
        assert 222 == resultElement0["value2"]
        