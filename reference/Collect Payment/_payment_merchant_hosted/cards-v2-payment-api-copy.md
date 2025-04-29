---
title: Cards  - v2 Payment API (COPY)
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

<RegisterMerchantPrerequiste />

**Environment**

<V2_paymentEnvironment />

## Request parameters

<V2_paymentHeader />

### Request body

<V2_paymentBodyParameters />

<V2CallbackActionsObject />

### additionalInfo object fields description

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        enforcePaymethod
         `optional`
      </td>

      <td>
        `String`Methods of payment that are enforced in the payment process.
      </td>
    </tr>

    <tr>
      <td>
        forcePgid\
         `optional`
      </td>

      <td>
        `String`Force identification for payment gateway integration.
      </td>
    </tr>

    <tr>
      <td>
        partnerHoldTime\
         `optional`
      </td>

      <td>
        `String`Time held by partner for the transaction.
      </td>
    </tr>

    <tr>
      <td>
        userCredentials\
         `optional`
      </td>

      <td>
        `String`Credentials for user authentication during payment.
      </td>
    </tr>
  </tbody>
</Table>

### order object fields description

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        productInfo
         `mandatory`
      </td>

      <td>
        `String`Details about the product being purchased. For more information, refer to[ userDefinedFields object fields description](#userdefinedfields-object-fields-description).
      </td>
    </tr>

    <tr>
      <td>
        userDefinedFields\
         `optional`
      </td>

      <td>
        `Object`Custom fields defined by the user for additional information.
      </td>
    </tr>

    <tr>
      <td>
        paymentChargeSpecification\
         `mandatory`
      </td>

      <td>
        `Object` Payment details including amount, additional charges and PayU offers to be applied. For more information, refer to [paymentChargeSpecification object fields description](#paymentchargespecification-object-fields-description).
      </td>
    </tr>
  </tbody>
</Table>

#### userDefinedFields object fields description

| Field | Description         |
| ----- | ------------------- |
| udf1  | User defined field. |
| udf2  | User defined field. |
| udf3  | User defined field. |
| udf4  | User defined field. |
| udf5  | User defined field. |
| udf6  | User defined field. |
| udf7  | User defined field. |
| udf8  | User defined field. |
| udf9  | User defined field. |
| udf10 | User defined field. |

#### paymentChargeSpecification object fields description

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        price
        `mandatory`
      </td>

      <td>
        This field must contain the price or transaction amount to be posted.
      </td>

      <td>
        10.00
      </td>
    </tr>
  </tbody>
</Table>

<ErrorHandling />

#### paymentChargeSpecification object fields description

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        price
        `mandatory`
      </td>

      <td>
        This field must contain the price or transaction amount to be posted.
      </td>

      <td>
        10.00
      </td>
    </tr>
  </tbody>
</Table>

<BillingDetailsObjectDescription />

<br />

## Sample request

```curl
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Tue, 05 Nov 2024 06:12:57 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="d583ff8069c7dfa8340464a24bdd01cbebf4432b4dfe4de862065cc9c9dc622c24c77cb1ac1142bf581ec07eca8d0ec78a66db93f6cd557d0da552f05c0825e3"' \
--header 'Content-Type: application/json' \
--header 'mid: 8390470' \
--header 'X-CREDENTIAL-USERNAME: UMXDPA' \
--data-raw '{
    "accountId": "UMXDPA",
    "referenceId": "ZP6267f0d2996ce",
    "amount": 10,
    "paymentMethod": {
        "name": "CreditCard",	
        "bankCode": "CC", 		
        "paymentCard": {	
            "cardNumber": 500***1234560***,	
            "validThrough": "04/2027",
            "ownerName": "Ashish",
            "cvv": ***,		
            "tavv": "/wAAAAAAPtP+g6IAmbSeg1gAAAA=",
            "last4Digits": "0000",
            "cardTokenType": "NETWORK",	
            "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1"
        }
    },
    "order": {
        "productInfo": "string",
        "orderedItem": [
            {
                "itemId": null,	
                "description": "AAA", 
                "quantity": null,
                "amount" : 10.0
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
      "paymentChargeSpecification": {
            "price": 10,
        }
  },   
    },
    "additionalInfo": { 
        "enforcePaymethod": "CC,DC"
    },
    "callBackActions": {
        "successAction": "https://testapi.payu.in/admin/testresponsev2?action=successAction",
        "failureAction": "https://testapi.payu.in/admin/testresponsev2?action=failureAction",
        "cancelAction": "https://testapi.payu.in/admin/testresponsev2?action=cancelAction",
        "codAction": "https://testapi.payu.in/admin/testresponsev2?action=codAction",
        "termAction": "string",
        "timeOutAction": null,
        "returnAction": "https://testapi.payu.in/admin/testresponsev2?action=successAction"
    }
  "billingDetails": {
    "firstName": "sartaj",
    "lastName": "",
    "address1": "Test Payu Gurgaon",
    "address2": "",
    "city": "Bharatpur",
    "state": "Rajasthan",
    "country": "India",
    "zipCode": "321028",
    "phone": "9876543210",
    "email": "testv2@example.in"
  }    
}'
```

## Response parameters

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        referenceId
      </td>

      <td>
        This parameter contains the reference ID of the transaction.\
        statusCode
      </td>
    </tr>

    <tr>
      <td>
        paymentId
      </td>

      <td>
        This parameter contains the payment ID of the transaction.\
        statusCode
      </td>
    </tr>

    <tr>
      <td>
        message
      </td>

      <td>
        This parameter contains the status message of the transaction.
      </td>
    </tr>
  </tbody>
</Table>

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
