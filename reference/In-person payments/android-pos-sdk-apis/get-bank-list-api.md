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

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| Handler object<br />`mandatory` | `handlerCreate` a handler inner class. This class will return response message. | handler |
| Amount<br />`mandatory` | `stringEMI` The transaction amount. | 2500 |

## Sample request

```java
initialization = new PaymentInitialization(getApplicationContext());
initialization.getEMIBankList(handler, amount);
```

## Response parameters

| Parameter     | Description                                                         | Example                                |
| :------------ | :------------------------------------------------------------------ | :------------------------------------- |
| AcquirerBanks | object List of Available bank names and minimum transaction amount. | Refer to AcquirerBanks payload objects. |
| Amount        | string The transaction amount.                                      | 2500                                   |

## Sample response

Use this code to fetch the response of this API.

```java
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
        AcquirerBanksListAdapter adapter = new AcquirerBanksListAdapter(EmiPayment.this, R.layout.custom_spinner, emiDetails);
        EmispinnerSelectProvider.setAdapter(adapter);
      }
    }
    if (msg.what == FAIL) {
      Toast.makeText(getApplicationContext(), msg.obj.toString(), Toast.LENGTH_LONG).show();
    }
  }
};
```