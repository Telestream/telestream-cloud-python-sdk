# coding: utf-8

"""
    Flip API

    Flip  # noqa: E501

    The version of the OpenAPI document: 3.1
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import telestream_cloud_flip
from telestream_cloud_flip.models.create_video_body import CreateVideoBody  # noqa: E501
from telestream_cloud_flip.rest import ApiException

class TestCreateVideoBody(unittest.TestCase):
    """CreateVideoBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateVideoBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_flip.models.create_video_body.CreateVideoBody()  # noqa: E501
        if include_optional :
            return CreateVideoBody(
                source_url = '0', 
                profiles = '0', 
                payload = '0', 
                pipeline = '0', 
                subtitle_files = [
                    '0'
                    ], 
                extra_files = {
                    'key' : [
                        '0'
                        ]
                    }, 
                extra_variables = {
                    'key' : '0'
                    }, 
                path_format = '0', 
                clip_end = '00:00:06:00@25', 
                clip_length = '00:20:00', 
                clip_offset = '00:00:10', 
                starting_timecode = '0', 
                store_id = '0'
            )
        else :
            return CreateVideoBody(
        )

    def testCreateVideoBody(self):
        """Test CreateVideoBody"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
