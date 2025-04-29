---
title: Send SMS and Email API
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
The **Send SMS and Email** API is used to send the details of a transaction over SMS and email.

**Method**: POST

Create a `PaymentInitialization` class object and call `sendSMSEmail()` method by passing the  
parameters mentioned in the request table.

## Request parameter

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Sample",
    "0-0": "Handler object   \n`mandatory`",
    "0-1": "`handler` Create a handler inner class. This class will return response message.",
    "0-2": "handler",
    "1-0": "referenceNmber   \n`mandatory`",
    "1-1": "`string` Pass the reference number after the transaction response.",
    "1-2": "12345678",
    "2-0": "Mobile No   \n`mandatory`",
    "2-1": "`string` The mobile Number of the customer",
    "2-2": "9000000000",
    "3-0": "Email id   \n`mandatory`",
    "3-1": "`string` The email Id of the customer.",
    "3-2": "[x@gmail.com](mailto:x@gmail.com)",
    "4-0": "Transaction type   \n`mandatory`",
    "4-1": "`string` Type of the transaction (Available inside PaymentTransactionConstants)",
    "4-2": "MICRO_ATM"
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample request

```Text JAVA
try {
PaymentInitialization initialization = new PaymentInitialization(
getApplicationContext());
initialization.initiateVoidTransaction(voidHandler,txnResponse.getReferenceNumber()
,null,null);
} catch (RuntimeException e) {
e.printStackTrace();
}
```

## Response parameters

| Parameter | Description                                                           |
| :-------- | :-------------------------------------------------------------------- |
| Success   | If the Email/SMS sent, then it displays success.                      |
| Fail      | If Email/SMS is not sent, then it is failed. (Due to network issues). |

## Sample response

Use this code to fetch the response of the API.

```Text JAVA
@SuppressLint("HandlerLeak")
private final Handler handler = new Handler() {
public void handleMessage(android.os.Message msg) {
if (msg.what == SUCCESS) {
Toast.makeText(SendSMSEmail.this, getString(R.string.success),
Toast.LENGTH_LONG).show();
finish();
} else if (msg.what == FAIL) {
Toast.makeText(SendSMSEmail.this, (String) msg.obj,
Toast.LENGTH_LONG).show();
finish();
} else if (msg.what == ERROR_MESSAGE) {
Toast.makeText(SendSMSEmail.this, (String) msg.obj,
Toast.LENGTH_LONG).show();
finish();
}
};
};
```