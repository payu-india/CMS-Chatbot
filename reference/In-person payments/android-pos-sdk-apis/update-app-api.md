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

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        handler
        `mandatory`
      </td>

      <td>
        `handlers`<br />Handlers are used to passing the data and receiving the data between the two classes.
      </td>
    </tr>

    <tr>
      <td>
        Current activity<br />`mandatory`
      </td>

      <td>
        `string`<br />Current class or activity
      </td>
    </tr>

    <tr>
      <td>
        DeviceType<br />`mandatory`
      </td>

      <td>
        `string`<br />Identifies the type of device Ex: N910
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```Text JAVA
if (paymentType.equalsIgnoreCase(APP_UPDATE)) {
  initialization = new PaymentInitialization(PaymentTransactionActivity.this);
  initialization.appUpdate(handler, this, DeviceType.N910);
}
```

<Callout icon="🚧" theme="warn">
  ### Warning

  Once the app is updated It will re-direct to the Intent of MTMS application.
</Callout>

<br />
