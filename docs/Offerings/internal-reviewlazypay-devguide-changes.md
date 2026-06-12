---
title: '[Internal Review]Lazypay Devguide Changes'
deprecated: false
hidden: true
metadata:
  robots: index
---
Use this section when you want **LazyPay** as a <Glossary>BNPL</Glossary> option on **your own checkout** (merchant hosted or seamless flow): you call PayU’s eligibility service, collect payment with the **`/_payment`** API, then verify the outcome on your servers. LazyPay lets customers pay later on their billing cycle while you settle with PayU as for other BNPL instruments.

This section describes how to integrate **LazyPay-specific** and uses **Get EMI / BNPL checkout details** for eligibility. For the **generic** merchant-hosted BNPL flow that starts from **Get Checkout Details**, see [Merchant Hosted BNPL Workflow](doc:general-flow-bnpl-integration-with-merchant-hosted). For PayU-hosted checkout (customer pays on PayU’s page), see [PayU Hosted Checkout BNPL Workflow](doc:bnpl-workflow-payu-hosted-checkout).



### Set 1 — Eligibility: header-authenticated JSON (Get EMI / BNPL checkout details)

| | |
| :-- | :-- |
| **Purpose** | Check LazyPay BNPL eligibility before you show LazyPay or post payment. |
| **HTTP** | `POST` to **`/info/linkAndPay/get_emi_checkout_details`** (see [Get EMI / BNPL Checkout Details API (LazyPay)](ref:get-emi-bnpl-checkout-details-lazypay)). |
| **Body** | JSON (`Content-Type: application/json`). |
| **Authentication** | **Request headers** — build **`Date`**, **`Digest`** (Base64 of SHA256 of the JSON body where applicable), and **`Authorization`** (HMAC scheme over `Date` / `Digest`), plus headers such as **`platformId`** and, in many samples, **`x-credential-username`**. Exact variants are in [Get EMI Checkout Details API](ref:get-emi-checkout-details-api). |
| **Not used here** | The **`hash`** field used on merchant-hosted **`/_payment`** (Set 2). |

### Set 2 — Collect payment: classic merchant-hosted `/_payment` (hash in POST body)

| | |
| :-- | :-- |
| **Purpose** | Charge the customer through LazyPay after eligibility succeeds. |
| **HTTP** | `POST` to **`/_payment`** (`https://test.payu.in/_payment` / `https://secure.payu.in/_payment` in typical integrations). |
| **Body** | `application/x-www-form-urlencoded` (form post or equivalent). |
| **Authentication** | **`hash`** parameter **in the form body**, computed per PayU merchant-hosted rules (see [Hashing request and response](doc:hashing-request-and-response) and `<HashingRequestParameters />` in Step 2). |
| **Not used here** | The **Get EMI / BNPL checkout details** header scheme from Set 1. |

### PayU `v2/payments` (separate collect-payment surface)

PayU also documents a **`POST /v2/payments`** collect path (for example `https://test.payu.in/v2/payments` in test — see internal blocks such as `V2_paymentEnvironment` and product guides like [Mobikwik Link Pay — Payment Initiation](doc:steps-to-integrate-mobikwik-link-pay)). That surface is **not** the same URL as **`/_payment`**, and signing/header rules can differ by product.

**There is no LazyPay-specific `LAZYPAY` + `v2/payments` page in this repository.** The LazyPay merchant-hosted flow on **this** guide is **Set 1 (headers) + Set 2 (`/_payment` + body hash)** only. If your integration pack or **PayU Key Account Manager (KAM)** specifies **`v2/payments`** for LazyPay, follow that pack and the official **v2** API reference—do not assume this page’s `/_payment` samples apply unchanged.

## Benefits for your customers

* Pay later with LazyPay on eligible purchases, subject to lender rules and approval.
* Checkout stays on your experience (no full redirect to a separate PayU payment page for the whole journey).
* Eligibility can be checked up front so LazyPay is shown only when the customer can use it.

## Benefits for your business

* You control layout, fields, and when to surface LazyPay (based on eligibility API responses).
* Standard PayU **hash**, **redirect**, and **verification** patterns apply, consistent with other merchant-hosted modes.
* You can align LazyPay with your wider BNPL or affordability strategy using the same PayU keys and reconciliation tools.

## Refunds

**LazyPay supports both full and partial refunds** on settled BNPL transactions (subject to PayU and lender rules). At a high level:

1. You **initiate the refund** (full or partial) against the original PayU transaction.
2. **PayU forwards the refund** to LazyPay for the same amount.
3. **LazyPay credits** the customer’s LazyPay balance and adjusts their account or billing position per LazyPay’s policy.
4. The **merchant settlement** is adjusted accordingly (for example the refunded amount is recovered from your account or future settlement).

You may run **multiple partial refunds** until the cumulative refunded amount does not exceed the original transaction amount. **Processing fees, GST, and lender charges** may or may not be reversed depending on lender and PayU policy—see the detailed notes in [Refunds for BNPL](doc:refunds-for-bnpl).

Internal **refund routing** (existing PayU PIH path vs LSP path) is shown in the **LazyPay Advance PIH** materials under [`PRDs/Lazypay/`](../../../../PRDs/Lazypay/README.md); merchant-facing refund initiation still uses the same PayU refund flows documented for BNPL.

<Callout icon="📘" theme="info">
  **Before you begin**

  * LazyPay and BNPL must be **enabled and configured** on your merchant account. For enablement, configuration, onboarding, and **test mobile whitelisting** for LazyPay, work with your **PayU Key Account Manager (KAM)**.
  * Use **HTTPS** for **`surl`** and **`furl`**. Plan for **server-side verification** of each transaction; do not treat the browser redirect alone as proof of payment.
  * For the **`bankcode`** value and other BNPL lenders, see [BNPL Codes](doc:bnpl-codes). For first-time vs repeat customer behaviour (linking, OTP, tokens) at the product level, see [BNPL Link and Pay](doc:collect-payments-with-bnpl-using-link-and-pay). For the BNPL product hub in this guide set, see [BNPL Integration](doc:payu-bnpl-integration-introduction).
</Callout>


> 🚧 Minimum amount for BNPL transaction
>
> Minimum amounts can vary by lender. Confirm allowed limits with your **PayU Key Account Manager (KAM)**.

##Eligibility Check for Lazypay
### Sample request

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

> 📘 Authorization calculation logic
>
> For authorization calculation logic, refer to [Get EMI Checkout Details API > Required parameters for calculating authorization](ref:get-emi-checkout-details-api#required-parameters-for-calculating-authorization).

### Sample response

* Success scenario (LazyPay in bnpl block)

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

| Field | Description |
| :-- | :-- |
| status | Provider status in BNPL context. |
| kfsLink | Key Fact Statement or disclosure URL when applicable. |
| eligible | Whether LazyPay can be offered for this amount and user context. |
| customerLinked | Whether the user has completed linking for repeat / one-click style flows. |
| PayuToken | Token used on subsequent calls when supported by your integration. |

For additional success and failure shapes (including multi-lender responses), refer to [Get EMI Checkout Details API > Sample response](ref:get-emi-checkout-details-api#sample-response).
