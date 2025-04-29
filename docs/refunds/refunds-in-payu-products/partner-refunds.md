---
title: Partner Refunds
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
​​PayU partners with merchants to build a trusted payment experience for their customers by refunding online payments within minutes! Offered as a separate service for the merchants, PayU does real-time credits of the refunds into the customer’s bank account. A merchant is charged based on the number of refunds credited instantly for this service.

## Payment channels

- Credit Card: Crediting refunds instantly to a customer’s credit card. The majority are supported via IMPS and others via NEFT.
- UPI: Direct credit into customer VPA using UPI P2P Push API
- Auth-Capture: In this model, transactions are authorized only and marked captured post order fulfilment, leading to a way to process the cancel/refund instantly for the services not offered
- Debit Card: Currently, DC refunds of issuer SBI processed via SBI Direct (135) PG will support instant refunds
- Net Banking: Partner bank (Kotak NB) offers instant refunds

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/09/image-23-1024x367.jpg)

## Integration requirements

If a merchant account already has the PayU Refund system integrated, the Instant Refund service does not need separate integration but only activation from the backend. ​Refunds for transactions done through PayU can be directly initiated using the existing Refund API or Merchant Dashboard.

1. Merchant Level Enablement: This service will be enabled on merchant Id. All eligible transactions will automatically be refunded via an alternate refund channel.
2. Transaction Level Enablement: Merchants can decide the service basis of a transaction and not on a global level. Merchant has to pass a new parameter in the refund initiation API which will process that specific refund through an alternate channel (IMPS/NEFT/UPI/MasterCard Send) if eligible. Please find below the additional parameter to be sent.

> 📘 Note: 
> 
> The platforms should collect the key and salt of the merchants to call the refund API.