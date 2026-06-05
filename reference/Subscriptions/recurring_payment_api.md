---
api:
  file: test_si_collection-6.json
  operationId: RecurringPaymentAPI
hidden: false
link:
  new_tab: false
metadata:
  title: Recurring Payment Transaction API
  description: >-
    Learn how to set up and make Recurring Payment Transaction using PayU's API.
    This API documentation provides specification for collecting recurring
    payments for Net Banking, Cards, and UPI, enabling seamless and automated
    billing for your customers
  keywords:
    - UPI Recurring Payment
    - ' UPI Mandate'
    - ' Card Recurring Payment'
    - ' Subscription using Card'
    - ' Recurring Payment using Card'
    - ' recurring status description'
    - ' Collect Recurring Payment using Card'
    - ' Collect Recurring Payment using UPI'
  robots: index
next:
  pages:
    - slug: using-api-integration-recurring-payments
      title: Using API Integration
      type: basic
    - slug: customer-experience-and-workflow-recurring-payments
      title: Customer Experience and Workflow
      type: basic
---
All successful registration transactions are charged over the recurring interface with server-to-server API without any additional 2FA or the customers’ involvement. This section describes how to achieve the Recurring Transaction for Net Banking, Cards, and UPI through the common platform.

> 📘
>
> **Notes**:
>
> - Banks do not support refunds for Net Banking Recurring Payment transactions (or e-NACH transaction) so you will get an error message, “Refund not accepted for txn” or Error 232. For the list of banks supporting e-NACH, refer to Recurring Payments Bank Codes.
> - Check the mandate status, call the **Pre-Debit Notification** API before calling the **Recurring Payment Transaction** API to make a recurring payment transaction.

> 🚧
>
> **Assumptions**: If the merchant has already performed a successful registration transaction with Net Banking/UPI/Card and mihpayid is received in response to the registration transaction captured successfully and mapped to the customer at the merchant’s end.

### Environment

|                        |                                                                    |
| :--------------------- | :----------------------------------------------------------------- |
| Production Environment | [`https://info.payu.in/merchant`](https://info.payu.in/merchant/>) |
| Test Environment       | [`https://test.payu.in/merchant`](https://test.payu.in/merchant/>) |

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location 'https://info.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642' \
  --data-urlencode 'form=2' \
  --data-urlencode 'key=BmTY3G' \
  --data-urlencode 'command=si_transaction' \
  --data-urlencode 'var1={"authpayuid":"6611192557","invoiceDisplayNumber":"12345678910","amount":"3.00","txnid":"REC15113506209","phone":"9999999999","email":"chota.bheem@gmail.com","udf2":"","udf3":"","udf4":"","udf5":""}' \
  --data-urlencode 'hash=YOUR_HASH_VALUE' \
  --data-urlencode 'salt=MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCm/k3tcvyLiHH0075vrXkhkjfaC+MOPnjaJRul9JXCdsXqWuYw12OZZlVWjJpi+oNpX0Dn8bq2y7wGXa5sL80XTx25PKTXY0mVOmXIrfydWS0e/p1TsrPS7gwdoN73Zz2rUfIQTAdyhnyFI29NftaEB69Lnve3FN82Skn821HUeGrc3ItPHTSnPAksCHvgNIL9EWfY6vYULO8EtPSnQ4pGgkWuQqU/e4Lty7VlLqp+7v/m6djxedBzo7DQsoTdxf6FjXj2z/5UCIieoovP+8RQwL5z/zk7LjKxlDnzyhEDCHvudYx70lzGAp3m3LoLAjZCwrKZNY+fU6gzjixUm4XjAgMBAAECggEAGH/w0Ohw0svW5DN4mgvaXKmGFjBuRHW351FQaB2lJx2j1ck2Qm4nR6cy1/rS37ifNQNrk1vsp8rmMAzofSjaLxRFaRrTmGIRtpoVusaD7FXb/9MdI91w8n5IOsSSUbvM2WixWeC9qvi+Jg5X0wfL0x0Jg8+zyiF+yglGJ5nJvKEdWCyohM8z7qE2K/zuoMyqXIW316BbmAAmD8jNRiTSTgXn7sjiZl63wc2orkQYGOx46TeK6ez90wweGGDGf3+YxAQuoFWdakSW9bYV//kfgNdIHUdZBoDbdOnYPeJHiD7u7lmAFCn+U8inLS27s6gFe4IWekE4ziN0q7N/ebyiIQKBgQDYqPW8DS18CvQdk1gA78x8QpR0tTMPPkLsq1JXdfyZuStqY1fkTms7bpYLFRlh188vVo4ffqyHaxlYRvkxfFlWEJOgZy1eLsR75Rubq1DBAvSxuL/V51ddou81WsN5+IT8Qr6RxjKUlVBSXjPDXBtbKH3lrn8ySk7h6ShIjny+cQKBgQDFUK7ntqsJDJu29BBXNyQua+OGxC6rldWc2y+gH2i91eMQvMVJjE+rkRBglwuAsre3ELt29AQPSFXq1FuAlSeIRwySqBIVssclPQbutDNSD9HUHJOYULooesmfkBesFmcVxnzzsHvMZyUu6pbjbERAvjXxrUvc20gq7d8VE8hbkwKBgQDWgSmR/mX6+olIQtoNS11j5TM//SpJPDZcRR5n8yudMqRWV3bsVet60vkAjeosYdMBpitd6Td9dz6HlPUg1mFIgW73j09ugNUNaP6Vd96iyX9j+WsMp1drIGa+p1cDilZ3vskYYGcxjkcQ1a1gDPAUp5lF7iaGruU8a2/zrga5MQKBgGc9zzaYoqdqfHNfAsnPpVPQyc0zC0Rmcs3O9f1vUcu6hUO1sfjIvMsFbS9M+QzO9keILr6P8SvZ6nKjyHjgEj5BBrgZztShpYe7hcwSZ6PxeRXmGeghnTYfAS5HI8u8MRX4tFqBplUORytkPa0jchb6L5mT1lTqO7mSmx4ZKsWXAoGAGZuTuOd4lXKrQ4nM3NuG4qEfWc4sJgg1y+9C88Za2b6kKvQ8nBj97rFX1kfFKckkp5qGmdKsqCTDKbj/t6in7Cd/zsW8Zdf/lqWtbAA6j5S8hhUswYwIpt8ruJBtTDpTaRokIaw6wivTSLUMYfr1lWqfE9KBmvUOxS35kVA5rIM='
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  **Success scenario**

  Here is a sample response object returned against recurring payment API when the transaction is successfully charged.

  ```json
  {
    "status": 1,
    "message": "Transaction Processed successfully",
    "details": {
        "REC15113506209": {
            "authpayuid": "25600342065",
            "transactionid": "REC15113506209",
            "amount": "1.00",
            "user_credentials": "",
            "card_token": "",
            "payuid": "",
            "status": "captured",
            "udf1": "",
            "field9": "Transaction Completed Successfully",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": "",
            "phone": "9999999999",
            "email": "chota.bheem@gmail.com"
        }
    }
  }
  ```

  **Failure scenarios**

  * Invalid hash

  ```json
  {
      "status": 0,
      "msg": "Invalid Hash."
  }
  ```

  * Basic authentication check failed

  ```json
  {
      "status": 1,
      "message": "Transaction Processed successfully",
      "details": {
          "REC9812123123": {
              "authpayuid": "6611192559",
              "transactionid": "REC9812123123",
              "amount": "1",
              "user_credentials": " ",
              "card_token": " ",
              "payuid": "",
              "status": "failed",
              "field9": "Basic authentication check failed",
              "phone": "",
              "email": ""
          }
      }
  }
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  **JSON fields description of the Details parameter**

  | JSON Field    | Description                                                                                                                                                                       |
  | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | transactionid | This field contains the value of transaction ID parameter which is echoed back in the response. This is unique transaction ID generated by merchant during calling recurring API. |
  | amount        | This field contains the requested transaction amount is echoed back in the payment response.                                                                                      |
  | payuid        | This field contains the PayU’s transaction ID for processed recurring transaction. Merchant can use this field for reference point in the settlement report.                      |
  | status        | This field gives the status of the transaction. Hence, the value of this field depends on whether the transaction was successful or not.                                          |
  | field9        | This field returns the description of transaction status which can help the merchant in providing better customer communication.                                                  |
  | phone         | The mobile number of the customer echoed back.                                                                                                                                    |
  | email         | Email ID of the customer echoed back.                                                                                                                                             |
  | udf1          | Extra information received in the request echoed back.                                                                                                                            |
  | udf2          | Extra information received in the request echoed back.                                                                                                                            |
  | udf3          | Extra information received in the request echoed back.                                                                                                                            |
  | udf4          | Extra information received in the request echoed back.                                                                                                                            |
  | udf5          | Extra information received in the request echoed back.                                                                                                                            |

  ### status field description

  This field gives the status of the transaction. Hence, the value of this field depends on whether the transaction was successful or not.\
  You must map the order status using this parameter only. The possible values of this parameter are:

  * **captured**: If the transaction is successful, the value will be captured. In some cases, the response of Net banking recurring can be captured over real-time basis (ICICI bank in the specific scenario).
  * **pending**: This is common with most Net Banking (except ICICI in the specific scenario) or UPI recurring transaction. In that case, the merchant should consider this as successful initiation of payment with bank / NPCI. The status will be notified back to the merchant over payment processing with individual bank gets completed.\
    For UPI, “pending” transactions get usually get converted into captured or failed within 10 mins from the time of initiation. The Query API can be called post 10 mins from initiation, whereas for Net Banking, it can be called up to T+2 once a day. For more information, refer to [Capture response of Recurring Transaction](#capture-response-of-recurring-transaction-for-net-banking-and-upi).\
    For Net Banking, “pending” transaction gets converted into “captured” or “failed” from the same day till T+2 anytime, depending upon the bank account used by the customer in setting up registration.
  * **failed**: The value of the status as “failed” or blank must be treated as a failed transaction only.
  * **in-progress**: The status of transaction is in progress.

  To capture the final status of “pending” transaction to either “captured” or “failed”, PayU recommends merchants to either implement Webhook URL or call **verify\_payment** API after regular intervals. For more information on:

  * Webhook: Refer to [Webhooks](doc:webhooks)
  * **verify\_payment** API: Refer to [Verify Payment API](ref:verify_payment_api)

  > 📘 Note:
  >
  > For UPI, call the **verify\_settlement** API after 10 mins from time of initiation whereas for Net Banking it can be called up to T+2 once in a day.
</Accordion>

## UPI Sequencing

You may attempt multiple pre-debits and executions simultaneously in certain scenarios. To address such scenarios, **mandateSeqNo** field in var1 parameter in the **Pre Debit Notification** API. This is applicable only for UPI autopay transactions.
A sequence is posted based on Mandate creation. When consent is taken, the first execution is carried out in real-time, and the execution sequence is set to 1. The subsequent pre-debit will start from 2.

<Accordion title="Sample request" icon="fa-flask">
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'form=2' \
  --data-urlencode 'key=smsplus' \
  --data-urlencode 'command=si_transaction' \
  --data-urlencode 'var1={"authpayuid": "25600438037", "invoiceDisplayNumber": "INV-12345", "amount": "100.00", "txnid": "TXN-2024-001-SEQ2", "phone": "9999999999", "email": "customer@example.com", "mandateSeqNo": 2}' \
  --data-urlencode 'hash=YOUR_HASH_VALUE'
  ```
</Accordion>

<Accordion title="Response in various scenarios" icon="fa-flask">
  # Table 3: Complete Error Scenarios and Response Codes

  # Table 3: Scenarios and Response Payloads

| Scenario | Response Payload |
|----------|------------------|
| **Success Cases** |
| Transaction In Progress | `{"status":1,"message":"Transaction Processed successfully","details":{...,"status":"in progress","field9":"92\|Transaction Initiated"}}` |
| Transaction Captured | `{"status":1,"message":"Transaction Processed successfully","details":{...,"status":"captured","field9":"Transaction Completed Successfully"}}` |
| **Transaction Errors** |
| Authentication Failed | `{"status":1,"message":"Transaction Processed successfully","details":{...,"status":"failed","field9":"Basic authentication check failed"}}` |
| Invalid Hash | `{"status":0,"msg":"Invalid Hash."}` |

</Accordion>

## Request parameters

<Accordion title="Reference information" icon="fa-flask">
  <HTMLBlock>{`
                        <table style="width: 100%; border-collapse: collapse;">
                        <thead>
                        <tr>
                          <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
                          <th style="border: 1px solid #ddd; padding: 8px;">Reference</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                          <td style="border: 1px solid #ddd; padding: 8px;"><p>&lt;&lt;glossary:key&gt;&gt;</p>
                        </td>
                          <td style="border: 1px solid #ddd; padding: 8px;"><p>For more information on how to generate the Key and Salt, refer to any of the following:  </p>
                        <ul>
                        <li><strong>Production</strong>: <a href="http://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard">Generate Merchant Key and Salt</a></li>
                        <li><strong>Test</strong>: <a href="http://docs.payu.in/docs/generate-test-merchant-key-and-salt">Generate Test Merchant Key and Salt</a></li>
                        </ul>
                        </td>
                        </tr>
                        <tr>
                          <td style="border: 1px solid #ddd; padding: 8px;"><p>&lt;&lt;glossary:hash&gt;&gt;</p>
                        </td>
                          <td style="border: 1px solid #ddd; padding: 8px;"><p>Hash logic for this API is:<br>sha512(key|command|var1|salt)sha512</p>
                        </td>
                        </tr>
                        <tr>
                          <td style="border: 1px solid #ddd; padding: 8px;"><p>var1</p>
                        </td>
                          <td style="border: 1px solid #ddd; padding: 8px;"><p>For JSON fields description, refer to <a href="http://docs.payu.in/reference/addl_info-payment-apis#/">Additional Info. Payment APIs</a></p>
                        </td>
                        </tr>
                        </tbody>
                        </table>
  `}</HTMLBlock>
</Accordion>

<br />
