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
from telestream_cloud_qc.models.summary import Summary  # noqa: E501
from telestream_cloud_qc.rest import ApiException

class TestSummary(unittest.TestCase):
    """Summary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Summary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_qc.models.summary.Summary()  # noqa: E501
        if include_optional :
            return Summary(
                num_sync_events = 56, 
                avsync_analysis = '0', 
                avsync_inference = '0', 
                confidence = 1.337, 
                skew = 56, 
                total_length = 1.337
            )
        else :
            return Summary(
        )

    def testSummary(self):
        """Test Summary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
