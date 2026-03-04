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

```
mihpayid=403993715528735905&mode=CASH&status=success&key=QyT13U&txnid=e41097ba86bffc0eb67f&amount=10.00&addedon=2023-04-18+17%3A53%3A43&productinfo=Product+Info&firstname=Payu-Admin&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40example.com&phone=1234567890&udf1=Test1&udf2=test2&udf3=Test3&udf4=Test4&udf5=Test5&card_token=&card_no=&field0=&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CASH-PG&error=E000&error_Message=No+Error&net_amount_debit=10&discount=0.00&offer_key=&offer_availed=&unmappedstatus=captured&hash=6cac0092a7b6bff2e17822e2917fed490c984392c6f5a5bbdc4c37b9a6f9660c30442a64254236eb10b0af628258288fb1eb94e724e05c8d2bff58957509b945&bank_ref_no=2eec20f3-3608-4c25-a1e7-2af96e5c47c5&bank_ref_num=2eec20f3-3608-4c25-a1e7-2af96e5c47c5&bankcode=AMON&surl=https%3A%2F%2Ftest.payu.in%2Fadmin%2Ftest_response&curl=https%3A%2F%2Ftest.payu.in%2Fadmin%2Ftest_response&furl=https%3A%2F%2Ftest.payu.in%2Fadmin%2Ftest_response
```

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
