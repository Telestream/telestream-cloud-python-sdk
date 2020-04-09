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
from telestream_cloud_qc.models.frame_aspect_ratio_test import FrameAspectRatioTest  # noqa: E501
from telestream_cloud_qc.rest import ApiException

class TestFrameAspectRatioTest(unittest.TestCase):
    """FrameAspectRatioTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FrameAspectRatioTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_qc.models.frame_aspect_ratio_test.FrameAspectRatioTest()  # noqa: E501
        if include_optional :
            return FrameAspectRatioTest(
                frame_aspect_ratio_numerator = 56, 
                frame_aspect_ratio_denominator = 56, 
                reject_on_error = True, 
                checked = True
            )
        else :
            return FrameAspectRatioTest(
        )

    def testFrameAspectRatioTest(self):
        """Test FrameAspectRatioTest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()