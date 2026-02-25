---
title: Get Transaction Info API
excerpt: 'API Command: **get_Transaction_info**'
api:
  file: get-transaction-info-5.json
  operationId: GetTransactionInfo
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: Get Transaction Details API
  description: >-
    The Get Transaction Info API allows users to input a specific time in
    minutes and seconds to retrieve transaction details in the same format as
    the Get Transaction Details API.
  keywords:
    - get_Transaction_info API Command
    - ' Get Transaction Info API'
    - ' get_Transaction_Details API'
    - get transaction information API
    - ' Get Transaction Information API'
  robots: index
---
The **Get Transaction Info** API (get_transaction_info) can take input as the exact time in terms of minutes and seconds the output would be in the same format as [get_Transaction_Details](ref:get_transaction_details_api) API output.

<Callout icon="📮" theme="default">
  **Postman Collection**: Access the **Get Transaction Info API Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/l9pox0u/get-transaction-info-api](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/l9pox0u/get-transaction-info-api)
</Callout>

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'Cookie: PHPSESSID=j601h8g2u1cofo4u5it8v1lk8r; PHPSESSID=6733470eb853c' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'command=get_transaction_info' \
  --data-urlencode 'var1=2024-10-11 12:00:00' \
  --data-urlencode 'var2=2024-10-11 14:00:00'
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
                    "action": "capture",
                    "status": "SUCCESS",
                    "issuing_bank": "HDFC",
                    "transaction_fee": "10.00",
                    "key": "JP***g",
                    "merchantname": "demo",
                    "txnid": "02fdb4f0a0decd1e4937",
                    "firstname": "Ashish",
                    "lastname": "Kumar",
                    "addedon": "2020-10-26 13:54:52",
                    "bank_name": "Credit Card",
                    "payment_gateway": "AXISPG",
                    "phone": "9876543210",
                    "email": "ashish25@mailinator.com",
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
                    "id": "403993715521889530",
                    "action": "capture",
                    "status": "SUCCESS",
                    "issuing_bank": "HDFC",
                    "transaction_fee": "10.00",
                    "key": "JPM7Fg",
                    "merchantname": "demo",
                    "txnid": "7fa6c4783a363b3da573",
                    "firstname": "K",
                    "lastname": "K",
                    "addedon": "2020-10-26 14:12:13",
                    "bank_name": "Credit Card",
                    "payment_gateway": "AXISPG",
                    "phone": "09599736876",
                    "email": "ashish.25cca@gmail.com",
                    "amount": "10.00",
                    "discount": "0.00",
                    "additional_charges": "0.00",
                    "productinfo": "Test",
                    "error_code": "E000",
                    "bank_ref_no": "721522",
                    "ibibo_code": "CC",
                    "mode": "CC",
                    "ip": "106.202.49.52",
                    "card_no": "512345XXXXXX2346",
                    "cardtype": "domestic",
                    "offer_key": "",
                    "field2": "177047",
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
  The **transaction\_details** parameter of the response is in JSON format for **Get Transaction Details** APIs. The fields in this JSON are described in the following table:

<Transaction_detailsResponseParameter />

  To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).
</Accordion>

## Request parameters

<Accordion title="Sample values" icon="fa-flask">
  Use the following sample values while trying out the API:

  * `var1`: 2020-10-20 16:00:00
  * `var2`: 2020-10-26 18:00:00
</Accordion>
