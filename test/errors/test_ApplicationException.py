# -*- coding: utf-8 -*-
"""
    tests.errors.test_ApplicationException
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services3_commons.errors import ApplicationException


class TestApplicationException:

    app_ex: ApplicationException
    ex: Exception

    category = 'category'
    correlation_id = 'correlation_id'
    code = 'code'
    message = 'message'

    def setup_method(self):
        self.ex = Exception('Cause exception')
        self.app_ex = ApplicationException(self.category, self.correlation_id, self.code, self.message)

    def test_with_cause(self):
        self.app_ex.with_cause(self.ex)

        assert self.ex == self.app_ex.cause

    def test_check_parameters(self):
        assert self.category == self.app_ex.category
        assert self.correlation_id == self.app_ex.correlation_id
        assert self.code == self.app_ex.code
        assert self.message == self.app_ex.message

    def test_with_code(self):
        new_code = 'new_code'
        app_ex = self.app_ex.with_code(new_code)

        assert self.app_ex == app_ex
        assert new_code == app_ex.code

    def test_with_correlation_id(self):
        new_correlation_id = 'new_correlation_id'
        app_ex = self.app_ex.with_correlation_id(new_correlation_id)

        assert self.app_ex == app_ex
        assert new_correlation_id == self.app_ex.correlation_id

    def test_with_status(self):
        new_status = 777
        app_ex = self.app_ex.with_status(new_status)

        assert self.app_ex == app_ex
        assert new_status == self.app_ex.status

    def test_with_details(self):
        key = 'key'
        obj = {}

        app_ex = self.app_ex.with_details(key, obj)
        new_obj = app_ex.details.get_as_object(key)

        assert self.app_ex == app_ex
        assert app_ex.details['key'] == new_obj

    def test_with_stack_trace(self):
        new_trace = 'new_trace'
        app_ex = self.app_ex.with_stack_trace(new_trace)

        assert self.app_ex == app_ex
        assert new_trace == app_ex.stack_trace

    def test_create_error(self):
        error = ApplicationException(None, None, None, 'Test error').with_code('TEST_ERROR')

        assert 'TEST_ERROR' == error.code
        assert 'Test error' == error.message

        error = ApplicationException()

        assert 'UNKNOWN' == error.code
        assert 'Unknown error' == error.message
