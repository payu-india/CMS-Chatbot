---
title: EMI Transaction API
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
The **EMI Transaction** API is used to initiate an EMI transaction for transactions on Android POs. Pass the parameters mentioned in the request parameters table with this method to initiate an EMI Transaction.

**Method**: POST

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "Handler   \n`mandatory`",
    "0-1": "`handler` Handlers are used for sending and receiving the data within the two classes.",
    "0-2": "handler",
    "1-0": "Device type   \n`mandatory`",
    "1-1": "`string` The name of the bluetooth of the respective device",
    "1-2": "DeviceType.ME30S",
    "2-0": "Address   \n`mandatory`",
    "2-1": "`string` The bluetooth address incase of MAC devices.",
    "2-2": "",
    "3-0": "Amount  \n`mandatory`",
    "3-1": "`string` The amount that is being transacted.",
    "3-2": "11.00",
    "4-0": "Transaction type   \n`mandatory`",
    "4-1": "`string` The type of the transaction.",
    "4-2": "PaymentTransactionConst ants.SALE/EMI",
    "5-0": "Payment Type   \n`mandatory`",
    "5-1": "`string` Type of payment is POS for Mobile POS devices.(PayU have multiple payment types like POS,Wallet,qr.)",
    "5-2": "PaymentTransactionConst ants.POS",
    "6-0": "Mobile Number  \n `Optional`",
    "6-1": "`string` The mobile number of the customer.",
    "6-2": "9000000000",
    "7-0": "Name  \n Optional",
    "7-1": "`string` The name of the customer.",
    "7-2": "",
    "8-0": "Latitude  \n `Optional`",
    "8-1": "`double` Geolocation where the transaction took place.",
    "8-2": "71.000001",
    "9-0": "Longitude  \n `Optional`",
    "9-1": "`double` Geolocation where the transaction took place.",
    "9-2": "17.0000001",
    "10-0": "Merchant reference number   \n`mandatory`",
    "10-1": "`string` Merchant Invoice Reference Number or pass current date time stamp. [Max upto 40 characters ]",
    "10-2": "123456",
    "11-0": "Cash back amount   \n `Optional`",
    "11-1": "**string** Pass cash back amount only for SALE WITH CASH BACK  \ntransaction type otherwise pass null value.",
    "11-2": "null",
    "12-0": "deviceCommMode   \n `Optional`",
    "12-1": "`int` Select device communication mode. It’s only applicable for QPOS device rest all devices can be ‘N’.",
    "12-2": "DeviceCommunicationMode.BLUETOOTHCOMMUNICATION",
    "13-0": "orderReferenceNo   \n `Optional`",
    "13-1": "`string` Order reference no (only for PayUs internal apps)",
    "13-2": "",
    "14-0": "appName   \n `Optional`",
    "14-1": "`string` The name of the app.",
    "14-2": "",
    "15-0": "appVersion  \n `Optional`",
    "15-1": "`string` The version of the app.",
    "15-2": "",
    "16-0": "EMI  \n`mandatory`",
    "16-1": "`objectComplete` details about EMI  \ntransaction.",
    "16-2": "<<Refer Section8.5>>"
  },
  "cols": 3,
  "rows": 17,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample request

```Text JAVA
initialization.getSelectedBankEMITenureList(selectedbankhandler, amount,
selectedBankDetails);
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "ICCTransactionRes  \nponse",
    "0-1": "`objectICCTransactionRespons` returns a list of transaction details such as `transactionStatus`,  `responseMessaege` etc.",
    "0-2": "Refer to `ICCTransactionResponse `payload objects."
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample response

Use this code to fetch the response of this API.

```Text JAVA
@SuppressLint("HandlerLeak")
private final Handler handler = new Handler()
	{
		public void handleMessage(android.os.Message msg)
			{
				checkFlag = true;
				if (msg.what == SOCKET_NOT_CONNECTED)
				{
					alertMessage((String) msg.obj);
				}
				else if (msg.what == QPOS_ID)
				{
					Toast.makeText(PaymentTransactionActivity.this, (String) msg.obj,
						Toast.LENGTH_LONG).show();
				}
				else if (msg.what == CHIP_TRANSACTION_APPROVED ||
					msg.what == SWIP_TRANSACTION_APPROVED)
				{
					ICCTransactionResponse iCCTransactionResponse = (ICCTransactionResponse)
					msg.obj;
					if (iCCTransactionResponse.isSignatureRequired())
					{
						Intent i = new Intent(PaymentTransactionActivity.this,
							SignatureCaptureActivity.class);
						i.putExtra("vo", iCCTransactionResponse);
						//mpaysdk 2.0
						i.putExtra("paymentType", paymentType);
						finish();
						PaymentTransactionActivity.this.startActivity(i);
					}
					else
					{
						Intent i = new Intent(PaymentTransactionActivity.this,
							TransactionDetails.class);
						i.putExtra("vo", iCCTransactionResponse);
						//mpaysdk 2.0
						i.putExtra("paymentType", paymentType);;
						f
						inish();
						PaymentTransactionActivity.this.startActivity(i);
					}
				}
				else if (msg.what == CHIP_TRANSACTION_DECLINED ||
					msg.what == SWIP_TRANSACTION_DECLINED)
				{
					ICCTransactionResponse vo = (ICCTransactionResponse) msg.obj;
					Intent i = new Intent(PaymentTransactionActivity.this,
						TransactionDetails.class);
					i.putExtra("vo", vo);
					i.putExtra("paymentType", paymentType);
					PaymentTransactionActivity.this.startActivity(i);
					Toast.makeText(PaymentTransactionActivity.this, "Transaction Status : " +
						vo.getResponseCode() + ":" + vo.getResponseMessage(), Toast.LENGTH_LONG).show();
					finish();
				}
				else if (msg.what == QPOS_DEVICE)
				{
					alertMessage((String) msg.obj);
				}
				else if (msg.what == TRANSACTION_FAILED)
				{
					ICCTransactionResponse vo = (ICCTransactionResponse) msg.obj;
					if (paymentType.equalsIgnoreCase(EMI))
					{
						Intent i = new Intent(PaymentTransactionActivity.this,
							TransactionDetails.class);
						i.putExtra("vo", vo);
						i.putExtra("paymentType", paymentType);
						PaymentTransactionActivity.this.startActivity(i);
						Toast.makeText(PaymentTransactionActivity.this, "Transaction Status :
							" + vo.getResponseCode() + ": " + vo.getResponseMessage(), Toast.LENGTH_LONG).show();
							finish();
						}
						else
						{
							Toast.makeText(PaymentTransactionActivity.this, "Transaction Status :
								" + vo.getResponseCode() + ": " + vo.getResponseMessage(), Toast.LENGTH_LONG).show();
								finish();
							}
						}
						else if (msg.what == TRANSACTION_INITIATED)
						{
							Toast.makeText(PaymentTransactionActivity.this, msg.obj.toString(),
								Toast.LENGTH_LONG).show();
						}
						else if (msg.what == ERROR_MESSAGE)
						{
							alertMessage((String) msg.obj);
						}
						else if (msg.what == TRANSACTION_PENDING)
						{
							Toast.makeText(PaymentTransactionActivity.this,
								(String) msg.obj + "Pending status", Toast.LENGTH_SHORT).show();
							finish();
						}
						else if (msg.what == DISPLAY_STATUS)
						{
							Toast.makeText(PaymentTransactionActivity.this,
								(String) msg.obj, Toast.LENGTH_SHORT).show();
						}
						else if (msg.what == QPOS_EMV_MULITPLE_APPLICATION)
						{
							ArrayList<String> applicationList = (ArrayList < String>) msg.obj;
							emvList = (ListView) findViewById(R.id.application_list);
							emvList.setVisibility(View.VISIBLE);
							ArrayAdapter<String> adapter = new
							ArrayAdapter<String> (PaymentTransactionActivity.this,
								android.R.layout.simple_list_item_1, applicationList);
							emvList.setAdapter(adapter);
							emvList.setOnItemClickListener(new OnItemClickListener()
							{
								@Override
								public void onItemClick(AdapterView<? > parent, View view,
									int position, long id)
								{
									if (initialization != null)
									{
										initialization.getQposListener().executeSelectedEMVApplication(position);
										emvList.setVisibility(View.GONE);
									}
								} });
						}
						else if (msg.what == SUCCESS)
						{
							Toast.makeText(PaymentTransactionActivity.this,
								(String) msg.obj, Toast.LENGTH_SHORT).show();
							Intent i = new Intent(PaymentTransactionActivity.this,
								MainActivity.class);
							finish();
							PaymentTransactionActivity.this.startActivity(i);
						}
					}
```