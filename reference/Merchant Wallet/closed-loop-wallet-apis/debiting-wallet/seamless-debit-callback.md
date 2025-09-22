---
title: Seamless Debit Callback
deprecated: false
hidden: false
metadata:
  robots: index
---
The Seamless Debit Callback feature allows merchants to handle payment responses through success (Surl) and failure (Furl) URLs. This section outlines the required parameters for implementing seamless debit callbacks in your PayU integration.

## Request Parameters

<HTMLBlock>{`
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Description</th>
            <th>Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>accountId</br><code>mandatory</code></td>
            <td><code>String</code> The merchant key provided by PayU during onboarding.</td>
            <td>MERCHANT123</td>
        </tr>
        <tr>
            <td>txnId<code></brmandatory</code></td>
            <td><code>String</code> Transaction ID for transaction tracking and this must be unique for every transaction.</td>
            <td>REF123456</td>
        </tr>
        <tr>
            <td>paymentMethod<code></brmandatory</code></td>
            <td><code>Object</code> Details about the payment method used. For UPI payments:<br>• name: Must be "UPI"<br>• bankCode: Must be "UPI"</td>
            <td>{"name": "UPI", "bankCode": "UPI"}</td>
        </tr>
        <tr>
            <td>order<code</br>mandatory</code></td>
            <td><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a>.</td>
            <td></td>
        </tr>
        <tr>
            <td>additionalInfo</br<code>mandatory</code></td>
            <td><code>Object</code> Additional information including UPI-specific parameters like VPA. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a>.</td>
            <td></td>
        </tr>
        <tr>
            <td>callBackActions<code>mandatory</code></td>
            <td><code>Object</code> Actions to perform on the payment server in different scenarios. For more information, refer to <a href="#callbackactions-object-fields-description">callBackActions object fields description</a>.</td>
            <td></td>
        </tr>
        <tr>
            <td>billingDetails<code>mandatory</code></td>
            <td><code>Object</code> Billing details of the customer including name, address, phone number, email, etc. For more information, refer to <a href="#billingdetails-object-fields-description">billingDetails object fields description</a>.</td>
            <td></td>
        </tr>
    </tbody>
</table>
`}</HTMLBlock>

> 📘 Implementation Notes
>
> * All parameters listed above are mandatory for seamless debit callback implementation
> * Ensure that the `txnId` is unique for every transaction to maintain proper tracking
> * For UPI payments, the `paymentMethod` object must specifically include `name` as "UPI" and `bankCode` as "UPI"
> * Object parameters like `order`, `additionalInfo`, `callBackActions`, and `billingDetails` require detailed field descriptions that should be referenced from their respective sections in the complete API documentation

<br />
