# coding: utf-8

"""
    Notifications API

    Notifications  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import telestream_cloud_notifications
from telestream_cloud_notifications.models.topic import Topic  # noqa: E501
from telestream_cloud_notifications.rest import ApiException

class TestTopic(unittest.TestCase):
    """Topic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Topic
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_notifications.models.topic.Topic()  # noqa: E501
        if include_optional :
            return Topic(
                account = '0', 
                service = '0', 
                event = '0', 
                project = '0', 
                factory = '0', 
                workflow = '0'
            )
        else :
            return Topic(
                service = '0',
                event = '0',
        )

    def testTopic(self):
        """Test Topic"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
