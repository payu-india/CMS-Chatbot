---
title: Signature Capture API
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
The** Signature Capture** API is used to capture the signature from the customer based on the `PinVerifiedFlag` parameter. When the PinVerifiedFlag is false then this API collects the signature from the customer and send it to SDK.

**Method**: POST

Create a `PaymentInitialization` class object and call `initiateSignatureCapture`() method by passing the parameters mentioned in the request parameter table.

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Sample",
    "0-0": "Handler object   \n`mandatory`",
    "0-1": "`handlerhandler` Create a handler inner class. This class will return response message",
    "0-2": "handler",
    "1-0": "Ref.No   \n`mandatory`",
    "1-1": "`stringPass` Transaction reference number which returns from initiateTransaction response.",
    "1-2": "Refer to \\<\\<**ICCTransactionResponse**>> payload objects.",
    "2-0": "Signature  \n`mandatory`",
    "2-1": "`byte` signature for transaction confirmation.",
    "2-2": ""
  },
  "cols": 3,
  "rows": 3,
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

| Parameter | Description                                                                                           | Example                            |
| :-------- | :---------------------------------------------------------------------------------------------------- | :--------------------------------- |
| Response  | `objectResponse` returns the details of response objects such as response code,response messaege etc. | Refer to Response payload objects. |

## Sample response

Use this code to fetch the response of the API.

```Text JAVA
private final Handler handler = new Handler()
{
	public void handleMessage(android.os.Message msg)
	{
		if (msg.what == SUCCESS)
		{
			Toast.makeText(SignatureCaptureActivity.this, getString(R.string.success),
				Toast.LENGTH_LONG).show();
			Intent i = new Intent(SignatureCaptureActivity.this,
				TransactionDetails.class);
			i.putExtra("vo", iccTransactionResponse);
			finish();
			SignatureCaptureActivity.this.startActivity(i);
		}
		else if (msg.what == FAIL)
		{
			Toast.makeText(SignatureCaptureActivity.this, (String) msg.obj,
				Toast.LENGTH_LONG).show();
		}
		else if (msg.what == ERROR_MESSAGE)
		{
			Toast.makeText(SignatureCaptureActivity.this, (String) msg.obj,
				Toast.LENGTH_LONG).show();
		}
	};
};
```