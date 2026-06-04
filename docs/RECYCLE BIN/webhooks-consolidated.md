---
title: Webhooks
excerpt: >-
  Create WebHooks to get notified about events related to Payments, Refunds,
  Subscriptions, and Payouts
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: ''
  description: ''
  robots: index
---
WebHooks (aka Web callback or Reverse APIs) are one of the most popular and efficient way in which one application sends information to another application when specific events occurs.

#### Example

Assume that you have you have added an Webhook endpoint to recive notification for a `payment.success `event, PayU will send you a notification everytime a payment is successful.

## Webhook Vs API

A Webhook sends you information only when specific events occur whereas an API sends you information when you request for it.

#### Example

If you want to know whether an user has purchased a product on your ecommerce website, using APIs, you need to keep polling a specific API every few seconds untill a purchase is made. However, if you have created an Webhooks to listen to `payment.successful` events, you will receive a realtime notification as soon as a payment is made.

## When to use PayU Webhooks

You can use PayU Webhooks to recieve a callback on your URL whenever a specific event occurs. When these events occurs, PayU sends an HTTP POST request with a JSON payload on the Webhook's configured endpoint.

* You can create Webhooks from PayU Dashboard and configure separate Webhooks URL for LIVE or TEST mode. Know more about creating Webhooks.
* An Webhook created in the TEST mode of PayU dashboard receives events for test transactions. Know more about testing your Webhooks.

## Webhook Security

Every Webhook payload that is sent to your URL contains an encoded Hash string which is created using the parameters you sent in the payment request along with your unique merchant key & salt in reverse order, know more about Reverse Hashing. It is important that you validate the hash sent in the Webhook payload to ensure the authenticity of the sender.

## Whitelist IPs

PayU can only send Webhook notifications on a public URL which is accessible on Web. If your Webhook URL is protected by a firewall then a Webhook delivery attempt by PayU may fail. To avoid such failure it is recommended to whitelist following URLs from which PayU sends an Webhook notification

| LIVE Webhooks       | TEST Webhooks   |
| ------------------- | --------------- |
| **180.179.174.1**   | **3.7.89.2**    |
| **52.140.8.88**     | **3.7.89.1**    |
| **180.179.174.2**   | **3.7.89.3**    |
| **180.179.165.250** | **3.7.89.8**    |
| **52.140.8.64**     | **3.7.89.9**    |
| **10.251.7.118**    | **3.7.89.10**   |
| **52.140.8.65**     | **52.140.8.89** |