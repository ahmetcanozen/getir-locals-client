# swagger_client.OrdersApi

All URIs are relative to *https://locals-integration-api-gateway.artisandev.getirapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_options**](OrdersApi.md#cancel_options) | **GET** /v1/orders/{orderId}/cancel-options | This method is used to select cancel reasons according to delivery option.
[**cancel_order**](OrdersApi.md#cancel_order) | **POST** /v1/orders/{orderId}/shop/{shopId}/cancel | This method is used to cancel  the order.
[**cancelled_orders**](OrdersApi.md#cancelled_orders) | **GET** /v1/orders/cancelled | It is used to get the list of cancelled orders by shop.
[**chain_unapproved_orders**](OrdersApi.md#chain_unapproved_orders) | **GET** /v1/orders/unapproved/chain-based | It is used to get the list of unapproved orders by chain.
[**deliver_order**](OrdersApi.md#deliver_order) | **POST** /v1/orders/{orderId}/shop/{shopId}/deliver | This method is used for the delivery of the prepared order.
[**get_active_orders**](OrdersApi.md#get_active_orders) | **GET** /v1/orders/{shopId}/active-orders | It is used to get the list of active orders by shop.
[**get_order**](OrdersApi.md#get_order) | **GET** /v1/orders/{orderId} | This method is used to get details of an order
[**get_order_report**](OrdersApi.md#get_order_report) | **GET** /v1/orders/report | It is used to get the list of orders by shopIds,startDate and endDate.
[**get_shop_delivered_orders**](OrdersApi.md#get_shop_delivered_orders) | **GET** /v1/orders/delivered | It is used to get the list of delivered orders by shopId,startDate and endDate.
[**handover_order**](OrdersApi.md#handover_order) | **POST** /v1/orders/{orderId}/shop/{shopId}/handover | This method is used for the delivery of the prepared order to the courier.
[**prepare_order**](OrdersApi.md#prepare_order) | **POST** /v1/orders/{orderId}/shop/{shopId}/prepare | This method is used to change the prepared order to the prepared status
[**send_invoice**](OrdersApi.md#send_invoice) | **POST** /v1/orders/{orderId}/invoice-link | This method is used to send the order&#x27;s invoice to the client
[**unapproved_orders**](OrdersApi.md#unapproved_orders) | **GET** /v1/orders/unapproved | It is used to get the list of unapproved orders by shop.
[**verify_order**](OrdersApi.md#verify_order) | **POST** /v1/orders/{orderId}/shop/{shopId}/verify | This method is used to approve the incoming order by the shop

# **cancel_options**
> ApiResponseListCancelOptionResponse cancel_options(order_id)

This method is used to select cancel reasons according to delivery option.

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
order_id = 'order_id_example'  # str | 

try:
    # This method is used to select cancel reasons according to delivery option.
    api_response = api_instance.cancel_options(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->cancel_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

[**ApiResponseListCancelOptionResponse**](ApiResponseListCancelOptionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order**
> ApiResponseObject cancel_order(body, order_id, shop_id)

This method is used to cancel  the order.

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
body = client.CancelOrderRequest()  # CancelOrderRequest | 
order_id = 'order_id_example'  # str | 
shop_id = 'shop_id_example'  # str | 

try:
    # This method is used to cancel  the order.
    api_response = api_instance.cancel_order(body, order_id, shop_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancelOrderRequest**](CancelOrderRequest.md)|  | 
 **order_id** | **str**|  | 
 **shop_id** | **str**|  | 

### Return type

[**ApiResponseObject**](ApiResponseObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancelled_orders**
> ApiResponseListOrderResponse cancelled_orders(shop_id, _date=_date)

It is used to get the list of cancelled orders by shop.

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
shop_id = 'shop_id_example'  # str | 
_date = '2013-10-20'  # date | Date format pattern is \"yyyy-MM-dd\". (optional)

try:
    # It is used to get the list of cancelled orders by shop.
    api_response = api_instance.cancelled_orders(shop_id, _date=_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->cancelled_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **str**|  | 
 **_date** | **date**| Date format pattern is \&quot;yyyy-MM-dd\&quot;. | [optional] 

### Return type

[**ApiResponseListOrderResponse**](ApiResponseListOrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chain_unapproved_orders**
> ApiResponseListOrderResponse chain_unapproved_orders(chain_id)

It is used to get the list of unapproved orders by chain.

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
chain_id = 'chain_id_example'  # str | 

try:
    # It is used to get the list of unapproved orders by chain.
    api_response = api_instance.chain_unapproved_orders(chain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->chain_unapproved_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**|  | 

### Return type

[**ApiResponseListOrderResponse**](ApiResponseListOrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deliver_order**
> ApiResponseObject deliver_order(order_id, shop_id)

This method is used for the delivery of the prepared order.

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
order_id = 'order_id_example'  # str | 
shop_id = 'shop_id_example'  # str | 

try:
    # This method is used for the delivery of the prepared order.
    api_response = api_instance.deliver_order(order_id, shop_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->deliver_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 
 **shop_id** | **str**|  | 

### Return type

[**ApiResponseObject**](ApiResponseObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_orders**
> ActiveOrderListResponse get_active_orders(shop_id)

It is used to get the list of active orders by shop.

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
shop_id = 'shop_id_example'  # str | 

try:
    # It is used to get the list of active orders by shop.
    api_response = api_instance.get_active_orders(shop_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_active_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **str**|  | 

### Return type

[**ActiveOrderListResponse**](ActiveOrderListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> ArtisanOrderResponse get_order(order_id)

This method is used to get details of an order

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
order_id = 'order_id_example'  # str | 

try:
    # This method is used to get details of an order
    api_response = api_instance.get_order(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

[**ArtisanOrderResponse**](ArtisanOrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_report**
> ApiResponseOrderReportResponseWrapper get_order_report(start_date, end_date, shop_id, page, page_size)

It is used to get the list of orders by shopIds,startDate and endDate.

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
start_date = '2013-10-20'  # date | Date format pattern is \"yyyy-MM-dd\".
end_date = '2013-10-20'  # date | Date format pattern is \"yyyy-MM-dd\".
shop_id = 'shop_id_example'  # str | 
page = 1.2  # float | 
page_size = 1.2  # float | 

try:
    # It is used to get the list of orders by shopIds,startDate and endDate.
    api_response = api_instance.get_order_report(start_date, end_date, shop_id, page, page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Date format pattern is \&quot;yyyy-MM-dd\&quot;. | 
 **end_date** | **date**| Date format pattern is \&quot;yyyy-MM-dd\&quot;. | 
 **shop_id** | **str**|  | 
 **page** | **float**|  | 
 **page_size** | **float**|  | 

### Return type

[**ApiResponseOrderReportResponseWrapper**](ApiResponseOrderReportResponseWrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shop_delivered_orders**
> FilterOrderResponse get_shop_delivered_orders(start_date, end_date, shop_id, page, page_size)

It is used to get the list of delivered orders by shopId,startDate and endDate.

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
start_date = '2013-10-20'  # date | Date format pattern is \"yyyy-MM-dd'T'HH:mm:ss.SSSXXX\".
end_date = '2013-10-20'  # date | Date format pattern is \"yyyy-MM-dd'T'HH:mm:ss.SSSXXX \".
shop_id = 'shop_id_example'  # str | 
page = 1.2  # float | 
page_size = 1.2  # float | 

try:
    # It is used to get the list of delivered orders by shopId,startDate and endDate.
    api_response = api_instance.get_shop_delivered_orders(start_date, end_date, shop_id, page, page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_shop_delivered_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Date format pattern is \&quot;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss.SSSXXX\&quot;. | 
 **end_date** | **date**| Date format pattern is \&quot;yyyy-MM-dd&#x27;T&#x27;HH:mm:ss.SSSXXX \&quot;. | 
 **shop_id** | **str**|  | 
 **page** | **float**|  | 
 **page_size** | **float**|  | 

### Return type

[**FilterOrderResponse**](FilterOrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handover_order**
> ApiResponseObject handover_order(order_id, shop_id)

This method is used for the delivery of the prepared order to the courier.

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
order_id = 'order_id_example'  # str | 
shop_id = 'shop_id_example'  # str | 

try:
    # This method is used for the delivery of the prepared order to the courier.
    api_response = api_instance.handover_order(order_id, shop_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->handover_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 
 **shop_id** | **str**|  | 

### Return type

[**ApiResponseObject**](ApiResponseObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prepare_order**
> ApiResponseObject prepare_order(order_id, shop_id, body=body)

This method is used to change the prepared order to the prepared status

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
order_id = 'order_id_example'  # str | 
shop_id = 'shop_id_example'  # str | 
body = client.PrepareOrderRequest()  # PrepareOrderRequest |  (optional)

try:
    # This method is used to change the prepared order to the prepared status
    api_response = api_instance.prepare_order(order_id, shop_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->prepare_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 
 **shop_id** | **str**|  | 
 **body** | [**PrepareOrderRequest**](PrepareOrderRequest.md)|  | [optional] 

### Return type

[**ApiResponseObject**](ApiResponseObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_invoice**
> ApiResponseVoid send_invoice(order_id, body=body)

This method is used to send the order's invoice to the client

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
order_id = 'order_id_example'  # str | 
body = client.InvoiceRequest()  # InvoiceRequest |  (optional)

try:
    # This method is used to send the order's invoice to the client
    api_response = api_instance.send_invoice(order_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->send_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 
 **body** | [**InvoiceRequest**](InvoiceRequest.md)|  | [optional] 

### Return type

[**ApiResponseVoid**](ApiResponseVoid.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unapproved_orders**
> ApiResponseListOrderResponse unapproved_orders(shop_id)

It is used to get the list of unapproved orders by shop.

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
shop_id = 'shop_id_example'  # str | 

try:
    # It is used to get the list of unapproved orders by shop.
    api_response = api_instance.unapproved_orders(shop_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->unapproved_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **str**|  | 

### Return type

[**ApiResponseListOrderResponse**](ApiResponseListOrderResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_order**
> ApiResponseObject verify_order(order_id, shop_id)

This method is used to approve the incoming order by the shop

### Example

```python
from __future__ import print_function
import time
import client
from client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = client.OrdersApi(client.ApiClient(configuration))
order_id = 'order_id_example'  # str | 
shop_id = 'shop_id_example'  # str | 

try:
    # This method is used to approve the incoming order by the shop
    api_response = api_instance.verify_order(order_id, shop_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->verify_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 
 **shop_id** | **str**|  | 

### Return type

[**ApiResponseObject**](ApiResponseObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

