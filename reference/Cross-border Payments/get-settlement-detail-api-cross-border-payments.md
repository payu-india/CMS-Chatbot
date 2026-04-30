---
title: Get Settlement Detail API - CB Payments
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
Get Settlement Detail API are build on top of settlement data that provides settlement details.

## Endpoint

| Environment | URL                                                                                                                                      |
| :---------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| Production  | [https://info.payu.intreasury/int/payu/settlement/settlementDetails](https://info.payu.intreasury/int/payu/settlement/settlementDetails) |

## Request parameters

### Authorization header

* Date: date time when request was triggered (`Wed, 28 Jun 2023 11:25:19 GMT`)

```javascript
var date = new Date().toUTCString()
```

* Authorisation: a `SHA512` token generated from the current date time, key and salt for the MID. Below is JS function to get the same.

```javascript
var merchant_key = '<key>';
var merchant_secret = '<salt or secret>';
// date
var date = new Date();
// var date = "Wed, 28 Jun 2023 11:25:19 GMT";
date = new Date().toUTCString();
// authorization
var authorization = getAuthHeader(date);
function getAuthHeader(date) {
  var AUTH_TYPE = 'sha512';
  var data = isEmpty(request['data'])?"":request['data'];
  var hash_string = data + '|' + date + '|' + merchant_secret;
  console.log("Hash String is ", hash_string);
  var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
  var authHeader = 'hmac username="' + merchant_key + '", ' + 'algorithm="' + AUTH_TYPE + '", headers="date", signature="' + hash + '"'
  return authHeader;
}
```

### Query parameters

| Parameter             | Reference                                                                                                                                                      | Example    |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- |
| settledOn `mandatory` | This parameter must either contain either date for the settlement or UTR (Unique Transaction Reference number).                                                | 2023-09-26 |
| isVersion `optional`  | This parameter must contain the version of the API that can be either 1 or 2.                                                                                  | 1          |
| pageSize `mandatory`  | This parameter must contain the number of records to be paginated on each page is specified in this parameter. If not specified, 2000 records will be fetched. | 1000       |
| page `mandatory`      | This parameter must contain the page number to be fetched.                                                                                                     | 5          |
| type `optional`       | This parameter must contain either G to get a detailed output or leave it blank.                                                                               | G          |

## Sample request/response

### Success scenarios

HTTP status is 200 for all success response

#### Date empty type and version

**Request**

```bash
curl --location 'https://info.payu.intreasury/int/payu/settlement/settlementDetails?settledOn=2024-04-08&pageSize=20000&page=1' \
--header 'mid: 135670'
```

**Response**

```json
{
    "rows": 20000,
    "message": "20000 settled on 2024-04-08 ",
    "status": 1,
    "result": [
        {
            "payuid": "19580843982",
            "txnid": "PZT24040523596DQOT01",
            "txndate": "2024-04-05 23:59:49",
            "mode": "CC",
            "amount": "218.00",
            "requestid": "13785835411",
            "requestdate": "2024-04-06 00:00:08",
            "requestaction": "capture",
            "requestamount": "218.00",
            "mer_utr": "UTIBR72024040800086935",
            "mer_service_fee": "3.16000",
            "mer_service_tax": "0.57000",
            "mer_net_amount": "214.27",
            "bank_name": "CC",
            "issuing_bank": "SBI",
            "merchant_subvention_amount": 0.0,
            "cgst": "0.00000",
            "igst": "0.57000",
            "sgst": "0.00000",
            "PG_TYPE": "AxisCYBER",
            "Card Type": "domestic",
            "token": null
        }
    ]
}
```

#### Date empty type and version is 2

**Request**

```bash
curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g&command=get_settlement_details&var1=2021-08-10&hash=259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8&var2&var3&var4=L&var5=2"
```

**Response**

```json
{
    "rows": 50002,
    "message": "50002 transaction settledOn 2024-04-08",
    "status": 1,
    "result": [
        {
            "payuid": "19588035480",
            "txnId": "PZT2404062056KJOM701",
            "txndate": "2024-04-06 20:56:50",
            "mode": "UPI",
            "amount": "188.00",
            "requestid": "13791685328",
            "requestdate": "2024-04-06 20:57:19",
            "requestaction": "capture",
            "requestamount": "188.00",
            "mer_utr": "UTIBR72024040800086935",
            "mer_service_fee": "0.00000",
            "mer_service_tax": "0.00000",
            "mer_net_amount": "188.0",
            "bank_name": "INTENT",
            "issuing_bank": null,
            "merchant_subvention_amount": 0.0,
            "cgst": "0.00000",
            "igst": "0.00000",
            "sgst": "0.00000",
            "PG_TYPE": "AIRTEL UPI ",
            "Card Type": null,
            "token": null,
            "PG": "AIRTEL UPI ",
            "SettlementType": "regular",
            "Scheme": "INTENT",
            "FeeType": "tdrFee",
            "InstantSettlementTDR": "0.00",
            "InstantSettlementTDRTax": "0.00",
            "InstantSettlementTdrType": "",
            "InstantRefundTDR": "0.00",
            "InstantRefundTDRTax": "0.00",
            "InstantRefundTdrType": "",
            "perDayServiceFee": "0.0",
            "perDayServiceTax": "0.0",
            "pricingDays": 1,
            "offerServiceFee": "0.00",
            "offerServiceTax": "0.00"
        },
        {
            "payuid": "ADJ_821142",
            "txnid": "ADJ_821142",
            "txndate": "2024-04-08 02:01:35",
            "mode": "Adjustmentdebit",
            "amount": "-23868.77",
            "requestid": "ADJ_821142",
            "requestdate": "2024-04-08 02:01:35",
            "requestaction": "debit",
            "requestamount": "-23868.77",
            "mer_utr": "UTIBR72024040800086935",
            "mer_service_fee": "-20227.77",
            "mer_service_tax": "-3641.00",
            "mer_net_amount": "-23868.77",
            "bank_name": "",
            "issuing_bank": "",
            "merchant_subvention_amount": "",
            "cgst": 0,
            "sgst": 0,
            "igst": 0,
            "PG_TYPE": "PayU",
            "Card Type": "",
            "token": "",
            "SettlementType": "",
            "PG": "",
            "Scheme": "",
            "FeeType": "",
            "InstantSettlementTDR": "",
            "InstantSettlementTDRTax": "",
            "InstantSettlementTdrType": "",
            "InstantRefundTDR": "",
            "InstantRefundTDRTax": "",
            "InstantRefundTdrType": "",
            "perDayServiceFee": "0.00",
            "perDayServiceTax": "0.00",
            "pricingDays": 1,
            "offerServiceFee": "0.0",
            "offerServiceTax": "0.0"
        }
    ]
}
```

#### Date Type G and Version Empty

**Request**

```bash
curl --location 'http://127.0.0.1:8090/treasury/int/payu/settlement/settlementDetails?settledOn=2024-04-08&type=G&page=1&pageSize=30000'
```

**Response**

```json
{
    "rows": 30000,
    "message": "30000 transaction settledOn 2024-04-08",
    "status": 1,
    "result": [
        {
            "txn_addedon": "2024-04-05 23:59:49",
            "settlement_addedon": "2024-04-06 00:11:12",
            "settledon": "2024-04-08 12:45:07",
            "settlementId": "202404071115",
            "time_zone": "UTC + 05:30",
            "merchant_id": 135670,
            "merchantName": "Flipkart Payments",
            "PSP": "PayU India",
            "action": "capture",
            "txnid": "PZT24040523596DQOT01",
            "payu_id": "19580843982",
            "request_id": "13785835411",
            "settlementUTR": "UTIBR72024040800086935",
            "pg_label": "AxisCYBER",
            "card_bin": 0,
            "Scheme": "VISA",
            "mode": "CC",
            "ibibo_code": "CC",
            "auth_code": "7123418019786142605964",
            "bank_ref_no": "7123418019786142605964",
            "transaction_currency": "INR",
            "settlement_currency": "INR",
            "forexRate": 80.45,
            "transaction_amount": 218.0,
            "payu_fee": "-3.16",
            "payu_fee_tax": "-0.57",
            "net_amount": 214.27,
            "ib_title": "SBI",
            "token": null,
            "bank_arn": null,
            "legal_entity": 202437,
            "company_name": "Flipkart Internet Pvt Ltd.",
            "merchant_key": "JP**y",
            "PG_TYPE": "AxisCYBER",
            "Card Type": "domestic"
        }
    ]
}
```

#### Date Type G and Version 2

**Request**

```bash
curl --location 'http://127.0.0.1:8090/treasury/int/payu/settlement/settlementDetails?settledOn=2024-04-08&type=G&isVersion=2&pageSize=30000&page=1' \
--header 'mid: 135670'
```

**Response**

```json
{
    "rows": 30002,
    "message": "30002 transaction settledOnsettledOn",
    "status": 1,
    "result": [
        [
            {
                "txn_addedon": "2024-04-05 23:59:49",
                "settlement_addedon": "2024-04-06 00:11:12",
                "settledon": "2024-04-08 12:45:07",
                "settlementId": "202404071115",
                "time_zone": "UTC + 05:30",
                "merchant_id": 135670,
                "merchantName": "Flipkart Payments",
                "PSP": "PayU India",
                "action": "capture",
                "txnid": "PZT24040523596DQOT01",
                "payu_id": "19580843982",
                "request_id": "13785835411",
                "settlementUTR": "UTIBR72024040800086935",
                "pg_label": "AxisCYBER",
                "card_bin": 0,
                "Scheme": "VISA",
                "mode": "CC",
                "ibibo_code": "CC",
                "auth_code": "7123418019786142605964",
                "bank_ref_no": "7123418019786142605964",
                "transaction_currency": "INR",
                "settlement_currency": "INR",
                "forexRate": 80.45,
                "transaction_amount": 218.0,
                "payu_fee": "-3.16",
                "payu_fee_tax": "-0.57",
                "net_amount": 214.27,
                "ib_title": "SBI",
                "token": null,
                "bank_arn": null,
                "legal_entity": 202437,
                "company_name": "Flipkart Internet Pvt Ltd.",
                "merchant_key": "JP**y",
                "PG_TYPE": "AxisCYBER",
                "Card Type": "domestic",
                "SettlementType": "regular",
                "FeeType": "tdrFee",
                "InstantSettlementTDR": "0.00",
                "InstantSettlementTDRTax": "0.00",
                "InstantSettlementTdrType": "",
                "InstantRefundTDR": "0.00",
                "InstantRefundTDRTax": "0.00",
                "InstantRefundTdrType": "",
                "perDayServiceFee": "0.0",
                "perDayServiceTax": "0.0",
                "pricingDays": 1,
                "offerServiceFee": "0.00",
                "offerServiceTax": "0.00"
            },
            {
                "txn_addedon": "2024-04-08 02:01:35",
                "settlement_addedon": "2024-04-07 00:11:12",
                "settledon": "2024-04-08 12:45:07",
                "settlementId": "202404081115",
                "time_zone": "UTC + 05:30",
                "merchant_id": "135670",
                "merchantName": "Flipkart Payments",
                "PSP": "PayU India",
                "action": "debit",
                "txnid": "ADJ_821142",
                "payu_id": "ADJ_821142",
                "request_id": "ADJ_821142",
                "settlementUTR": "UTIBR72024040800086935",
                "pg_label": "",
                "card_bin": "",
                "Scheme": "",
                "mode": "Adjustmentdebit",
                "ibibo_code": "",
                "auth_code": "",
                "bank_ref_no": "",
                "transaction_currency": "INR",
                "settlement_currency": "INR",
                "forexRate": 80.45,
                "transaction_amount": "-23868.77",
                "payu_fee": "-20227.77",
                "payu_fee_tax": "-3641.00",
                "net_amount": "-23868.77",
                "ib_title": "",
                "token": "",
                "bank_arn": "",
                "legal_entity": "202437",
                "company_name": "Flipkart Internet Pvt Ltd.",
                "merchant_key": "BmzsVc",
                "PG_TYPE": "PayU",
                "Card Type": "",
                "SettlementType": "",
                "FeeType": "",
                "InstantSettlementTDR": "",
                "InstantSettlementTDRTax": "",
                "InstantSettlementTdrType": "",
                "InstantRefundTDR": "",
                "InstantRefundTDRTax": "",
                "InstantRefundTdrType": "",
                "perDayServiceFee": "20227.77",
                "perDayServiceTax": "3641.0",
                "pricingDays": "1",
                "offerServiceFee": "0.0",
                "offerServiceTax": "0.0"
            }
        ]
    ]
}
```

### Failure scenarios

* Invalid Response (Bad Request): HTTP status 401

```json
{
    "rows": 0,
    "message": "Please check date format it should be YYYY-MM-DD or utr format which should be alphanumeric",
    "status": 0,
    "result": "validation failed"
}
```

## Response parameters description

### result JSON fields description

| **Field**            | **Description**                                                                                                                                                                                                                            | **Example**            |
| :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| txn_addedon          | This parameter contains the transaction added date.                                                                                                                                                                                        | 2024-04-05 23:59:49    |
| settlement_addedon   | This parameter contains the settlement added date.                                                                                                                                                                                         | 2024-04-06 00:11:12    |
| settledon            | This parameter contains the date when the settled on.                                                                                                                                                                                      | 2024-04-08 12:45:07    |
| settlementId         | This parameter contains the settlement ID.                                                                                                                                                                                                 | 202404071115           |
| time_zone            | This parameter contains the time zone in which the transaction was perform.                                                                                                                                                                | UTC + 05:30            |
| merchant_id          | This parameter contains the merchant ID.                                                                                                                                                                                                   | JP***g                 |
| merchantName         | This parameter contains the merchant name.                                                                                                                                                                                                 | ABC company            |
| PSP                  | This parameter contains the payment service provider.                                                                                                                                                                                      | PayU                   |
| action               | This parameter contains the action taken on the transaction. For description of the various unampped status, refer to [List of Unmapped Status](#list-of-unmapped-status)                                                                  | capture                |
| txnid                | This parameter contains the transaction ID.                                                                                                                                                                                                | PZT24040523596DQOT01   |
| payu_id              | This parameter contains a unique reference number created for each transaction at PayU's end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund. | 403993715521937565     |
| request_id           | This parameter contains the request ID value posted by the merchant during the transaction request.                                                                                                                                        | 131278418              |
| settlementUTR        | This parameter contains the unique number generated by the bank to identify a settlement and track the amounts settled. A UTR is a 12-digit alphanumeric code that is assigned to each electronic transaction.                             | UTIBR72024040800086935 |
| pg_label             | This parameter contains the payment gateway used.                                                                                                                                                                                          | AxisCYBER              |
| card_bin             | This parameter contains the card BIN.                                                                                                                                                                                                      |                        |
| Scheme               | This parameter contains the card scheme.                                                                                                                                                                                                   | VISA                   |
| mode                 | This parameter contains the payment mode used.                                                                                                                                                                                             | CC                     |
| ibibo_code           | This parameter contains the bank code.                                                                                                                                                                                                     | CC                     |
| auth_code            | This parameter contains the authorization code.                                                                                                                                                                                            | 7123418019786142605964 |
| bank_ref_no          | This parameter contains the bank reference number.                                                                                                                                                                                         | 7123418019786142605964 |
| transaction_amount   | This parameter contains the original amount which was sent in the transaction request by the merchant.                                                                                                                                     | 100                    |
| transfer_currency    | This parameter contain the currency to which conversion was done.                                                                                                                                                                          | INR                    |
| transaction_currency | This parameter contain the currency with which transaction was performed.                                                                                                                                                                  | USD                    |
| forexRate            | This parameter contain the foreign exchange rate for currency in the **transactionCurrency** to **transactionCurrency** parameter.                                                                                                         | 80.45                  |
| finalSettlement      | This parameter contain the final settlement done to merchant.                                                                                                                                                                              | 20000.45               |
| payu_fee             | This parameter contains the PayU fee for this transaction.                                                                                                                                                                                 | -3.16                  |
| payu_fee_tax         | This parameter contains the tax incurred for PayU fee.                                                                                                                                                                                     | -0.57                  |
| net_amount           | This parameter contains the net amount paid to merchant.                                                                                                                                                                                   | 214.27                 |
| ib_title             | This parameter contains the bank code.                                                                                                                                                                                                     | SBI                    |
| token                | This parameter contains the saved card token (if any).                                                                                                                                                                                     |                        |
| bank_arn             | This parameter contains the unique number assigned to a credit or debit card transaction that helps banks and other parties track the transaction.                                                                                         |                        |
| legal_entity         | This parameter contains the legal entity number.                                                                                                                                                                                           | 202437                 |
| company_name         | This parameter contains the company name of the merchant.                                                                                                                                                                                  |                        |
| merchant_key         | This parameter contains the merchant key.                                                                                                                                                                                                  |                        |
| PG_TYPE              | This parameter contains the PG type.                                                                                                                                                                                                       | AxisCYBER              |
| Card Type            | This parameter contains whether card type is domestic or international.                                                                                                                                                                    | domestic               |

### List of Unmapped Status

| Unmapped Status    | Status  | Description                                                                                                                                                    |
| ------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| auth               | Success | Auth refers to a transaction that has been authorized by the bank, where the amount is blocked on the customer's account but not yet captured by the merchant. |
| capture            | Success | Capture refers to the transaction where the previously authorized amount is successfully collected from the customer, completing the payment.                  |
| cancel             | Failure | This status is used when an authorized transaction is canceled before capture, and the blocked amount is released back to the customer.                        |
| refund             | Success | Refund refers to the process where a captured (successful) transaction amount is returned back to the customer, either fully or partially.                     |
| refundreversal     | Failure | Refund Reversal occurs when a previously initiated refund is canceled or fails, resulting in the amount being retained by the merchant.                        |
| chargeback         | Failure | Chargeback occurs when a customer disputes a transaction with their bank, leading to the amount being debited from the merchant and returned to the customer.  |
| chargebackreversal | Success | Chargeback Reversal occurs when the merchant successfully contests a chargeback and the disputed amount is returned back to the merchant.                      |
