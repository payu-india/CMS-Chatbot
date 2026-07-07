---
title: '[Temp]Closed Loop Wallet - Overview and API Conventions'
deprecated: false
hidden: true
metadata:
  robots: index
---
## Overview [Separate prompt]

A **Closed Loop Wallet** is a digital payment solution that allows customers to store money and make transactions exclusively within your platform or merchant ecosystem. Unlike open-loop wallets (like Paytm or PhonePe) that work across multiple merchants, a closed loop wallet is tied specifically to your business—think of store credits, gift cards, or loyalty wallets.

PayU's Closed Loop Wallet provides a one-stop solution for:

* **Wallet issuance** – Creating digital wallets for your customers
* **Wallet loading/unloading** – Adding or withdrawing funds
* **Lifecycle management** – Managing wallet status and customer profiles
* **Transaction processing** – Enabling seamless payments within your ecosystem

### Key Terminology

| Term                              | Description                                                                  |
| :-------------------------------- | :--------------------------------------------------------------------------- |
| **Closed Loop Wallet (CLW)**      | A digital wallet that can only be used within a specific merchant's platform |
| **KYC (Know Your Customer)**      | Verification process to validate customer identity                           |
| **URN (Unique Reference Number)** | A unique identifier assigned to each wallet/card                             |
| **Load Transaction**              | Adding funds to the wallet                                                   |
| **Debit Transaction**             | Using wallet balance to make payments                                        |
| **HMAC-SHA512**                   | The encryption algorithm used for API authentication                         |

### API Authentication

All Prepaid APIs are authenticated using hmac-sha256 algorithm and requires PayU salt and key.

***

## API Conventions

### HTTP Verbs

The following are the HTTP verbs supported by Wibmo Prepaid Platform:

| Verb  | Description                                                     |
| :---- | :-------------------------------------------------------------- |
| GET   | Used for retrieving resources. For ex. Retrieve cust record API |
| POST  | Used for creating resources. For ex. Register customer API      |
| PATCH | Used for updating resources. For ex. Wallet status API          |

***

### HTTP Request Headers

| Parameter                          | Description                                                                                                                                                                              | Example                       |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------- |
| walletIdentifier <br />`mandatory` | `String` - Program Type                                                                                                                                                                  | CLW                           |
| date <br />`mandatory`             | `String` - The date and time should be in the GMT time conversion (not the IST). For example, current time in India is 18:00:00 IST, the time in the date header should be 12:30:00 GMT. | Thu, 17 Feb 2022 08:17:59 GMT |
| Authorisation <br /> `mandatory`   | `String` - See Authorization format below                                                                                                                                                |                               |

#### Authorization Field Format

The Authorization field format is similar to the following example:

```
hmac username="smsplus", algorithm="sha512", headers="date", signature="7ff938849aa79265a3de63fe241dfecb1c680f58c6d11e9f9ca08512afea374705eb9f8995ef6c4584e16eca2e1dc688262bb0937a36cc0f75ec22a9eea33523"
```

Where, the fields in this example are:

* **username**: The merchant key of the merchant.
* **algorithm**: This must have the value as hmac-sha512 that is used for this API.
* **headers**: This must have the value as date digest.
* **signature**: This must contain the hmacsha512 of (signing_string, merchant_secret), where:
  * **signing_string**: It must be in the "date: \{dateValue}" format. Here, the dateValue is the same values in the fields listed in this table. For example, "date: Thu, 17 Feb 2022 08:17:59 GMT"
  * **merchant_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to Generate Merchant Key and Salt.

***

### HTTP Status Codes

| HTTP Status Code | HTTP Status Description |
| :--------------- | :---------------------- |
| 200              | OK                      |
| 201              | Created                 |
| 404              | Not Found               |
| 500              | Internal Server Error   |
| 403              | Forbidden               |
| 400              | Bad Request             |
| 401              | Unauthorized            |
| 503              | Service Unavailable     |
