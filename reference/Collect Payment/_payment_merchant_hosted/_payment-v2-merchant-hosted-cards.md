---
title: Cards  - v2 Payment API
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
You can collect payments from customers with leading wallets using the Merchant Hosted integration. You need to ensure that **CreditCard** or **DebitCard** for the **paymentMethod.name** parameter and  card code based on the desired card provider for the **paymentMethod.bankcode** parameter is posted.

> 📘 Note:
>
> PayU accepts domestic and international transactions, but international transactions need to be enabled by writing to PayU Integration Team ([integration@pay.in](mailto:integration@pay.in)).

**Environment**

<V2_payment_envrionment />

## Request header

<V2_payment_header_params />

## Request body

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
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>accountId</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Represents the merchant key provided by PayU during onboarding.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">MERCHANT123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnId</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Transaction ID for transaction tracking. Must be unique for every transaction. </td>
  <td style="border: 1px solid #ddd; padding: 8px;">TXN123456</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentMethod</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains details of the payment method. For more information, refer to <a href="#paymentmethod-object-fields-description">paymentMethod object fields description</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>order</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains transaction order details such as product info, ordered items, user-defined fields, and payment charge details. For more information, refer to <a href="#order-object-fields-description">order Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Additional metadata for the transaction. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>callBackActions</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL actions for payments (e.g., success, failure, cancel). For more information, refer to <a href="#callbackactions-object-fields-description">callBackActions Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>billingDetails</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Customer billing details including name, phone, and address. For more information, refer to <a href="#billingdetails-object-fields-description">billingDetails Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>authorization</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Authorization details for the payment process, including 3DS metadata. For more information, refer to <a href="#authorization-object-fields-description">authorization Object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentMethod object fields description

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
  <td style="border: 1px solid #ddd; padding: 8px;">Represents the payment method used. For credit card, include CreditCard.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CreditCard</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>bankCode</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains the bank code. Valid values: CC, MAST, VISA.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CC</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentCard</strong><br/><code>mandatory for cards</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains physical card or saved card details. For more information, refer to </td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentCard object fields description

<V2_paymentCard />

### order object fields description

<V2_order_object />

### additionalInfo object fields description

<AdditionalI_Info_object />

### callBackActions object fields description

<CallbackActions_object />

### billingDetails object fields description

<BillingDetails_object />

### authorization object fields description

<V2_authorization_cards />

### threeDS2RequestData

<ThreeDSRequestData_object />

## Sample request

```json
{
    "accountId": "smsplus",
    "txnId": "b5f2d8785768087678fm9",
    "amount": "1000",
    "paymentMethod": {
        "name": "CreditCard",
        "bankCode": "CC",
        "paymentCard": {
            "cardNumber": "5497774415170603",
            "validThrough": "05/2025",
            "cvv": "123",
            "ownerName": "Ashish"
        }
    },
    "order": {
        "productInfo": "Product details",
        "orderedItem": [
            {
                "itemId": "1",
                "description": "Product A",
                "quantity": 1,
                "amount": 1000
            }
        ],
        "userDefinedFields": {
            "udf1": "test1",
            "udf2": "test2",
            "udf3": "test3",
            "udf4": "test4",
            "udf5": "test5"
        },
        "paymentChargeSpecification": {
            "price": "1000"
        }
    },
    "additionalInfo": {
        "enforcePaymethod": "CC",
        "createOrder": true,
        "authOnly": false
    },
    "callBackActions": {
        "successAction": "https://checkout.payu.in/testCB/success",
        "failureAction": "https://checkout.payu.in/testCB/failure",
        "cancelAction": "https://checkout.payu.in/testCB/cancel"
    },
    "billingDetails": {
        "firstName": "Ashish",
        "lastName": "Kumar",
        "address1": "123 Main Street",
        "phone": "9123456789",
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
}
```

## Response parameters

<V2_payment_response_params />

## Sample response

```
Array
(
    [txnId] => b5f2d8785768087678fm9
    [paymentId] => 1999110000001769
    [message] => Please call verify api to get the transaction status
)
```

> 📘 Reference:
>
> To check the transaction status, refer to[Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api).