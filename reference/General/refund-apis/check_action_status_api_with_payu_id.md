---
title: Check Action Status with PayU ID
api:
  file: payu_check_action_status_payuid_oas31.json
  operationId: checkActionStatusWithPayUId
hidden: false
link:
  new_tab: false
metadata:
  title: Check Refund Status API with PayU ID
  description: >-
    The **check_action_status** API returns the status of capture, refund, and
    cancel requests for a specific PayUID. More information on payment states
    can be found in the [Payment States
    Explanations](https://docs.payu.in/reference/payment-state-explanations)
    document.
  keywords:
    - Check Refund Status API with PayU ID
    - check_action_status API Command
    - Using PayU ID to Check Refund Status API
---
The **check_action_status** API has another usage too. For a particular PayUID, it returns any of the following the states:

<Callout icon="📮" theme="default">
  **Postman Collection**: Access the **Check Refund Status with PayU ID API Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/cq5vwr8/check-action-status-payu-id](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/cq5vwr8/check-action-status-payu-id)
</Callout>

<Accordion title="Refund states" icon="fa-hourglass">
  <RefundStates />
</Accordion>

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=check_action_status&var1=403993715521937565&var2=payuid&hash=81bdb5b8e625f254398d744269844fc6b9d87b3782670331c2a6b856f42f315b9898f397df7292cfd33a6153abf4acac58ce3ac671e41999ff81d98ce432f48e"
  ```
```python
import requests

url = "https://test.payu.in/merchant/postservice?form=2"

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'key': 'JP***g',
    'command': 'check_action_status',
    'var1': '403993715521937565',
    'var2': 'payuid',
    'hash': '81bdb5b8e625f254398d744269844fc6b9d87b3782670331c2a6b856f42f315b9898f397df7292cfd33a6153abf4acac58ce3ac671e41999ff81d98ce432f48e'
}

response = requests.post(url, headers=headers, data=data)
print(response.json())
```
```javascript
const axios = require('axios');

const url = 'https://test.payu.in/merchant/postservice?form=2';

const data = new URLSearchParams({
  key: 'JP***g',
  command: 'check_action_status',
  var1: '403993715521937565',
  var2: 'payuid',
  hash: '81bdb5b8e625f254398d744269844fc6b9d87b3782670331c2a6b856f42f315b9898f397df7292cfd33a6153abf4acac58ce3ac671e41999ff81d98ce432f48e'
});

axios.post(url, data, {
  headers: {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
  }
})
.then(response => console.log(response.data))
.catch(error => console.error(error));
```
```java
import java.io.*;
import java.net.http.*;
import java.net.*;

public class PayURequest {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        
        String formData = "key=JP***g&command=check_action_status&var1=403993715521937565&var2=payuid&hash=81bdb5b8e625f254398d744269844fc6b9d87b3782670331c2a6b856f42f315b9898f397df7292cfd33a6153abf4acac58ce3ac671e41999ff81d98ce432f48e";
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://test.payu.in/merchant/postservice?form=2"))
            .header("accept", "application/json")
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```
```php
<?php
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://test.payu.in/merchant/postservice?form=2',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_POST => true,
  CURLOPT_HTTPHEADER => array(
    'accept: application/json',
    'Content-Type: application/x-www-form-urlencoded'
  ),
  CURLOPT_POSTFIELDS => http_build_query(array(
    'key' => 'JP***g',
    'command' => 'check_action_status',
    'var1' => '403993715521937565',
    'var2' => 'payuid',
    'hash' => '81bdb5b8e625f254398d744269844fc6b9d87b3782670331c2a6b856f42f315b9898f397df7292cfd33a6153abf4acac58ce3ac671e41999ff81d98ce432f48e'
  ))
));

$response = curl_exec($curl);
curl_close($curl);
echo $response;
?>
```
```csharp
using System;
using System.Net.Http;
using System.Collections.Generic;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        var client = new HttpClient();
        
        var data = new FormUrlEncodedContent(new[]
        {
            new KeyValuePair<string, string>("key", "JP***g"),
            new KeyValuePair<string, string>("command", "check_action_status"),
            new KeyValuePair<string, string>("var1", "403993715521937565"),
            new KeyValuePair<string, string>("var2", "payuid"),
            new KeyValuePair<string, string>("hash", "81bdb5b8e625f254398d744269844fc6b9d87b3782670331c2a6b856f42f315b9898f397df7292cfd33a6153abf4acac58ce3ac671e41999ff81d98ce432f48e")
        });
        
        client.DefaultRequestHeaders.Add("accept", "application/json");
        
        var response = await client.PostAsync("https://test.payu.in/merchant/postservice?form=2", data);
        var result = await response.Content.ReadAsStringAsync();
        
        Console.WriteLine(result);
    }
}
```

Each example sends a POST request with URL-encoded form data to check the action status ✅
</Accordion>
<Accordion title="Example values" icon="fa-info">

  * `var1` (mihpayid): 403993715521937565
  * `var2`: payuid

  **Failure Scenarios:**

  **If mihpayid is not found:**

  ```json
  {
    "status": 0,
    "msg": "0 out of 1 Transactions Fetched Successfully",
    "transaction_details": {
      "13127842": "No action status found"
    }
  }
  ```

  **If mihpayid is missing:**

  ```json
  {
    "status": 0,
    "msg": "Parameter missing"
  }
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  **On successful processing from PayU, the response is similar to the following:**

  ```json
  {
    "status": 1,
    "msg": "1 out of 1 Transactions Fetched Successfully",
    "transaction_details": {
      "403993715521937565": {
        "131278418": {
          "mihpayid": "403993715521937565",
          "bank_ref_num": "399900",
          "request_id": "131278418",
          "amt": "100.00",
          "mode": "CC",
          "action": "capture",
          "token": "",
          "status": "SUCCESS",
          "bank_arn": null,
          "settlement_id": null,
          "amount_settled": null,
          "UTR_no": null,
          "value_date": null,
          "refund_mode": "-"
        },
        "131278422": {
          "mihpayid": "403993715521937565",
          "bank_ref_num": "527013524405",
          "request_id": "131278422",
          "amt": "10.00",
          "mode": "CC",
          "action": "refund",
          "token": "RefundToken1",
          "status": "success",
          "bank_arn": null,
          "settlement_id": null,
          "amount_settled": null,
          "UTR_no": null,
          "value_date": null,
          "refund_mode": "Back to Source"
        },
        "131278430": {
          "mihpayid": "403993715521937565",
          "bank_ref_num": "527013524405",
          "request_id": "131278430",
          "amt": "10.00",
          "mode": "CC",
          "action": "refund",
          "token": "RefundToken2",
          "status": "success",
          "bank_arn": null,
          "settlement_id": null,
          "amount_settled": null,
          "UTR_no": null,
          "value_date": null,
          "refund_mode": "Back to Source"
        },
        "131278458": {
          "mihpayid": "403993715521937565",
          "bank_ref_num": "527013524405",
          "request_id": "131278458",
          "amt": "10.00",
          "mode": "CC",
          "action": "refund",
          "token": "RefundToken3",
          "status": "success",
          "bank_arn": null,
          "settlement_id": null,
          "amount_settled": null,
          "UTR_no": null,
          "value_date": null,
          "refund_mode": "Back to Source"
        },
        "131278471": {
          "mihpayid": "403993715521937565",
          "bank_ref_num": "527013524405",
          "request_id": "131278471",
          "amt": "10.00",
          "mode": "CC",
          "action": "refund",
          "token": "RefundToken4",
          "status": "success",
          "bank_arn": null,
          "settlement_id": null,
          "amount_settled": null,
          "UTR_no": null,
          "value_date": null,
          "refund_mode": "Back to Source"
        },
        "131278484": {
          "mihpayid": "403993715521937565",
          "bank_ref_num": "527013524405",
          "request_id": "131278484",
          "amt": "10.00",
          "mode": "CC",
          "action": "refund",
          "token": "RefundToken5",
          "status": "success",
          "bank_arn": null,
          "settlement_id": null,
          "amount_settled": null,
          "UTR_no": null,
          "value_date": null,
          "refund_mode": "Back to Source"
        },
        "131278499": {
          "mihpayid": "403993715521937565",
          "bank_ref_num": "527013524405",
          "request_id": "131278499",
          "amt": "10.00",
          "mode": "CC",
          "action": "refund",
          "token": "RefundToken6",
          "status": "success",
          "bank_arn": null,
          "settlement_id": null,
          "amount_settled": null,
          "UTR_no": null,
          "value_date": null,
          "refund_mode": "Back to Source"
        },
        "131278515": {
          "mihpayid": "403993715521937565",
          "bank_ref_num": "527013524405",
          "request_id": "131278515",
          "amt": "10.00",
          "mode": "CC",
          "action": "refund",
          "token": "RefundToken7",
          "status": "success",
          "bank_arn": null,
          "settlement_id": null,
          "amount_settled": null,
          "UTR_no": null,
          "value_date": null,
          "refund_mode": "Back to Source"
        },
        "131287648": {
          "mihpayid": "403993715521937565",
          "bank_ref_num": "527013524405",
          "request_id": "131287648",
          "amt": "10.00",
          "mode": "CC",
          "action": "refund",
          "token": "RefundToken8",
          "status": "success",
          "bank_arn": null,
          "settlement_id": null,
          "amount_settled": null,
          "UTR_no": null,
          "value_date": null,
          "refund_mode": "Back to Source"
        },
        "131295795": {
          "mihpayid": "403993715521937565",
          "bank_ref_num": "527013524405",
          "request_id": "131295795",
          "amt": "10.00",
          "mode": "CC",
          "action": "refund",
          "token": "RefundToken9",
          "status": "success",
          "bank_arn": null,
          "settlement_id": null,
          "amount_settled": null,
          "UTR_no": null,
          "value_date": null,
          "refund_mode": "Back to Source"
        },
        "131297379": {
          "mihpayid": "403993715521937565",
          "bank_ref_num": "527013524405",
          "request_id": "131297379",
          "amt": "10.00",
          "mode": "CC",
          "action": "refund",
          "token": "RefundToken10",
          "status": "success",
          "bank_arn": null,
          "settlement_id": null,
          "amount_settled": null,
          "UTR_no": null,
          "value_date": null,
          "refund_mode": "Back to Source"
        }
      }
    }
  }
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  The **transaction\_details** parameter of the response is in JSON format. For more information, refer to [Additional Info for General APIs](/reference/addl-info-general-apis#response-parameters-check-refund-status-with-request-idpayu-id-or-get-transaction-details).

  | **Parameter**        | **Description**                                                                       |
  | :------------------- | :------------------------------------------------------------------------------------ |
  | status               | Indicates the success (1) or failure (0) of the API call                              |
  | msg                  | Descriptive message about the API response status                                     |
  | transaction\_details | JSON object containing all transaction details for the requested PayUID               |
  | mihpayid             | Unique reference number created for each transaction at PayU's end                    |
  | bank\_ref\_num       | Bank reference number generated by the bank for the transaction                       |
  | request\_id          | The Request ID associated with each action on the transaction                         |
  | amt                  | Amount of the transaction or refund action                                            |
  | mode                 | Payment method used for the transaction (CC for Credit Card, DC for Debit Card, etc.) |
  | action               | Type of action performed (e.g., "capture", "refund")                                  |
  | token                | Security token associated with the transaction                                        |
  | status               | Current status of the action/transaction                                              |
  | bank\_arn            | Bank Acquirer Reference Number (if available)                                         |
  | settlement\_id       | Settlement identifier (if available)                                                  |
  | amount\_settled      | Amount that has been settled (if available)                                           |
  | UTR\_no              | Unique Transaction Reference number (if available)                                    |
  | value\_date          | Value date of the transaction (if available)                                          |
  | refund\_mode         | Mode of refund processing (e.g., "Back to Source")                                    |
</Accordion>

## Request parameters

<Accordion title="Additional Info for Request parameters" icon="fa-book">
  ## Reference Information for Request Parameters

  | Parameter | Reference                                                                                                                                                                                                                                                                                              |
  | :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | key       | For more information on how to generate the Key and Salt, refer to any of the following:<br />• **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)<br />• **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt) |
  | hash      | Hash logic for this API is: sha512(key\\\|command\\\|var1\\\|salt) sha512                                                                                                                                                                                                                              |

  <KeyHashForGeneralParametersDescription />

  **Required Parameters:**

  * `key` - Merchant key provided by PayU
  * `command` - Set to "check\_action\_status" for this API
  * `var1` - The PayUID (mihpayid) for which to retrieve action status
  * `var2` - Should be set to "payuid" to indicate the PayUID lookup mode
  * `hash` - Hash value for security validation

  **Example Values:**
  Use the following sample values while trying out the API:

  * `var1` (mihpayid): 403993715521937565
  * `var2`: payuid

  **Hash Calculation:**
  The hash should be calculated using the sha512 algorithm with the format: sha512(key|command|var1|salt)

  **Important Notes:**

  1. This API usage returns all actions associated with a particular PayUID
  2. Unlike the request\_id lookup, this returns the complete transaction history
  3. The response includes details of capture and all refunds associated with the transaction
  4. Multiple refund actions will be listed with their individual request\_ids and statuses
</Accordion>
