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
        Handler 
        `mandatory`
      </td>

      <td>
        `handler` Handlers are used to passing the data and receiving the data between the two classes.
      </td>

      <td>
        handler
      </td>
    </tr>

    <tr>
      <td>
        DeviceName \
        `mandatory`
      </td>

      <td>
        `string` Device name is used to find the device.
      </td>

      <td>
        DeviceType.N 910
      </td>
    </tr>

    <tr>
      <td>
        address \
        `Optional`
      </td>

      <td>
        `string` Connected device mac address.
      </td>

      <td>
        “XXXXXXX69 09”
      </td>
    </tr>

    <tr>
      <td>
        deviceCom mMode \
        `Optional`
      </td>

      <td>
        `int` Type of communication (USB or bluetooth).
      </td>

      <td>
        0
      </td>
    </tr>
  </tbody>
</Table>

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
