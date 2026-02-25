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

<br />

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

The **transaction_details** parameter of the response is in JSON format for **Get Transaction Details** APIs. The fields in this JSON are described in the following table:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        **JSON Parameter**
      </th>

      <th style={{ textAlign: "left" }}>
        **Description**
      </th>

      <th style={{ textAlign: "left" }}>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        mihpayupid
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter contains a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.
      </td>

      <td style={{ textAlign: "left" }}>
        403993715521937565
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        bank_ref_num
      </td>

      <td style={{ textAlign: "left" }}>
        For each successful transaction – this parameter contains the bank reference number generated by the bank.
      </td>

      <td style={{ textAlign: "left" }}>
        527013524405
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        request_id
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter contains the request ID value posted by the merchant during the transaction request.
      </td>

      <td style={{ textAlign: "left" }}>
        131278422
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        amt
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter contains the original amount which was sent in the transaction request by the merchant.
      </td>

      <td style={{ textAlign: "left" }}>
        10.00
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        mode
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter contains the mode of the transaction such as credit card, debit card, etc. For more information, refer to [Payment Mode Codes](doc:payment-mode-codes).
      </td>

      <td style={{ textAlign: "left" }}>
        CC
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        action
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter contains action taken on the transaction. The action can be any of the following:

        * capture
        * refund
        * cancel
      </td>

      <td style={{ textAlign: "left" }}>
        refund
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        token
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter contains the Token ID (unique token from the merchant) for the refund request.
      </td>

      <td style={{ textAlign: "left" }}>
        20201105secrettokenatur
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        status
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter contains the status and can be any of the following:

        * 0 - If web service call failed.
        * 1 - If web service call succeeded
      </td>

      <td style={{ textAlign: "left" }}>
        1
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        bank_arn
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter contains the Acquirer Reference Number (ARN) is a unique number is generated by the bank. This ARN is generated within 24-72 business hours of initiating the refund.
      </td>

      <td style={{ textAlign: "left" }}>
        74799877002005071918062
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        settlement_id
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter contains the settlement ID of the transaction.
      </td>

      <td style={{ textAlign: "left" }}>
        202110181245
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        amount_settled
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter contains the amount settled to the merchant.
      </td>

      <td style={{ textAlign: "left" }}>
        10.00
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        UTR_no
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter contains the merchant Unique Transaction Reference (UTR) number.
      </td>

      <td style={{ textAlign: "left" }}>
        N223211598444659
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        value_date
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter contains the date when the refund took place or when the amount is reflected in merchant account in this parameter, where the date format is YYYY-MM-DD.
      </td>

      <td style={{ textAlign: "left" }}>
        2020-10-20
      </td>
    </tr>
  </tbody>
</Table>

  To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).
</Accordion>

## Request parameters

<Accordion title="Sample values" icon="fa-flask">
  Use the following sample values while trying out the API:

  * `var1`: 2020-10-20 16:00:00
  * `var2`: 2020-10-26 18:00:00
</Accordion>
