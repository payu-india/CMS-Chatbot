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

|                            |                                                                                |
| :------------------------- | :----------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://apitest.payu.in/v2/payments>](https://apitest.payu.in/v2/payments>) |
| **Production Environment** | \<[https://api.payu.in/v2/payments>](https://api.payu.in/v2/payments>)         |

## Request header

| Parameter     | Description                                                                                                                                                                                                    |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| date          | The current date and time. For example,  format of the date is Wed, 28 Jun 2023 11:25:19 GMT.                                                                                                                  |
| authorization | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to[ authorization fields description](#authorization-fields-description). |

#### authorization fields description

| Field     | Description                                                                                                                         |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| username  | Represents the username or identifier for the client or merchant, for example smsplus.                                              |
| algorithm | Indicates the hashing algorithm used for the HMAC signature, for example sha512.                                                    |
| headers   | Specifies which headers have been used in generating the hash, for example date.                                                    |
| signature | The HMAC signature generated using the specified algorithm. For more information, refer to [hashing algorithm](#hashing-algorithm). |

#### hashing algorithm

Yo must hash the request parameters using the following hash logic:

**Hash logic**: sha512(`<Body data>` + '|' + date + '|' + merchant\_secret)

Where `<Body data>` contains the request body posted with the request.

<details>
  <summary>Sample header code</summary>

  ```javascript
  var merchant_key = 'smsplus';
  var merchant_secret = 'izF09TlpX4ZOwmf9MvXijwYsBPUmxYHD';
  // date
  var date = new Date();
  date = date.toUTCString();

  // authorization
  var authorization = getAuthHeader(date);

  function getAuthHeader(date) {
      var AUTH_TYPE = 'sha512';
      var data = isEmpty(request['data']) ? "" : request['data'];
      var hash_string = data + '|' + date + '|' + merchant_secret;
      var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
      return `hmac username="${merchant_key}", algorithm="${AUTH_TYPE}", headers="date", signature="${hash}"`;
  }
  ```
</details>

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
  <td style="border: 1px solid #ddd; padding: 8px;">Transaction ID for transaction tracking. Must be unique for every transaction.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">TXN123456</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>amount</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Amount of the transaction. This will not be considered as the transaction amount, only the order.paymentChargeSpecification.price field will be considered.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">1000</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentMethod</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains details of the payment method.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>order</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains transaction order details such as product info, ordered items, user-defined fields, and payment charge details.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Additional metadata for the transaction.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>callBackActions</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL actions for payments (e.g., success, failure, cancel).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>billingDetails</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Customer billing details including name, phone, and address.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>authorization</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Authorization details for the payment process, including 3DS metadata.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>threeDS2RequestData</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">3DS Version and device details for advanced authentication flows.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>siDetails</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Standing Instructions details for recurring payments.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>splitDetails</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Split payment details for multi-recipient transactions.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentMethod

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
  <td style="border: 1px solid #ddd; padding: 8px;">Represents the payment method used. Valid values: CreditCard, DebitCard, NetBanking, UPI, EMI, Wallet, CashCard, COD, Challan, LazyPay, PayPal, Sodexo, Payout, CLEMI, ENACH, qr, neftrtgs.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CreditCard</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>bankCode</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains the bank code. Valid values: CC, MAST, VISA.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CC</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentCard</strong><br/><code>mandatory for cards</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains physical card or saved card details.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentCard

<V2_paymentCard />

### order

<V2_order_object />

### paymentChargeSpecification

<V2_paymentChargeSpecification_object />

### additionalInfo

<AdditionalI_Info_object />

### callBackActions

<CallbackActions_object />

### billingDetails

<BillingDetails_object />

### authorization

<V2_authorization_cards />

### threeDS2RequestData



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