---
title: Split by Percentage - PayU Hosted Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Split by Percentage During Transaction - PayU Hosted Checkout
excerpt: >-
  Split a payment by percentage among child merchants at transaction time using
  the `_payment` API with PayU Hosted Checkout.
deprecated: false
hidden: false
metadata:
  title: Split by Percentage During Transaction - PayU Hosted Checkout | PayU
  description: >-
    API reference for percentage-based split settlements during a PayU Hosted
    Checkout `_payment` request. Includes splitRequest JSON, hash calculation,
    and callback response parameters.
  keywords:
    - split settlements
    - split by percentage
    - payu hosted checkout
    - _payment API
    - split during transaction
    - splitRequest
  robots: index
---

Use this API to collect a payment on PayU Hosted Checkout and split the amount by percentage among child merchants at transaction time. Post the `splitRequest` parameter with `_payment`; PayU redirects the customer to the hosted payment page and returns split details in the success or failure callback.

<Callout icon="📘" theme="info">
  **Note**: Specify two decimal places for each split percentage, and ensure the sum of all split percentages equals **100**.
</Callout>

<br />

<Callout icon="👍" theme="okay">
  Experience the end-to-end **PayU Hosted Checkout **> **Split** flow and instantly generate the complete code for seamless, zero-coding integration into your website. 



  <HTMLBlock>{`
                  <style>
                  .tooltip-btn {
                      position: relative;
                      background-color: #4CAF50;
                      color: white;
                      padding: 10px 20px;
                      border: none;
                      border-radius: 5px;
                      cursor: pointer;
                      font-weight: bold; /* Added this line */
                  }
                  .tooltip-btn:hover::after {
                      content: attr(data-tooltip);
                      position: absolute;
                      bottom: 125%;
                      left: 50%;
                      transform: translateX(-50%);
                      background-color: #333;
                      color: white;
                      padding: 5px 10px;
                      border-radius: 4px;
                      white-space: nowrap;
                      font-size: 12px;
                      z-index: 1;
                  }
                  </style>

                  <button onclick="window.open('https://payu.in/integrationlab/split', '_blank')" 
                          class="tooltip-btn" 
                          data-tooltip="Click here to see the PayU Hosted Checkout > Split end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                      Experience the flow and get the code
                  </button>
  `}</HTMLBlock>
</Callout>

<br />

<br />

<Callout icon="📮" theme="default">
  **Postman Collection**: Access the **Split by Percentage Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/x39xtf7/absolute-split-during-transaction](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/x39xtf7/absolute-split-during-transaction)
</Callout>

## Environment

| Environment | URL                                                                |
| ----------- | ------------------------------------------------------------------ |
| Test        | [https://test.payu.in/_payment](https://test.payu.in/_payment)     |
| Production  | [https://secure.payu.in/_payment](https://secure.payu.in/_payment) |

**HTTP Method**: POST

## Request Headers

| Header       | Description                                  | Example                           |
| ------------ | -------------------------------------------- | --------------------------------- |
| Content-Type | `mandatory` Content type of the request body | application/x-www-form-urlencoded |

## Request Parameters

| Parameter                | Description                                                                                                                                                                      | Example                                                                                    |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| key `mandatory`          | `String` Merchant key provided by PayU during onboarding.                                                                                                                        | a4vGC2                                                                                     |
| txnid `mandatory`        | `String` Unique transaction ID generated by the merchant for the order.                                                                                                          | TXN_SPL_1779178418_441                                                                     |
| amount `mandatory`       | `String` Total payment amount for the transaction.                                                                                                                               | 2000                                                                                       |
| productinfo `mandatory`  | `String` Brief description of the product or order.                                                                                                                              | iPhone                                                                                     |
| firstname `mandatory`    | `String` Customer first name.                                                                                                                                                    | John                                                                                       |
| lastname `optional`      | `String` Customer last name.                                                                                                                                                     | Doe                                                                                        |
| email `mandatory`        | `String` Customer email address.                                                                                                                                                 | [pragram@gmail.com](mailto:pragram@gmail.com)                                              |
| phone `mandatory`        | `String` Customer phone number.                                                                                                                                                  | 9876543210                                                                                 |
| splitRequest `mandatory` | `JSON` Split payment details in JSON format. URL-encode this value when posting as form data. For field descriptions, see [splitRequest JSON fields](#splitrequest-json-fields). | `{"type":"percentage","splitInfo":{...}}`                                                  |
| surl `mandatory`         | `String` Success URL. PayU redirects here after a successful payment.                                                                                                            | [https://payu.in/integrationlab/callback.php](https://payu.in/integrationlab/callback.php) |
| furl `mandatory`         | `String` Failure URL. PayU redirects here after a failed payment.                                                                                                                | [https://payu.in/integrationlab/callback.php](https://payu.in/integrationlab/callback.php) |
| hash `mandatory`         | `String` SHA-512 hash calculated on your server. When `splitRequest` is included, append it at the end of the hash string. See [Hash calculation](#hash-calculation).            | 13bdef80fee845daddcca3b56a99ab1d...                                                        |
| address1 `optional`      | `String` First line of the billing address. Recommended for fraud detection.                                                                                                     |                                                                                            |
| address2 `optional`      | `String` Second line of the billing address.                                                                                                                                     |                                                                                            |
| city `optional`          | `String` Customer city.                                                                                                                                                          |                                                                                            |
| state `optional`         | `String` Customer state.                                                                                                                                                         |                                                                                            |
| country `optional`       | `String` Customer country.                                                                                                                                                       |                                                                                            |
| zipcode `optional`       | `String` Billing address zip code. Character limit: 20.                                                                                                                          |                                                                                            |
| udf1–udf5 `optional`     | `String` User-defined fields to store merchant-specific transaction data.                                                                                                        |                                                                                            |

### splitRequest JSON fields

| Field                                                   | Description                                                                                                                                  | Example                                         |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| type `mandatory`                                        | `String` Split type. Use **percentage** for percentage-based splits. The percentage for each child is set in `aggregatorSubAmt`.             | percentage                                      |
| splitInfo `mandatory`                                   | `JSON` Map of child merchant keys to split details. Keys are child merchant keys (for example, `gYoEaY`, `5rgA73`).                          | See [Sample splitRequest](#sample-splitrequest) |
| splitInfo.\<merchantKey>.aggregatorSubTxnId `mandatory` | `String` Unique sub-transaction ID for the child merchant, generated by the merchant.                                                        | child_1779180636589_7309                        |
| splitInfo.\<merchantKey>.aggregatorSubAmt `mandatory`   | `String` Percentage of the total payable amount allocated to this child. Use two decimal places. Sum across all children must equal **100**. | 50                                              |
| splitInfo.\<merchantKey>.aggregatorCharges `optional`   | `String` Percentage allocated to aggregator charges. Only parent aggregators can include this field.                                         | 0.00                                            |

### Sample splitRequest

```json
{
  "type": "percentage",
  "splitInfo": {
    "gYoEaY": {
      "aggregatorSubTxnId": "child_1779180636589_7309",
      "aggregatorSubAmt": "50",
      "aggregatorCharges": "0.00"
    },
    "5rgA73": {
      "aggregatorSubTxnId": "child_1779180636590_5791",
      "aggregatorSubAmt": "50",
      "aggregatorCharges": "0.00"
    }
  }
}
```

### Hash calculation

When you send `splitRequest` at payment time, include it at the end of the hash string:

```plaintext
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|splitRequest)
```

<Callout icon="📘" theme="info">
  **Note**: Use the pipe (`|`) character between parameters. The `splitRequest` value in the hash string must match the exact JSON string posted in the request (no extra spaces).
</Callout>

For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).

## Sample Request

<Accordion title="Sample Request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=a4vGC2" \
    -d "txnid=TXN_SPL_1779178418_441" \
    -d "amount=2000" \
    -d "productinfo=iPhone" \
    -d "firstname=John" \
    -d "lastname=Doe" \
    -d "email=pragram@gmail.com" \
    -d "phone=9876543210" \
    --data-urlencode 'splitRequest={"type":"percentage","splitInfo":{"gYoEaY":{"aggregatorSubTxnId":"child_1779180636589_7309","aggregatorSubAmt":"50","aggregatorCharges":"0.00"},"5rgA73":{"aggregatorSubTxnId":"child_1779180636590_5791","aggregatorSubAmt":"50","aggregatorCharges":"0.00"}}}' \
    -d "surl=https://payu.in/integrationlab/callback.php" \
    -d "furl=https://payu.in/integrationlab/callback.php" \
    -d "hash=13bdef80fee845daddcca3b56a99ab1dde21b486c78d14a4c91c7911728e43de27ae56bdfb02f2dbce3a6911090a82817c3134b068310969ee4e7568c1023d51"
  ```
  ```python
  import requests

  url = "https://test.payu.in/_payment"

  split_request = (
      '{"type":"percentage","splitInfo":{'
      '"gYoEaY":{"aggregatorSubTxnId":"child_1779180636589_7309",'
      '"aggregatorSubAmt":"50","aggregatorCharges":"0.00"},'
      '"5rgA73":{"aggregatorSubTxnId":"child_1779180636590_5791",'
      '"aggregatorSubAmt":"50","aggregatorCharges":"0.00"}}}'
  )

  data = {
      "key": "a4vGC2",
      "txnid": "TXN_SPL_1779178418_441",
      "amount": "2000",
      "productinfo": "iPhone",
      "firstname": "John",
      "lastname": "Doe",
      "email": "pragram@gmail.com",
      "phone": "9876543210",
      "splitRequest": split_request,
      "surl": "https://payu.in/integrationlab/callback.php",
      "furl": "https://payu.in/integrationlab/callback.php",
      "hash": "13bdef80fee845daddcca3b56a99ab1dde21b486c78d14a4c91c7911728e43de27ae56bdfb02f2dbce3a6911090a82817c3134b068310969ee4e7568c1023d51",
  }

  response = requests.post(
      url,
      headers={"Content-Type": "application/x-www-form-urlencoded"},
      data=data,
  )
  print(response.text)
  ```
  ```javascript
  const url = "https://test.payu.in/_payment";

  const splitRequest = JSON.stringify({
    type: "percentage",
    splitInfo: {
      gYoEaY: {
        aggregatorSubTxnId: "child_1779180636589_7309",
        aggregatorSubAmt: "50",
        aggregatorCharges: "0.00",
      },
      "5rgA73": {
        aggregatorSubTxnId: "child_1779180636590_5791",
        aggregatorSubAmt: "50",
        aggregatorCharges: "0.00",
      },
    },
  });

  const formData = new URLSearchParams({
    key: "a4vGC2",
    txnid: "TXN_SPL_1779178418_441",
    amount: "2000",
    productinfo: "iPhone",
    firstname: "John",
    lastname: "Doe",
    email: "pragram@gmail.com",
    phone: "9876543210",
    splitRequest,
    surl: "https://payu.in/integrationlab/callback.php",
    furl: "https://payu.in/integrationlab/callback.php",
    hash: "13bdef80fee845daddcca3b56a99ab1dde21b486c78d14a4c91c7911728e43de27ae56bdfb02f2dbce3a6911090a82817c3134b068310969ee4e7568c1023d51",
  });

  fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: formData,
  })
    .then((response) => response.text())
    .then((data) => console.log(data));
  ```
  ```php
  <?php
  $url = "https://test.payu.in/_payment";

  $splitRequest = json_encode([
      "type" => "percentage",
      "splitInfo" => [
          "gYoEaY" => [
              "aggregatorSubTxnId" => "child_1779180636589_7309",
              "aggregatorSubAmt" => "50",
              "aggregatorCharges" => "0.00",
          ],
          "5rgA73" => [
              "aggregatorSubTxnId" => "child_1779180636590_5791",
              "aggregatorSubAmt" => "50",
              "aggregatorCharges" => "0.00",
          ],
      ],
  ]);

  $postData = [
      "key" => "a4vGC2",
      "txnid" => "TXN_SPL_1779178418_441",
      "amount" => "2000",
      "productinfo" => "iPhone",
      "firstname" => "John",
      "lastname" => "Doe",
      "email" => "pragram@gmail.com",
      "phone" => "9876543210",
      "splitRequest" => $splitRequest,
      "surl" => "https://payu.in/integrationlab/callback.php",
      "furl" => "https://payu.in/integrationlab/callback.php",
      "hash" => "13bdef80fee845daddcca3b56a99ab1dde21b486c78d14a4c91c7911728e43de27ae56bdfb02f2dbce3a6911090a82817c3134b068310969ee4e7568c1023d51",
  ];

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
  curl_setopt($ch, CURLOPT_HTTPHEADER, [
      "Content-Type: application/x-www-form-urlencoded",
  ]);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

  $response = curl_exec($ch);
  curl_close($ch);

  echo $response;
  ?>
  ```
</Accordion>

## Sample Response

<Accordion title="Sample Response" icon="fa-code">
  When the request is valid, PayU returns the hosted checkout page (HTML). After the customer completes payment, PayU redirects to `surl` or `furl` and posts transaction details including `splitInfo`.

  ### Success callback (TDR model)

  ```plaintext
  mihpayid=41**45678912383977
  &mode=CC
  &status=success
  &unmappedstatus=captured
  &key=a4vGC2
  &txnid=TXN_SPL_1779178418_441
  &amount=2000.00
  &productinfo=iPhone
  &firstname=John
  &lastname=Doe
  &email=pragram@gmail.com
  &phone=9876543210
  &hash=6e700275583072c0361bac771a4166a4be5334112d59e40181c5668895c477a047c7be250068186fd26ca72928d7e168f92bb96003a7fffbf4933bb818f4c48a
  &splitInfo={"splitStatus":"success","splitSegments":[{"merchantKey":"gYoEaY","amount":1000,"subvention_amount":0,"txnId":"child_1779180636589_7309"},{"merchantKey":"5rgA73","amount":1000,"subvention_amount":0,"txnId":"child_1779180636590_5791"}]}
  ```

  ### Parsed splitInfo

  ```json
  {
    "splitStatus": "success",
    "splitSegments": [
      {
        "merchantKey": "gYoEaY",
        "amount": 1000,
        "subvention_amount": 0,
        "txnId": "child_1779180636589_7309"
      },
      {
        "merchantKey": "5rgA73",
        "amount": 1000,
        "subvention_amount": 0,
        "txnId": "child_1779180636590_5791"
      }
    ]
  }
  ```

  ### Reverse hash (payment response)

  Validate the callback using:

  ```plaintext
  sha512(SALT|status|splitInfo||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```
</Accordion>

## Response Parameters

| Parameter      | Type        | Description                                                                                                                                    |
| -------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| mihpayid       | String      | PayU transaction reference ID.                                                                                                                 |
| mode           | String      | Payment mode (for example, CC, DC, NB, UPI).                                                                                                   |
| status         | String      | Transaction status: `success`, `failure`, or `pending`.                                                                                        |
| unmappedstatus | String      | Internal PayU status (for example, captured, failed, pending).                                                                                 |
| key            | String      | Merchant key.                                                                                                                                  |
| txnid          | String      | Merchant transaction ID from the request.                                                                                                      |
| amount         | String      | Transaction amount.                                                                                                                            |
| productinfo    | String      | Product description from the request.                                                                                                          |
| firstname      | String      | Customer first name from the request.                                                                                                          |
| lastname       | String      | Customer last name from the request.                                                                                                           |
| email          | String      | Customer email from the request.                                                                                                               |
| phone          | String      | Customer phone from the request.                                                                                                               |
| hash           | String      | Response hash for verification.                                                                                                                |
| splitInfo      | JSON String | Split settlement outcome. Contains `splitStatus` and `splitSegments` with `merchantKey`, `amount`, `subvention_amount`, and `txnId` per child. |
| error          | String      | Error code for failed transactions.                                                                                                            |
| error_Message  | String      | Error description. Refer to [Error Codes](ref:error-codes).                                                                                    |

## Error Codes

| Code                   | Message                            | Cause                                        | Resolution                                                                |
| ---------------------- | ---------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------- |
| E000                   | No Error                           | Transaction completed successfully.          | None.                                                                     |
| Invalid hash           | Hash validation failed             | Hash string or `splitRequest` JSON mismatch. | Regenerate hash with the exact `splitRequest` JSON posted in the request. |
| Split validation error | Split percentages do not total 100 | Sum of `aggregatorSubAmt` values is not 100. | Adjust percentages so the total equals 100.00.                            |

<Callout icon="📘" theme="info">
  For Split Settlements enablement or child-merchant configuration, contact your **PayU Key Account Manager (KAM)**.
</Callout>

## Related APIs

* [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) — Base `_payment` API for PayU Hosted Checkout.
* [Split by Percentage During Transaction](ref:split-by-percentage-during-transaction) — Same split type for server-to-server (card) `_payment` flows.
* [Absolute Split During Transaction](ref:absolute-split-during-transaction) — Split by fixed amount during transaction.
* [Split During Transaction using _payment](ref:split-during-transaction-using-_payment) — Overview of split-during-transaction parameters.
