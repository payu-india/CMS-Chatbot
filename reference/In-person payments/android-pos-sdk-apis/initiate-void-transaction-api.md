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
The **Initiate Void Transaction** API is used void an existing transaction that was initiated on an Android POS device.

**Method**: POST

Create a `PaymentInitialization` class object and call `initiateVoidTransaction()` method by passing the parameters mentioned in the request parameter table.

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
        Example
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
        `handler` Create a handler inner class. This class will return the response message.
      </td>

      <td>
        handler
      </td>
    </tr>

    <tr>
      <td>
        referenceNumber \
        `mandatory`
      </td>

      <td>
        `string` Pass this parameter to receive the receipt reference number after transaction completed.
      </td>

      <td>
        OD0576
      </td>
    </tr>

    <tr>
      <td>
        appName \
        `mandatory`
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
        appVersion \
        `mandatory`
      </td>

      <td>
        `string` The version of the application.
      </td>

      <td>
        null
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
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Reference number
      </td>

      <td>
        The reference number of the transaction.
      </td>

      <td>
        150410087276
      </td>
    </tr>

    <tr>
      <td>
        Amount
      </td>

      <td>
        The transaction amount.
      </td>

      <td>
        200.00
      </td>
    </tr>

    <tr>
      <td>
        Amount authorized
      </td>

      <td>
        The authorized transaction amount.
      </td>

      <td>
        10.00
      </td>
    </tr>

    <tr>
      <td>
        RRN
      </td>

      <td>
        RRN is a unique 12-digit number to identify a particular transaction.
      </td>

      <td>
        453654
      </td>
    </tr>

    <tr>
      <td>
        Transaction Status
      </td>

      <td>
        The status of the void transaction.    

        Fail - If transaction is not voided, then it will return fail.  

        Success - If the transaction is voided, then it will return the TransactionResponse object.
      </td>

      <td>
        Success
      </td>
    </tr>

    <tr>
      <td>
        isSignature required
      </td>

      <td>
        Whether the signature is required. Default possible values are - Yes/No
      </td>

      <td>
        Yes
      </td>
    </tr>
  </tbody>
</Table>

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
