---
title: Get Bank List API
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
Fetch the list of banks for an EMI transaction by passing the handler and amount parameters with this method.

**Method**: POST

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "Handler object  \n`mandatory`",
    "0-1": "`handlerCreate` a handler inner class. This class will return response message.",
    "0-2": "handler",
    "1-0": "Amount   \n`mandatory`",
    "1-1": "`stringEMI` The transaction amount.",
    "1-2": "2500"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample request

```Text JAVA
initialization = new PaymentInitialization(getApplicationContext());
initialization.getEMIBankList(handler, amount);
```

## Response paramters

| Parameter     | Description                                                         |                                         |
| :------------ | :------------------------------------------------------------------ | :-------------------------------------- |
| AcquirerBanks | object List of Available bank names and minimum transaction amount. | Refer to AcquirerBanks payload objects. |
| Amount        | stringThe transaction amount.                                       | 2500                                    |

## Sample response

Use this code to fetch the response of this API.

```Text JAVA
@SuppressLint("HandlerLeak")
private final Handler handler = new Handler() {
@SuppressWarnings("unchecked")
public void handleMessage(android.os.Message msg) {
if (msg.what == SUCCESS) {
acquirerBanks = new AcquirerBanks();
acquirerBanks = (AcquirerBanks) msg.obj;
emiDetails = new ArrayList<EMI>();
emiDetails = acquirerBanks.getEmiDetails();
if (emiDetails != null && emiDetails.size() > 0) {
AcquirerBanksListAdapter adapter = new
AcquirerBanksListAdapter(EmiPayment.this,
R.layout.custom_spinner, emiDetails);
EmispinnerSelectProvider.setAdapter(adapter);
}
}i
f (msg.what == FAIL) {
Toast.makeText(getApplicationContext(), msg.obj.toString(),
Toast.LENGTH_LONG).show();
}
};
};
```