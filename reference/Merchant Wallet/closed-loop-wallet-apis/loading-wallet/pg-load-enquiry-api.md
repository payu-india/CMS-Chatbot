---
title: PG Load Enquiry API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Load Enquiry** API allows you to check the status of a wallet load transaction that was initiated using the PG Load API. This is essential for transaction reconciliation and status verification.

## Environment

| Environment | URL                                                                     |
| ----------- | ----------------------------------------------------------------------- |
| Test        | `https://apitest.payu.in/loyalty-points/ppi/payment/pg-load/enquiry/v1` |
| Production  | `https://api.payu.in/loyalty-points/ppi/payment/pg-load/enquiry/v1`     |

**HTTP Method**: POST

## Request Headers

<Closed_Loop_HMAC />

## Request Parameters

### Body Parameters

| Parameter                               | Description                                                                   | Example      |
| --------------------------------------- | ----------------------------------------------------------------------------- | ------------ |
| clientTxnId<br /><code>mandatory</code> | <code>Alphanumeric(100)</code> Unique transaction ID from the PG Load request | PGLOAD123456 |

## Response Parameters

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
        merchantCode
      </td>

      <td>
        Merchant's unique ID provided by PayU
      </td>

      <td>
        180012
      </td>
    </tr>

    <tr>
      <td>
        clientTxnId
      </td>

      <td>
        Echoes the client's transaction ID
      </td>

      <td>
        PGLOAD123456
      </td>
    </tr>

    <tr>
      <td>
        txnAmount
      </td>

      <td>
        The amount intended to be loaded into the wallet
      </td>

      <td>
        4100
      </td>
    </tr>

    <tr>
      <td>
        accosaRefNo
      </td>

      <td>
        Auto-generated sequence number
      </td>

      <td>
        ACC123456789
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        Transaction status
      </td>

      <td>
        SUCCESS/FAILED/PENDING
      </td>
    </tr>

    <tr>
      <td>
        responseCode
      </td>

      <td>
        Numeric response code
      </td>

      <td>
        00
      </td>
    </tr>

    <tr>
      <td>
        refundTxnExist
      </td>

      <td>
        Indicates if the transaction was refunded
      </td>

      <td>
        false
      </td>
    </tr>

    <tr>
      <td>
        message
      </td>

      <td>
        Response Message or description for
        the response code.
      </td>

      <td>
        Failed
      </td>
    </tr>

    <tr>
      <td>
        VerifyPaymentResponse.message
      </td>

      <td>
        Message related to the status
      </td>

      <td>
        Transaction successful
      </td>
    </tr>

    <tr>
      <td>
        VerifyPaymentResponse.status
      </td>

      <td>
        Status of execution of load enquiry API
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        VerifyPaymentResponse.result
      </td>

      <td>
        Status result from payment gateway
      </td>

      <td>
        PG result for **Verify Payment** API. For more information, refer to

        [Verify Payment API](ref:verify_payment_api)

        .
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```json
curl --location --request POST 'hhttps://apitest.payu.in/loyalty-points/ppi/payment/pg-load/enquiry/v1\ 
--header 'walletIdentifier: CLW' \ 
--header 'date: Wed, 12 Jun 2024 08:53:43 GMT' \ 
--header 'digest: lrGnpxCydiyLo5KPdXrJczwJgtsUbJiBj9N5QHTt+ho=' \ 
--header 'authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="v15rnvh1InSEWRq6EW9BCfXlxO0QI/4Sxxmdxd2f4Q0="' \ 
--header 'Content-Type: application/json' \ 
--data-raw '{  
 "clientTxnId": "123parentTxnPayuId" 
  }

```

## Sample Response

### Successful Transaction

```json
{ 
"merchantCode": "2", 
"clientTxnId": "Test_008", 
"txnAmount": "10000", 
"status": "FAILED", 
"responseCode": "1303", 
"refundTxnExist": true, 
"refundEnquiryResponse": { 
"txnId": "999810590007501", 
"refundId": "3001378553", 
"requestId": "4993824106986", 
"merchantId": "3", 
"amount": "100.0", 
"refundStatus": "PENDING", 
"merchantRefId": "loyalty_ppi_9", 
"refundType": "FULL", 
"lastRefundType": "PARTIAL", 
"isReconSuccess": false, 
"isAutoRefund": false, 
"discountAdjusted": 0, 
"reversed": false 
}, 
"verifyPaymentResponse": { 
"mihpayId": 999810590007501, 
"bankReferenceNumber": "39594217", 
"amount": 100, 
"mode": "NB", 
"requestId": "", 
"originalAmount": 100, 
"additionalCharges": 0, 
"discount": 0, 
"netDebitAmount": 100, 
"productInfo": "Product Info", 
"firstName": "Manali", 
"bankcode": "DSHB", 
"cardNo": null, 
"cardType": null, 
"cardToken": null, 
"udf1": "loadTag=PG", 
"udf2": null, 
"udf3": null, 
"udf4": null, 
"udf5": null, 
"field2": null, 
"field9": "Transaction Completed Successfully", 
"errorCode": "E000", 
"errorMessage": "No Error", 
"addedOn": "2025-02-12 17:40:35", 
"settledAt": "0000-00-00 00:00:00", 
"paymentSource": "payu", 
"pgType": "NB-PG", 
"status": "success", 
"unmappedStatus": "captured", 
"merchantUTR": null, 
"mcpLookupId": null, 
"mcpAmount": null, 
"mcpCurrency": null, 
"mcpExchangeRate": null, 
"originalCurrency": "INR", 
"merNetAmount": null, 
"offerAvailed": null, 
"message": "Found TxnId", 
"txnId": "Test_008" 
} 
}

```

#### Failed Transaction

```json
{
  "merchantCode": "180012",
  "clientTxnId": "56894",
  "txnAmount": "4100",
  "accosaRefNo": null,
  "status": "FAILED",
  "responseCode": "00",
  "refundTxnExist": false,
  "refundEnquiryResponse": null,
  "verifyPaymentResponse": {
    "message": "Success",
    "status": 1,
    "result": [
      {
        "payuId": 999000000002603,
        "transactionDetails": {
          "id": 999000000002603,
          "transactionId": "61042",
          "merchantKey": "travelibibo",
          "merchantName": "Name409208872",
          "status": "failed",
          "discount": 0,
          "amount": 51,
          "transactionFee": 51,
          "additionalCharges": 0,
          "mode": "UPI",
          "baseTxnId": 999000000002602,
          "firstName": "FGHJ",
          "lastName": "FGHJ",
          "addedOn": "2025-01-09 17:34:36",
          "phone": "XXXXXX693252",
          "email": "tegyh@gh.com",
          "productInfo": "Product Info",
          "errorCode": "E317",
          "ibiboCode": "UPI",
          "address": "",
          "city": "",
          "zipcode": "",
          "cardNo": null,
          "cardType": null,
          "cardToken": null,
          "udf1": "loadTag=PG",
          "udf2": null,
          "udf3": null,
          "udf4": null,
          "udf5": null,
          "field0": null,
          "field1": "kk@okaxis",
          "field2": null,
          "field3": "kk@okaxis",
          "field4": "KUNAL KUKREJA",
          "field5": "AXI918605XXXXXXXXXXXX61531422612197",
          "field6": null,
          "field7": "01",
          "field8": "googlepay",
          "field9": "01|PENDING|Completed Using Verify API",
          "errorMessage": "Bank was unable to authenticate.",
          "paymentSource": "payu",
          "partnerToken": null,
          "clearToken": false,
          "ccAvenueOrderid": null,
          "merchantUTR": null,
          "threeDsEci": null,
          "threeDSEnrolled": null,
          "threeDSStatus": null,
          "appName": "GooglePay",
          "mcpLookupId": null,
          "mcpAmount": null,
          "mcpCurrency": null,
          "mcpExchangeRate": null,
          "rupayAuthRefNo": null,
          "originalCurrency": null,
          "curl": "https://pp1api.payu.in/loyalty-points/ppi/payment/pg-load/success/v1",
          "furl": "https://pp1api.payu.in/loyalty-points/ppi/payment/pg-load/success/v1",
          "surl": null,
          "state": null,
          "country": null,
          "bankRefNo": "868212138432",
          "ip": "10.50.10.111",
          "issuingBank": null,
          "paymentGateway": null,
          "address2": ""
        }
      }
    ]
  }
}

```

## Response codes

| Response Code | Description                                                    |
| ------------- | -------------------------------------------------------------- |
| 00            | SUCCESS                                                        |
| 1009          | CARD_CANCELLED_CLOSED_EXPIRED                                  |
| 1010          | CARD_TEMPORARY_BLOCK                                           |
| 1012          | CARD_PENDING_CANCELLATION                                      |
| 1013          | AML_MIN_LIMIT                                                  |
| 1030          | INVALID_MESSAGE                                                |
| 1045          | UNABLE_TO_PROCESS_REQUEST                                      |
| 1055          | MALFORMED REQUEST                                              |
| 1056          | INVALID MESSAGE CODE                                           |
| 1058          | INVALID_WALLETS                                                |
| 1088          | INVALID REQUEST DATE format                                    |
| 1093          | INVALID CLIENT TXN ID                                          |
| 1101          | UNKNOWN_SOURCE_ACCOUNT_TYPE                                    |
| 1121          | CARD_CREDIT_DEBIT_BLOCK                                        |
| 1135          | REFUND_AMOUNT_GREATER_THAN_ORIGINAL_TXN_AMOUNT                 |
| 1246          | ORIGINAL_TXN_NOT_EXIST                                         |
| 1247          | SOURCE_ACC_TYPE_NOT_MACHED_WITH_IMPL                           |
| 1303          | CUSTOMER DETAILS NOT PRESENT                                   |
| 1304          | MORE THAN ONE CUSTOMER IDENTIFIER NOT ALLOWED                  |
| 1322          | TRANSACTION AMOUNT CANNOT BE ZERO                              |
| 1325          | FUND FLOW TYPE MISMATCH                                        |
| 1326          | IMPL ID MISMATCH                                               |
| 1357          | WALLET DETAILS NOT FOUND                                       |
| 1353          | COOLING OFF PERIOD BETWEEN TWO LOADS NOT COMPLETED             |
| 1354          | CORPORATE_LEVEL_LIMIT_EXCEEDED                                 |
| 1363          | INVALID ACTIVITY STATUS                                        |
| 1366          | PROGRAM IS INACTIVE                                            |
| 1367          | PROGRAM NOT FOUND                                              |
| 1376          | INVALID UNLOAD AMOUNT                                          |
| 1368          | WALLET OR ACCOUNTNO SHOULD BE PRESENT                          |
| 1398          | ACCOUNTNO SHOULD BE PRESENT                                    |
| 1501          | SYSTEM_ERROR_DB                                                |
| 1504          | SYSTEM_CACHE_FAILURE                                           |
| 3007          | UNLOAD AMOUNT SHOULD BE LESS THAN AVAILABLE BALANCE            |
| 10153         | AMOUNT IS NOT WITHIN MIN-MAX RANGE                             |
| 10163         | PROGRAM DAILY LIMIT EXCEEDED                                   |
| 6000          | ACCOUNT DORMANT                                                |
| 6002          | ACCOUNT PERMANENTLY BLOCKED OR CLOSED                          |
| 6014          | ACCOUNT IN TEMPORARILY BLOCKED STATE                           |
| 6016          | ACCOUNT IN CREDIT BLOCKED STATE                                |
| 6017          | ACCOUNT ALREADY IN CREDIT_DEBIT BLOCKED STATE                  |
| 1392          | FUND FLOW TYPE NOT PRESENT IN THE REQUEST                      |
| 6909          | SENDER CUSTOMER NOT FOUND                                      |
| 10044         | SENDER INFO INVALID LENGTH                                     |
| 1319          | SOURCE_ACCOUNT_INVALID_LENGTH                                  |
| 1103          | INVALID_TRANSACTION_AMOUNT                                     |
| 6911          | Invalid reserved field 1                                       |
| 6912          | Invalid reserved field 2                                       |
| 6913          | Invalid reserved field 3                                       |
| 1298          | INVALID_SOURCE_ACCOUNT_TYPE                                    |
| 1322          | Transaction amount cannot be zero                              |
| 10012         | IMPLID NOT PRESENT                                             |
| 10013         | IMPLTYPE NOT PRESENT                                           |
| 6933          | INVALID SOURCE TYPE                                            |
| 84114         | Invalid data type for field Transaction Amount                 |
| 9343          | CLIENT TXN ID IS MANDATORY                                     |
| 303178        | Request Date Time Length should not be more than 14 characters |
| 1361          | INVALID ACCOUNT NUMBER                                         |
| 6935          | SOURCE TYPE SHOULD BE 0 OR 1                                   |
| 10160         | WALLET DAILY LIMIT EXCEEDED                                    |
| 10164         | WALLET MONTHLY LIMIT EXCEEDED                                  |
| 10168         | WALLET YEARLY LIMIT EXCEEDED                                   |
| 10216         | WALLET DAILY COUNT EXCEEDED                                    |
| 10220         | WALLET MONTHLY COUNT EXCEEDED                                  |
| 10224         | WALLET YEARLY COUNT EXCEEDED                                   |
| 13047         | WALLET_PER_TRANSACTION_LIMIT_EXCEEDED                          |