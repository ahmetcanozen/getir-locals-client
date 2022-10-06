# swagger_client.AuthApi

All URIs are relative to *https://locals-integration-api-gateway.artisandev.getirapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthApi.md#login) | **POST** /v1/auth/token | This endpoint is used to get a token for authentication.

# **login**
> ApiResponseAuthenticationResponse login()

This endpoint is used to get a token for authentication.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

try:
    # This endpoint is used to get a token for authentication.
    api_response = api_instance.login()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponseAuthenticationResponse**](ApiResponseAuthenticationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

