---
title: EMI Tenure List API
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
The **EMI Tenure List** API is used to get EMI Tenure list from the corresponding bank by passing the parameters mentioned in the request parameter table.

**Method**: POST

## Request parameters

| Parameter | Description | Sample |
| --------- | ----------- | ------ |
| Handler object<br />`mandatory` | `handler` Create a handler inner class. This class will return response message | handler |
| Amount<br />`mandatory` | `string` The amount that is being used for the transaction. | 2000.00 |
| selectedBankDetails<br />`mandatory` | `object` The bank which is selected to process the EMI transaction (selected from EMI list VO). | Bank Details |

## Sample request

```java
initialization.getSelectedBankEMITenureList(selectedbankhandler, amount,
selectedBankDetails);
```

## Response parameters

| Parameter          | Description                                                                                | Sample                                      |
| :----------------- | :----------------------------------------------------------------------------------------- | :------------------------------------------ |
| ArrayList\<EMI\> | `object` Returns the list of the available banks' name and the minimum transaction amount. | Refer to \<\<AcquirerBanks\>\> payload objects. |
|                    |                                                                                            |                                             |

## Sample response

Use this code to fetch the response for this API.

```java
@SuppressLint("HandlerLeak")
private final Handler selectedbankhandler = new Handler()
{
	@SuppressWarnings("unchecked")
	public void handleMessage(android.os.Message msg)
	{
		if (msg.what == SUCCESS)
		{
			acquirerBanks = new AcquirerBanks();
			acquirerBanks = (AcquirerBanks) msg.obj;
			emiDetails = new ArrayList<EMI> ();
			emiDetails = acquirerBanks.getEmiDetails();
			if (emiDetails != null && emiDetails.size() > 0)
			{
				EmiListAdapter emiadapter = new EmiListAdapter(EmiPayment.this,
					R.layout.emi_options, emiDetails);
				emilist.setAdapter(emiadapter);
				emilist.setOnItemClickListener(EmiPayment.this);
			}
		}
		else if (msg.what == FAIL)
		{
			Toast.makeText(getApplicationContext(), msg.obj.toString(),
				Toast.LENGTH_LONG).show();
		}
	};
};
```