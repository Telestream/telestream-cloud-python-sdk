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
from telestream_cloud_qc.models.audio_ppm_level_test import AudioPpmLevelTest  # noqa: E501
from telestream_cloud_qc.rest import ApiException

class TestAudioPpmLevelTest(unittest.TestCase):
    """AudioPpmLevelTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AudioPpmLevelTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_qc.models.audio_ppm_level_test.AudioPpmLevelTest()  # noqa: E501
        if include_optional :
            return AudioPpmLevelTest(
                min_ppm_level_enabled = True, 
                min_ppm_level = 1.337, 
                max_ppm_level_enabled = True, 
                max_ppm_level = 1.337, 
                mode = 'PpmModeM3', 
                channels = telestream_cloud_qc.models.channels.channels(
                    channel = [
                        True
                        ], ), 
                reject_on_error = True, 
                do_correction = True, 
                checked = True
            )
        else :
            return AudioPpmLevelTest(
        )

    def testAudioPpmLevelTest(self):
        """Test AudioPpmLevelTest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()