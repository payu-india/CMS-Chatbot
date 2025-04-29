---
title: Get Device Information API
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
The **Get Device Information**API  is used to device-related information. To get the device related information such as device serial number, device model, device OS pass the parameters as mentioned in the request parameter table.

> 🚧 Warning!
> 
> The get device information feature is applicable only for N910 device.

**Method**: POST

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "Handler   \n`mandatory`",
    "0-1": "`handler` Handlers are used to passing the data and receiving the data between the two classes.",
    "0-2": "handler",
    "1-0": "DeviceName   \n`mandatory`",
    "1-1": "`string` Device name is used to find the device.",
    "1-2": "DeviceType.N 910",
    "2-0": "address   \n`Optional`",
    "2-1": "`string` Connected device mac address.",
    "2-2": "“XXXXXXX69 09”",
    "3-0": "deviceCom mMode   \n`Optional`",
    "3-1": "`int` Type of communication (USB or bluetooth).",
    "3-2": "0"
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
  initialization = new PaymentInitialization(PaymentTransactionActivity.this);
  initialization.getDeviceInfo(handler, deviceName, deviceCommMode, address);
} catch (RuntimeException e) {
  e.printStackTrace();
}
```

## Response parameters

| Parameter            | Description                                    | Example      |
| :------------------- | :--------------------------------------------- | :----------- |
| Device serial number | Returns the serial number of the device.       | N7NL00411280 |
| Firmware version     | Returns the current firmware of the device.    | V.2.3.00     |
| Model                | string Returns the model number of the device. | N910         |

## Sample response

Use this code to fetch the response of this API.

```Text JAVA
private final Handler handler = new Handler() {
  public void handleMessage(android.os.Message msg) {
    if (msg.what == DEVICE_INFO) {
      DeviceInformation deviceInfo = (DeviceInformation) msg.obj;
      Toast.makeText(PaymentTransactionActivity.this, "Device Serail number:
        "+deviceInfo.getSerialNumer()+"\
        n "+"
        Modelnumber: "+deviceInfo.getModelNumber
        (), Toast.LENGTH_LONG).show();
      finish();
    } else if (msg.what == ERROR_MESSAGe) {
      Toast.makeText(PaymentTransactionActivity.this, (String) msg.obj, Toast.LENGTH_LONG).show();
      finish();
    }
  };
};
```