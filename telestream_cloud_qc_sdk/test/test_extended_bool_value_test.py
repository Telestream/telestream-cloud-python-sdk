# coding: utf-8

"""
    Qc API

    Qc API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import telestream_cloud_qc
from telestream_cloud_qc.models.extended_bool_value_test import ExtendedBoolValueTest  # noqa: E501
from telestream_cloud_qc.rest import ApiException

class TestExtendedBoolValueTest(unittest.TestCase):
    """ExtendedBoolValueTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtendedBoolValueTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_qc.models.extended_bool_value_test.ExtendedBoolValueTest()  # noqa: E501
        if include_optional :
            return ExtendedBoolValueTest(
                value = 'true', 
                reject_on_error = True, 
                checked = True
            )
        else :
            return ExtendedBoolValueTest(
        )

    def testExtendedBoolValueTest(self):
        """Test ExtendedBoolValueTest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()