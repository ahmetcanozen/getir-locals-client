# swagger_client.HealthApi

All URIs are relative to *https://locals-integration-api-gateway.artisandev.getirapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](HealthApi.md#health_check) | **GET** /health | Health Check for Getir Infrastructure

# **health_check**
> HealthResponse health_check()

Health Check for Getir Infrastructure

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HealthApi()

try:
    # Health Check for Getir Infrastructure
    api_response = api_instance.health_check()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->health_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

