# coding: utf-8

"""
    MELI Markeplace SDK

    This is a the codebase to generate a SDK for Open Platform Marketplace  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import meli
from meli.models.attributes_values import AttributesValues  # noqa: E501
from meli.rest import ApiException

class TestAttributesValues(unittest.TestCase):
    """AttributesValues unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AttributesValues
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = meli.models.attributes_values.AttributesValues()  # noqa: E501
        if include_optional :
            return AttributesValues(
                id = '0', 
                name = '8 GB', 
                struct = meli.models.attributes_value_struct.Attributes_value_struct(
                    number = 8, 
                    unit = 'GB', )
            )
        else :
            return AttributesValues(
        )

    def testAttributesValues(self):
        """Test AttributesValues"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
