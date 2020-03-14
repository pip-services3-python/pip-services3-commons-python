# -*- coding: utf-8 -*-

from pip_services3_commons.data.SortField import SortField
from pip_services3_commons.data.SortParams import SortParams


class TestSortParams:
    def test_create_and_push(self):
        sort = SortParams(SortField('f1'), SortField('f2'))
        sort.append(SortField('f3', False))
        assert len(sort) == 3
