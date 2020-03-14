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

    def test_create_error(self):
        error = ApplicationException(None, None, None, 'Test error').with_code('TEST_ERROR')

        assert 'TEST_ERROR' == error.code
        assert 'Test error' == error.message

        error = ApplicationException()

        assert 'UNKNOWN' == error.code
        assert 'Unknown error' == error.message
