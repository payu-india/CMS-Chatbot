---
title: Create or Register Beneficiary API
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
The Create Beneficiary API command is used to register a beneficiary under the merchant. After registering, the merchant can use the beneficiary id to make the payout.

HTTP Method: **POST**

**Environment**

|                            |                                                                                                    |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| **Test Environment**       | [https://uatoneapi.payu.in/payout/beneficiary](https://uatoneapi.payu.in/payout/beneficiary)       |
| **Production Environment** | [https://payout.payumoney.com/payout/beneficiary](https://payout.payumoney.com/payout/beneficiary) |

## Request header

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Authorization
        `mandatory`
      </td>

      <td>
        `String` Specify the access token generated earlier in this parameter.
      </td>

      <td>
        Bearer `{access_token}`
      </td>
    </tr>

    <tr>
      <td>
        payoutMerchantId
        `mandatory`
      </td>

      <td>
        `String` Specify the payout merchant id provided while onboarding or creating Payout account.
      </td>

      <td>
        1111126
      </td>
    </tr>

    <tr>
      <td>
        Content-Type
        `mandatory`
      </td>

      <td>
        `String` Indicates the format in which the request is sent.
      </td>

      <td>
        application/json
      </td>
    </tr>
  </tbody>
</Table>

<Callout icon="📘" theme="info">
  ### Note:

  The **pid** is **payoutMerchantId**, however it is different from the PayU merchant id. Check the Payouts Dashboard or call the PayU Customer Support if you don't know your **payoutsMerchantID**.
</Callout>

## Request parameters

<Table>
  <thead>
    <tr>
      <th>
        **Parameters**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        accountNo
        `conditional`
      </td>

      <td>
        `String` Indicates Account number of customer
      </td>
    </tr>

    <tr>
      <td>
        ifsc
        `conditional`
      </td>

      <td>
        `String` Indicates IFSC code of the bank account
      </td>
    </tr>

    <tr>
      <td>
        vpa
        `conditional`
      </td>

      <td>
        `String` Indicates UPI ID of customer<br />**Note:** Same value will be used by the merchant in the status check of transfer.
      </td>
    </tr>

    <tr>
      <td>
        name
        `optional`
      </td>

      <td>
        `String` Indicates of the customer
      </td>
    </tr>

    <tr>
      <td>
        email
        `optional`
      </td>

      <td>
        `String` Indicates Email Address of customer
      </td>
    </tr>

    <tr>
      <td>
        mobile
        `conditional`
      </td>

      <td>
        `String` Indicates Mobile Number of customer
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```curl
curl --location 'https://uatoneapi.payu.in/payout/beneficiary' \
--header 'Content-Type: application/json' \
--header 'payoutMerchantId: 2225335' \
--header 'Authorization: Bearer 6e47dc301158318020af04917b256422cf7f8e11147807102abe5b984c7a03e7' \
--data-raw '{ 
        "name": "test", 
        "email": "test@gmail.com", 
        "mobile": "1234567890", 
        "ifsc": "ABCD0123456", 
        "vpa": "test@upi", 
        "cardNo": "", 
        "beneCode": "BENECODE123" 
    }'
```

## Response parameters

| **Parameter** | **Description**                                                                                                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| status        | This parameter returns the status of web service call. The status can be any of the following:<br /><br />- **0** - If web service call succeeded<br />- **1** - If web service call failed |
| msg           | This parameter returns the success or failure message.                                                                                                                                      |
| code          | This parameter returns the error code if the API failed to verify or invalid details.                                                                                                       |
| data          | This parameter returns the saved card details in a JSON format. For more information, refer to the next table.                                                                              |

### Description of data JSON Fields

| **Field**     | **Description**                                                                                                                                           |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| beneficiaryId | This field returns PayU beneficiary ID for the beneficiary added.                                                                                         |
| name          | This field returns the beneficiary name.                                                                                                                  |
| email         | This field returns the email ID of the beneficiary.                                                                                                       |
| mobile        | This field returns the mobile number of the beneficiary.                                                                                                  |
| accountNo     | This fields returns the account number of the beneficiary.                                                                                                |
| ifsc          | This field returns the IFSC code of the bank branch with which the beneficiary holds the account.                                                         |
| vpa           | This field returns the VPA ID of the beneficiary if they have registered for UPI.                                                                         |
| merchantId    | This field returns the PayU merchant ID of the beneficiary.                                                                                               |
| isValid       | This field returns any of the following values to indicate whether the account is valid or not:                                                           |
| addedOn       | This field returns any of the date and time stamp when the beneficiary was added with PayU.                                                               |
| updatedOn     | This field returns any of the date and time stamp when the beneficiary details were updated with PayU.                                                    |
| isVerified    | This field returns any of the following values to indicate account was verified by PayU. The value null is returned if the account is yet to be verified. |
| nameWithBank  | This field returns the beneficiary name as in the bank records.                                                                                           |
| cardNo        | This field returns the card number if the beneficiary holds a card with bank.                                                                             |

## Sample response

- Success scenario

```json
{ 
    "status": 0, 
    "msg": "Beneficiary Created with Id :16", 
    "code": null, 
    "data": { 
        "beneficiaryId": 16, 
        "name": "Deepak", 
        "email": "deepak@gmail.com", 
        "mobile": "1234567890", 
        "accountNo": "12", 
        "ifsc": "ICIC1234567", 
        "vpa": null, 
        "merchantId": 1111167, 
        "isValid": true, 
        "addedOn": "2020-06-22T08:13:37.000+0000", 
        "updatedOn": "2020-06-22T08:13:37.000+0000", 
        "isVerified": null, 
        "nameWithBank": null, 
        "cardNo": null 
    }
}
```

- Failure scenario

```json
{
  "status": 0,
  "msg": null,
  "code": null,
  "data": {
    "error": "card beneficiary creation is not supported",
    "errorCodes": [
      1018
    ]
  }
}
```

<br />
