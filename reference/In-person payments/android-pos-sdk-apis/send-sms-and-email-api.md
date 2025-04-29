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

Create a `PaymentInitialization` class object and call `sendSMSEmail()` method by passing the\
parameters mentioned in the request table.

## Request parameter

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
        referenceNmber \
        `mandatory`
      </td>

      <td>
        `string` Pass the reference number after the transaction response.
      </td>

      <td>
        12345678
      </td>
    </tr>

    <tr>
      <td>
        Mobile No \
        `mandatory`
      </td>

      <td>
        `string` The mobile Number of the customer
      </td>

      <td>
        9000000000
      </td>
    </tr>

    <tr>
      <td>
        Email id \
        `mandatory`
      </td>

      <td>
        `string` The email Id of the customer.
      </td>

      <td>
        [x@gmail.com](mailto:x@gmail.com)
      </td>
    </tr>

    <tr>
      <td>
        Transaction type \
        `mandatory`
      </td>

      <td>
        `string` Type of the transaction (Available inside PaymentTransactionConstants)
      </td>

      <td>
        MICRO\_ATM
      </td>
    </tr>
  </tbody>
</Table>

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
