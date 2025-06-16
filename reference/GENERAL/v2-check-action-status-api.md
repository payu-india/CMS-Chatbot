---
title: v2 Check Action Status API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Check Action Status** API is a new information service designed to allow merchants to retrieve the current status of transaction actions, particularly refund requests. Unlike the v1 API, this enhanced version provides comprehensive details about transaction lifecycles, including capture and refund actions, with improved response formats and support for complex use cases.

### Endpoint

```
POST /v1/transaction
```

### Request Headers

The request header contains the following fields:

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
        Date
        `mandatory`
      </td>

      <td>
        The date and time should be in the GMT time conversion(not the IST). For example, current time in India is 18:00:00 IST, the time in the date header should be 12:30:00 GMT.
      </td>

      <td>
        Thu, 17 Feb 2022 08:17:59 GMT
      </td>
    </tr>

    <tr>
      <td>
        Digest
        `mandatory`
      </td>

      <td>
        Base 64 encode of (sha256 hash of the JSON data (post to server).
      </td>

      <td>
        `vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=`
      </td>
    </tr>

    <tr>
      <td>
        Authorization
        **mandatory**
      </td>

      <td>
        This field is in the following format:
        `hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4="`
        Where the above format includes the following:

        * **username**: The merchant key of the merchant.
        * **algorithm**: This must have the value as **hmac-sha256** that is used for this API
        * **headers**: This must have the value as **date digest**
        * **signature**: This must contain the hmacsha256 of (signing\_string, merchant\_secret), where:
          * **signing\_string**: This is in the "**Date**"+"
            "+"**Digest**" format. Here, the Date and Digest is the same values in the fields listed in this table For example, "Thu, 17 Feb 2022 08:17:59 GMT""
            "+"vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0="
          * **merchant\_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to [Generate Merchant Key and Salt on PayU Dashboard](https://docs.payu.in/v1/docs/generate-merchant-key-and-salt-on-payu-dashboard)
      </td>

      <td>
        hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI="
      </td>
    </tr>

    <tr>
      <td>
        platformId\
        `mandatory`
      </td>

      <td>
        This field contains the platform ID and include the value as **1**.
      </td>

      <td>
        1
      </td>
    </tr>
  </tbody>
</Table>

### Request Parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
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
        key
        `mandatory`
      </td>

      <td>
        `String` This parameter must contain the merchant key provided by PayU.
      </td>

      <td>
        `iDJYfd`
      </td>
    </tr>

    <tr>
      <td>
        requestId
        `optional`
      </td>

      <td>
        `String Array` This parameter includes array of child merchant request IDs to query.
      </td>

      <td>
        `["11763053990", "11763053112"]`
      </td>
    </tr>

    <tr>
      <td>
        payuId
        `optional`
      </td>

      <td>
        `String Array`This parameter must contain the PayU ID (mihpayuid) that you receive in the response for a successful payment transaction.
      </td>

      <td>
        `["11763053990"]`
      </td>
    </tr>

    <tr>
      <td>
        tokenId
        `optional`
      </td>

      <td>
        `String` Token ID (unique token from the merchant) for the refund request. Token ID has to be generated at your end for each new refund request. It is an identifier for each new refund request which can be used for tracking it. It must be unique for every new refund request generated – otherwise the refund request would not be generated successfully. Token ID length should not be greater than 23 characters
      </td>

      <td>
        `["TOKEN12345"]`
      </td>
    </tr>

    <tr>
      <td>
        request
        `mandatory`
      </td>

      <td>
        `JSON` String containing additional parameters
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

> 📘 Note:
>
> At least one of the following parameters must be provided: `requestId`, `payuId`, or `tokenId`.

### Sample Request

```bash
curl --location 'http://localhost:8080/v1/transaction' \
--header 'mid: 8759546' \
--header 'Content-Type: application/json' \
--header 'Info-Command: check_action_status' \
--header 'Date: Thu, 17 Feb 2022 08:17:59 GMT' \
--header 'Digest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI="' \
--header 'platformId: 1' \
--data '{
    "requestId": ["11763053990", "11763053112"],
    "payuId": null,
    "tokenId": null
}'
```

### Response Parameters

| Parameter                | Description                                           | Example                                    |
| ------------------------ | ----------------------------------------------------- | ------------------------------------------ |
| message                  | Indicates the result of the API call                  | `"Success"`                                |
| status                   | Status of the API call (1 for success, 0 for failure) | `1`                                        |
| result                   | Array containing the detailed transaction information | See JSON example                           |
| payuId                   | The PayU ID of the transaction                        | `17173825989`                              |
| transactionDetails       | Basic details of the transaction                      | Contains ID, status, amount, etc.          |
| transactionActionDetails | Actions performed on the transaction                  | Contains action type, status, amount, etc. |
| splitTransactionDetails  | Details of split transactions (if applicable)         | Array of split transaction details         |

### Sample Response

#### Success Response

```json
{
    "message": "Success",
    "status": 1,
    "result": [
        {
            "payuId": 17173825989,
            "transactionDetails": {
                "id": 17173825989,
                "transactionId": "PB34794479S",
                "status": "captured",
                "amount": 843.0,
                "mode": "CASH",
                "addedOn": "2023-04-13 20:29:30",
                "phone": "8448480680",
                "email": "example@example.com",
                "productInfo": "PBProduct",
                "errorCode": "E000",
                "errorMessage": "No Error"
            },
            "transactionActionDetails": [
                {
                    "id": 11968786530,
                    "bankRefNo": "T2304132030077646051321",
                    "actionType": "capture",
                    "amount": 843.0,
                    "status": "SUCCESS",
                    "updatedAt": "2023-04-17 12:26:11",
                    "createdAt": "2023-04-13 20:30:15",
                    "settlementId": null,
                    "refundMode": "-"
                }
            ]
        }
    ]
}
```

#### Failure Response

```json
{
    "status": 0,
    "msg": "0 out of 1 Transactions Fetched Successfully",
    "transaction_details": {
        "16988019552": "No action status found value of var1 sent in the request"
    }
}
```