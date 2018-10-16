# -*- coding: utf-8 -*-
"""
    tests.refer.test_RandomDateTime
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest
import datetime
import pytz

from pip_services_commons.random import RandomDateTime

class TestRandomDateTime:

    def test_next_date(self):
        date = RandomDateTime.next_date(2015, 2016)
        assert date.year == 2015 or date.year == 2016  

        date = RandomDateTime.next_date()
        assert date.year >= datetime.datetime.now().year - 10 \
            and date.year <= datetime.datetime.now().year

    def total_secs(days):
        return days * 24 * 3600000

    # def test_update_datetime(self):
    #     old_date = datetime.datetime(2016, 10, 10, 0, 0, 0, 0, pytz.utc)
    #
    #     # date = RandomDateTime.update_datetime(old_date)
    #     # delta = old_date - date
    #     # assert date.total_seconds() >= old_date.total_seconds() - self.total_secs(-10) or \
    #     #        date.total_seconds() >= old_date.total_seconds() - self.total_secs(10)
    #
    #     date = RandomDateTime.update_datetime(old_date)
    #     delta = old_date - date
    #     assert delta.total_seconds() >= self.total_secs(-10) or delta.total_seconds() >= self.total_secs(10)
    #
    #     date = RandomDateTime.update_datetime(old_date, 3)
    #     delta = old_date - date
    #     assert delta.total_seconds() >= self.total_secs(-3) or delta.total_seconds() >= self.total_secs(3)
    #
    #     date = RandomDateTime.update_datetime(old_date, -3)
    #     assert date.year == old_date.year
