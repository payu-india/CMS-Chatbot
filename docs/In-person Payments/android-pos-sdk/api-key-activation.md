---
title: API Key Activation
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
On every launch of your application use validate activation method to check if the API key is activated, else use the activate api method to activate the API.

***

## Validate activation

Create an object of Account Validator class and call the isAccountActivated() method from the onCreate() method of your Application class.

> 👍 Callout!
> 
> The Is `accountActivated()` method will return true if the API keys are already activated. Else it will return false. If the method returns false , populate Activation Activity class of activation UI screen with fields of EditText to capture merchant API key and click the button to activate.

```Text JAVA
AccountValidator validator = new AccountValidator(getApplicationContext());
if (!validator.isAccountActivated()) {
  Intent i = new Intent(getApplicationContext(), ActivationActivity.class);
  startActivity(i);
}
```

***

## Activate API

Method: accountActivation()

Create an Account Validator class object and call accountActivation() method by passing the parameters of handler object, merchant API key , partner API key as inputs. Response will be either success or fail with appropriate message

### Request parameter

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "Merchant API Key  \n`mandatory`",
    "0-1": "`String` PayU uses this key for authentication and authorization over the secured layer.",
    "0-2": "ABC515ABC515",
    "1-0": "Partner API  \n`mandatory`",
    "1-1": "`String` PayU uses this key for authentication and authorization over the secured layer. ",
    "1-2": "ABC515ABC515",
    "2-0": "Handler  \n`mandatory`",
    "2-1": "`Handler`  \nHandlers are used to passing the data and receiving the data between the SDK and application UI.",
    "2-2": "handler"
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


### Sample request

```Text JAVA
String mkey = merchantKey.getText().toString();
if (mkey != null) {
  if (mkey.length() == 12) {
    try {
      AccountValidatorvalidator = new
      AccountValidator(getApplicationContext());
      validator.accountActivation(handler, MerchantAPIKey,
        partnerAPIKey);
    } catch (RuntimeException e) {
      e.printStackTrace();
    }
  } else {
    Toast.makeText(ActivationActivity.this,
      "Enter the 12 characters key", Toast.LENGTH_SHORT).show();
  }
} else {
  Toast.makeText(ActivationActivity.this, "Enter the key",
    Toast.LENGTH_SHORT).show();
}
}
```

## Response parameter

| Parameter | Description                                                       |
| :-------- | :---------------------------------------------------------------- |
| Success   | If the API Key Activated                                          |
| Fail      | If API Key is not activated (Ex:-Account block, Invalid API key). |

### Sample response

```Text JAVA
private Handler handler = new Handler() {
  public void handleMessage(android.os.Message msg) {
    if (msg.what == SUCCESS) {
      Intent i = new Intent(ActivationActivity.this,
        MainActivity.class);
      startActivity(i);
    } else if (
      msg.what == FAIL) {
      Toast.makeText(ActivationActivity.this, (String) msg.obj,
        Toast.LENGTH_SHORT).show();
    }
  };
};
```