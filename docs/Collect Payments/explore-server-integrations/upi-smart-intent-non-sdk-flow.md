---
title: UPI Smart Intent - Non SDK Flow
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: UPI Smart Intent - Non SDK Flow
  description: ''
  keywords:
    - UPI Smart Intent Non SDK integration
    - Non SDK Integration for PayU UPI Smart Intent
    - UPI Smart Intent non SDK implementation
    - Smart Intent UPI payments integration using Non SDK
    - ' PayU UPI Smart Intent with non SDK integration guide'
  robots: index
next:
  description: ''
---


<Accordion title="Step 3: Retrieve Deeplink(uriIntentData) from the response," icon="fa-code">
If metaData.unmappedStatus = pending, then get the result.intentURIData and add the prefix upi://pay?to make it to create a fully qualified deeplink to trigger the UPI App.

```json
{
    "metaData": {
        "message": null,
        "referenceId": "c99a6455b3e0dc5cd7167ab8c8cc10d2fa153cb509e3f64c6cd0ed9c5b64a8c9",
        "statusCode": null,
        "txnId": "my_order_26075",
        "txnStatus": "pending",
        "unmappedStatus": "pending"
    },
    "result": {
        "paymentId": "403993715535965242",
        "merchantName": "Sudhanshu",
        "merchantVpa": "payutest@hdfcbank",
        "amount": "1.00",
        "intentURIData": "pa=payutest@hdfcbank&pn=Kumar&tr=403993715535965242&tid=PPPL403993715535965242080126220900&am=1.00&cu=INR&tn=UPIIntent",
        "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vdGVzdC5wYXl1LmluL2M5OWE2NDU1YjNlMGRjNWNkNzE2N2FiOGM4Y2MxMGQyYzgzYTk5NmFhNDhiYTk4MmZjMGQ4MTI1MGY1ODgxZjMvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0b2tlbiIgdmFsdWU9IjhERDNFRUFFLUI5NTktQzY1RS03MDczLTYzQTNGQUUxMjZGRiI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYW1vdW50IiB2YWx1ZT0iMS4wMCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0ibWlocGF5aWQiIHZhbHVlPSJjOTlhNjQ1NWIzZTBkYzVjZDcxNjdhYjhjOGNjMTBkMmZhMTUzY2I1MDllM2Y2NGM2Y2QwZWQ5YzViNjRhOGM5Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJkaXNhYmxlSW50ZW50U2VhbWxlc3NGYWlsdXJlIiB2YWx1ZT0iMCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVWcGEiIHZhbHVlPSJwYXl1dGVzdEBoZGZjYmFuayI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVOYW1lIiB2YWx1ZT0iU3VkaGFuc2h1Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJhZGRpdGlvbmFsQ2hhcmdlcyIgdmFsdWU9IjAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InRyYW5zYWN0aW9uRmVlIiB2YWx1ZT0iMS4wMCI+PC9mb3JtPjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0Jz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5vbmxvYWQ9ZnVuY3Rpb24oKXsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb2N1bWVudC5mb3Jtc1sncGF5bWVudF9wb3N0J10uc3VibWl0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvc2NyaXB0PjwvYm9keT48L2h0bWw+",
        "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
    }
}
  ```
</Accordion>

<Accordion title="Step 4: Set the Package Name" icon="fa-code">
Set the packageName as per the app selected by the customer on your checkout page. and start the activity.

  ```java
 fun makePayment(packageName: String,mActivity: Activity,intentUri:String) {
        val i = Intent()
        i.setPackage(packageName)
        i.action = Intent.ACTION_VIEW
        i.data = Uri.parse("upi://pay" + intentUri)
        if (null != mActivity && !mActivity.isFinishing() && !mActivity.isDestroyed()) {
            mActivity.startActivityForResult(i, 101)
        }
    }
  ```
</Accordion>

<Accordion title="Step 5: Handle the response" icon="fa-code">
Once the user completes the payment the UPI app will be closed, and then handle the response onActivityResult.
```java
override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
      super.onActivityResult(requestCode, resultCode, data)
      if (requestCode == 101) {
          data?.getStringExtra("Status")?.let { Log.d("result", it) }
          data?.getStringExtra("response")?.let { Log.d("response", it) }
          //get Status
          //if Status == Success
          // Call Verify Payemnt//
      }
}
```
</Accordion>

<Accordion title="Step 6: Verify the payment" icon="fa-code">
<Verify_Payment_Tabs />
</Accordion>