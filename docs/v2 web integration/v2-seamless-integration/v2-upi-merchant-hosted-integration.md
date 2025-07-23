---
title: v2 UPI Integration
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
PayU allows you to collect payments using UPI handles. For the list of UPI providers supported, refer to [UPI Handles](doc:upi-handles).

**Steps to Integrate:**

1. [Validate the UPI handle](#step1-validate-the-vpa-handle)
2. [Initiate the Payment to PayU](#step-2-initiate-the-payment-to-payu)
3. [Verify the payment](#step-3-verify-the-payment)

> 👍 Before you begin:
>
> PayU recommends you to integrate with Test environment initially. For more information, contact you PayU Key Account Manager (KAM) or PayU Support.

## Step 1: Validate the UPI handle

When your customer makes payment through UPI, you can validate the customer's Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle. Validate the VPA (UPI handle) using the **validateVpa** API.  For more information, refer to [Validate VPA Handle API](https://docs.payu.in/v2/reference/v2_validate_vpa_api).

## Step 2: Initiate the payment to PayU

The following parameters vary for the UPI payment mode in the **Collect Payment** API (**v2/payments** API).

<V2_payment_envrionment />

> 📘 Reference:
>
> For the **Try It** experience and response, refer to <a href="https://docs.payu.in/v2/reference/_payment_v2_merchant_hosted_upi" target="_blank">Collect Payments API</a> under API Reference.

### Request Header

<V2_payment_header_params />

### Request Body

The following table describes the request body parameters:

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>accountId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The merchant key provided by PayU during onboarding.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>MERCHANT123</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Transaction ID for transaction tracking and this must be unique for every transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>REF123456</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentMethod<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Contains the payment method details. For UPI, includes name and bankCode.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{ "name": "UPI", "bankCode": "UPI" }</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Contains UPI-specific information including the customer's VPA (UPI handle).</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{ "vpa": "test@payu" }</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

<br />

#### order object

<V2_order_object />

#### callBackActions object

<CallbackActions_object />

#### billingDetails object

<BillingDetails_object />

### Sample request

```curl
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Thu, 27 Mar 2025 10:12:27 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="<signature>"' \
--header 'Content-Type: application/json' \
--data-raw '{
    "accountId": "smsplus",
    "referenceId": "b5f2d8785768087678fn4",
    "currency": "INR",
    "paymentSource": "WEB",
    "paymentMethod": {
        "name": "UPI",
        "bankCode": "UPI"
    },
    "additionalInfo": {
        "vpa": "test@payu"
    },
    "order": {
        "productInfo": "qwertyuiopasdfghjkl",
        "userDefinedFields": {
            "udf1": "",
            "udf2": ""
        },
        "paymentChargeSpecification": {
            "price": "10"
        }
    },
    "callBackActions": {
        "successAction": "https://pp78admin.payu.in/test_response",
        "failureAction": "https://pp78admin.payu.in/test_response",
        "cancelAction": "https://pp78admin.payu.in/test_response"
    },
    "billingDetails": {
        "firstName": "John",
        "lastName": "",
        "phone": "9876543210",
        "email": "testv2@example.in",
        "city": "Bharatpur",
        "state": "Rajasthan",
        "country": "India",
        "zipCode": "321028"
    }
}'
```

### Sample response

<V2_payment_response_params />

```json
{
    "referenceId": "b5f2d8785768087678fm9",
    "paymentId": "1999110000001769",
    "message": "Please call verify api to get the transaction status"
}
```

## Step 3: Verify the payment

After initiating the payment, you must verify the payment status using the **Verify Payment** API. For more information, refer to [Verify Payment API](https://docs.payu.in/v2/reference/verify_payment_api).

The customer can complete the UPI payment through their UPI app, and you can verify the transaction status to confirm the payment.

> 📘 Note:
>
> * The UPI transaction may take some time to complete
> * Always verify the payment status before providing the service to the customer
> * Use the referenceId from the initial request to track the transaction