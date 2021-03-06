# coding: utf-8

"""
    Tts API

    Description  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import telestream_cloud_tts
from telestream_cloud_tts.models.result import Result  # noqa: E501
from telestream_cloud_tts.rest import ApiException

class TestResult(unittest.TestCase):
    """Result unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Result
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_tts.models.result.Result()  # noqa: E501
        if include_optional :
            return Result(
                transcript = '0', 
                start_time = 0.11, 
                fragments = [
                    telestream_cloud_tts.models.fragment.Fragment(
                        start_time = 0.11, 
                        variants = [
                            telestream_cloud_tts.models.fragment_variant.FragmentVariant(
                                fragment = 'Lorem', 
                                confidence = 0.9, )
                            ], 
                        end_time = 0.45, )
                    ], 
                end_time = 0.99, 
                confidence = 0.95
            )
        else :
            return Result(
        )

    def testResult(self):
        """Test Result"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
