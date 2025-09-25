---
title: TWID Pay Redemption Integraiton
deprecated: false
hidden: true
metadata:
  robots: index
---
Integrate TWID pay to enable customers to redeem their TWID loyalty points during checkout. Follow these sequential steps to implement a complete TWID pay solution.

> 📘 Header-based authentication
>
> All the APIs mentioned in this section uses the following header-based authentication. Include the following headers in all API requests:
>
> ```http
> Authorization: Bearer {API_KEY}
> Content-Type: application/json
> X-Merchant-Key: {MERCHANT_KEY}
> ```



## Overview
This documentation provides the complete integration guide for TWID Pay API, enabling merchants to integrate TWID points as a payment method in their applications.

## Base URLs
- **Production**: `https://api.payu.in/loyalty-points/`
- **Test**: `https://apitest.payu.in/loyalty-points/`

## Authentication

### For Non-Seamless Merchants
Add the following header to all API requests:
```http
mid: {MERCHANT_ID}
```

### For Seamless Merchants
Add the following headers to all API requests:
```http
Date: {DATE_IN_GMT_FORMAT}
Authorization: hmac username="{MERCHANT_KEY}", algorithm="sha512", headers="date", signature="{FULL_BODY_HASH}"
```

**Date Format**: `"EEE, dd MMM yyyy HH:mm:ss 'GMT'"`

**Note**: The signature (fullBodyHash) is generated using SHA512 algorithm. Refer to PayU documentation for signature generation details.

## API Integration Steps

<details>
<summary><strong>Step 1: Fetch Balance API</strong></summary>

The Fetch Balance API is used to retrieve TWID points balance for a customer. This endpoint allows you to check the available TWID points that can be used for a transaction before proceeding with the payment process.

**Endpoint**: `POST {{loyalty-service-url}}/v1/balance`

<details>
<summary><strong>Request Parameters</strong></summary>

| Parameter                 | Description                                                         | Example                                    |
| ------------------------- | ------------------------------------------------------------------- | ------------------------------------------ |
| loyaltyProvider           | `String` - The loyalty provider for the response                    | `"TWID"`                                   |
| mobileNumber              | `String` - Customer's mobile number                                 | `"88001085**"`                             |
| fetchRevisedEarn          | `Boolean` - Whether to fetch revised earn points                    | `true`                                     |
| orderAmount               | `Number` - Total order amount                                       | `1000`                                     |

</details>

<details>
<summary><strong>Sample Request</strong></summary>

```json
{
  "loyaltyProvider": "TWID",
  "mobileNumber": "88001085**",
  "fetchRevisedEarn": true,
  "orderAmount": 1000
}
```

</details>

<details>
<summary><strong>Sample Response</strong></summary>

```json
{
  "loyaltyProvider": "TWID",
  "usableAmount": 500.0,
  "usablePoints": 500,
  "title": "Save Rs 500 using 500 twid Cash Points",
  "rewardId": 270943,
  "earnConfig": {
    "points": 0
  },
  "issuerDetailDTO": {
    "brandName": "TWID Cash",
    "logo": "https://cdn.twidpay.com/..."
  },
  "holdApplicable": false
}
```

</details>

</details>

<details>
<summary><strong>Step 2: Hold TWID Coins API</strong></summary>

The Hold TWID Coins API is used to hold or reserve TWID points for a transaction. This step ensures that the required points are temporarily blocked for the transaction, preventing them from being used elsewhere during the payment process.

**Endpoint**: `POST {{loyalty-service-url}}/payment/v1/createPayment`

<details>
<summary><strong>Request Parameters</strong></summary>

| Parameter | Description | Example |
|-----------|-------------|---------|
| surl `optional` | `String` - Success URL after holding points | `"http://api.payu.in/success"` |
| furl `optional` | `String` - Failure URL after holding points | `"http://api.payu.in/failure"` |
| merchantKey `mandatory` | `String` - PayU merchant key for authentication | `"18001"` |
| parentPayuTxnId `mandatory` | `String` - Parent transaction ID from main payment transaction | `"65646400234509041"` |
| totalAmount `mandatory` | `Number` - Total monetary reward amount to be held/redeemed | `1000` |
| mobile `mandatory` | `String` - User's mobile number | `"9304204**"` |
| email `optional` | `String` - User's email address | `"test@gmail.com"` |
| loyaltyProvider `mandatory` | `String` - Loyalty provider identifier | `"TWID"` |
| rewardId `mandatory` | `Number` - Reward ID from balance API response | `270940` |
| currency `mandatory` | `String` - Currency code | `"INR"` |
| orderAmount `mandatory` | `Number` - Total order/bill amount for transaction | `10000` |

</details>

<details>
<summary><strong>Sample Request</strong></summary>

```json
{
  "surl": "http://api.payu.in/success",
  "furl": "http://api.payu.in/failure",
  "merchantKey": "18001",
  "parentPayuTxnId": "65646400234509041",
  "totalAmount": 1000,
  "mobile": "9304204**",
  "email": "test@gmail.com",
  "loyaltyProvider": "TWID",
  "rewardId": 270940,
  "currency": "INR",
  "orderAmount": 10000
}
```

</details>

<details>
<summary><strong>Sample Response</strong></summary>

```json
{
  "statusCode": 1,
  "status": "PENDING",
  "loyaltyTxnId": "d1dce98d-98ec-4b90-a7d8-853fee82a113"
}
```

</details>

</details>

<details>
<summary><strong>Step 3: Redeem TWID Points API</strong></summary>

The Redeem TWID Points API is used to complete the redemption of held TWID points. This is the final step that confirms the transaction and deducts the points from the customer's account after successful payment processing.

**Endpoint**: `POST {{loyalty-service-url}}/payment/v1/continue`

<details>
<summary><strong>Request Parameters</strong></summary>

| Parameter | Description | Example |
|-----------|-------------|---------|
| loyaltyTxnId `mandatory` | `String` - Reference ID provided by the Loyalty-Service during the Create Payment call | `"bd1a77b6-1596-46e1-b79f-2770bcb636c7"` |
| loyaltyProvider `mandatory` | `String` - The loyalty provider identifier (e.g., TWID) | `"TWID"` |

</details>

<details>
<summary><strong>Sample Request</strong></summary>

```json
{
  "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
  "loyaltyProvider": "TWID"
}
```

</details>

<details>
<summary><strong>Sample Response</strong></summary>

```json
{
  "status": "SUCCESS",
  "loyaltyTxnId": "1821b1e2-34dd-47e3-9b54-b56b9d352a6b",
  "rewardPartnerRefId": "7251637276230479872"
}
```

</details>

</details>

<details>
<summary><strong>Step 4: Transaction Enquiry API (Optional)</strong></summary>

The Transaction Enquiry API is used to query the status and details of TWID transactions. This optional step allows you to check the current status of any transaction using either the loyalty transaction ID or PayU transaction ID.

**Endpoint**: `POST {{loyalty-service-url}}/payment/v1/enquiry`

<details>
<summary><strong>Request Parameters</strong></summary>

| Parameter | Description | Example |
|-----------|-------------|---------|
| loyaltyTxnId `optional` | `String` - Reference ID generated during Create Payment or Redeem TWID Points calls | `"bd1a77b6-1596-46e1-b79f-2770bcb636c7"` |
| payuTxnId `optional` | `String` - PayU transaction ID | `"89887897898"` |

**Note**: At least one parameter must be provided

</details>

<details>
<summary><strong>Sample Request</strong></summary>

```json
{
  "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
  "payuTxnId": "89887897898"
}
```

</details>

<details>
<summary><strong>Sample Response</strong></summary>

```json
{
  "status": "SUCCESS",
  "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
  "payuTxnId": "89887897898",
  "transactionDetails": {
    "amount": 1000,
    "currency": "INR",
    "points": 500,
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

</details>

</details>

## Integration Flow

The complete integration flow follows these steps:
1. **Fetch Balance**: Check available TWID points for the customer
2. **Hold Points**: Reserve the required points for the transaction
3. **Process Payment**: Complete the main payment transaction
4. **Redeem Points**: Confirm and deduct the points from customer account
5. **Enquiry** (Optional): Check transaction status if needed

## Error Handling

All APIs may return error responses. Implement proper error handling for:
- Invalid parameters
- Insufficient balance
- Authentication failures
- Network timeouts
- Server errors

## Security Best Practices

1. **Secure Storage**: Store API keys and merchant credentials securely
2. **HTTPS Only**: All API calls must use HTTPS
3. **Input Validation**: Validate all input parameters before API calls
4. **Error Logging**: Log errors for debugging but avoid logging sensitive data
5. **Timeout Handling**: Implement appropriate timeout values for API calls
