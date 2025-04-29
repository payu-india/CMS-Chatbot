---
title: Transaction Details API
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
The **Transaction Details** API is used to get the transaction details.

**Method**: POST

Create a `PaymentInitialization` class object and call `initiateTransactionDetails()` method by passing the parameters mentioned in the request parameter table.

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Sample",
    "0-0": "Handler object  \n`mandatory`",
    "0-1": "`handler` Create a handler inner class. This class will return response message.",
    "0-2": "handler",
    "1-0": "`RefNO`   \nmandatory",
    "1-1": "`string` Pass transaction reference number that returns the initiateTransaction response.",
    "1-2": "Refer to **<<ICCTransactionResponse>>** payload objects.",
    "2-0": "merchantRefNo   \n`mandatory`",
    "2-1": "`string` Pass merchant reference number.",
    "2-2": "123654789",
    "3-0": "appName   \n`Optional`",
    "3-1": "`string` The name of the application.",
    "3-2": "null",
    "4-0": "appVersion   \n`Optional`",
    "4-1": "`string` The version of the application.",
    "4-2": "null",
    "5-0": "Transaction Type   \n`Optional`",
    "5-1": "`string` Pass the Type of the transaction (Available inside Payment TransactionConstants class)",
    "5-2": "MICRO_ATM"
  },
  "cols": 3,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample request

```Text JAVA
try
{
	Bitmap bitmap = BitmapFactory.decodeFile(SignatureCaptureActivity.this.getFilesDir()
		.getPath() + SIGNATURE);
	PaymentInitialization initialization = new PaymentInitialization(SignatureCaptureActivity.this);
	initialization.initiateSignatureCapture(handler,
		iccTransactionResponse.getReferenceNumber(), UtilManager.convertBitmapToByteArray(bitmap));
}
catch (RuntimeException e)
{
	e.printStackTrace();
}
```

## Response parameters

| Parameter                    | Description                                                                                                                  | Sample                                            |
| :--------------------------- | :--------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------ |
| `TransactionStatus Response` | objectTransactionStatusResponse returns the details of transaction such as card type, card holder name, reference number etc | Refer to <<TransactionResponse>> payload objects. |

## Sample response

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