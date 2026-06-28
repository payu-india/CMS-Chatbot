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
        `handler` Create a handler inner class. This class will return response message.
      </td>

      <td>
        handler
      </td>
    </tr>

    <tr>
      <td>
        `RefNO` <br />mandatory
      </td>

      <td>
        `string` Pass transaction reference number that returns the initiateTransaction response.
      </td>

      <td>
        Refer to **{user.ICCTransactionResponse}** payload objects.
      </td>
    </tr>

    <tr>
      <td>
        merchantRefNo <br />`mandatory`
      </td>

      <td>
        `string` Pass merchant reference number.
      </td>

      <td>
        123654789
      </td>
    </tr>

    <tr>
      <td>
        appName <br />`Optional`
      </td>

      <td>
        `string` The name of the application.
      </td>

      <td>
        null
      </td>
    </tr>

    <tr>
      <td>
        appVersion <br />`Optional`
      </td>

      <td>
        `string` The version of the application.
      </td>

      <td>
        null
      </td>
    </tr>

    <tr>
      <td>
        Transaction Type <br />`Optional`
      </td>

      <td>
        `string` Pass the Type of the transaction (Available inside Payment TransactionConstants class)
      </td>

      <td>
        MICRO\_ATM
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

| Parameter                    | Description                                                                                                                 | Sample                                               |
| :--------------------------- | :-------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------- |
| `TransactionStatus Response` | objectTransactionStatusResponse returns the details of transaction such as card type, cardholder name, reference number etc | Refer to {user.TransactionResponse} payload objects. |

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

<br />
