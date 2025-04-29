---
title: Initiate Void Transaction API
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
The **Initiate Void Transaction **API is used void an existing transaction that was initiated on an Android POS device.

**Method**: POST

Create a `PaymentInitialization` class object and call `initiateVoidTransaction()` method by passing the parameters mentioned in the request parameter table.

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "Handler object   \n`mandatory`",
    "0-1": "`handler` Create a handler inner class. This class will return the response message.",
    "0-2": "handler",
    "1-0": "referenceNumber   \n`mandatory`",
    "1-1": "`string` Pass this parameter to receive the receipt reference number after transaction completed.",
    "1-2": "OD0576",
    "2-0": "appName   \n`mandatory`",
    "2-1": "`string` The name of the application.",
    "2-2": "null",
    "3-0": "appVersion   \n`mandatory`",
    "3-1": "`string` The version of the application.",
    "3-2": "null"
  },
  "cols": 3,
  "rows": 4,
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

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "Reference number",
    "0-1": "The reference number of the transaction.",
    "0-2": "150410087276",
    "1-0": "Amount",
    "1-1": "The transaction amount.",
    "1-2": "200.00",
    "2-0": "Amount authorized",
    "2-1": "The authorized transaction amount.",
    "2-2": "10.00",
    "3-0": "RRN",
    "3-1": "RRN is a unique 12-digit number to identify a particular transaction.",
    "3-2": "453654",
    "4-0": "Transaction Status",
    "4-1": "The status of the void transaction.    \n  \nFail - If transaction is not voided, then it will return fail.  \n  \nSuccess - If the transaction is voided, then it will return the TransactionResponse object.",
    "4-2": "Success",
    "5-0": "isSignature required",
    "5-1": "Whether the signature is required. Default possible values are - Yes/No",
    "5-2": "Yes"
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


## Sample response

Use this code to fetch the response of this API.

```Text JAVA
private final Handler voidHandler = new Handler()
{
	public void handleMessage(android.os.Message msg)
	{
		if (msg.what == SUCCESS)
		{
			String data = null;
			try
			{
				TransactionResponse hs = (TransactionResponse) msg.obj;
				data = new
				ObjectMapper().writerWithDefaultPrettyPrinter().writeValueAsString(hs);
			}
			catch (JsonGenerationException e1)
			{
				e1.printStackTrace();
			}
			catch (JsonMappingException e1)
			{
				e1.printStackTrace();
			}
			catch (IOException e1)
			{
				e1.printStackTrace();
			}
			t
			ransactionresponse.setText(getString(R.string.void_Data) + "\n" + data);
			Toast.makeText(PaymentDetails.this, getString(R.string.void_success),
				Toast.LENGTH_LONG).show();
		}
		i
		f(msg.what == FAIL)
		{
			Toast.makeText(PaymentDetails.this, (String) msg.obj,
				Toast.LENGTH_LONG).show();
		}
		else if (msg.what == ERROR_MESSAGE)
		{
			Toast.makeText(PaymentDetails.this, (String) msg.obj,
				Toast.LENGTH_LONG).show();
		}
	};
};
```