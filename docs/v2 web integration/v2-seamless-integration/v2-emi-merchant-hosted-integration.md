---
title: v2 EMI Integration
excerpt: >-
  When your customer wants to opt for the EMI option with cards, you can use EMI
  APIs to check the customer’s eligibility and get the EMI amount, interest,
  processing fee, or No-Cost EMI and tenure. If the customer is eligible, you
  can post the transaction with EMI conversion.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can collect payments from customers with leading wallets using the **v2/payments** API > Merchant Hosted integration. You need to ensure that **EMI** for the **paymentMethod.name** field and EMI bank code based on the desired wallet for the **paymentMethod.bankcode** field.

**Steps to Integrate**

1. [Initiate the payment with PayU](#step-1-initiate-the-payment-with-payu)
2. [Verify Payment](#step-3-verify-the-payment)

## Step 1: Initiate the payment with PayU

**Environment**

|                            |                                                                                |
| :------------------------- | :----------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://apitest.payu.in/v2/payments>](https://apitest.payu.in/v2/payments>) |
| **Production Environment** | \<[https://api.payu.in/v2/payments>](https://api.payu.in/v2/payments>)         |

### Request header

| Parameter     | Description                                                                                                                                                                                                    |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| date          | The current date and time. For example,  format of the date is Wed, 28 Jun 2023 11:25:19 GMT.                                                                                                                  |
| authorization | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to[ authorization fields description](#authorization-fields-description). |

#### authorization fields description

| Parameter | Description                                                                                                                                                                      |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| username  | Represents the username or identifier for the client or merchant, in this case, it's "smsplus".                                                                                  |
| algorithm | Indicates the hashing algorithm used for the HMAC signature. Here, it is set to "sha512".                                                                                        |
| headers   | Specifies which headers have been used in generating the hash. In this case, only the "date" header is used.                                                                     |
| signature | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to [hashing algorithm](#hashing-algorithm). |

#### hashing algorithm

You must hash the request parameters using the following hash logic:

```
sha512(<Body data> + '|' + date + '|' + merchant_secret}
```

Where, \<Body data> contains the request Body posted with the request.

<details>
  <summary>Sample header code</summary>

  ```
  var merchant_key = 'smsplus';
  var merchant_secret = 'izF09TlpX4ZOwmf9MvXijwYsBPUmxYHD';

  // date
  var date = new Date();
  // var date = "Wed, 28 Jun 2023 11:25:19 GMT";
  date = date.toUTCString();

  // authorization
  var authorization = getAuthHeader(date);
  console.log(authorization);

  function getAuthHeader(date) {
  var AUTH_TYPE = 'sha512';
  var data = isEmpty(request['data'])?"":request['data'];
  var hash_string = data + '|' + date + '|' + merchant_secret;
  console.log("Hash String is ", hash_string);
  var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
  var authHeader = 'hmac username="' + merchant_key + '", ' + 'algorithm="' + AUTH_TYPE + '", headers="date", signature="' + hash + '"'
  return authHeader;
  }

  pm.environment.set('date', date);
  pm.environment.set('authorization', authorization);
  pm.environment.set('merchant_key',merchant_key);
  pm.environment.set('merchant_secret',merchant_secret);

  function isEmpty(obj) {
  for(var key in obj) {
  if(obj.hasOwnProperty(key))
  return false;
  }
  return true;
  }
  ```
</details>

### Request body

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>accountId<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The merchant key provided by PayU during onboarding.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>MERCHANT123</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnId<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Transaction ID for transaction tracking and this must be unique for every transaction.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>REF123456</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentMethod<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the payment method used. For EMI payments:<br>• name: Must be "EMI"<br>• bankCode: EMI code based on card issuer and tenure (refer to <a href="https://docs.payu.in/v1/docs/emi-codes">EMI Codes</a>)<br>• paymentCard: Card details object</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{"name": "EMI", "bankCode": "EMI6"}</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Additional information including transaction flow configuration and other EMI-specific options. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a>.</p></td>
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

### paymentMethod object fields description

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>name<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the payment mode code. For EMI payments, this must be "EMI". For more information, refer to <a href="https://docs.payu.in/v1/docs/payment-mode-codes">Payment Mode Codes</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>EMI</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankCode<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the EMI code based on card issuer and tenure. For more information, refer to <a href="https://docs.payu.in/v1/docs/emi-codes">EMI Codes</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>EMI6</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentCard<br><code>mandatory for EMI</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> This object contains the physical card or saved card token details. For more information, refer to <a href="#paymentcard-object-fields-description">paymentCard object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentCard object fields description

<V2_paymentCard />

### order object fields description

<V2_order_object />

### additionalInfo object fields description

<br />

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
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>enforcePaymethod</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Use **EMI** for EMI. </td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnS2sFlow<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Transaction server-to-server flow configuration for EMI payments.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>4</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>createOrder<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Whether to create an order during the payment process.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>createOrder</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">A flag to store the order details (true/false).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">true</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

<br />

### callBackActions object fields description

<CallbackActions_object />

### billingDetails object fields description

<BillingDetails_object />

## Sample request

```curl
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Thu, 27 Mar 2025 10:12:27 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="ec84843a663143bb89391f6fa2d4b9404bab1543a3eee81263b4a507ebf5d289d8fad1fbcdd59da820951e3e0f9b0b0b3d1bad9b41338804e7c42a8a6197c6e9"' \
--header 'Content-Type: application/json' \
--data-raw '{
    "accountId": "smsplus",
    "referenceId": "b5f2d8785768087678fn4",
    "amount": 10000,
    "currency": "INR",
    "paymentSource": "WEB",
    "paymentMethod": {
        "name": "EMI",
        "bankCode": "EMI6",
        "paymentCard": {
            "cardNumber": "5004461234560000",
            "validThrough": "04/2025",
            "ownerName": "John Doe",
            "cvv": "123"
        }
    },
    "order": {
        "productInfo": "EMI Payment for Electronics",
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
        "paymentChargeSpecification": {
            "price": "10000.00"
        }
    },
    "additionalInfo": {
        "txnS2sFlow": "4",
        "createOrder": "false"
    },
    "callBackActions": {
        "successAction": "https://yoursite.com/success",
        "failureAction": "https://yoursite.com/failure",
        "cancelAction": "https://yoursite.com/cancel"
    },
    "billingDetails": {
        "firstName": "John",
        "lastName": "Doe",
        "phone": "9876543210",
        "email": "john.doe@example.com",
        "city": "Mumbai",
        "state": "Maharashtra",
        "country": "India",
        "zipCode": "400001"
    }
}'
```

## Sample response

```json
{
    "referenceId": "b5f2d8785768087678fn4",
    "paymentId": "1999110000001769",
    "message": "Please call verify api to get the transaction status"
}
```

## Step 2: Verify the payment

Verify the transaction details using the Verification APIs. For API reference, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api) under API Reference.

> 📘 Tip
>
> The transaction ID that you posted in Step 1 with PayU must be used here.