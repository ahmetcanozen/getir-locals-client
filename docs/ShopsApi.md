# swagger_client.ShopsApi

All URIs are relative to *https://locals-integration-api-gateway.artisandev.getirapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_shop**](ShopsApi.md#get_shop) | **GET** /v1/shops/{shopId} | It is used to get the shop informations.
[**update_shop_courier_working_status**](ShopsApi.md#update_shop_courier_working_status) | **PUT** /v1/shops/{shopId}/couriers/working-status | It is used to put the shops couiers working status.
[**update_shop_working_hours**](ShopsApi.md#update_shop_working_hours) | **PUT** /v1/shops/{shopId}/working-hours | It is used to put the shops working hours.
[**update_shop_working_status**](ShopsApi.md#update_shop_working_status) | **PUT** /v1/shops/{shopId}/working-status | It is used to put the shops working status.

# **get_shop**
> ApiResponseGetShopResponse get_shop(shop_id)

It is used to get the shop informations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ShopsApi(swagger_client.ApiClient(configuration))
shop_id = 'shop_id_example' # str | 

try:
    # It is used to get the shop informations.
    api_response = api_instance.get_shop(shop_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShopsApi->get_shop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **str**|  | 

### Return type

[**ApiResponseGetShopResponse**](ApiResponseGetShopResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shop_courier_working_status**
> ApiResponseShopCouriersWorkingStatusResponse update_shop_courier_working_status(body, shop_id)

It is used to put the shops couiers working status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ShopsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateShopCouriersStatusRequest() # UpdateShopCouriersStatusRequest | 
shop_id = 'shop_id_example' # str | 

try:
    # It is used to put the shops couiers working status.
    api_response = api_instance.update_shop_courier_working_status(body, shop_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShopsApi->update_shop_courier_working_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateShopCouriersStatusRequest**](UpdateShopCouriersStatusRequest.md)|  | 
 **shop_id** | **str**|  | 

### Return type

[**ApiResponseShopCouriersWorkingStatusResponse**](ApiResponseShopCouriersWorkingStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shop_working_hours**
> ApiResponseShopWorkingHoursResponse update_shop_working_hours(body, shop_id)

It is used to put the shops working hours.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ShopsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateShopWorkingHoursRequest() # UpdateShopWorkingHoursRequest | 
shop_id = 'shop_id_example' # str | 

try:
    # It is used to put the shops working hours.
    api_response = api_instance.update_shop_working_hours(body, shop_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShopsApi->update_shop_working_hours: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateShopWorkingHoursRequest**](UpdateShopWorkingHoursRequest.md)|  | 
 **shop_id** | **str**|  | 

### Return type

[**ApiResponseShopWorkingHoursResponse**](ApiResponseShopWorkingHoursResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shop_working_status**
> ApiResponseObject update_shop_working_status(body, shop_id)

It is used to put the shops working status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ShopsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateShopStatusRequest() # UpdateShopStatusRequest | 
shop_id = 'shop_id_example' # str | 

try:
    # It is used to put the shops working status.
    api_response = api_instance.update_shop_working_status(body, shop_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShopsApi->update_shop_working_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateShopStatusRequest**](UpdateShopStatusRequest.md)|  | 
 **shop_id** | **str**|  | 

### Return type

[**ApiResponseObject**](ApiResponseObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

