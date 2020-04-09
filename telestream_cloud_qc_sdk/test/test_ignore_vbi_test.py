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
from telestream_cloud_qc.models.ignore_vbi_test import IgnoreVbiTest  # noqa: E501
from telestream_cloud_qc.rest import ApiException

class TestIgnoreVbiTest(unittest.TestCase):
    """IgnoreVbiTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IgnoreVbiTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_qc.models.ignore_vbi_test.IgnoreVbiTest()  # noqa: E501
        if include_optional :
            return IgnoreVbiTest(
                reject_on_error = True, 
                checked = True
            )
        else :
            return IgnoreVbiTest(
        )

    def testIgnoreVbiTest(self):
        """Test IgnoreVbiTest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()