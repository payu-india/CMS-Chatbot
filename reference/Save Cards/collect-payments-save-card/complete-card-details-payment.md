---
title: Complete Card Details
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payment from Saved Card with Complete Card Details
  description: >-
    Learn how to use the _ayment API to process transactions using full card
    details. This sectoin provides detailed instructions, request parameters,
    and sample responses for efficient card management.
  robots: index
next:
  description: ''
---
This scenario is applicable where a customer is providing the complete card number do the transaction (card number, card expiry, CVV, and name on card) 

HTTP Method: **POST**

## Applicable scenarios

* It is a guest checkout  
* It is a standard checkout request where there is no need to save the card 

<Callout icon="📘" theme="info">
  **Note**: Plain card details coming from the merchant, so no changes are applicable in the request & response.
</Callout>

Request and response elements will remain intact as it is.

**Environment**

|                            |                                                                             |
| :------------------------- | :-------------------------------------------------------------------------- |
| **Test Environment**       | [https://apitest.payu.in/v2/payments](https://apitest.payu.in/v2/payments>) |
| **Production Environment** | [https://api.payu.in/v2/payments](https://api.payu.in/v2/payments>)         |

## Request headers

<V2_payment_header_params />

## Request body

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Amount of the transaction.<br><strong>Note</strong>: This value will not be considered as the transaction. Only the details in the <code>order.paymentChargeSpecificationparameter.price</code>field will be considered.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1000</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>currency<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Currency of the transaction. By default, <code>INR</code> is posted.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>INR</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentSource<code> optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Contains the payment source.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>WEB</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentMethod<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the payment method used. For more information, refer to <a href="#paymentmethod-object-fields-description">paymentMethod object fields description </a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {<br>        &quot;name&quot;: &quot;NetBanking&quot;,	<br>        &quot;bankCode&quot;: &quot;TESTNB&quot;<br>    }</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="https://docs.payu.in/v2/reference/addl_info-payment-apis#order-object-fields-description">order object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Additional information including enforced payment methods, single instalment, virtual payment address (VPA), and various options for user preferences during the transaction. For more information, refer to <a href="https://docs.payu.in/v2/reference/addl_info-payment-apis#additionalinfo-object-fields-description">additionalInfo object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>callBackActions<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc. For more information, refer to <a href="https://docs.payu.in/v2/reference/addl_info-payment-apis#callbackactions-object-fields-description">callbackActions object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingDetails<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Billing details of the customer including name, address, phone number, email, etc. For more information, refer to <a href="href="https://docs.payu.in/v2/reference/addl_info-payment-apis#billingdetails-object-field-descriptions">billingDetails object field descriptions target="_blank"</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentMethod JSON object Fields

<HTMLBlock>{`
<table>
<thead>
<tr style="background-color: #f2f2f2;">
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Field</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
name<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for seamless</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Payment method name (e.g., CreditCard, DebitCard, NetBanking, UPI). This replaces the 'pg' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 10<br/><br/>
<strong>Possible values:</strong><br/>
• CreditCard<br/>
• DebitCard<br/>
• NetBanking<br/>
• UPI<br/>
• Wallet<br/>
• EMI<br/>
• BNPL
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
CreditCard
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
bankCode<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for seamless</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Bank code or payment gateway code. This replaces the 'bankcode' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 10<br/><br/>
<strong>Common values:</strong><br/>
• CC (Credit Card)<br/>
• DC (Debit Card)<br/>
• NB (Net Banking)<br/>
• UPI (UPI payments)<br/>
• WALLET (Wallet payments)
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
CC
</td>
</tr>

</tbody>
</table>
`}</HTMLBlock>

##### paymentCard object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardNumber<br> <code>mandatory for physical card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the card number. For validating the card number, refer to <a href="https://docs.payu.in/v1/docs/card-number-formats">Card Number Formats</a>.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>validThrough<br> <code>mandatory for physical card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the card expiry in MM/YYYY format.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ownerName<br> <code>mandatory for physical card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the name of the card holder as printed on card.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cvv<br> <code>mandatory for physical card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the CVV printed on the back of the card.  </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>tavv<br> <code>mandatory for saved card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the cryptogram of card.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>last4Digits<br> <code>mandatory for saved card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the last four digits of card.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardTokenType<br> <code>mandatory for saved card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the any of the following based on the:  </p>
<ul>
<li>PAYU</li>
<li>NETWORK</li>
<li>ISSUER&quot;</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardToken<br> <code>mandatory for saved card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the card token of stored card.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

<V2_Error_Handling />

## Sample request

```curl
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Thu, 27 Mar 2025 10:12:27 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="ec84843a663143bb89391f6fa2d4b9404bab1543a3eee81263b4a507ebf5d289d8fad1fbcdd59da820951e3e0f9b0b0b3d1bad9b41338804e7c42a8a6197c6e9"' \
--header 'Content-Type: application/json' \
--header 'Cookie: PHPSESSID=sclorpmpb4ngion5e996os22ao' \
--data-raw '{
    "accountId": "smsplus",
    "txnId": "b5f2d8785768087678fn4",
    "paymentMethod": {
        "name": "CreditCard",
        "bankCode": "CC",
        "paymentCard": {
            "cardNumber": 5497774415170603,
            "validThrough": "05/2025",
            "cvv": 123,
            "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
            "ownerName": "Ashish",
            "issuer": "ICICI",
            "bin": "500446",
            "last4Digits": "0000",
            "cardHash": null,
            "cardTokenType": "NETWORK",
            "tavv": "/wAAAAAAPtP+g6IAmbSeg1gAAAA="
        }
    },
    "order": {
        "productInfo": "qwertyuiopasdfghjkl",
        "orderedItem": [
            {
                "itemId": "1",
                "description": "string",
                "quantity": 1
            }
        ],
        "userDefinedFields": {
            "udf1": "",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": "",
            "udf6": "",
            "udf7": "",
            "udf8": "",
            "udf9": "",
            "udf10": ""
        },
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
    },
    "authorization": {
        "eci": "05",
        "cavv": "AAABAWFlmQAAAABjRWWZEEFgFz",
        "flowType": "Frictionless",
        "threeDSTransID": "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
        "threeDSServerTransID": "eea30d14-71cf-41af-b961-f95b7d67dc93",
        "threeDSTransStatus": "Y",
        "threeDSTransStatusReason": "01",
        "aquirer_bin": "401200",
        "additionalInfo": {
            "authUdf1": "string",
            "authUdf2": "string"
        }
    },
    "threeDS2RequestData": {
        "threeDSVersion": "2.2.0",
        "deviceChannel": "APP"
    }
}'
```

## Response parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>referenceId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the reference ID of the transaction.<br>statusCode</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the payment ID of the transaction.<br>statusCode</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>message</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the status message of the transaction.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample response

```
Array
(
    [referenceId] => b5f2d8785768087678fm9
    [paymentId] => 1999110000001769
    [message] => Please call verify api to get the transaction status
)
```

> 📘 Reference:
>
> To check the transaction status, refer to[Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api).

## Response

In addition to the parameters in the response of a Merchant Hosted Checkout transaction with a card, PayU returns network token, network token expiry for PCI complied or PayU token & its expiry for non-PCI complied merchants.