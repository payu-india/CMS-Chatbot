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
The **Signature Capture** API is used to capture the signature from the customer based on the `PinVerifiedFlag` parameter. When the PinVerifiedFlag is false then this API collects the signature from the customer and send it to SDK.

**Method**: POST

Create a `PaymentInitialization` class object and call `initiateSignatureCapture`() method by passing the parameters mentioned in the request parameter table.

## Request parameters

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
        Sample
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Handler object 
        `mandatory`
      </td>

      <td>
        `handlerhandler` Create a handler inner class. This class will return response message
      </td>

      <td>
        handler
      </td>
    </tr>

    <tr>
      <td>
        Ref.No <br />`mandatory`
      </td>

      <td>
        `stringPass` Transaction reference number which returns from initiateTransaction response.
      </td>

      <td>
        Refer to \<\<**ICCTransactionResponse**>> payload objects.
      </td>
    </tr>

    <tr>
      <td>
        Signature<br />`mandatory`
      </td>

      <td>
        `byte` signature for transaction confirmation.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

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

| Parameter | Description                                                                                          | Example                            |
| :-------- | :--------------------------------------------------------------------------------------------------- | :--------------------------------- |
| Response  | `objectResponse` returns the details of response objects such as response code,response message etc. | Refer to Response payload objects. |

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

<br />
