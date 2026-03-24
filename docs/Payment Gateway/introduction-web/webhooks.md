---
title: Webhooks for Payments
excerpt: >-
  Webhooks are a way for one server to communicate with another server by
  sending an HTTP callback or message. These callbacks are triggered by specific
  events or instances and they operate at the server-to-server (S2S) level.
deprecated: false
hidden: false
metadata:
  title: Webhooks
  description: >-
    Webhooks are used to receive real-time HTTP notifications of changes to
    specific objects in the PayU social graph. The page provides a detailed
    description of the notification payload object, which is a combination of
    nested objects of JSON arrays and objects that contain information about a
    change. The notification payload object contains details for the change that
    triggered the webhook. This object is nested within the changes array of the
    entry array.
  keywords:
    - Webhooks PayU integration
    - Configure Webhooks in PayU
    - PayU Webhooks
    - Webhooks IP
  robots: index
next:
  description: ''
---
PayU utilizes webhooks technology to establish a secure and accountable architecture for payment processing between the merchant’s server and our own. When certain events occur within the payment workflow, such as a successful transaction or a change in order status, webhooks are used to send real-time updates between the servers.

It is important to note that in order to receive webhooks, the merchant will need to set up a listener on their server to handle the incoming requests. Additionally, proper security measures, such as SSL/TLS encryption, should be implemented to ensure the confidentiality and integrity of the information being sent via webhooks.

## PayU Webhooks

PayU offers Hosted and Merchant Hosted integration options that operate at the browser level. It involves switching the customer between the merchant, PayU, and the bank’s website, redirecting to success or failure URLs. Using browser redirection may be technically challenging to ensure the integrity of responses, affecting customer experience. To overcome this, PayU also offers Webhooks which is a server-to-server callback where PayU will send an additional S2S response. PayU recommends using S2S response to ensure optimum transaction outcomes instead of browser redirection, responses every time, affecting the customer experience.

## Why PayU uses Webhook?

When integrating with PayU, the server-to-server (S2S) callback feature is a highly recommended option. PayU will typically send the final transaction response to the merchant through browser redirection. However, in cases where network issues or other technical difficulties cause the browser redirection to fail, the transaction may be dropped between PayU and the merchant. This can make it difficult for the merchant to complete the processing of the order.

To address this potential issue, the S2S callback feature can be utilized effectively. With this feature enabled, PayU will send the final transaction response to the merchant’s server directly, rather than relying on browser redirection. This ensures that the merchant will receive the response regardless of any issues with the browser redirection.

## Configure Webhooks in PayU

### Using Dashboard

You can configure webhooks using PayU Dashboard quickly. For more information, refer to [Manage Webhooks using Dashboard](doc:manage-webhooks-using-dashboard).

### Manually

To use Webhooks during integration with PayU:

1. Create a server URL from your business server landscape and share it with PayU, along with its server IP address. It is the URL at which the transaction response from PayU will hit. For example, [www.test.payu.in/success/response](http://www.test.payu.in/success/response)
2. PayU will configure the merchant’s server URL at its backend, mapping it against the MID and key of that particular merchant.
3. PayU will whitelist the webhook URL provided by the merchant in its systems. For more information, contact the PayU Integration Team by email: [integration@payu.in](mailto:integration@payu.in).
4. Whitelist the following IP address in your Firewall to receive a response from the PayU servers:

|                 |           |
| --------------- | --------- |
| 52.140.8.88     | 3.7.89.1  |
| 52.140.8.89     | 3.7.89.2  |
| 180.179.174.2   | 3.7.89.3  |
| 180.179.165.250 | 3.7.89.8  |
| 52.140.8.64     | 3.7.89.9  |
| 52.140.8.65     | 3.7.89.10 |
| 3.6.73.183      | 3.6.83.44 |

5. PayU will send an S2S response to the merchant’s server URL. The merchant’s server URL should be capable of handling the following content types:
   * FormData
   * application/x-www-form-urlencode

> 📘 Note:
>
> While creating the server URL, ensure that it can accept the data in the above content formats.

Sample response from PayU to the merchant:

* **Payment Success**

```json
{
  "timestamp": "2026-02-26 11:35:25.000000",
  "request_identifier": "27455843883",
  "event_type": "payment",
  "status": "Success",
  "webhook_delivery_message": null,
  "http_method": "POST",
  "endpoint": "https://partnerapilayer.payu.in/apilayer/partner/paymentCallback",
  "response_code": 200,
  "response_body": "",
  "endpoint_latency": 1085,
  "event_payload": {
    "country": "",
    "curl": "https://api.payu.in/partner/paymentCancelled",
    "udf10": "",
    "discount": "0.00",
    "offer_key": "",
    "error_Message": "The Bank servers are unreachable over the network",
    "state": "",
    "payment_source": "payuPureS2S",
    "txnid": "25841132755570991",
    "surl": "https://api.payu.in/partner/paymentSuccess",
    "net_amount_debit": "0",
    "lastname": "",
    "zipcode": "",
    "offer_availed": "",
    "phone": "918921784385",
    "pa_name": "Camspay",
    "productinfo": "25841132755570991",
    "hash": "bd4b8272f8a2d3b57a42f4c444642ef9c7c965e41378264f1d94645e386b4c22f4bf810d1020e38586b3e44d3197154be136f467821a166a5119af7d042d426c",
    "status": "pending",
    "firstname": "",
    "city": "",
    "authenticaticationMethod": "",
    "error": "E214",
    "bank_ref_no": "",
    "addedon": "2026-02-26 11:12:25",
    "udf9": "",
    "udf7": "",
    "udf8": "",
    "bank_ref_num": "",
    "key": "rM5M43",
    "email": "",
    "amount": "1.00",
    "unmappedstatus": "in progress",
    "address2": "",
    "address1": "",
    "udf5": "whatsapp",
    "mihpayid": "27455843883",
    "udf6": "",
    "udf3": "",
    "udf4": "",
    "udf1": "",
    "udf2": "",
    "field1": "",
    "field0": "",
    "field7": "VERNEGATIVE",
    "field6": "",
    "furl": "https://api.payu.in/partner/paymentFailed",
    "field9": "HTTP/1.1 500 Internal Server Error",
    "field8": "Verification | failed | Transaction failed at bank end",
    "field3": "",
    "field2": "",
    "field5": "",
    "PG_TYPE": "UPI-PG",
    "field4": ""
  }
}
```

<br />

* **Payment Failure**

```json
{
  "timestamp": "2026-02-27 14:24:45.000000",
  "request_identifier": "27472524682",
  "event_type": "payment",
  "status": "Failed",
  "webhook_delivery_message": "HTTP/2 405 ",
  "http_method": "POST",
  "endpoint": "https://payu.in",
  "response_code": 405,
  "response_body": "<html>\r\n<head><title>405 Not Allowed</title></head>\r\n<body>\r\n<center><h1>405 Not Allowed</h1></center>\r\n<hr><center>nginx</center>\r\n</body>\r\n</html>\r\n",
  "endpoint_latency": 7,
  "event_payload": {
    "country": "",
    "curl": "https://admin.payu.in/test_response",
    "udf10": "",
    "discount": "0.00",
    "offer_key": "",
    "error_Message": "Bank failed to authenticate the customer",
    "state": "",
    "payment_source": "payu",
    "txnid": "5e2e5eb03a45f13a8bdb",
    "surl": "https://admin.payu.in/test_response",
    "net_amount_debit": "0",
    "lastname": "",
    "zipcode": "",
    "offer_availed": "",
    "additionalCharges": "0.03",
    "phone": "1234567890",
    "pa_name": "PayU",
    "productinfo": "Product Info",
    "hash": "5aa580a257fc7f7acd8350db00142360d385b105d6b1aa1cb4bb9e14a945fc0bd84afecba321561485046a46d009581c77ec4d184cdf02d134a9c6e41b398817",
    "status": "failure",
    "firstname": "Payu-Admin",
    "city": "",
    "authenticaticationMethod": "",
    "error": "E500",
    "bank_ref_no": "",
    "addedon": "2026-02-27 14:24:42",
    "udf9": "",
    "udf7": "",
    "udf8": "",
    "bank_ref_num": "",
    "key": "rM5M43",
    "email": "test@example.com",
    "amount": "1.00",
    "unmappedstatus": "failed",
    "address2": "",
    "address1": "",
    "udf5": "",
    "mihpayid": "27472524682",
    "udf6": "",
    "udf3": "",
    "udf4": "",
    "udf1": "",
    "udf2": "",
    "field1": "",
    "field0": "",
    "field7": "AUCNEGATIVE",
    "field6": "",
    "furl": "https://admin.payu.in/test_response",
    "field9": "UNKNOWN",
    "field8": "Message Received Invalid",
    "field3": "",
    "field2": "",
    "field5": "",
    "PG_TYPE": "DC-PG",
    "field4": ""
  }
}
```

<Accordion title="Description of fields in event_payload JSON Object" icon="fa-table">
  | Field                    | Description                                                                                                                                                                                                                                                     |
  | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | mihpayid                 | Unique transaction ID assigned by PayU for each transaction. Use for inquiry or refund.                                                                                                                                                                         |
  | key                      | Merchant key identifying the merchant's PayU account; same as in the transaction request.                                                                                                                                                                       |
  | txnid                    | Transaction ID (Order ID) that was sent by the merchant in the transaction request.                                                                                                                                                                             |
  | amount                   | Original payment amount sent in the transaction request by the merchant.                                                                                                                                                                                        |
  | productinfo              | Product description sent in the transaction request.                                                                                                                                                                                                            |
  | firstname                | Customer first name as sent in the transaction request.                                                                                                                                                                                                         |
  | lastname                 | Customer last name as sent in the transaction request.                                                                                                                                                                                                          |
  | email                    | Customer email as sent in the transaction request.                                                                                                                                                                                                              |
  | phone                    | Customer phone number as sent in the transaction request.                                                                                                                                                                                                       |
  | address1                 | Customer address line 1 (from request).                                                                                                                                                                                                                         |
  | address2                 | Customer address line 2 (from request).                                                                                                                                                                                                                         |
  | city                     | Customer city (from request).                                                                                                                                                                                                                                   |
  | state                    | Customer state (from request).                                                                                                                                                                                                                                  |
  | country                  | Customer country (from request).                                                                                                                                                                                                                                |
  | zipcode                  | Customer zip/postal code (from request).                                                                                                                                                                                                                        |
  | udf1 – udf10             | User-defined fields (udf1–udf5 documented; udf6–udf10 in response). Same values as sent in the transaction request. Character limit 255 for udf1–udf5.                                                                                                          |
  | hash                     | Hash calculated by PayU. Merchant must verify it before marking the transaction success/failure to ensure integrity. See [Generate Hash](doc:generate-hash-merchant-hosted).                                                                                    |
  | status                   | Outcome of the transaction: `success`, `failure`, or `pending`. Treat only `success` as successful.                                                                                                                                                             |
  | error                    | Error code indicating the reason for failure (e.g. E500). Failure reasons vary by bank.                                                                                                                                                                         |
  | error\_Message           | Human-readable error message. Refer to [Error Codes](ref:error-codes) for the list.                                                                                                                                                                             |
  | PG\_TYPE                 | Payment gateway type used for the transaction (e.g. `CC-PG` for credit card, `DC-PG` for debit card, `UPI-PG`, `CASH-PG`, `EMI-PG`, `BNPL-PG`, `QR-PG`).                                                                                                        |
  | bank\_ref\_num           | For successful transactions, the bank reference number generated by the bank.                                                                                                                                                                                   |
  | bank\_ref\_no            | Same as bank\_ref\_num; alternate parameter name for bank reference number.                                                                                                                                                                                     |
  | unmappedstatus           | Transaction status in PayU’s internal system; can include intermediate states. Values include: dropped, bounced, captured, auth, failed, usercancelled, pending. See [Payment State Explanations](ref:payment-state-explanations).                              |
  | surl                     | Success URL – URL on which PayU redirects when the transaction is successful.                                                                                                                                                                                   |
  | furl                     | Failure URL – URL on which PayU redirects when the transaction fails.                                                                                                                                                                                           |
  | curl                     | Cancel URL – URL used when the user cancels (character limit 50 in request).                                                                                                                                                                                    |
  | addedon                  | Date and time when the transaction was recorded (e.g. `2026-02-27 14:24:42`).                                                                                                                                                                                   |
  | discount                 | Discount amount applied (e.g. `0.00`).                                                                                                                                                                                                                          |
  | net\_amount\_debit       | Net amount debited from the customer.                                                                                                                                                                                                                           |
  | additionalCharges        | Additional charges applied (e.g. convenience fee).                                                                                                                                                                                                              |
  | payment\_source          | Source of the payment (e.g. `payu`).                                                                                                                                                                                                                            |
  | pa\_name                 | Name of the payment aggregator through which the transaction was routed (e.g. PayU, RazorPay). Shown when using Maximiser / other aggregators.                                                                                                                  |
  | offer\_key               | Key of the offer applied, if any.                                                                                                                                                                                                                               |
  | offer\_availed           | Indicates whether an offer was availed.                                                                                                                                                                                                                         |
  | authenticaticationMethod | Authentication method used (e.g. 3DS). Note: name may appear with typo in payload.                                                                                                                                                                              |
  | field0 – field9          | Gateway- or flow-specific fields. Content varies by payment mode and outcome (e.g. bank reference, RRN, auth result, status message). For cards, field7/field8/field9 often carry auth result or message (e.g. AUCNEGATIVE, UNKNOWN, Message Received Invalid). |
</Accordion>

The parameters used in generating the above response block are similar to those you shared with PayU while triggering the transaction.

> 📘 Notes:
>
> * In case a parameter has not been consumed, PayU sends it back to you with an empty string.
> * For reverse hashing the response, refer to [Generate Hash](doc:generate-hash-merchant-hosted).

6. Confirm (your server) the receipt with the success status response code: **200 OK** after the PayU response hits the merchant’s server URL.

<Callout icon="📘" theme="info">
  **Retries:** PayU will retry 3 times to get a 200 OK response from the merchant’s servers before flagging it as a timeout. Ensure correct configuration of the merchant’s server URL that accepts key-value pairs or hashmap formats and handles the content types mentioned in the documentation.
</Callout>

## Webhook events for Payments

The table below lists down the webhook events that are supported for Payment Webhooks types. See [Create a new Webhook ](https://docs.payu.in/docs/create-a-new-webhook) to learn more about how to create payment webhooks and subscribe to payment events.

| Event Name | Event Type | Description                                      |
| :--------- | :--------- | :----------------------------------------------- |
| Successful | Payment    | Triggered when a payment is successful           |
| Failed     | Payment    | Triggered when a payment is failed               |
| Refund     | Payment    | Triggered when the payment is refunded           |
| Dispute    | Payment    | Triggered when a dispute is raised for a payment |

> 📘 callback_on_failure
>
> PayU supports another type of callback which allows the merchants to recieve webhook payloads for  pending cases in realtime. Currently this callback flag is enabled by the support team on request.
>
> ***
>
> If you choose to enable this flag, you will be recieving webhooks in realtime for all types of pending payment statuses—see [Payment state explanation](https://docs.payu.in/reference/payment-state-explanations)—following by a successful/failed webhook when the payment state is changed to Successful or falied.

## Testing Your webhook

It's recommended to test your webhook implementation to ensure it's working correctly:

1. Configure your webhook as described above
2. Set up your endpoint to log incoming webhook requests
3. Wait for a payment event or request a test webhook from PayU support
4. Verify that your endpoint receives the webhook payload and processes it correctly
