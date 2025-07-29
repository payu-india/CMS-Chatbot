---
title: ' UPI Integration'
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
PayU allows you to collect payments using UPI handles with seamless integration. For the list of UPI providers supported, refer to <Anchor label="UPI Handles" target="_blank" href="https://docs.payu.in/docs/upi-handles/">UPI Handles</Anchor>.

**Steps to Integrate:**

1. [Validate the UPI handle](#step1-validate-the-vpa-handle)
2. [Initiate the Payment to PayU](#step-2-initiate-the-payment-to-payu)
3. [Verify the payment](#step-3-verify-the-payment)

> 👍 Before you begin:
>
> PayU recommends you to integrate with Test environment initially. For more information, contact you PayU Key Account Manager (KAM) or PayU Support.

## Step 1: Validate the UPI handle

When your customer makes payment through UPI, you can validate the customer's Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle. Validate the VPA (UPI handle) using the **validateVpa** API.  For more information, refer to <Anchor label="Validate VPA Handle API" target="_blank" href="https://docs.payu.in/v2/reference/v2-validate-vpa-api/">Validate VPA Handle API</Anchor>.

## Step 2: Initiate the payment to PayU

The following parameters vary for the UPI payment mode in the **Collect Payment** API (**v2/payments** API).

### Environment

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Contains the payment method details. For UPI, includes name and bankCode. For more information, refer to <a href="#paymentmethod-object" additonalInfo object</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{ "name": "UPI", "bankCode": "UPI" }</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Contains UPI-specific information including the customer's VPA (UPI handle). For more information, refer to <a href="#additonalinfo-object" additonalInfo object</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{"vpa": "test@payu", "txnS2sFlow": "seamless"}</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>callBackActions<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Actions to perform on the payment server in different scenarios. For more information, refer to <a href="#callbackactions-object-fields-description">callBackActions object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingDetails<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Billing details of the customer including name, address, phone number, email, etc. For more information, refer to <a href="#billingdetails-object-fields-description">billingDetails object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>

</tbody>
</table>
`}</HTMLBlock>

#### paymentMethod object

<Accordion title="paymentMethod object" icon="fa-code">
  <HTMLBlock>{`
                                    <table style="width: 100%; border-collapse: collapse;">
                                    <thead>
                                    <tr>
                                      <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
                                      <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
                                      <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <tr>
                                      <td style="border: 1px solid #ddd; padding: 8px;"><strong>name</strong><br/><code>mandatory</code></td>
                                      <td style="border: 1px solid #ddd; padding: 8px;">Represents the payment method used. For UPI, use UPI</td>
                                      <td style="border: 1px solid #ddd; padding: 8px;">UPI</td>
                                    </tr>
                                    <tr>
                                      <td style="border: 1px solid #ddd; padding: 8px;"><strong>bankCode</strong><br/><code>mandatory</code></td>
                                      <td style="border: 1px solid #ddd; padding: 8px;">Contains the bank code.For UPI, use UPI</td>
                                      <td style="border: 1px solid #ddd; padding: 8px;">UPI</td>
                                    </tr>
                                    </tbody>
                                    </table>
  `}</HTMLBlock>
</Accordion>

<br />

#### order object

<Accordion title="order object" icon="fa-code">
  <V2_order_object />
</Accordion>

#### callBackActions object

<Accordion title="callBackActions object" icon="fa-code">
  <CallbackActions_object />
</Accordion>

#### billingDetails object

<Accordion title="billingDetails object" icon="fa-code">
  <BillingDetails_object />
</Accordion>

#### additionalInfo object

<Accordion title="Additional Info Object" icon="fa-code">
  <HTMLBlock>{`
                                                              <table style="width: 100%; border-collapse: collapse;">
                                                              <thead>
                                                              <tr>
                                                                <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
                                                                <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
                                                                <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
                                                              </tr>
                                                              </thead>
                                                              <tbody>
                                                              <tr>
                                                                <td style="border: 1px solid #ddd; padding: 8px;"><strong>partnerHoldTime</strong><br/><code>optional</code></td>
                                                                <td style="border: 1px solid #ddd; padding: 8px;">Time held by the partner for the transaction.</td>
                                                                <td style="border: 1px solid #ddd; padding: 8px;">60</td>
                                                              </tr>
                                                              <tr>
                                                                <td style="border: 1px solid #ddd; padding: 8px;"><strong>createOrder</strong><br/><code>optional</code></td>
                                                                <td style="border: 1px solid #ddd; padding: 8px;">A flag to store the order details (true/false).</td>
                                                                <td style="border: 1px solid #ddd; padding: 8px;">true</td>
                                                              </tr>
                                                              <tr>
                                                                <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnFlow</strong><br/><code>optional</code></td>
                                                                <td style="border: 1px solid #ddd; padding: 8px;">For defining seamless/non-seamless flows in handling payments.</td>
                                                                <td style="border: 1px solid #ddd; padding: 8px;">seamless</td>
                                                              </tr>
                                                              </tbody>
                                                              </table>
  `}</HTMLBlock>
</Accordion>

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
        "vpa": "test@payu",
         "txnFlow": "seamless"
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

After initiating the payment, you must verify the payment status using the **Verify Payment** API. For more information, refer to <Anchor label="Verify Payment API" target="_blank" href="https://docs.payu.in/v2/reference/v2_verify_payment_api#/">Verify Payment API</Anchor>.

The customer can complete the UPI payment through their UPI app, and you can verify the transaction status to confirm the payment.

> 📘 Note:
>
> * The UPI transaction may take some time to complete
> * Always verify the payment status before providing the service to the customer
> * Use the referenceId from the initial request to track the transaction