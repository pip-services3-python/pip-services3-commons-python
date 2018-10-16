# -*- coding: utf-8 -*-
"""
    tests.validate.TestObject
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from .TestSubObject import TestSubObject

class TestObject(object):
    _private_field = None
    _private_property = None
    int_field = None
    string_property = None
    null_property = None
    int_array_property = None
    string_list_property = None
    map_property = None
    sub_object_property = None
    sub_array_property = None

    def __init__(self):
        self._private_field = 124
        self._private_property = "XYZ"
        self.int_field = 12345
        self.string_property = "ABC"
        self.null_property = None
        self.int_array_property = [ 1, 2, 3 ]
        self.string_list_property = [ "AAA", "BBB" ]
        self.map_property = { 'Key1': 111, 'Key2': 222 }
        self.sub_object_property = TestSubObject("1")
        self.sub_array_property = [ TestSubObject("2"), TestSubObject("3") ]
