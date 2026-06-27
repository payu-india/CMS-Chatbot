---
title: Initiate Transaction API
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
Create a Payment Initialization class object and call initiate transaction method by passing the parameters mentioned in the request parameters table.

PayU’s POS terminals support two types of transaction as follows:

- **Sale**<br />Customer can use debit or credit card in Sale mode and make transaction “N” number of times. For Sale Transaction, Amount should above Rs. 1000/- (check test cases) in UAT Environment. For production amount should be Minimum of Rs. 5/-.
- **EMI**<br />Customer can use credit card in EMI mode and make transaction “N” number of times. To support EMI<br />transaction type please refer EMI Transaction APIs

<Callout icon="❗️" theme="error">
  ### Watch Out

  Request parameters are consistent for all types of transaction . Only the `transactionType` parameter will be changed with the corresponding transaction type.
</Callout>

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
        `handler` Handlers are used for sending and receiving the data within the two classes.
      </td>

      <td>
        handler
      </td>
    </tr>

    <tr>
      <td>
        Device type <br />`mandatory`
      </td>

      <td>
        `string` The name of the bluetooth of the respective device.
      </td>

      <td>
        DeviceType.ME30S
      </td>
    </tr>

    <tr>
      <td>
        Address <br />`mandatory`
      </td>

      <td>
        `string` The bluetooth address in case of MAC devices.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Amount<br />`mandatory`
      </td>

      <td>
        `string` The amount that is being transacted.
      </td>

      <td>
        11.00
      </td>
    </tr>

    <tr>
      <td>
        Transaction type <br />`mandatory`
      </td>

      <td>
        `string` The type of the transaction.
      </td>

      <td>
        PaymentTransactionConst ants.SALE/EMI
      </td>
    </tr>

    <tr>
      <td>
        Payment Type <br />`mandatory`
      </td>

      <td>
        `string` Type of payment is POS for Mobile POS devices.(PayU have multiple payment types like POS,Wallet,qr.)
      </td>

      <td>
        PaymentTransactionConst ants.POS
      </td>
    </tr>

    <tr>
      <td>
        Mobile Number<br /> `Optional`
      </td>

      <td>
        `string` The mobile number of the customer.
      </td>

      <td>
        9000000000
      </td>
    </tr>

    <tr>
      <td>
        Name<br /> `Optional`
      </td>

      <td>
        `string` The name of the customer.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Latitude<br /> `Optional`
      </td>

      <td>
        `double` Geolocation where the transaction took place.
      </td>

      <td>
        71.000001
      </td>
    </tr>

    <tr>
      <td>
        Longitude<br /> `Optional`
      </td>

      <td>
        `double` Geolocation where the transaction took place.
      </td>

      <td>
        17.0000001
      </td>
    </tr>

    <tr>
      <td>
        Merchant reference number <br />`mandatory`
      </td>

      <td>
        `string` Merchant Invoice Reference Number or pass current date time stamp. \[Max upto 40 characters].
      </td>

      <td>
        123456
      </td>
    </tr>

    <tr>
      <td>
        Cash back amount <br /> `Optional`
      </td>

      <td>
        `string` Pass cash back amount only for SALE WITH CASH BACK transaction type otherwise pass null value.
      </td>

      <td>
        null
      </td>
    </tr>

    <tr>
      <td>
        deviceCommMode <br /> `Optional`
      </td>

      <td>
        `int` Select device communication mode. It’s only applicable for QPOS device rest all devices can be ‘N’.
      </td>

      <td>
        DeviceCommunicationMode.BLUETOOTHCOMMUNICATION
      </td>
    </tr>

    <tr>
      <td>
        orderReferenceNo <br /> `Optional`
      </td>

      <td>
        `string` Order reference no (only for PayUs internal apps)
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        appName <br /> `Optional`
      </td>

      <td>
        `string` The name of the app.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        appVersion<br /> `Optional`
      </td>

      <td>
        `string` The version of the app.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```Text JAVA
try {
  initialization = new PaymentInitialization(
    PaymentTransactionActivity.this);
  initialization.initiateTransaction(handler, deviceName, address, amount,
    paymentType, PaymentTransactionConstants.POS, null, null, 71.000001, 17.000001,
    merchantRefNo, null, deviceCommMode, merchantRefNo, null, null);
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
        ICCTransactionRes
        ponse
      </td>

      <td>
        `objectICCTransactionRespons` returns a list of transaction details such as `transactionStatus`,  `responseMessaege` etc.
      </td>

      <td>
        Refer to {user.ICCTransactionRespons} payload objects.
      </td>
    </tr>
  </tbody>
</Table>

## Sample response

Use this code to fetch the response of this API.

```Text JAVA
@SuppressLint("HandlerLeak")
private final Handler handler = new Handler() {
    public void handleMessage(android.os.Message msg) {
        checkFlag = true;
        if (msg.what == SOCKET_NOT_CONNECTED) {
          alertMessage((String) msg.obj);
        }
        i
        f(msg.what == QPOS_ID) {
          Toast.makeText(PaymentTransactionActivity.this, (String) msg.obj,
            Toast.LENGTH_LONG).show();
        } else if (msg.what == CHIP_TRANSACTION_APPROVED ||
          msg.what == SWIP_TRANSACTION_APPROVED) {
          ICCTransactionResponse iCCTransactionResponse = (ICCTransactionResponse)
          msg.obj;
          if (iCCTransactionResponse.isSignatureRequired()) {
            Intent i = new Intent(PaymentTransactionActivity.this,
              SignatureCaptureActivity.class);
            i.putExtra("vo", iCCTransactionResponse);
            //mpaysdk 2.0
            i.putExtra("paymentType", paymentType);
            finish();
            PaymentTransactionActivity.this.startActivity(i);
          } else {
            Intent i = new Intent(PaymentTransactionActivity.this,
              TransactionDetails.class);
            i.putExtra("vo", iCCTransactionResponse);
            //mpaysdk 2.0
            i.putExtra("paymentType", paymentType);;
            f
            inish();
            PaymentTransactionActivity.this.startActivity(i);
          }
        } else if (msg.what == CHIP_TRANSACTION_DECLINED ||
          msg.what == SWIP_TRANSACTION_DECLINED) {
          ICCTransactionResponse vo = (ICCTransactionResponse) msg.obj;
          Intent i = new Intent(PaymentTransactionActivity.this, TransactionDetails.class);
          i.putExtra("vo", vo);
          i.putExtra("paymentType", paymentType);
          PaymentTransactionActivity.this.startActivity(i);
          Toast.makeText(PaymentTransactionActivity.this, "Transaction Status : " +
            vo.getResponseCode() + ":" + vo.getResponseMessage(), Toast.LENGTH_LONG).show();
          finish();
        } else if (msg.what == QPOS_DEVICE) {
          alertMessage((String) msg.obj);
        } else if (msg.what == TRANSACTION_FAILED) {
          ICCTransactionResponse vo = (ICCTransactionResponse) msg.obj;
          if (paymentType.equalsIgnoreCase(EMI)) {
            Intent i = new Intent(PaymentTransactionActivity.this,
              TransactionDetails.class);
            i.putExtra("vo", vo);
            i.putExtra("paymentType", paymentType);
            PaymentTransactionActivity.this.startActivity(i);
            Toast.makeText(PaymentTransactionActivity.this, "Transaction Status :
              " + vo.getResponseCode() + ": " + vo.getResponseMessage(), Toast.LENGTH_LONG).show();
              finish();
            }
            else {
              Toast.makeText(PaymentTransactionActivity.this, "Transaction Status :
                " + vo.getResponseCode() + ": " + vo.getResponseMessage(), Toast.LENGTH_LONG).show();
                finish();
              }
            } else if (msg.what == TRANSACTION_INITIATED) {
              Toast.makeText(PaymentTransactionActivity.this, msg.obj.toString(), Toast.LE NGTH_LONG).show();
            } else if (msg.what == ERROR_MESSAGE) {
              alertMessage((String) msg.obj);
            } else if (msg.what == TRANSACTION_PENDING) {
              Toast.makeText(PaymentTransactionActivity.this,
                (String) msg.obj + "Pending status",
                Toast.LENGTH_SHORT).show();
              finish();
            } else if (msg.what == DISPLAY_STATUS) {
              Toast.makeText(PaymentTransactionActivity.this,
                (String) msg.obj, Toast.LENGTH_SHORT).show();
            } else if (msg.what == QPOS_EMV_MULITPLE_APPLICATION) {
              ArrayList < String > applicationList = (ArrayList < String > ) msg.obj;
              emvList = (ListView) findViewById(R.id.application_list);
              emvList.setVisibility(View.VISIBLE);
              ArrayAdapter < String > adapter = new
              ArrayAdapter < String > (PaymentTransactionActivity.this,
                android.R.layout.simple_list_item_1, applicationList);
              emvList.setAdapter(adapter);
              emvList.setOnItemClickListener(new OnItemClickListener() {
                @Override
                public void onItemClick(AdapterView < ? > parent, View view,
                  int position, long id) {
                  if (initialization != null) {
                    initialization.getQposListener().executeSelectedEMVApplication(position);
                    emvList.setVisibility(View.GONE);
                  }
                }
              });
            } else if (msg.what == SUCCESS) {
              Toast.makeText(PaymentTransactionActivity.this,
                (String) msg.obj, Toast.LENGTH_SHORT).show();
              Intent i = new Intent(PaymentTransactionActivity.this,
                MainActivity.class);
              finish();
              PaymentTransactionActivity.this.startActivity(i);
            }
          }
        };
```

<br />
