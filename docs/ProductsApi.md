# swagger_client.ProductsApi

All URIs are relative to *https://locals-integration-api-gateway.artisandev.getirapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_batch_request_result**](ProductsApi.md#get_batch_request_result) | **GET** /v1/products/price-and-quantity/batch-requests/{batchRequestId} | Get products update result with using batchRequestId
[**get_chain_products**](ProductsApi.md#get_chain_products) | **GET** /v1/products | Product integration allows you to list information such as stock, price, brand of seller&#x27;s listings.
[**get_chain_productsby_chain_id**](ProductsApi.md#get_chain_productsby_chain_id) | **GET** /v1/chains/{chainId}/products | This method is used to get products by chain id.
[**get_shop_productsby_shop_id**](ProductsApi.md#get_shop_productsby_shop_id) | **GET** /v1/shops/{shopId}/products | This method is used to get products by shop id.
[**update_price_and_quantity**](ProductsApi.md#update_price_and_quantity) | **PUT** /v1/products/price-and-quantity | Update price and quantity of products

# **get_batch_request_result**
> ApiResponsePriceAndQuantityBatchResponse get_batch_request_result(batch_request_id)

Get products update result with using batchRequestId

By using this service, the product's price and quantity are updated in groups of 1000. This method supports single and multiple items in a single request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
batch_request_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get products update result with using batchRequestId
    api_response = api_instance.get_batch_request_result(batch_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_batch_request_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_request_id** | [**str**](.md)|  | 

### Return type

[**ApiResponsePriceAndQuantityBatchResponse**](ApiResponsePriceAndQuantityBatchResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chain_products**
> PageableResponseSupplierProductResponse get_chain_products(page, page_size)

Product integration allows you to list information such as stock, price, brand of seller's listings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
page = 56 # int | 
page_size = 56 # int | 

try:
    # Product integration allows you to list information such as stock, price, brand of seller's listings.
    api_response = api_instance.get_chain_products(page, page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_chain_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | 
 **page_size** | **int**|  | 

### Return type

[**PageableResponseSupplierProductResponse**](PageableResponseSupplierProductResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chain_productsby_chain_id**
> PageableResponseSupplierProductResponse get_chain_productsby_chain_id(chain_id, page, page_size)

This method is used to get products by chain id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
chain_id = 'chain_id_example' # str | 
page = 56 # int | 
page_size = 56 # int | 

try:
    # This method is used to get products by chain id.
    api_response = api_instance.get_chain_productsby_chain_id(chain_id, page, page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_chain_productsby_chain_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**|  | 
 **page** | **int**|  | 
 **page_size** | **int**|  | 

### Return type

[**PageableResponseSupplierProductResponse**](PageableResponseSupplierProductResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shop_productsby_shop_id**
> ApiResponsePageableResponseShopProductsResponse get_shop_productsby_shop_id(shop_id, page, page_size)

This method is used to get products by shop id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
shop_id = 'shop_id_example' # str | 
page = 56 # int | 
page_size = 56 # int | 

try:
    # This method is used to get products by shop id.
    api_response = api_instance.get_shop_productsby_shop_id(shop_id, page, page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_shop_productsby_shop_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **str**|  | 
 **page** | **int**|  | 
 **page_size** | **int**|  | 

### Return type

[**ApiResponsePageableResponseShopProductsResponse**](ApiResponsePageableResponseShopProductsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_price_and_quantity**
> ApiResponseProductBatchTicketResponse update_price_and_quantity(body)

Update price and quantity of products

This method is used for updating price and quantity information of approved products. You can send stock and price information separately on request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProductBatchRequest() # ProductBatchRequest | 

try:
    # Update price and quantity of products
    api_response = api_instance.update_price_and_quantity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->update_price_and_quantity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductBatchRequest**](ProductBatchRequest.md)|  | 

### Return type

[**ApiResponseProductBatchTicketResponse**](ApiResponseProductBatchTicketResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

