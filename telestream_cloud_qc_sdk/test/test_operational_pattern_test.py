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
from telestream_cloud_qc.models.operational_pattern_test import OperationalPatternTest  # noqa: E501
from telestream_cloud_qc.rest import ApiException

class TestOperationalPatternTest(unittest.TestCase):
    """OperationalPatternTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OperationalPatternTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_qc.models.operational_pattern_test.OperationalPatternTest()  # noqa: E501
        if include_optional :
            return OperationalPatternTest(
                op1a = True, 
                op2a = True, 
                op3a = True, 
                op1b = True, 
                op2b = True, 
                op3b = True, 
                op1c = True, 
                op2c = True, 
                op3c = True, 
                external_essence = '0', 
                non_streamable = '0', 
                multi_track = '0', 
                op_atom = True, 
                multi_source = '0', 
                multi_essence = '0', 
                reject_on_error = True, 
                checked = True
            )
        else :
            return OperationalPatternTest(
        )

    def testOperationalPatternTest(self):
        """Test OperationalPatternTest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
