# coding: utf-8

"""
    Getir-Locals Integration Swagger Documentation

    This documentation is created by Getir Developers for Getir-Locals Integration.For this integration, you need to take CLIENT NAME and CLIENT SECRET keys from Getir-dev team and use these keys for authentication. You also need to use access token provided after successful login to be able to use all other endpoints  You can view information about the active order through /orders/unapproved endpoints. The status of the order is managed via verify, prepare, handover and cancel endpoints. Details on order management are as follows:  For orders to be made by the Getir courier, the flow is as follows:  Supplier confirms order --verify<br />Supplier prepares order --prepare (1-2 minutes must pass before delivery)<br />Supplier hands over the order to Getir courier --handover<br />For Getir delivery, transactions are made by the Getir courier after handover.  A valid reason will be requested from the supplier to cancel an order. Valid reasons may vary depending on the instant status of the order. For this reason, before canceling an order, you have to get instant valid order cancellation reasons from /orders/{orderId}/cancel-options endpoint.   # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import client
from client.models.product_request import ProductRequest  # noqa: E501
from client.rest import ApiException


class TestProductRequest(unittest.TestCase):
    """ProductRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductRequest(self):
        """Test ProductRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = client.models.product_request.ProductRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
