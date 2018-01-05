# coding: utf-8

"""
    Qc API

    QC API

    OpenAPI spec version: 1.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from telestream_cloud_qc.apis.qc_api import QcApi


class TestQcApi(unittest.TestCase):
    """ QcApi unit test stubs """

    def setUp(self):
        self.api = telestream_cloud_qc.apis.qc_api.QcApi()

    def tearDown(self):
        pass

    def test_cancel_job(self):
        """
        Test case for cancel_job

        
        """
        pass

    def test_create_job(self):
        """
        Test case for create_job

        Create a new job
        """
        pass

    def test_create_project(self):
        """
        Test case for create_project

        Create a new project
        """
        pass

    def test_get_job(self):
        """
        Test case for get_job

        Get QC job
        """
        pass

    def test_get_project(self):
        """
        Test case for get_project

        Get project by Id
        """
        pass

    def test_list_jobs(self):
        """
        Test case for list_jobs

        Get jobs form projects
        """
        pass

    def test_list_projects(self):
        """
        Test case for list_projects

        List all projects for an account
        """
        pass

    def test_modify_project(self):
        """
        Test case for modify_project

        Modify project
        """
        pass

    def test_proxy(self):
        """
        Test case for proxy

        
        """
        pass

    def test_remove_job(self):
        """
        Test case for remove_job

        
        """
        pass

    def test_remove_project(self):
        """
        Test case for remove_project

        
        """
        pass

    def test_signed_urls(self):
        """
        Test case for signed_urls

        
        """
        pass

    def test_upload_video(self):
        """
        Test case for upload_video

        Creates an upload session
        """
        pass


if __name__ == '__main__':
    unittest.main()