---
api:
  file: get-transaction-details-7.json
  operationId: GetTransactionDetails
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: Get Transaction Details API
  description: >-
    The Get Transaction Details API retrieves transaction details between two
    specified dates, providing information such as transaction status, amount,
    and payment method in an array format.
  keywords:
    - get_Transaction_Details API Command
    - get_Transaction_Details command
    - Get Transaction Details API
  robots: index
---
The Get Transaction Details **(get_Transaction_Details)** API works based on input as two dates (initial and final), between which the transaction details are needed. The output consists of the status of the API (success or failure) and all the transaction details in an array format.

<Callout icon="📮" theme="default">
  **Postman Collection**: Access the **Get Transaction Details API Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/g3nukpg/get-transaction-details-api](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/g3nukpg/get-transaction-details-api)
</Callout>

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=get_Transaction_Details&var1=2020-10-20&var2=2020-10-27&hash=0545c11641bd91ed7ba2b5c937480b0f8737962ccc4959994f2aa950ca16212283e7c440a4251ffebd725e0c2c2c03701186eec82c8dd667e75dfbb3cba8e634"
  ```
  ```python
  import requests

  url = "https://test.payu.in/merchant/postservice?form=2"
  headers = {
      "accept": "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
  }
  data = {
      "key": "JP***g",
      "command": "get_Transaction_Details",
      "var1": "2020-10-20",
      "var2": "2020-10-27",
      "hash": "0545c11641bd91ed7ba2b5c937480b0f8737962ccc4959994f2aa950ca16212283e7c440a4251ffebd725e0c2c2c03701186eec82c8dd667e75dfbb3cba8e634"
  }

  response = requests.post(url, headers=headers, data=data)
  print(response.json())
  ```
  ```javascript
  const axios = require('axios');

  const url = "https://test.payu.in/merchant/postservice?form=2";
  const data = new URLSearchParams({
      "key": "JP***g",
      "command": "get_Transaction_Details",
      "var1": "2020-10-20",
      "var2": "2020-10-27",
      "hash": "0545c11641bd91ed7ba2b5c937480b0f8737962ccc4959994f2aa950ca16212283e7c440a4251ffebd725e0c2c2c03701186eec82c8dd667e75dfbb3cba8e634"
  });

  axios.post(url, data, {
      headers: {
          "accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
      }
  })
  .then(response => console.log(response.data));
  ```
  ```java
  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;

  String url = "https://test.payu.in/merchant/postservice?form=2";
  String formData = "key=JP***g&command=get_Transaction_Details&var1=2020-10-20&var2=2020-10-27&hash=0545c11641bd91ed7ba2b5c937480b0f8737962ccc4959994f2aa950ca16212283e7c440a4251ffebd725e0c2c2c03701186eec82c8dd667e75dfbb3cba8e634";

  HttpClient client = HttpClient.newHttpClient();
  HttpRequest request = HttpRequest.newBuilder()
      .uri(URI.create(url))
      .header("accept", "application/json")
      .header("Content-Type", "application/x-www-form-urlencoded")
      .POST(HttpRequest.BodyPublishers.ofString(formData))
      .build();

  HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
  System.out.println(response.body());
  ```
  ```php
  <?php
  $url = "https://test.payu.in/merchant/postservice?form=2";
  $data = array(
      "key" => "JP***g",
      "command" => "get_Transaction_Details",
      "var1" => "2020-10-20",
      "var2" => "2020-10-27",
      "hash" => "0545c11641bd91ed7ba2b5c937480b0f8737962ccc4959994f2aa950ca16212283e7c440a4251ffebd725e0c2c2c03701186eec82c8dd667e75dfbb3cba8e634"
  );

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      "accept: application/json",
      "Content-Type: application/x-www-form-urlencoded"
  ));

  $response = curl_exec($ch);
  curl_close($ch);

  $result = json_decode($response, true);
  print_r($result);
  ?>
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  * Success scenario

  ```json
  {
        "status": 1,
        "msg": "Transaction Fetched Successfully",
        "Transaction_details": [
              {
                    "id": "403993715521889443",
                    "status": "captured",
                    "key": "JPM7Fg",
                    "merchantname": "demo",
                    "txnid": "02fdb4f0a0decd1e4937",
                    "firstname": "Ashish",
                    "lastname": "Kumar",
                    "addedon": "2020-10-26 13:54:52",
                    "bank_name": "Credit Card",
                    "payment_gateway": "AXISPG",
                    "phone": "9876543210",
                    "email": "ashish25@mailinator.com",
                    "transaction_fee": "10.00",
                    "amount": "10.00",
                    "discount": "0.00",
                    "additional_charges": "0.00",
                    "productinfo": "iPhone",
                    "error_code": "E000",
                    "bank_ref_no": "895255",
                    "ibibo_code": "CC",
                    "mode": "CC",
                    "ip": "106.202.49.52",
                    "card_no": "512345XXXXXX2346",
                    "cardtype": "domestic",
                    "offer_key": "",
                    "field2": "171519",
                    "udf1": "",
                    "pg_mid": null,
                    "offer_type": null,
                    "failure_reason": null,
                    "mer_service_fee": "0.00",
                    "mer_service_tax": "0.00"
              },
              {
                    "id": "403993715521889519",
                    "status": "failed",
                    "key": "JPM7Fg",
                    "merchantname": "demo",
                    "txnid": "4c5355da12224188d0ff",
                    "firstname": "K",
                    "lastname": "K",
                    "addedon": "2020-10-26 14:10:02",
                    "bank_name": "Credit Card",
                    "payment_gateway": "AXISPG",
                    "phone": "09599736876",
                    "email": "ashish.25cca@gmail.com",
                    "transaction_fee": "10.00",
                    "amount": "10.00",
                    "discount": "0.00",
                    "additional_charges": "0.00",
                    "productinfo": "i Phone",
                    "error_code": null,
                    "bank_ref_no": "372218",
                    "ibibo_code": "CC",
                    "mode": "CC",
                    "ip": "106.202.49.52",
                    "card_no": "512345XXXXXX2346",
                    "cardtype": "domestic",
                    "offer_key": "",
                    "field2": "603129",
                    "udf1": "",
                    "pg_mid": null,
                    "offer_type": null,
                    "failure_reason": null,
                    "mer_service_fee": null,
                    "mer_service_tax": null
              },
              {
                    "id": "403993715521891555",
                    "status": "captured",
                    "key": "JPM7Fg",
                    "merchantname": "demo",
                    "txnid": "e3bb0408ef94af722de5",
                    "firstname": "Ashish",
                    "lastname": "Kumar",
                    "addedon": "2020-10-26 20:59:41",
                    "bank_name": "Credit Card",
                    "payment_gateway": "AXISPG",
                    "phone": "0987654321",
                    "email": "ashish.kumar@payu.in",
                    "transaction_fee": "10.00",
                    "amount": "10.00",
                    "discount": "0.00",
                    "additional_charges": "0.00",
                    "productinfo": "iPhone",
                    "error_code": "E000",
                    "bank_ref_no": "734154",
                    "ibibo_code": "CC",
                    "mode": "CC",
                    "ip": "106.202.39.89",
                    "card_no": "512345XXXXXX2346",
                    "cardtype": "domestic",
                    "offer_key": "",
                    "field2": "157887",
                    "udf1": "",
                    "pg_mid": null,
                    "offer_type": null,
                    "failure_reason": null,
                    "mer_service_fee": "0.00",
                    "mer_service_tax": "0.00"
              }
        ]
  }
  ```

  * Failure scenario

  If transaction is not found, the response is similar to the following:

  ```json
  {
        "status": 1,
        "msg": "Transaction Fetched Successfully",
        "Transaction_details": []
  }
  ```

  If invalid date is posted, the response is similar to the following:

  ```json
  {
        "status": 0,
        "msg": "Invalid Date Entered. Date format should be yyyy-mm-dd"
  }
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  The **transaction\_details** parameter of the response is in JSON format. The fields in this JSON are described in the following table:

  <Transaction_detailsResponseParameter />

  For more information on the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).
</Accordion>

## Request parameters

<Accordion title="Reference information for request parameters" icon="fa-book">
<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Parameter
      </th>

      <th style={{ textAlign: "left" }}>
        Reference
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        <Glossary>key</Glossary>
      </td>

      <td style={{ textAlign: "left" }}>
        For more information on how to generate the Key and Salt, refer to any of the following:

        * **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)

        * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        var3  <br/>
        `optional`
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter is used pagination to retrieve subsequent pages of results.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        <Glossary>hash</Glossary>
      </td>

      <td style={{ textAlign: "left" }}>
        Hash logic for this API is:  
        `sha512(key|command|var1|salt) sha512`
      </td>
    </tr>
  </tbody>
</Table>
</Accordion>

<Accordion title="Sample values" icon="fa-flask">
  Use the following sample values while trying out the API:

  * `var1`: 2020-10-20
  * `var2`: 2020-10-27
</Accordion>

<br />
