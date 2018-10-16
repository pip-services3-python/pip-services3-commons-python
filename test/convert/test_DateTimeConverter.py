# -*- coding: utf-8 -*-
"""
    tests.convert.test_DateTimeConverter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from datetime import *
from pip_services_commons.convert.UTC import UTC

from pip_services_commons.convert import DateTimeConverter

class TestDateTimeConverter:

    def test_to_datetime(self):
        assert DateTimeConverter.to_datetime(None) == None

        date1 = datetime(1975, 4, 8, 0, 0, 0, 0, UTC)
        assert date1 == DateTimeConverter.to_datetime_with_default(None, date1)
        assert date1 == DateTimeConverter.to_datetime(datetime(1975, 4, 8))
        
        date2 = DateTimeConverter.to_utc_datetime(datetime.fromtimestamp(123456))
        assert date2 == DateTimeConverter.to_datetime(123456)
        
        date3 = datetime(1975, 4, 8, 0, 0, 0, 0, UTC)
        assert date3 == DateTimeConverter.to_datetime("1975-04-08T00:00:00Z")
        #assert date1 == DateTimeConverter.to_datetime("1975/04/08")
        
        assert DateTimeConverter.to_datetime("XYZ") == None
