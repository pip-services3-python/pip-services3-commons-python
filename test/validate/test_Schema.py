# -*- coding: utf-8 -*-
"""
    tests.validate.test_Schema
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from .TestSubObject import TestSubObject
from .TestObject import TestObject

from pip_services3_commons.convert import JsonConverter, MapConverter
from pip_services3_commons.convert import RecursiveMapConverter
from pip_services3_commons.validate import Schema
from pip_services3_commons.validate import ObjectSchema
from pip_services3_commons.validate import ArraySchema
from pip_services3_commons.validate import MapSchema


class TestSchema:

    def test_empty_schema(self):
        schema = ObjectSchema()
        results = schema.validate(None)
        assert 0 == len(results)

    def test_required(self):
        schema = Schema().make_required()
        results = schema.validate(None)
        assert 1 == len(results)

    def test_unexpected(self):
        schema = ObjectSchema()
        obj = TestObject()
        results = schema.validate(obj)
        assert 8 == len(results)

    def test_optional_properties(self):
        schema = ObjectSchema() \
            .with_optional_property("int_field", None) \
            .with_optional_property("string_property", None) \
            .with_optional_property("null_property", None) \
            .with_optional_property("int_array_property", None) \
            .with_optional_property("string_list_property", None) \
            .with_optional_property("map_property", None) \
            .with_optional_property("sub_object_property", None) \
            .with_optional_property("sub_array_property", None)

        obj = TestObject()
        results = schema.validate(obj)
        assert 0 == len(results)

    def test_required_properties(self):
        schema = ObjectSchema() \
            .with_required_property("int_field", None) \
            .with_required_property("string_property", None) \
            .with_required_property("null_property", None) \
            .with_required_property("int_array_property", None) \
            .with_required_property("string_list_property", None) \
            .with_required_property("map_property", None) \
            .with_required_property("sub_object_property", None) \
            .with_required_property("sub_array_property", None)

        obj = TestObject()
        obj.sub_array_property = None

        results = schema.validate(obj)
        assert 2 == len(results)

    def test_object_types(self):
        schema = ObjectSchema() \
            .with_required_property("int_field", int) \
            .with_required_property("string_property", str) \
            .with_optional_property("null_property", object) \
            .with_required_property("int_array_property", list) \
            .with_required_property("string_list_property", list) \
            .with_required_property("map_property", dict) \
            .with_required_property("sub_object_property", TestSubObject) \
            .with_required_property("sub_array_property", list)

        obj = TestObject()
        results = schema.validate(obj)
        assert 0 == len(results)

    def test_string_types(self):
        schema = ObjectSchema() \
            .with_required_property("int_field", "Integer") \
            .with_required_property("string_property", "String") \
            .with_optional_property("null_property", "Object") \
            .with_required_property("int_array_property", "int[]") \
            .with_required_property("string_list_property", "list") \
            .with_required_property("map_property", "dict") \
            .with_required_property("sub_object_property", "TestSubObject") \
            .with_required_property("sub_array_property", "TestSubObject[]")

        obj = TestObject()
        results = schema.validate(obj)
        assert 0 == len(results)

    def test_sub_schema(self):
        sub_schema = ObjectSchema() \
            .with_required_property("Id", "String") \
            .with_required_property("FLOAT_FIELD", "float") \
            .with_optional_property("null_property", "Object")

        schema = ObjectSchema() \
            .with_required_property("int_field", "Integer") \
            .with_required_property("string_property", "String") \
            .with_optional_property("null_property", "Object") \
            .with_required_property("int_array_property", "int[]") \
            .with_required_property("string_list_property", "list") \
            .with_required_property("map_property", "map") \
            .with_required_property("sub_object_property", sub_schema) \
            .with_required_property("sub_array_property", "TestSubObject[]")

        obj = TestObject()
        results = schema.validate(obj)
        assert 0 == len(results)

    def test_array_and_map_schema(self):
        sub_schema = ObjectSchema() \
            .with_required_property("Id", "String") \
            .with_required_property("FLOAT_FIELD", "float") \
            .with_optional_property("null_property", "Object")

        schema = ObjectSchema() \
            .with_required_property("int_field", "Integer") \
            .with_required_property("string_property", "String") \
            .with_optional_property("null_property", "Object") \
            .with_required_property("int_array_property", ArraySchema("Integer")) \
            .with_required_property("string_list_property", ArraySchema("String")) \
            .with_required_property("map_property", MapSchema("String", "Integer")) \
            .with_required_property("sub_object_property", sub_schema) \
            .with_required_property("sub_array_property", ArraySchema(sub_schema))

        obj = TestObject()
        results = schema.validate(obj)
        assert 0 == len(results)
