---
title: S2S UPI Integration
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
In UPI Collect, the sequence of APIs is called to follow for redirection less experience.

### **Steps to Integrate**

1. [Validate VPA](#step-1-validate-vpa)
2. [Initiate the payment to PayU](#step-2-initiate-the-payment-to-payu)
3. [Check UPI Transaction Status](#step-3-check-upi-transaction-status)

> 👍 Before you begin:
>
> PayU recommends you to integrate with Test environment initially. For more information, contact you PayU Key Account Manager (KAM) or PayU Support.

<br />

## Step 1: Validate VPA

This web service will let you validate VPA if it is a valid VPA or not.

After the customer enters VPA on your website, you need to call this API to check for VPA validation. If VPA is valid, you need to proceed with the next step. For a sample request or response, refer to  <a href="v2_validate_vpa_api" target="_blank"> Validate VPA</a>.

Collect the response in the  <a href="https://docs.payu.in/v2/reference/v2_payment_s2s_upi_collection" target="_blank"> UPI Collection</a> under API Reference. The response for the S2S payment request is not similar to Merchant Hosted or PayU Hosted Checkout. For description of response parameters, refer to <a href="addl_info-payment-apis" target="_blank"> Additional Info for Payment APIs</a>.

## Step 2: Initiate the payment to PayU

To start with, the request is raised from the Merchant to PayU with the required transaction mandatory/optional parameters. This needs to be a server-to-server curl call request. This API is used for both Cards and UPI for generating a new transaction. Parameters and their descriptions are mentioned below.

For the "Try It" experience, refer to <a href="https://docs.payu.in/v2/reference/_payment_s2s_upi_collection" target="_blank"> UPI Collection</a>.
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
<Accordion title="paymentMethod object" icon="fa-code">
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
</Accordion>

### order object fields description
<Accordion title="order object" icon="fa-code">
<V2_order_object />
</Accordion>

### additionalInfo object fields description
<Accordion title="addtionalInfo object" icon="fa-code">
<AdditionalI_Info_object />
</Accordion>

### callbackActions object fields description
<Accordion title="callbackActions object" icon="fa-code">
<CallbackActions_object />
</Accordion>

### billingDetails object fields description
<Accordion title="billingDetails object" icon="fa-code">
<BillingDetails_object />
</Accordion>

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

### Response Parameters

| Field                 | Description                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------- |
| redirectUrl           | URL to which the user is redirected after the payment process is completed.                       |
| authAction            | URL for authentication actions like OTP submission during the payment process.                    |
| paymentId             | Unique identifier for the payment transaction.                                                    |
| redirectTemplate      | Encoded HTML template used for auto-redirecting or displaying information post-payment.           |
| card.binData          | Contains information about the card used in the transaction.                                      |
| card.pureS2SSupported | Boolean indicating if the card supports pure server-to-server transactions.                       |
| card.issuingBank      | Name of the bank that issued the card.                                                            |
| card.category         | Category of the card, e.g., credit card, debit card.                                              |
| card.cardType         | Type of the card, for example, MAST for Mastercard.                                               |
| card.isDomestic       | Boolean indicating if the card is a domestic card (issued within the country of the transaction). |

## Step 3: Check UPI transaction status

### Sample response

```
{
  "result": {
    "redirectUrl": "https://secure.payu.in/ResponseHandler.php",
    "authAction": "https://api.payu.in/payments/21667772394/otps",
    "paymentId": "21667772394",
    "redirectTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vbmV0YmFua2luZy5oZGZjYmFuay5jb20vbmV0YmFua2luZy9tZXJjaGFudD9DbGllbnRDb2RlPTE1NDkxMyZNZXJjaGFudENvZGU9UEFZVUZBQ0VCT09LJlR4bkN1cnJlbmN5PUlOUiZUeG5BbW91bnQ9MjUwMDAuMDAmVHhuU2NBbW91bnQ9MCZNZXJjaGFudFJlZk5vPWs0cWh3NGVsYXY2MmxwNjJjbSZTdWNjZXNzU3RhdGljRmxhZz1OJkZhaWx1cmVTdGF0aWNGbGFnPU4mRGF0ZT0yNi8xMS8yMDI0IDAwOjAwOjAwJlJlZjE9JlJlZjI9NDAzYmIzODkxY2Y5NGEzNmI0ZGQxOTlkOWNjZWVjNmUmUmVmMz0mUmVmND0mUmVmNT0mRHluYW1pY1VybD1odHRwczovL3NlY3VyZS5wYXl1LmluL2I0NDdmZmViZDg4NDNjZTEzYzlmODVhZjhlOTA0ZmQyL0NvbW1vblBnUmVzcG9uc2VIYW5kbGVyLnBocCZDaGVja1N1bT0zMTAxMzgyNDM2IiBtZXRob2Q9InBvc3QiPjwvZm9ybT48c2NyaXB0IHR5cGU9J3RleHQvamF2YXNjcmlwdCc+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB3aW5kb3cub25sb2FkPWZ1bmN0aW9uKCl7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZG9jdW1lbnQuZm9ybXNbJ3BheW1lbnRfcG9zdCddLnN1Ym1pdCgpOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgICAgICAgICA8L3NjcmlwdD48L2JvZHk+PC9odG1sPg==",
    "card": {
      "binData": {
        "pureS2SSupported": false,
        "issuingBank": "INDUSIND",
        "category": "upi",
      }
    }
  },
  "status": "PENDING"
}
```

Check the UPI transaction status using the **Verify Payment API** (verify\_payment) API. For more information, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api).