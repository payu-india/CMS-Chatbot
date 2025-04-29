---
title: Dynamic Storefront QR
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: >-
    PayU POS Dynamic Storefront Integrations for Dynamic QR | PayU Developer
    Guide
  description: >-
    Learn how to integrate PayU’s POS dynamic storefront with dynamic QR into
    your point of sale (POS) system, and start accepting payments seamlessly.
    Get started with our developer guide today.
  robots: index
next:
  description: ''
---
Integrated Dynamic Storefront QR allows you to seamlessly generate dynamic storefront QRs to collect payments from your customers.

There is no requirement of any manual intervention and all the details to generate the dynamic-QR can be sent to PayU via an API

Unlike UPI-QRs which only support payment from UPI, the storefront QR can be scanned by the customer to pay through any of the available modes of payment.

In API response, the merchant can either get a QR (which the merchant can show on a digital display screen or print on an invoice) or a payment link (which he can send as an SMS to the customer) or both. Merchant also can request PayU to trigger the SMS to the customer.

After the customer scans the QR (using google lens, phone camera or third-party QR scanning apps) or clicks the payment link, the customer lands on the Order Summary screen to verify order details. Later, the customer can proceed to make payment using any available or enforced payment modes on PayU’s checkout page (PayU Hosted Checkout).

After completing the payment, the customer will see a ‘payment confirmation’ screen on his device. The merchant gets a response in a server-to-server callback or can also use Verify Payment API to fetch the transaction status. For more information, refer to Verify Transactions API.

> 👍 Callout
>
> * The Dynamic storefront QR is not a UPI-QR or a Bharat-QR and as such cannot be scanned through UPI applications. The customer can scan this QR using applications like camera or google lens or third party scanners on his smart phone.
> * The customer can pay using any of the available payment modes which are activated on the merchant.
