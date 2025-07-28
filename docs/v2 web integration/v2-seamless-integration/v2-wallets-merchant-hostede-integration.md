---
title: Wallets Integration
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
You can collect payments from customers with leading wallets using the Merchant Hosted integration. You need to ensure that **Wallet** for the **paymentMethod.name** field and wallet code based on the desired wallet for the **paymentMethod.bankCode** parameter is posted.

**Steps to Integrate**

1. [Initiate the payment with PayU](#step-1-initiate-the-payment-with-payu)
2. [Verify Payment](#step-2-verify-the-payment)

<V2_Prerequisite_Payment_Integration />

## Step 1: Initiate the payment with PayU

The following parameters vary for the Wallet payment mode in the **Collect Payment** API (**v2/payments** API).

<V2_payment_envrionment />

> 📘 Reference:
>
> For the API reference, refer to <a href="https://docs.payu.in/v2/reference/collect_v2_payment_wallet" target="_blank">Collect Payments API</a> under API Reference.

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>referenceId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Reference ID for transaction tracking and this must be unique for every transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>REF123456</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentMethod<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Contains the payment method details. For wallet payments, includes name and bankCode for the specific wallet.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{ "name": "Wallet", "bankCode": "PAYTM" }</p>
</td>
</tr>
<tr>
<td>order<br/><code>mandatory</code></td>
<td>Order details containing product information and pricing. <a href="#order-object">See order object</a></td>
<td><code>{"productInfo": "Wallets Integration", "paymentChargeSpecification": {"price": 10000.00}}</code></td>
</tr>
<tr>
<td>billingDetails<br/><code>mandatory</code></td>
<td>Customer billing information. <a href="#billingdetails-object">See billingDetails object</a></td>
<td><code>{"firstName": "John", "email": "john@example.com", "phone": "9876543210"}</code></td>
</tr>
<tr>
<td>callBackActions<br/><code>optional</code></td>
<td>Callback URLs for different payment outcomes. <a href="#callbackactions-object">See callBackActions object</a></td>
<td><code>{"successAction": "https://merchant.com/success", "failureAction": "https://merchant.com/failure"}</code></td>
</tr>
<tr>
<td>additionalInfo<br/><code>mandatory</code></td>
<td>Additional transaction parameters including flow type. <a href="#additionalinfo-object">See additionalInfo object</a></td>
<td><code>{"txnFlow": "seamless"}</code></td>
</tr>
<tr>

</tbody>
</table>
`}</HTMLBlock>

<br />

#### order object

<Accordion title="order Object" icon="fa-code">
  <V2_order_object />
</Accordion>

#### callBackActions object

<Accordion title="callBackActions Object" icon="fa-code">
  <CallbackActions_object />
</Accordion>

#### billingDetails object

<Accordion title="billingDetails Object" icon="fa-code">
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
curl --location 'https://apitest.payu.in/v2/payments' \\
--header 'date: Thu, 27 Mar 2025 10:12:27 GMT' \\
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="<signature>"' \\
--header 'Content-Type: application/json' \\
--data-raw '{
    "accountId": "smsplus",
    "referenceId": "b5f2d8785768087678fn4",
    "currency": "INR",
    "paymentSource": "WEB",
    "paymentMethod": {
        "name": "Wallet",
        "bankCode": "PAYTM"
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
        "firstName": "sartaj",
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

## Step 2: Verify the payment

After initiating the payment, you must verify the payment status using the **Verify Payment** API. For more information, refer to [Verify Payment API](https://docs.payu.in/v2/reference/verify_payment_api).

The customer will be redirected to the wallet provider (e.g., Paytm) to complete the payment, and you can verify the transaction status to confirm the payment.

> 📘 Note:
>
> * The wallet transaction may take some time to complete
> * Always verify the payment status before providing the service to the customer
> * Use the referenceId from the initial request to track the transaction
> * For supported wallet codes, refer to [Wallet Codes](https://docs.payu.in/v1/docs/wallet-codes)