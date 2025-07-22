---
title: Net Banking - v2 Payment API
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Collect Payment using Net Banking with Merchant Checkout API Reference
  description: >-
    Discover the PayU API Reference for integrating NetBanking payments with
    Merchant Hosted Checkout. Access detailed guides on secure authentication
    and transaction processing NetBanking payments or Net Banking.  Ideal for
    developers looking to incorporate efficient NetBanking, internet banking,
    virtual banking or web banking solutions into their custom checkout systems.
  keywords:
    - Net Banking Merchant Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - Net Banking Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for Net Banking Merchant Hosted Checkout
    - _payment API for Net Banking Merchant Hosted Checkout
    - _payment API simulation for Net Banking Custom Checkout
    - _payment API simulation for Net Banking Merchant Hosted Checkout
    - NetBanking Custom Checkout API Reference
    - NetBanking Merchant Hosted Checkout API Reference
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: collect-payments-with-net-banking-seamless
      title: Net Banking Integration
---
The PayU v2 seamless Net Banking integration allows merchants to collect Net Banking payments directly without redirecting customers to PayU's hosted checkout page.

> 📘 **Note**
>
> This documentation covers **seamless Net Banking** integration. For hosted checkout flows, refer to the [v2 Payment API (Non-Seamless)](doc:v2-payment-api-non-seamless) documentation.

## Environment Details

| Environment | Base URL                              |
| ----------- | ------------------------------------- |
| Test        | `https://apitest.payu.in/v2/payments` |
| Production  | `https://api.payu.in/v2/payments`     |

<br />

<V2_payment_header_params />

## Request body

| Parameter           | Data Type | Required | Description                                                                                                     |
| ------------------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------- |
| `accountId`         | String    | Yes      | Merchant key provided by PayU. Character limit: 50                                                              |
| `referenceId`       | String    | Yes      | Unique reference ID for the transaction. Character limit: 50                                                    |
| `paymentMethod`     | Object    | Yes      | Net Banking payment method details. [See paymentMethod object](#paymentmethod-object)                           |
| `order`             | Object    | Yes      | Order details containing product information and pricing. [See order object](#order-object)                     |
| `billingDetails`    | Object    | Yes      | Customer billing information. [See billingDetails object](#billingdetails-object)                               |
| `callBackActions`   | Object    | No       | Callback URLs for different payment outcomes. [See callBackActions object](#callbackactions-object)             |
| `additionalInfo`    | Object    | Yes      | Additional transaction parameters including flow type. [See additionalInfo object](#additionalinfo-object)      |
| `beneficiaryDetail` | Object    | Yes      | Beneficiary account details for Net Banking transfer. [See beneficiaryDetail object](#beneficiarydetail-object) |

## Object Specifications

### paymentMethod Object

| Parameter  | Data Type | Required | Description                                                                                                                   |
| ---------- | --------- | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `name`     | String    | Yes      | Payment method type. Must be set to `"NetBanking"`. Character limit: 10                                                       |
| `bankCode` | String    | Yes      | Bank code for the selected bank. Character limit: 10. [See Net Banking codes](https://docs.payu.in/v1/docs/net-banking-codes) |

### order Object

<V2_order_object />

### paymentChargeSpecification Object

<V2_paymentChargeSpecification_object />

### billingDetails Object

<BillingDetails_object />

### callBackActions Object

<CallbackActions_object />

### additionalInfo Object

<AdditionalI_Info_object />

### beneficiaryDetail Object

| Parameter                  | Data Type | Required | Description                                                                   |
| -------------------------- | --------- | -------- | ----------------------------------------------------------------------------- |
| `beneficiaryName`          | String    | Yes      | Name of the beneficiary account holder. Character limit: 100                  |
| `beneficiaryAccountNumber` | String    | Yes      | Bank account number of the beneficiary. Character limit: 50                   |
| `beneficiaryAccountType`   | String    | Yes      | Type of beneficiary account (e.g., "SAVINGS", "CURRENT"). Character limit: 20 |

## Sample Request

```bash
curl -X POST \
  https://apitest.payu.in/v2/payments \
  -H 'date: Mon, 05 Oct 2024 11:00:00 GMT' \
  -H 'authorization: HMAC smsplus:4d1ea4e74243ea5b2b5b8b1d8a7b1a2e3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9' \
  -H 'content-type: application/json' \
  -d '{
  "accountId": "smsplus",
  "referenceId": "REF_" + Math.random().toString(36).substring(7),
  "paymentMethod": {
    "name": "NetBanking",
    "bankCode": "EFTAXIS"
  },
  "order": {
    "productInfo": "Net Banking Payment",
    "paymentChargeSpecification": {
      "price": 10000.00,
      "convenienceFee": "NB:15"
    },
    "userDefinedFields": {
      "udf1": "Net Banking Transaction",
      "udf2": "Seamless Payment"
    }
  },
  "billingDetails": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "phone": "9876543210",
    "address": "123 Main Street",
    "city": "New Delhi",
    "state": "Delhi",
    "country": "India",
    "zipCode": "110001"
  },
  "callBackActions": {
    "successAction": "https://merchant.com/success",
    "failureAction": "https://merchant.com/failure",
    "cancelAction": "https://merchant.com/cancel"
  },
  "additionalInfo": {
    "txnFlow": "seamless",
    "createOrder": true,
    "enforcePaymethod": "NB",
    "txnS2sFlow": "2"
  },
  "beneficiaryDetail": {
    "beneficiaryName": "Merchant Account",
    "beneficiaryAccountNumber": "1234567890",
    "beneficiaryAccountType": "SAVINGS"
  }
}'
```

## Response

### Response Parameters

| Parameter     | Data Type | Description                                        |
| ------------- | --------- | -------------------------------------------------- |
| `referenceId` | String    | The reference ID sent in the request               |
| `paymentId`   | String    | Unique payment ID generated by PayU                |
| `status`      | String    | Payment status (SUCCESS, FAILED, PENDING)          |
| `message`     | String    | Status message describing the payment state        |
| `redirectUrl` | String    | URL for customer redirection (if required by bank) |
| `orderId`     | String    | Order ID (returned when createOrder is enabled)    |

### Sample Response

```json
{
  "referenceId": "REF_abc123",
  "paymentId": "10012345678",
  "status": "PENDING",
  "message": "Transaction initiated successfully. Please verify the payment status.",
  "redirectUrl": "https://bankportal.com/authenticate?txnid=abc123",
  "orderId": "order_789012"
}
```

## Verify Payment

> ⚠️ **Important**
>
> After creating a payment, you **must** call the [Verify Payment API](doc:verify-payment-api) to get the final transaction status. Net Banking transactions may require additional verification steps.

## Error Responses

### Error Response Format

```json
{
  "status": "FAILED",
  "message": "Invalid bank code provided",
  "errorCode": "E001",
  "details": [
    {
      "field": "paymentMethod.bankCode",
      "message": "Bank code TESTNB is not supported"
    }
  ]
}
```

**Common Error Codes:**

* `E001`: Invalid request parameters
* `E002`: Authentication failed
* `E003`: Merchant not found
* `E004`: Transaction limit exceeded
* `E005`: Bank service unavailable
* `E006`: Invalid beneficiary details

## Related APIs

* [Get Net Banking Status API](https://docs.payu.in/v1/reference/get_net_banking_status_api)
* [Verify Payment API](doc:verify-payment-api)
* [Refund API](doc:refund-api)
* [Get Transaction Details API](doc:get-transaction-details-api)
* [Create Order API](doc:create-order-api)