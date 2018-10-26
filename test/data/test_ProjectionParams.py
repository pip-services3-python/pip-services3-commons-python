# -*- coding: utf-8 -*-
"""
    tests.data.test_ProjectionParams
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_commons.data.ProjectionParams import ProjectionParams

class TestProjectionParams():

    def test_create_projection_params_from_null_object(self):
        params = ProjectionParams.from_value(None)
        assert len(params) == 0

    #todo ["field1", "field2", "field3"] in parameters
    # def test_create_projection_from_object(self):
    #     params = ProjectionParams.from_value("field1", "field2", "field3")
    #     assert len(params) == 3
    #     assert params[0] == "field1"
    #     assert params[1] == "field2"
    #     assert params[2] == "field3"

    # def test_convert_parameters_from_values(self):
    #     params = ProjectionParams.from_values("field1", "field2", "field3")
    #
    #     assert len(params) == 3
    #     assert params[0] == "field1"
    #     assert params[1] == "field2"
    #     assert params[2] == "field3"
