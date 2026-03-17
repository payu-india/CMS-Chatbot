---
title: Get All Refunds from Transaction ID
excerpt: >-
  Retrieve comprehensive refund history for a specific transaction.


  This API returns detailed information about all refund attempts including:

  - All refund requests (successful and failed)

  - Refund amounts and dates

  - Request IDs for each refund attempt

  - Settlement status and details

  - Remaining refundable amount

  - Transaction summary information


  **Transaction ID:** Use the transaction ID from your original payment
  transaction.
api:
  file: payu_get_all_refunds_txnid_oas31.json
  operationId: getAllRefundsFromTransactionId
hidden: false
link:
  new_tab: false
metadata:
  title: Get All Refunds for a Transaction IDs API
  description: >-
    The document describes the **Get All Refunds for a Transaction ID** API
    command, which retrieves the status of all refund requests for a specific
    Transaction ID, providing details such as request ID, payment gateway used,
    refund status, and creation date.
  keywords:
    - getAllRefundsFromTxnIds API Command
    - Get All Refunds from Transaction IDs
    - Get All Refunds API
---
The **Get All Refunds for a Transaction ID** API (getAllRefundsFromTxnIds) command is used to retrieve the status of all the refund requests fired for a particular Transaction ID. The output of this API provides the request ID, and the PG used the status of a refund request and the creation of refund date information. It returns any of the following the states:

<Callout icon="📮" theme="default">
  **Postman Collection**: Access the **Get All Refunds from Transaction ID API Postman Collection** from the following location:

  https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/h40i4so/get-all-refunds-from-transaction-ids-api
</Callout>
<Accordion title="Refund States" icon="fa-code">
<RefundStates />
</Accordion>
<GENERALAPIsEnvironment />
<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2
  -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&command=getAllRefundsFromTxnIds&var1=db97dd56eff7296e5061&hash=69543c08018121cc882d2f8b1761567367c1806becde3db7f54ab552362677cc08d8dfa4b9411e234e4876e6aba80c05a32e75ed499aff458c7f6027bf4ef2a8"
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
    'command': 'getAllRefundsFromTxnIds',
    'var1': 'db97dd56eff7296e5061',
    'hash': '69543c08018121cc882d2f8b1761567367c1806becde3db7f54ab552362677cc08d8dfa4b9411e234e4876e6aba80c05a32e75ed499aff458c7f6027bf4ef2a8'
}

response = requests.post(url, headers=headers, data=data)
print(response.json())
```
```javascript
const axios = require('axios');

const url = 'https://test.payu.in/merchant/postservice?form=2';

const data = new URLSearchParams({
  key: 'JP***g',
  command: 'getAllRefundsFromTxnIds',
  var1: 'db97dd56eff7296e5061',
  hash: '69543c08018121cc882d2f8b1761567367c1806becde3db7f54ab552362677cc08d8dfa4b9411e234e4876e6aba80c05a32e75ed499aff458c7f6027bf4ef2a8'
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
        
        String formData = "key=JP***g&command=getAllRefundsFromTxnIds&var1=db97dd56eff7296e5061&hash=69543c08018121cc882d2f8b1761567367c1806becde3db7f54ab552362677cc08d8dfa4b9411e234e4876e6aba80c05a32e75ed499aff458c7f6027bf4ef2a8";
        
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
    'command' => 'getAllRefundsFromTxnIds',
    'var1' => 'db97dd56eff7296e5061',
    'hash' => '69543c08018121cc882d2f8b1761567367c1806becde3db7f54ab552362677cc08d8dfa4b9411e234e4876e6aba80c05a32e75ed499aff458c7f6027bf4ef2a8'
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
            new KeyValuePair<string, string>("command", "getAllRefundsFromTxnIds"),
            new KeyValuePair<string, string>("var1", "db97dd56eff7296e5061"),
            new KeyValuePair<string, string>("hash", "69543c08018121cc882d2f8b1761567367c1806becde3db7f54ab552362677cc08d8dfa4b9411e234e4876e6aba80c05a32e75ed499aff458c7f6027bf4ef2a8")
        });
        
        client.DefaultRequestHeaders.Add("accept", "application/json");
        
        var response = await client.PostAsync("https://test.payu.in/merchant/postservice?form=2", data);
        var result = await response.Content.ReadAsStringAsync();
        
        Console.WriteLine(result);
    }
}
```

Each example sends a POST request with URL-encoded form data to retrieve all refunds from transaction IDs 💳
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">

  **Success Scenario**

  On successful processing from PayU, the response is similar to the following:

  ```json
  {
        "status": 1,
        "msg": "Refunds fetched successfully.",
        "Refund Details": {
              "403993715521937565": [
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278422",
                          "RefundToken": "RefundToken1",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 01:23:19",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 01:24:04"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278430",
                          "RefundToken": "RefundToken2",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 01:29:13",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 01:30:08"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278458",
                          "RefundToken": "RefundToken3",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 01:47:36",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 01:49:04"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278471",
                          "RefundToken": "RefundToken4",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 01:53:28",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 01:55:05"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278484",
                          "RefundToken": "RefundToken5",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 01:58:32",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 02:00:09"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278499",
                          "RefundToken": "RefundToken6",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 02:05:42",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 02:07:04"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131278515",
                          "RefundToken": "RefundToken7",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-05 02:15:11",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2020-11-05 02:16:03"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131287648",
                          "RefundToken": "RefundToken8",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-06 19:21:32",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2021-01-28 10:25:17"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131295795",
                          "RefundToken": "RefundToken9",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-09 18:59:45",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2021-02-10 01:01:14"
                    },
                    {
                          "PayuID": "403993715521937565",
                          "RequestID": "131297379",
                          "RefundToken": "RefundToken10",
                          "PaymentGateway": "AXISPG",
                          "Amount": "10.00",
                          "Status": "success",
                          "RefundCreationDate": "2020-11-10 09:39:33",
                          "bank_ref_no": "527013524405",
                          "bank_arn": null,
                          "success_at": "2021-02-01 15:50:25"
                    }
              ]
        }
  }
  ```

  **Failure scenario**

  If no refunds found for the transaction:

  ```
  {
        "status": 1,
        "msg": "No Refunds Found for the transaction."
  }
  ```
</Accordion>

<Accordion title="Response parameters description" icon="fa-table">

  <Table>
    <thead>
      <tr>
        <th>
          **Parameter**
        </th>

        <th>
          **Description**
        </th>

        <th>
          **Example**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          status
        </td>

        <td>
          The status of the response can be any of the following:

          * **1:** Success
          * **2:** Failure
        </td>

        <td>
          1
        </td>
      </tr>

      <tr>
        <td>
          msg
        </td>

        <td>
          The description of the response whether the card details were stored successfully or not.
        </td>

        <td>
          Refunds fetched successfully.
        </td>
      </tr>

      <tr>
        <td>
          Refund Details
        </td>

        <td>
          The details are sent by PayU in JSON format for the successful response. For more information, refer to [Additional Info for General APIs](ref:addl-info-general-apis#description-of-the-refund-details-json-fields).
        </td>

        <td />
      </tr>
    </tbody>
  </Table>
</Accordion>

## Request parameters

<Accordion title="Reference information for request parameters" icon="fa-flask">

  <KeyHashForGeneralParametersDescription />
</Accordion>

**Example values**

Use the following sample values while trying out the API:

* `var1` (txnid): db97dd56eff7296e5061
