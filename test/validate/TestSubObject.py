# -*- coding: utf-8 -*-
"""
    tests.validate.TestSubObject
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

class TestSubObject(object):
    _id = None
    _null_property = None

    def __init__(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    id = property(get_id, set_id)

    float_field = 432.

    def get_null_property(self):
        return self._null_property

    def set_null_property(self, value):
        self._null_property = value

    null_property = property(get_null_property, set_null_property)

