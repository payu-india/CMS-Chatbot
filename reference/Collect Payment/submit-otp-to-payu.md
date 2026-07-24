---
title: Submit OTP API
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
After collecting the OTP from your customer on the payment page, submit the OTP to PayU by using this API.

You must pass the **reference id** of the corresponding transaction along with other parameters (see request parameters) in the request body of the Submit OTP API.

> 📘 Note:
>
> To find the reference id, see the response of the initiate transaction request of the corresponding transaction.

HTTP Method: **POST**

## Environment

| Environment                | URL                                                                                      |
| :------------------------- | :--------------------------------------------------------------------------------------- |
| **Test Environment**       | [https://test.payu.in/ResponseHandler.php](https://test.payu.in/ResponseHandler.php)     |
| **Production Environment** | [https://secure.payu.in/ResponseHandler.php](https://secure.payu.in/ResponseHandler.php) |

## Request parameters

| **Parameter**           | **Description**                                                                                                                                                                                                                                     | **Example**                        |
| :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------- |
| referenceId `mandatory` | `String` Pass the ID returned in the response of the transaction request.                                                                                                                                                                           | `bbed416d21dda9941a90cc72819c5b52` |
| consent `conditional`   | `String` If the transaction request returns parameter such as **tncUrl** and **tncText** that indicates that the merchant need to collect the consent from the customer. In such cases, collect the customer's consent and pass the value as **1**. | 1                                  |
| data `optional`         | `String` You must pass `{ "payuPureS2S": "1" }` as the value of this parameter.                                                                                                                                                                     | \{ "payuPureS2S": "1" }            |
| otp `mandatory`         | `String` The OTP collected from the customer that they receive from the bank.                                                                                                                                                                       | 345635                             |

## Sample request

### Without consent

```
curl --location --request POST 'https://test.payu.in/ResponseHandler.php' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=ef4510abes5uo7ephv7o20ossc; PHPSESSID=63fefa045789a' \
--data-urlencode 'referenceId=42df570fa8c4d9de6209a71970acb661' \
--data-urlencode 'otp=725356' \
--data-urlencode 'consent=0'
```

### With consent

Certain issuers require their customer to provide consent while authorizing a transaction. For such issuers, you need to capture your customer's consent and pass them to PayU using the **Submit OTP** API.

```bash
curl --location --request POST 'https://test.payu.in/ResponseHandler.php' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=ef4510abes5uo7ephv7o20ossc; PHPSESSID=63fefa045789a' \
--data-urlencode 'referenceId=42df570fa8c4d9de6209a71970acb661' \
--data-urlencode 'otp=725356' \
--data-urlencode 'consent=1'
```

> 📘 **Note:**
>
> If you fail to collect and send the consent with the **Submit OTP** API, the transaction will remain in an **In Progress** state.

## Sample response

Based on the type of request sent (with consent/without consent) you may receive the following responses from PayU:

### Submit OTP success

```json
{ 
    "metaData": { 
        "message": "No Error", 
        "referenceId": "6a037a290af9253a1d300c8ad0b24c94", 
        "statusCode": "E000", 
        "txnId": "5b7d06c6bf7d4dc2d3a8", 
        "unmappedStatus": "success", 
        "submitOtp": { 
            "status": "success" 
        } 
    }, 
    "result": { 
        "mihpayid": "999000000000582", 
        "mode": "BNPL", 
        "status": "success", 
        "key": "KOEfPI", 
        "txnid": "5b7d06c6bf7d4dc2d3a8", 
        "amount": "2.00", 
        "addedon": "2022-12-27 16:24:53", 
        "productinfo": "Product Info", 
        "firstname": "Payu-Admin", 
        "lastname": "", 
        "address1": "", 
        "address2": "", 
        "city": "", 
        "state": "", 
        "country": "", 
        "zipcode": "", 
        "email": "test@example.com", 
        "phone": "9205845755", 
        "udf1": "", 
        "udf2": "", 
        "udf3": "", 
        "udf4": "1672138493180012pass123", 
        "udf5": "", 
        "udf6": "", 
        "udf7": "", 
        "udf8": "", 
        "udf9": "", 
        "udf10": "",  
        "card_token": "", 
        "card_no": "", 
        "field0": "", 
        "field1": "9205845755", 
        "field2": "EMI210142576638888947", 
        "field3": "", 
        "field4": "Transaction is successful", 
        "field5": "", 
        "field6": "", 
        "field7": "PAYMENT_SUCCESSFUL", 
        "field8": "SUCCESS", 
        "field9": "Transaction is successful", 
        "payment_source": "payuPureS2S", 
        "PG_TYPE": "BNPL-PG", 
        "error": "E000", 
        "error_Message": "No Error", 
        "net_amount_debit": "2", 
        "discount": "0.00", 
        "offer_key": "", 
        "offer_availed": "", 
        "unmappedstatus": "captured", 
        "hash": "781e999b0e7944a91815434d8429ade60882173702211453f7ee3772417009121c67f08a085c450787e1597700334b75477e6b3574cd84e9e4ffb18171183ab5", 
        "bank_ref_no": "TXN1288577", 
        "bank_ref_num": "TXN1288577", 
        "bankcode": "LAZYPAY", 
        "surl": "https://pp94admin.payu.in/test_response", 
        "curl": "https://pp94admin.payu.in/test_response", 
        "furl": "https://pp94admin.payu.in/test_response" 
    } 
}
```

### Consent required but not sent

```json
{ 
    "metaData": { 
        "message": "Consent not given by the customer for Terms & Conditions", 
        "referenceId": "4f3c09ffe3e9756cb95d7e144469d6d5", 
        "txnId": "N4SH5OrRY2", 
        "unmappedStatus": "in progress" 
    }, 
    "result": null 
}
```

### Submit OTP failed

```json
{ 
    "metaData": { 
        "message": "Unauthorized", 
        "referenceId": "ac2155676982514fd2e3199e83a9c9ec", 
        "txnId": "ad5a54b6af3e52ab24d6", 
        "unmappedStatus": "in progress", 
        "submitOtp": { 
            "status": "in progress", 
            "retryAttemptCount": "2" 
        } 
    }, 
    "result": null 
}
```

> 📘 **Notes:**
>
> * In case of a failed response the **retryAttemptCount** parameter indicates the number of retries left for OTP submission. In the above-failed response scenario, the `"retryAttemptCount": "2"` indicates that the customer can retry the OTP submission twice.
> * If the customer enters an incorrect OTP or it had expired, you need to use the **Resend OTP** API to resend the OTP. With each retry, you need to submit the OTP using the **Submit OTP** API described in this section. For more information on **Resend OTP** API, refer to [Resend OTP API](ref:resend-otp-api)