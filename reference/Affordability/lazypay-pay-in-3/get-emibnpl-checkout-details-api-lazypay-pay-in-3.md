---
title: Get EMI/BNPL Checkout Details API - LazyPay Pay-in-3
deprecated: false
hidden: true
metadata:
  robots: index
---
This API is used to **check LazyPay eligibility** and related checkout details (for example linking status, KFS link, tokens, and Pay-in-3 instalment context when applicable) before you call `/_payment`. It is the same **Get EMI / BNPL checkout details** service as the full reference; this page focuses on `LAZYPAY` (classic BNPL) and `LZYPI3` (Pay-in-3 — some internal samples use `LAZYPI3`; use the literal your **v1** pack prints). For all headers, digest and HMAC variants, NTB flows, and the complete body schema, refer to [Get EMI Checkout Details API](ref:get-emi-checkout-details-api).

> **Signing (hash-based only):** `Digest` and `Authorization` use SHA / HMAC over the JSON body and `Date` as in [Get EMI Checkout Details API](ref:get-emi-checkout-details-api). That is **not** the same string construction as the `hash` field on merchant-hosted `/_payment`, and **not** the `sha512(key|command|var1|SALT)` string used for **[Get Checkout Details](ref:get_checkout_details)** on `postservice.php`—follow each endpoint’s sample. Pay-in-3 seamless flows often call **Get Checkout Details** first (command hash) and then this API.

### Environment

|                        |                                                                                                                                   |
| :--------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/info/linkAndPay/get\_emi\_checkout\_details](https://test.payu.in/info/linkAndPay/get_emi_checkout_details) |
| Production Environment | [https://info.payu.in/linkAndPay/get\_emi\_checkout\_details](https://info.payu.in/linkAndPay/get_emi_checkout_details)           |

## Request parameters

###

| Parameter                  | Description                                                 | Example                                          |
| :------------------------- | :---------------------------------------------------------- | :----------------------------------------------- |
| bankCode `mandatory`       | LazyPay product: classic BNPL or Pay-in-3                   | `LAZYPAY` or `LZYPI3` (some packs use `LAZYPI3`) |
| Key `mandatory`            | Merchant key from the PayU Dashboard                        | `yFbXg3`                                         |
| phone `mandatory`          | Customer mobile number for eligibility                      | `9999999999`                                     |
| amount `mandatory`         | Transaction amount (numeric or string per integration pack) | `21`                                             |
| userCredentials `optional` | Unique user identifier in the form `merchantKey:userId`     | `yFbXg3:test_sud`                                |
| payuToken `optional`       | PayU instrument token when applicable                       | `null`                                           |
| requestId `optional`       | Correlation id for the request                              | `Testing_111`                                    |

> 📘 Note
>
> For **NTB** or **cardless EMI** style payloads (`LPEMI`, `customerDetails`, `pg`, `checkCustomerEligibilityWithDetails`, and so on), refer to the canonical [Get EMI Checkout Details API](ref:get-emi-checkout-details-api).

## Sample request

### LazyPay eligibility (Link and Pay)

```curl
curl --location 'https://test.payu.in/info/linkAndPay/get_emi_checkout_details' \
--header 'x-credential-username: smsplus' \
--header 'Content-Type: application/json' \
--header 'authorization: hmac username="x0i6r2", algorithm="sha512", headers="date", signature="0e0ebc518c085d8ff49058b7c232bfe2e8779e9e9cafd34a4cdf1c11114035eea75b0e404a9b9e152757dbcc4926f78b6f18ba7f6643e2bf687a65942d3bde38"' \
--header 'date: Mon, 28 Oct 2024 10:34:49 GMT' \
--data '{
  "Key": "yFbXg3",
  "amount": 21,
  "userCredentials": "yFbXg3:test_sud",
  "phone": "9999999999",
  "bankCode": "LAZYPAY",
  "payuToken": null,
  "requestId": "Testing_111"
}'
```

### Pay-in-3 (bankCode `LZYPI3`)

Same headers and signing rules as above; only the JSON body’s `bankCode` (and typically **amount / phone**) change per your Pay-in-3 pack.

```curl
curl --location 'https://test.payu.in/info/linkAndPay/get_emi_checkout_details' \
--header 'Content-Type: application/json' \
--header 'date: Mon, 28 Oct 2024 10:34:49 GMT' \
--header 'digest: SHA-256=<computed>' \
--header 'authorization: hmac username="<clientId>", algorithm="sha512", headers="date digest", signature="<computed>"' \
--data '{
  "Key": "yFbXg3",
  "amount": 10000,
  "phone": "9999999999",
  "bankCode": "LZYPI3",
  "payuToken": null,
  "requestId": "Testing_payin3_001"
}'
```

> 📘 Authorization calculation logic
>
> For authorization calculation logic, refer to [Get EMI Checkout Details API > Required parameters for calculating authorization](ref:get-emi-checkout-details-api#required-parameters-for-calculating-authorization).

## Sample response

### Success scenario (LazyPay in bnpl block)

```json
{
   "bnpl":{
      "all":[
         {
            "Lazypay":{
               "status":1,
               "kfsLink":"https://",
               "eligible":true,
               "customerLinked":true,
               "PayuToken":"Token12345"
            }
         }
      ]
   }
}
```

| Field          | Description                                                                |
| :------------- | :------------------------------------------------------------------------- |
| status         | Provider status in BNPL context.                                           |
| kfsLink        | Key Fact Statement or disclosure URL when applicable.                      |
| eligible       | Whether LazyPay can be offered for this amount and user context.           |
| customerLinked | Whether the user has completed linking for repeat / one-click style flows. |
| PayuToken      | Token used on subsequent calls when supported by your integration.         |

For additional success and failure shapes (including multi-lender responses), refer to [Get EMI Checkout Details API > Sample response](ref:get-emi-checkout-details-api#sample-response).
