# swagger_client.SupplierApi

All URIs are relative to *https://locals-integration-api-gateway.artisandev.getirapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supplier**](SupplierApi.md#get_supplier) | **GET** /v1/suppliers/supplier | get supplier data.
[**reset_password**](SupplierApi.md#reset_password) | **PUT** /v1/suppliers/password/reset | Shops can reset the password they use via this endpoint and create a new password.

# **get_supplier**
> SupplierDataResponse get_supplier()

get supplier data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SupplierApi(swagger_client.ApiClient(configuration))

try:
    # get supplier data.
    api_response = api_instance.get_supplier()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierApi->get_supplier: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupplierDataResponse**](SupplierDataResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> ApiResponseVoid reset_password(body=body)

Shops can reset the password they use via this endpoint and create a new password.

The password must comply with the following rules. <br> - The new password must be at least 8 characters. - The password must contain one digit. - The password must contain one lowercase letter. - The password must contain one uppercase letter. - The password must contain one special character. - The password must contain no whitespace. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SupplierApi()
body = swagger_client.PasswordResetRequest() # PasswordResetRequest |  (optional)

try:
    # Shops can reset the password they use via this endpoint and create a new password.
    api_response = api_instance.reset_password(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupplierApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordResetRequest**](PasswordResetRequest.md)|  | [optional] 

### Return type

[**ApiResponseVoid**](ApiResponseVoid.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

