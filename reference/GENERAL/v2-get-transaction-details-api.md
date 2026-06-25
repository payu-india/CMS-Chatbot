---
title: Get Transaction Details API
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Get Transaction Details API
deprecated: false
hidden: false
metadata:
  title: Get Transaction Details API
  description: >-
    The Get Transaction Details API retrieves transaction details between two
    specified dates with pagination support, including transaction status,
    amount, payment method, and action details such as capture and refund.
  robots: index
---
The **Get Transaction Details** API retrieves transaction details between a start date and end date. The response includes transaction status, amount, payment mode, customer details, and optional action details such as capture and refund. Results are returned in a paginated array format.


HTTP Method: **POST**

**Environment**

|                        |                                                                                              |
| :--------------------- | :------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/v4/reporting/transactions](https://test.payu.in/v4/reporting/transactions) |
| Production Environment | [https://info.payu.in/v4/reporting/transactions](https://info.payu.in/v4/reporting/transactions) |

## Request headers


## Request body parameters

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
        pageNumber
        `mandatory`
      </td>

      <td>
        `Number` The page number to retrieve. Use `1` for the first page and increment for subsequent pages.
      </td>

      <td>
        `1`
      </td>
    </tr>

    <tr>
      <td>
        startDate
        `mandatory`
      </td>

      <td>
        `String` The start date for the transaction search in `YYYY-MM-DD` format.
      </td>

      <td>
        `2025-08-11`
      </td>
    </tr>

    <tr>
      <td>
        endDate
        `mandatory`
      </td>

      <td>
        `String` The end date for the transaction search in `YYYY-MM-DD` format.
      </td>

      <td>
        `2025-08-11`
      </td>
    </tr>

    <tr>
      <td>
        totalRecord
        `mandatory`
      </td>

      <td>
        `Number` The total number of records to fetch for the given date range.
      </td>

      <td>
        `514`
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```bash
curl --location 'https://test.payu.in/v4/reporting/transactions' \
--header 'Accept: application/json' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="{{signature}}"' \
--header 'Digest: {{digest}}' \
--header 'Date: Tue, 12 Aug 2025 16:44:30 GMT' \
--header 'Content-Type: application/json' \
--data '{
    "pageNumber": 1,
    "startDate": "2025-08-11",
    "endDate": "2025-08-11",
    "totalRecord": 514
}'
```

## Response parameters

| Parameter | Description                                                                                                                          | Example     |
| :-------- | :----------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| message   | Response message indicating the operation result.                                                                                    | `Success`   |
| status    | Status code for the API call. `1` for success, `0` for failure.                                                                      | `1`         |
| result    | Array of transaction objects. For field descriptions, refer to [result JSON fields description](#result-json-fields-description).    |             |
| currentPage | The current page number in the paginated response.                                                                                 | `1`         |
| totalRecords | Total number of transaction records available for the given date range.                                                           | `83`        |
| pageSize  | Number of transaction records returned in the current page.                                                                          | `5`         |
| totalPages | Total number of pages available for the given date range.                                                                           | `17`        |
| hasNextPage | Indicates whether a next page of results is available.                                                                              | `true`      |
| hasPreviousPage | Indicates whether a previous page of results is available.                                                                        | `false`     |

### result JSON fields description

Each item in the `result` array contains the following fields:

| Field | Description | Example |
| :---- | :---------- | :------ |
| payuId | PayU transaction ID assigned to the transaction. | `403993715534525267` |
| transactionDetails | JSON object containing the transaction details. For more information, refer to [transactionDetails JSON fields description](#transactiondetails-json-fields-description). | |
| transactionActionDetails | `optional` Array of action details such as capture and refund performed on the transaction. For more information, refer to [transactionActionDetails JSON fields description](#transactionactiondetails-json-fields-description). | |

### transactionDetails JSON fields description

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
      <td>id</td>
      <td>PayU transaction ID.</td>
      <td>`403993715534525267`</td>
    </tr>

    <tr>
      <td>transactionId</td>
      <td>Merchant transaction ID.</td>
      <td>`TXN1754891007637_38614`</td>
    </tr>

    <tr>
      <td>merchantKey</td>
      <td>Merchant key associated with the transaction.</td>
      <td>`PRiQvJ`</td>
    </tr>

    <tr>
      <td>merchantName</td>
      <td>Merchant name.</td>
      <td>`Sudhanshu`</td>
    </tr>

    <tr>
      <td>status</td>
      <td>Transaction status. For example, `captured`, `failed`, `dropped`, or `bounced`.</td>
      <td>`captured`</td>
    </tr>

    <tr>
      <td>discount</td>
      <td>Discount amount applied to the transaction.</td>
      <td>`0.00`</td>
    </tr>

    <tr>
      <td>amount</td>
      <td>Total transaction amount including additional charges.</td>
      <td>`1000.00`</td>
    </tr>

    <tr>
      <td>transactionFee</td>
      <td>Base transaction amount before additional charges.</td>
      <td>`1000.00`</td>
    </tr>

    <tr>
      <td>additionalCharges</td>
      <td>Additional charges applied to the transaction.</td>
      <td>`0.00`</td>
    </tr>

    <tr>
      <td>mode</td>
      <td>Payment mode used for the transaction. For example, `CC`, `NB`, `UPI`, `CASH`, or `SI`.</td>
      <td>`NB`</td>
    </tr>

    <tr>
      <td>baseTxnId</td>
      <td>Base transaction ID for linked or child transactions. `0` if not applicable.</td>
      <td>`0`</td>
    </tr>

    <tr>
      <td>firstName</td>
      <td>Customer first name.</td>
      <td>`Payu-Admin`</td>
    </tr>

    <tr>
      <td>lastName</td>
      <td>Customer last name.</td>
      <td>`Tyagi`</td>
    </tr>

    <tr>
      <td>addedOn</td>
      <td>Timestamp when the transaction was created.</td>
      <td>`2025-08-11 11:13:30`</td>
    </tr>

    <tr>
      <td>updatedOn</td>
      <td>Timestamp when the transaction was last updated.</td>
      <td>`2025-08-11 11:13:40`</td>
    </tr>

    <tr>
      <td>phone</td>
      <td>Customer phone number.</td>
      <td>`9876543210`</td>
    </tr>

    <tr>
      <td>email</td>
      <td>Customer email address.</td>
      <td>`sunit.kumar1@payu.in`</td>
    </tr>

    <tr>
      <td>productInfo</td>
      <td>Product or service description.</td>
      <td>`Test Product`</td>
    </tr>

    <tr>
      <td>errorCode</td>
      <td>Error code for the transaction. `E000` indicates no error.</td>
      <td>`E000`</td>
    </tr>

    <tr>
      <td>errorDescription</td>
      <td>Description of the error code.</td>
      <td>`No Error`</td>
    </tr>

    <tr>
      <td>ibiboCode</td>
      <td>Payment option or bank code used for the transaction.</td>
      <td>`AXNBTPV`</td>
    </tr>

    <tr>
      <td>address</td>
      <td>Customer address.</td>
      <td>``</td>
    </tr>

    <tr>
      <td>city</td>
      <td>Customer city.</td>
      <td>``</td>
    </tr>

    <tr>
      <td>zipcode</td>
      <td>Customer postal code.</td>
      <td>``</td>
    </tr>

    <tr>
      <td>cardNo</td>
      <td>Masked card number, if applicable.</td>
      <td>`XXXXXXXXXXXX4242`</td>
    </tr>

    <tr>
      <td>cardType</td>
      <td>Card type, if applicable.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>cardToken</td>
      <td>Card token, if applicable.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>udf1 to udf5</td>
      <td>User-defined fields passed during the transaction.</td>
      <td>`udf1`</td>
    </tr>

    <tr>
      <td>field0 to field9</td>
      <td>Additional transaction-specific fields returned by the payment gateway or PayU.</td>
      <td>`Transaction Completed Successfully`</td>
    </tr>

    <tr>
      <td>errorMessage</td>
      <td>Human-readable error message for the transaction.</td>
      <td>`No Error`</td>
    </tr>

    <tr>
      <td>paymentSource</td>
      <td>Source through which the payment was initiated. For example, `payu`, `payuS2S`, or `payuPureS2S`.</td>
      <td>`payu`</td>
    </tr>

    <tr>
      <td>partnerToken</td>
      <td>Partner token, if applicable.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>clearToken</td>
      <td>Indicates whether the token should be cleared.</td>
      <td>`false`</td>
    </tr>

    <tr>
      <td>ccAvenueOrderid</td>
      <td>CCAvenue order ID, if applicable.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>merchantUTR</td>
      <td>Merchant Unique Transaction Reference.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>threeDsEci</td>
      <td>3D Secure Electronic Commerce Indicator.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>threeDSEnrolled</td>
      <td>Indicates whether the card is enrolled for 3D Secure.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>threeDSStatus</td>
      <td>3D Secure authentication status.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>appName</td>
      <td>UPI app name used for the transaction, if applicable.</td>
      <td>`GooglePay`</td>
    </tr>

    <tr>
      <td>mcpLookupId</td>
      <td>Multi-currency pricing lookup ID, if applicable.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>mcpAmount</td>
      <td>Multi-currency pricing amount, if applicable.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>mcpCurrency</td>
      <td>Multi-currency pricing currency, if applicable.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>mcpExchangeRate</td>
      <td>Multi-currency pricing exchange rate, if applicable.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>rupayAuthRefNo</td>
      <td>RuPay authorization reference number, if applicable.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>originalCurrency</td>
      <td>Original transaction currency, if applicable.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>curl</td>
      <td>Cancel URL configured for the transaction.</td>
      <td>`https://admin.payu.in/test_response`</td>
    </tr>

    <tr>
      <td>furl</td>
      <td>Failure URL configured for the transaction.</td>
      <td>`https://admin.payu.in/test_response`</td>
    </tr>

    <tr>
      <td>surl</td>
      <td>Success URL configured for the transaction.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>state</td>
      <td>Customer state.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>country</td>
      <td>Customer country.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>bankRefNo</td>
      <td>Bank reference number for the transaction.</td>
      <td>`3abaf676-4385-491e-9488-6490672baa42`</td>
    </tr>

    <tr>
      <td>ip</td>
      <td>IP address from which the transaction was initiated.</td>
      <td>`14.141.149.50`</td>
    </tr>

    <tr>
      <td>issuingBank</td>
      <td>Issuing bank name, if applicable.</td>
      <td>`AMEX`</td>
    </tr>

    <tr>
      <td>paymentGateway</td>
      <td>Payment gateway used for the transaction.</td>
      <td>`null`</td>
    </tr>

    <tr>
      <td>address2</td>
      <td>Additional address information.</td>
      <td>``</td>
    </tr>
  </tbody>
</Table>

### transactionActionDetails JSON fields description

The `transactionActionDetails` array is returned for transactions that have associated actions such as capture or refund.

| Field | Description | Example |
| :---- | :---------- | :------ |
| id | Unique ID for the action. | `138492940` |
| bankRefNo | Bank reference number for the action. | `3abaf676-4385-491e-9488-6490672baa42` |
| token | Token associated with the action. For refund actions, this contains the refund token. | `REF_sHGe_906836` |
| actionType | Type of action performed. For example, `capture` or `refund`. | `capture` |
| prevStatus | Previous status before the action. | `null` |
| amount | Amount associated with the action. | `1000.0` |
| status | Status of the action. For example, `SUCCESS` or `queued`. | `SUCCESS` |
| bankArn | Bank ARN for the action. | `null` |
| updatedAt | Timestamp when the action was last updated. | `2025-08-11 11:13:40` |
| createdAt | Timestamp when the action was created. | `2025-08-11 11:13:40` |
| settlementId | Settlement ID associated with the action. | `null` |
| amountSettled | Amount settled for the action. | `null` |
| refundMode | Refund mode for refund actions. For example, `Back to Source`. | `-` |
| settledOn | Timestamp when the action was settled. | `null` |
| merchantUTR | Merchant UTR for the action. | `null` |
| merchantServiceFee | Merchant service fee for the action. | `0.0` |
| merchantServiceTax | Merchant service tax for the action. | `0.0` |
| successAmount | Successful amount processed for the action. | `null` |

## Sample response

### Success scenario

```json
{
    "message": "Success",
    "status": 1,
    "result": [
        {
            "payuId": 403993715534525267,
            "transactionDetails": {
                "id": 403993715534525267,
                "transactionId": "TXN1754891007637_38614",
                "merchantKey": "PRiQvJ",
                "merchantName": "Sudhanshu",
                "status": "captured",
                "discount": 0.00,
                "amount": 1000.00,
                "transactionFee": 1000.00,
                "additionalCharges": 0.00,
                "mode": "NB",
                "baseTxnId": 0,
                "firstName": "Payu-Admin",
                "lastName": "Tyagi",
                "addedOn": "2025-08-11 11:13:30",
                "updatedOn": "2025-08-11 11:13:40",
                "phone": "9876543210",
                "email": "sunit.kumar1@payu.in",
                "productInfo": "Test Product",
                "errorCode": "E000",
                "errorDescription": "No Error",
                "ibiboCode": "AXNBTPV",
                "bankRefNo": "3abaf676-4385-491e-9488-6490672baa42",
                "field9": "Transaction Completed Successfully",
                "errorMessage": "No Error",
                "paymentSource": "payu",
                "ip": "14.141.149.50"
            },
            "transactionActionDetails": [
                {
                    "id": 138492940,
                    "bankRefNo": "3abaf676-4385-491e-9488-6490672baa42",
                    "token": "",
                    "actionType": "capture",
                    "prevStatus": null,
                    "amount": 1000.0,
                    "status": "SUCCESS",
                    "bankArn": null,
                    "updatedAt": "2025-08-11 11:13:40",
                    "createdAt": "2025-08-11 11:13:40",
                    "settlementId": null,
                    "amountSettled": null,
                    "refundMode": "-",
                    "settledOn": null,
                    "merchantUTR": null,
                    "merchantServiceFee": 0.0,
                    "merchantServiceTax": 0.0,
                    "successAmount": null
                }
            ]
        },
        {
            "payuId": 403993715534525275,
            "transactionDetails": {
                "id": 403993715534525275,
                "transactionId": "Txn_Id_642759",
                "merchantKey": "PRiQvJ",
                "merchantName": "Sudhanshu",
                "status": "captured",
                "discount": 0.00,
                "amount": 10014.60,
                "transactionFee": 9991.00,
                "additionalCharges": 23.60,
                "mode": "NB",
                "baseTxnId": 0,
                "firstName": "Test",
                "lastName": "User",
                "addedOn": "2025-08-11 11:13:56",
                "updatedOn": "2025-08-11 11:14:14",
                "phone": "9876543210",
                "email": "test@example.com",
                "productInfo": "Test Product",
                "errorCode": "E000",
                "errorDescription": "No Error",
                "ibiboCode": "AIRNB",
                "bankRefNo": "86249aea-7368-409b-8742-72fa854c555e",
                "field9": "Transaction Completed Successfully",
                "errorMessage": "No Error",
                "paymentSource": "payu",
                "ip": "14.141.149.50"
            },
            "transactionActionDetails": [
                {
                    "id": 138492944,
                    "bankRefNo": "86249aea-7368-409b-8742-72fa854c555e",
                    "token": "",
                    "actionType": "capture",
                    "prevStatus": null,
                    "amount": 10014.6,
                    "status": "SUCCESS",
                    "bankArn": null,
                    "updatedAt": "2025-08-11 11:14:05",
                    "createdAt": "2025-08-11 11:14:05",
                    "settlementId": null,
                    "amountSettled": null,
                    "refundMode": "-",
                    "settledOn": null,
                    "merchantUTR": null,
                    "merchantServiceFee": 20.0,
                    "merchantServiceTax": 3.6,
                    "successAmount": null
                },
                {
                    "id": 138492946,
                    "bankRefNo": null,
                    "token": "REF_sHGe_906836",
                    "actionType": "refund",
                    "prevStatus": null,
                    "amount": 9991.0,
                    "status": "queued",
                    "bankArn": null,
                    "updatedAt": "2025-08-11 11:14:14",
                    "createdAt": "2025-08-11 11:14:14",
                    "settlementId": null,
                    "amountSettled": null,
                    "refundMode": "Back to Source",
                    "settledOn": null,
                    "merchantUTR": null,
                    "merchantServiceFee": 0.0,
                    "merchantServiceTax": 0.0,
                    "successAmount": null
                }
            ]
        }
    ],
    "currentPage": 1,
    "totalRecords": 83,
    "pageSize": 5,
    "totalPages": 17,
    "hasNextPage": true,
    "hasPreviousPage": false
}
```

### Failure scenario

If no transactions are found for the given date range, the response returns an empty `result` array with pagination details:

```json
{
    "message": "Success",
    "status": 1,
    "result": [],
    "currentPage": 1,
    "totalRecords": 0,
    "pageSize": 5,
    "totalPages": 0,
    "hasNextPage": false,
    "hasPreviousPage": false
}
```