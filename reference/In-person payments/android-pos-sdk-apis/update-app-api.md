---
title: Update App API
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
To update the application pass the parameters mentioned in the request parameter table as inputs.

**Method**: POST

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parmeter",
    "h-1": "Description",
    "0-0": "handler  \n`mandatory`",
    "0-1": "`handlers`  \nHandlers are used to passing the data and receiving the data between the two classes.",
    "1-0": "Current activity  \n`mandatory`",
    "1-1": "`string`  \nCurrent class or activity",
    "2-0": "DeviceType  \n`mandatory`",
    "2-1": "`string`  \nIdentifies the type of device Ex: N910"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Sample request

```Text JAVA
if (paymentType.equalsIgnoreCase(APP_UPDATE)) {
  initialization = new PaymentInitialization(PaymentTransactionActivity.this);
  initialization.appUpdate(handler, this, DeviceType.N910);
}
```

> 🚧 Warning
> 
> Once the app is updated It will re-direct to the Intent of MTMS application.