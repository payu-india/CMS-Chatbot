---
title: UPI Flow - v2 Payment API
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The UPI Seamless Integration allows merchants to process UPI payments directly through a server-to-server (S2S) flow without redirecting customers to external payment pages. This integration provides a smooth payment experience by handling UPI transactions programmatically using the customer's Virtual Payment Address (VPA).

## When to Use UPI Seamless Integration

Use this integration when:

* You want to accept UPI payments without redirecting customers away from your platform
* Your customers prefer to stay on your application during the payment process
* You need to integrate UPI payments into mobile apps or web applications seamlessly
* You want to provide a faster checkout experience for UPI users

### Environment

<V2_payment_envrionment />

## Request header

<V2_payment_header_params />

## Request parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>accountId<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The merchant key provided by PayU during onboarding.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>UMXDPA</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnId<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Transaction ID provided by the merchant and this must be unique for every transaction.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ZP6267f0d2996ce</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Additional information including S2S flow configuration and redirect flow settings. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>callBackActions<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Actions to perform on the payment server in different scenarios. For more information, refer to <a href="#callbackactions-object-fields-description">callBackActions object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingDetails<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Billing details of the customer including name, address, phone number, email, etc. For more information, refer to <a href="#billingdetails-object-fields-description">billingDetails object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## paymentMethod object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>name<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the payment mode code. For UPI, use "UPI."</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>UPI</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankCode<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the card type code. For more information, refer to <a href="https://docs.payu.in/v1/docs/card-type-codes-and-supported-banks-for-cards">Card Type Codes and Supported Banks for Cards</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>CC</p></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### order object fields description

<V2_order_object />

### additionalInfo object fields description

<AdditionalI_Info_object />

### callbackActions object fields description

<CallbackActions_object />

### billingDetails object fields description

<BillingDetails_object />

## Sample request

```bash
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Thu, 27 Mar 2025 10:12:27 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="ec84843a663143bb86c46b46c5c5ccae8c2cf6b9beb3e14d0be04119daffe83f2de2a8e28c20cb0c1c8e23d5e86e5cbdc5774e6a2e9a7186e1b8b9b6f8a8b9c8c1e3c4c5c1a3c7c9b7b2a1a3e7e8e9c8c1e3c4c5c1a3c7c9b7b2a1a"' \
--header 'Content-Type: application/json' \
--data-raw '{
  "accountId": "KOEfPI",
  "txnId": "Test123UPI",
  "amount": 424.38,
  "paymentMethod": {
    "name": "UPI",
    "bankCode": "NB",
    "upi": {
      "vpa": "xyz@axis"
    }
  },
  "order": {
    "productInfo": "Example Product",
    "paymentChargeSpecification": {
      "price": 424.38,
      "netAmountDebit": 424.38
    }
  },
  "additionalInfo": {
    "vpa": "xyz@axis", 
    "txnFlow": "seamless",
    "createOrder": "true"
  },
  "callBackActions": {
    "successAction": "https://merchantwebsite.com/success",
    "failureAction": "https://merchantwebsite.com/failure"
  },
  "billingDetails": {
    "firstName": "John",
    "phone": "9876543210",
    "email": "john_doe@example.com"
  }
}'
```

## Sample response

```json
{
  "result": {
    "redirectUrl": "https://secure.payu.in/ResponseHandler.php",
    "authAction": "https://api.payu.in/payments/21667772394/otps",
    "paymentId": "21667772394",
    "redirectTemplate": "<html><body><form name='payment_post' id='payment_post' action='https://upi.return.url' method='post'></form></body></html>",
    "upi": {
      "amount": "424.38",
      "merchantVpa": "facebookadsmanager.payu@hdfcbank", 
      "intentURIData": "pa=facebookadsmanager.payu@hdfcbank&pn=Facebook India Online Services Private Limited&tr=21667772414&tid=PPPL21667772XXXXXXXXXXXX0016744c229&am=424.38&cu=INR&tn=UPIIntent",
      "merchantName": "FacebookIndiaOnlineServicesPrivateLimited"
    }
  },
  "orderId": "b5f2d8785768087678f4",
  "status": "PENDING"
}
```

## Response Parameters

<V2_payment_response_params />

## UPI-Specific Response Parameters

For UPI payments, the response includes additional UPI-specific fields:

| Parameter             | Description                               |
| --------------------- | ----------------------------------------- |
| **upi.amount**        | Transaction amount for UPI payment        |
| **upi.merchantVpa**   | Merchant's VPA for receiving payment      |
| **upi.intentURIData** | UPI intent data for payment apps          |
| **upi.merchantName**  | Merchant name displayed in UPI apps       |
| **orderId**           | Generated order ID if createOrder is true |

## Implementation Steps

### Step 1: Collect Customer VPA

Obtain the customer's Virtual Payment Address (VPA) through your application interface. The VPA format is typically `username@bankname` (e.g., `customer@paytm`, `user@googlepay`).

### Step 2: Create Payment Request

Submit the payment request with the customer's VPA and all required parameters as shown in the sample request above.

### Step 3: Handle UPI Response

Process the response which contains:

* **UPI Intent Data**: Use for triggering UPI apps on mobile devices
* **Payment ID**: For tracking and verification
* **Merchant VPA**: For displaying payment details

### Step 4: Verify Payment Status

Always call the Verify Payment API to confirm the final transaction status:

```bash
curl --location 'https://apitest.payu.in/v2/payments/verify' \
--header 'date: Thu, 27 Mar 2025 10:12:27 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="your_signature_here"' \
--header 'Content-Type: application/json' \
--data-raw '{
  "txnId": ["Test123UPI"]
}'
```

## UPI Integration Flow Types

### 1. Intent-Based Flow

For mobile applications, use the UPI intent data to launch UPI-enabled apps:

* Extract `intentURIData` from the response
* Trigger UPI app with the intent data
* Handle the callback from UPI apps

### 2. Collect Request Flow

For web applications or when customer needs to enter UPI PIN:

* Present QR code or payment details
* Allow customer to complete payment in their UPI app
* Poll for payment status updates

### 3. Direct VPA Flow

When customer provides VPA directly:

* Validate VPA format
* Submit payment request with VPA
* Handle authentication if required