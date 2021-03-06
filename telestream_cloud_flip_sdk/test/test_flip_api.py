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

import telestream_cloud_flip
from telestream_cloud_flip.api.flip_api import FlipApi  # noqa: E501
from telestream_cloud_flip.rest import ApiException


class TestFlipApi(unittest.TestCase):
    """FlipApi unit test stubs"""

    def setUp(self):
        self.api = telestream_cloud_flip.api.flip_api.FlipApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_encoding(self):
        """Test case for cancel_encoding

        Cancels an Encoding.  # noqa: E501
        """
        pass

    def test_cancel_video(self):
        """Test case for cancel_video

        Cancel video and all encodings  # noqa: E501
        """
        pass

    def test_copy_profile(self):
        """Test case for copy_profile

        Copies a given Profile  # noqa: E501
        """
        pass

    def test_create_encoding(self):
        """Test case for create_encoding

        Creates an Encoding  # noqa: E501
        """
        pass

    def test_create_factory(self):
        """Test case for create_factory

        Creates a new factory  # noqa: E501
        """
        pass

    def test_create_profile(self):
        """Test case for create_profile

        Creates a Profile  # noqa: E501
        """
        pass

    def test_create_video(self):
        """Test case for create_video

        Creates a Video from a provided source_url.  # noqa: E501
        """
        pass

    def test_delete_encoding(self):
        """Test case for delete_encoding

        Deletes an Encoding from both Telestream Cloud and your storage. Returns an information whether the operation was successful.  # noqa: E501
        """
        pass

    def test_delete_profile(self):
        """Test case for delete_profile

        Deletes a given Profile  # noqa: E501
        """
        pass

    def test_delete_video(self):
        """Test case for delete_video

        Deletes a Video object.  # noqa: E501
        """
        pass

    def test_delete_video_source(self):
        """Test case for delete_video_source

        Delete a video's source file.  # noqa: E501
        """
        pass

    def test_encodings_count(self):
        """Test case for encodings_count

        Returns a number of Encoding objects created using a given factory.  # noqa: E501
        """
        pass

    def test_get_encoding(self):
        """Test case for get_encoding

        Returns an Encoding object.  # noqa: E501
        """
        pass

    def test_get_factory(self):
        """Test case for get_factory

        Returns a Factory object.  # noqa: E501
        """
        pass

    def test_get_profile(self):
        """Test case for get_profile

        Returns a Profile object.  # noqa: E501
        """
        pass

    def test_get_video(self):
        """Test case for get_video

        Returns a Video object.  # noqa: E501
        """
        pass

    def test_list_encodings(self):
        """Test case for list_encodings

        Returns a list of Encoding objects  # noqa: E501
        """
        pass

    def test_list_factories(self):
        """Test case for list_factories

        Returns a collection of Factory objects.  # noqa: E501
        """
        pass

    def test_list_profiles(self):
        """Test case for list_profiles

        Returns a collection of Profile objects.  # noqa: E501
        """
        pass

    def test_list_video_encodings(self):
        """Test case for list_video_encodings

        Returns a list of Encodings that belong to a Video.  # noqa: E501
        """
        pass

    def test_list_videos(self):
        """Test case for list_videos

        Returns a collection of Video objects.  # noqa: E501
        """
        pass

    def test_list_workflows(self):
        """Test case for list_workflows

        Returns a collection of Workflows that belong to a Factory.  # noqa: E501
        """
        pass

    def test_profile_encodings(self):
        """Test case for profile_encodings

        Returns a list of Encodings that belong to a Profile.  # noqa: E501
        """
        pass

    def test_queued_videos(self):
        """Test case for queued_videos

        Returns a collection of Video objects queued for encoding.  # noqa: E501
        """
        pass

    def test_resubmit_video(self):
        """Test case for resubmit_video

        Resubmits a video to encode.  # noqa: E501
        """
        pass

    def test_retry_encoding(self):
        """Test case for retry_encoding

        Retries a failed encoding.  # noqa: E501
        """
        pass

    def test_signed_encoding_url(self):
        """Test case for signed_encoding_url

        Returns a signed url pointing to an Encoding.  # noqa: E501
        """
        pass

    def test_signed_encoding_urls(self):
        """Test case for signed_encoding_urls

        Returns a list of signed urls pointing to an Encoding's outputs.  # noqa: E501
        """
        pass

    def test_signed_video_url(self):
        """Test case for signed_video_url

        Returns a signed url pointing to a Video.  # noqa: E501
        """
        pass

    def test_update_encoding(self):
        """Test case for update_encoding

        Updates an Encoding  # noqa: E501
        """
        pass

    def test_update_factory(self):
        """Test case for update_factory

        Updates a Factory's settings. Returns a Factory object.  # noqa: E501
        """
        pass

    def test_update_profile(self):
        """Test case for update_profile

        Updates a given Profile  # noqa: E501
        """
        pass

    def test_video_metadata(self):
        """Test case for video_metadata

        Returns a Video's metadata  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
