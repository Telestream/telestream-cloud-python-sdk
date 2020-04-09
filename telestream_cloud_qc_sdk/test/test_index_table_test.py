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
from telestream_cloud_qc.models.index_table_test import IndexTableTest  # noqa: E501
from telestream_cloud_qc.rest import ApiException

class TestIndexTableTest(unittest.TestCase):
    """IndexTableTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IndexTableTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_qc.models.index_table_test.IndexTableTest()  # noqa: E501
        if include_optional :
            return IndexTableTest(
                edit_rate_num = 56, 
                edit_rate_denom = 56, 
                duration_min = 56, 
                duration_max = 56, 
                e_ubyte_count_min = 56, 
                e_ubyte_count_max = 56, 
                e_ubyte_count_constant = True, 
                slice_count = 56, 
                single_index_location = '0', 
                single_essence_location = '0', 
                forward_index_direction = '0', 
                index_entry_array = '0', 
                reject_on_error = True, 
                checked = True
            )
        else :
            return IndexTableTest(
        )

    def testIndexTableTest(self):
        """Test IndexTableTest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()