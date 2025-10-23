---
title: Verify Payment API
excerpt: ''
api:
  file: general-34.json
  operationId: verifypayment
deprecated: false
hidden: false
metadata:
  title: Verify Payment API
  description: >-
    The Verify Payment API provides transaction status information, including
    details such as payment source, card type, and offer availed at cart or
    transaction level. It also includes response parameters like status,
    message, and transaction details in JSON format.
  keywords:
    - verify_payment
    - verify_payment command
    - Verify Payment API
    - Check Transaction Status API
  robots: index
next:
  description: ''
---
The Verify Payment (**verify_payment**) API gives you the status of the transaction. PayU recommends using this API to reconcile with PayU's database after you receive the response, where var1 is your transaction ID.

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'command=verify_payment' \
  --data-urlencode 'var1=IhfgcZnXR4o4nB' \
  --data-urlencode 'hash=a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  * If credit card payment is made, the response is similar to the following:

  ```plaintext
  {
      "status": 1,
      "msg": "1 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
          "1733900931584": {
              "mihpayid": "21820644083",
              "request_id": null,
              "bank_ref_num": null,
              "amt": "1.00",
              "transaction_amount": "1.00",
              "txnid": "1733900931584",
              "additional_charges": "0.00",
              "productinfo": "Macbook Pro",
              "firstname": "Abc",
              "bankcode": "MAST",
              "udf1": "udf1",
              "udf2": "udf2",
              "udf3": "udf3",
              "udf4": "udf4",
              "udf5": "udf5",
              "field2": null,
              "field9": "OTP/ATM page expired due to no user action",
              "error_code": "E1602",
              "addedon": "2024-12-11 12:43:03",
              "payment_source": "payu",
              "card_type": "MAST",
              "error_Message": "Bank was unable to authenticate.",
              "net_amount_debit": "0.00",
              "disc": "0.00",
              "mode": "DC",
              "PG_TYPE": "DC-PG",
              "card_no": "XXXXXXXXXXXX7596",
              "status": "failure",
              "unmappedstatus": "dropped",
              "Merchant_UTR": null,
              "Settled_At": null,
              "cardhash": "095d184331be367bb92aa3eeecb57d0728de96cc598dd563d407982d75021149",
              "name_on_card": null,
              "card_token": "4e97156bc2d6320cdfe15",
              "field4": null,
              "threeDSVersion": "2.2.0",
              "offerAvailed": null
          }
      }
  }
  ```

  * Offer availed on cart level

  ```
  {
      "status": 1,
      "msg": "1 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
          "1036-f0cf85f2": {
              "mihpayid": "21564143078",
              "request_id": "",
              "bank_ref_num": "431998369241",
              "amt": "2.00",
              "transaction_amount": "2.00",
              "txnid": "1036-f0cf85f2",
              "additional_charges": "0.00",
              "productinfo": "EXPRESS",
              "firstname": "guest",
              "bankcode": "TEZOMNI",
              "udf1": "Magento2",
              "udf2": "",
              "udf3": "",
              "udf4": "",
              "udf5": "qs8rbc1ng2hmqtakk381en6j2p",
              "field2": "114390824407",
              "field9": "SUCCESS|Completed Using Callback",
              "error_code": "E000",
              "addedon": "2024-11-14 16:06:40",
              "payment_source": "express",
              "card_type": null,
              "error_Message": "NO ERROR",
              "net_amount_debit": 2.00,
              "disc": "0.00",
              "mode": "UPI",
              "PG_TYPE": "UPI-PG",
              "card_no": "",
              "status": "success",
              "unmappedstatus": "captured",
              "Merchant_UTR": null,
              "Settled_At": "0000-00-00 00:00:00",
              "App_Name": "GooglePay",
              "card_token": null,
              "field4": null,
              "offerAvailed": null,
              "cart_details": {
                  "id": "2446425",
                  "payu_id": "21564143078",
                  "total_items": "1",
                  "total_cart_amount": "2.00",
                  "offer_applied": null,
                  "offer_availed": null,
                  "offer_auto_apply": "0",
                  "instant_discount": "0.00",
                  "cashback_discount": "0.00",
                  "total_discount": "0.00",
                  "net_cart_amount": "2.00",
                  "created_at": "2024-11-14 16:06:40",
                  "updated_at": "2024-11-14 16:06:40",
                  "sku_details": [
                      {
                          "id": "3468748",
                          "cart_id": "2446425",
                          "payu_id": "21564143078",
                          "mid": "2",
                          "sku_id": "Sample Sofa Design-Red",
                          "sku_name": "Sample Sofa Designtest?=!name",
                          "amount_per_sku": "2.00",
                          "quantity": "1",
                          "amount_before_discount": "2.00",
                          "discount": "0.00",
                          "amount_after_discount": "2.00",
                          "offer_applied": null,
                          "offer_availed": null,
                          "offer_status": null,
                          "offer_type": null,
                          "offer_auto_apply": "0",
                          "is_nce": "0",
                          "failure_reason": null,
                          "created_at": "2024-11-14 16:06:40",
                          "updated_at": "2024-11-14 16:06:40",
                          "offer_title": null,
                          "offer_description": null,
                          "instant_discount": null,
                          "cashback_discount": null,
                          "offers_raw_response": null,
                          "raw_response": null
                      }
                  ]
              }
          }
      }
  }
  ```

  * Offer availed at Transaction level

  ```
  {
      "status": 1,
      "msg": "1 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
          "1725950872187": {
              "mihpayid": "20911942990",
              "request_id": null,
              "bank_ref_num": null,
              "amt": "9900.00",
              "transaction_amount": "10000.00",
              "txnid": "1725950872187",
              "additional_charges": "0.00",
              "productinfo": "Macbook Pro",
              "firstname": "Abc",
              "bankcode": "MAST",
              "udf1": "udf1",
              "udf2": "udf2",
              "udf3": "udf3",
              "udf4": "udf4",
              "udf5": "udf5",
              "field2": null,
              "field9": "You have reached credit card load limit. Please use other payment options to continue.",
              "error_code": "E4936",
              "addedon": "2024-09-10 12:18:20",
              "payment_source": "payu",
              "card_type": "MAST",
              "error_Message": "Bank was unable to authenticate.",
              "net_amount_debit": "0.00",
              "disc": "100.00",
              "mode": "DC",
              "PG_TYPE": "DC-PG",
              "card_no": "XXXXXXXXXXXX9528",
              "status": "failure",
              "unmappedstatus": "failed",
              "Merchant_UTR": null,
              "Settled_At": null,
              "cardhash": "31056eb2112b68cdc90896f1953ca26605bb525249096172c178881bcd45ac93",
              "name_on_card": null,
              "card_token": null,
              "field4": null,
              "offerApplied": "LoadTest1@m3phN7YptAA6",
              "offerAvailed": "LoadTest1@m3phN7YptAA6",
              "transactionOffer": "{"offer_data":[{"offer_key":"LoadTest1@m3phN7YptAA6","discount":100,"offer_type":"INSTANT","isNoCost":false,"flag_to_fail":false,"status":"SUCCESS","failure_code":null,"failure_reason":"Offer Applied Successfully","offer_description":"Load Test 1","offer_title":"Load Test 1","record_type":"OFFER","parent_offer_key":null,"offer_category":null,"isDpEmi":false}],"discount_data":{"total_discount":100,"cashback_discount":0,"instant_discount":100,"total_nce_discount":0,"instant_nce_discount":0,"cashback_nce_discount":0,"gstSubventedViaOffer":false,"downPaymentAmount":0}}",
              "offerType": "instant",
              "offerLevel": "TRANSACTION_LEVEL"
          }
      }
  }
  ```

  #### Failure Responses

  * If txnID is not found, the response is similar to the following:

  ```plaintext
  {
  "status":0,"msg":"0 out of 1 Transactions Fetched

  Successfully","transaction_details":{"IhfgcZnXR4o4nB":{"mihpayid":"Not Found","status":"Not Found"}}
  }
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          **Parameter**
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
          status
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter returns the status of web service call. The status can be any of the following:

          * 0 - If web service call failed.
          * 1 - If web service call succeeded
        </td>

        <td style={{ textAlign: "left" }}>
          0
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          msg
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter returns the reason string.
        </td>

        <td style={{ textAlign: "left" }}>
          For example, any of the following messages are displayed:

          * Parameter missing
          * Token is empty
          * Amount is empty
          * Transaction not exists
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          transaction\_details
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the response in a JSON format. For more information refer to [JSON fields description for transaction\_details parameter ](#json-field-description-for-transaction_details-parameter).
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          request\_id
        </td>

        <td style={{ textAlign: "left" }}>
          PayU Request ID for a request in a Transaction. For example, a transaction can have a refund request.
        </td>

        <td style={{ textAlign: "left" }}>
          7800456
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          bank\_ref\_num
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter returns the bank reference number. If the bank provides after a successful action.
        </td>

        <td style={{ textAlign: "left" }}>
          204519474956
        </td>
      </tr>
    </tbody>
  </Table>

  To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).
</Accordion>

## Request parameters

<Accordion title="Sample values" icon="fa-flask">
  Use the following sample values while trying out the API:

  * `var1` (your transaction ID/order ID): 7fa6c4783a363b3da573
</Accordion>

<Recipe slug="parse-the-verify-payment-api-response" title="Parse the Verify Payment API response" />
