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
from telestream_cloud_qc.models.media import Media  # noqa: E501
from telestream_cloud_qc.rest import ApiException

class TestMedia(unittest.TestCase):
    """Media unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Media
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_qc.models.media.Media()  # noqa: E501
        if include_optional :
            return Media(
                audio = [
                    telestream_cloud_qc.models.audio_stream.AudioStream(
                        duration = 78.345, 
                        codec = 'PCM', 
                        channels = 6, 
                        program = '0', 
                        bitrate = 4608000, 
                        sample_rate = 48000, )
                    ], 
                video = [
                    telestream_cloud_qc.models.video_stream.VideoStream(
                        duration = 78.3450116, 
                        codec = 'MPEG-2', 
                        width = 1920, 
                        height = 1080, 
                        bitrate = 56, 
                        fps = 29.97, )
                    ], 
                container = telestream_cloud_qc.models.container.Container(
                    type = 'mp4', 
                    bitrate = 56, )
            )
        else :
            return Media(
        )

    def testMedia(self):
        """Test Media"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
