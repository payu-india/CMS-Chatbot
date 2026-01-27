---
title: Generate UPI Intent API
deprecated: false
hidden: false
metadata:
  robots: index
---
This API allows merchants to generate a UPI payment intent for accepting UPI payments.

HTTP Method: **POST**

**Environment**

|                        |                                                                              |
| :--------------------- | :--------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/info/v1/intent`](https://test.payu.in/info/v1/intent`) |
| Production Environment | [https://info.payu.in/v1/intent](https://info.payu.in/v1/intent)             |

## Request headers

<V2_payment_header_params />

## Request parameters

| Parameter                                     | Description                                                                                                                        | Example                                  |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| transactionId<br /><code>mandatory</code>     | <code>String</code> Unique identifier for the transaction. This should be unique for each request.                                 | 0fd9829f68                               |
| transactionAmount<br /><code>mandatory</code> | <code>String</code> Amount to be paid. The amount should be in the format of "XX.XX".                                              | 190                                      |
| expiryTime<br /><code>mandatory</code>        | <code>String</code> Expiry time for the intent in seconds. After this time, the intent will expire and cannot be used for payment. | 10000                                    |
| refUrl<br /><code>optional</code>             | <code>String</code> Reference URL for the transaction. This can be your website URL or any reference page.                         | [http://www.payu.in](http://www.payu.in) |
| category<br /><code>optional</code>           | <code>String</code> Category code for the transaction. This helps in categorizing the payment for reporting purposes.              | 01                                       |

## Sample request

```bash
curl --location 'https://info.payu.in/v1/intent' \
--header 'mid: 2' \
--header 'Content-Type: application/json' \
--data '{
 "transactionId": "0fd9829f68",
 "transactionAmount": "190",
 "expiryTime": "10000",
 "refUrl": "http://www.payu.in",
 "category": "01"
}'
```

## Sample response

```json
{
    "message": "Success",
    "status": 1,
    "result": {
        "intentId": "upi://pay?pa=payumoney@hdfcbank&pn=PayUMoney&tr=0fd9829f68&am=190.00&cu=INR&mc=5411&tn=Payment%20to%20Merchant",
        "intentUri": "upi://pay?pa=payumoney@hdfcbank&pn=PayUMoney&tr=0fd9829f68&am=190.00&cu=INR&mc=5411&tn=Payment%20to%20Merchant",
        "intentUrl": "https://secure.payu.in/omni?id=000b",
        "intentUrlWithQR": "https://secure.payu.in/omni?id=000b",
        "bankAccounts": [
            {
                "bankName": "HDFC Bank",
                "accountNumber": "XXXXXXXX1234",
                "ifscCode": "HDFC0000001"
            }
        ],
        "transactionId": "0fd9829f68",
        "expiryTime": 10000
    }
}
```

## Response Parameters

| Parameter                           | Description                                                                                           | Example                                                                                                        |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| message                             | <code>String</code> Response message indicating the operation result.                                 | Success                                                                                                        |
| status                              | <code>Integer</code> Status code for the operation. 1 for success, 0 for failure.                     | 1                                                                                                              |
| result.intentId                     | <code>String</code> Generated UPI intent ID in the format of a UPI URI that can be used for payment.  | upi://pay?pa=payumoney@hdfcbank&pn=PayUMoney&tr=0fd9829f68&am=190.00&cu=INR&mc=5411&tn=Payment%20to%20Merchant |
| result.intentUri                    | <code>String</code> URI for UPI payment that can be used in mobile apps for deep linking to UPI apps. | upi://pay?pa=payumoney@hdfcbank&pn=PayUMoney&tr=0fd9829f68&am=190.00&cu=INR&mc=5411&tn=Payment%20to%20Merchant |
| result.intentUrl                    | <code>String</code> URL for payment that can be used in web applications.                             | [https://secure.payu.in/omni?id=000b](https://secure.payu.in/omni?id=000b)                                     |
| result.intentUrlWithQR              | <code>String</code> URL with QR code for payment that can be displayed to users for scanning.         | [https://secure.payu.in/omni?id=000b](https://secure.payu.in/omni?id=000b)                                     |
| result.bankAccounts                 | <code>Array</code> Array of bank account details associated with the merchant.                        | [Object]                                                                                                       |
| result.bankAccounts[].bankName      | <code>String</code> Name of the bank.                                                                 | HDFC Bank                                                                                                      |
| result.bankAccounts[].accountNumber | <code>String</code> Partially masked account number.                                                  | XXXXXXXX1234                                                                                                   |
| result.bankAccounts[].ifscCode      | <code>String</code> IFSC code of the bank branch.                                                     | HDFC0000001                                                                                                    |
| result.transactionId                | <code>String</code> Transaction ID provided in the request.                                           | 0fd9829f68                                                                                                     |
| result.expiryTime                   | <code>Integer</code> Expiry time in seconds as provided in the request.                               | 10000                                                                                                          |
