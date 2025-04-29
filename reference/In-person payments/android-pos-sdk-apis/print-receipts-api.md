---
title: Print Receipts API
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
The **Print Receipts** API is used to print the charge slip of a transaction for N10 devices only.

**Method**: POST

> 🚧 Warning
>
> This API is applicable only for N10 device.

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
        `handler` Create a handler inner class. This class will return the response message.
      </td>

      <td>
        handler
      </td>
    </tr>

    <tr>
      <td>
        deviceType \
        `mandatory`
      </td>

      <td>
        `string` The device type of the POS terminal
      </td>

      <td>
        N910
      </td>
    </tr>

    <tr>
      <td>
        referenceNumber\
        `mandatory`
      </td>

      <td>
        `string` The transaction reference number.
      </td>

      <td>
        123-45-8575
      </td>
    </tr>

    <tr>
      <td>
        receiptImage \
        `Optional`
      </td>

      <td>
        `bitmap` Pass this parameter to print your company logo in the receipt.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        customerCopy \
        `Optional`
      </td>

      <td>
        `boolean` Determines whether or not to print the customer copy.
      </td>

      <td>
        True
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```Text JAVA
PaymentInitialization initialization=new PaymentInitialization(
PaymentDetails.this);
Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.drawable.payswiff);
initialization.initiatePrintReceipt(printHandler,
DeviceType.N910,txnResponse.getReferenceNumber(),null,customerCopy);
```

## Sample response

```Text JAVA
@SuppressLint("HandlerLeak")
private final Handler printHandler = new Handler()
{
	public void handleMessage(android.os.Message msg)
	{
		if (msg.what == SUCCESS)
		{
			Toast.makeText(PaymentDetails.this, "Success",
				Toast.LENGTH_LONG).show();
		}
		i
		f(msg.what == FAIL)
		{
			Toast.makeText(PaymentDetails.this, (String) msg.obj,
				Toast.LENGTH_LONG).show();
			//finish();
		}
		else if (msg.what == ERROR_MESSAGE)
		{
			Toast.makeText(PaymentDetails.this, (String) msg.obj,
				Toast.LENGTH_LONG).show();
		}
	};
};
```

***

# Custom printer

Use the custom printer API for customization of print receipt such as the size of the fonts in the receipt, the alignment of the texts in the receipt, etc.

> ❗️ Warning
>
> This API is applicable only for N910 device.

Custom printer allows you to print the following:

* Print text
* Print image
* Print QR code.
* Print multi-language and special characters

Custom printer has the following customization options:

### Font Size

| Type                                      | Parameter | Description                                               |
| :---------------------------------------- | :-------- | :-------------------------------------------------------- |
| `Small font`                              | s         | Prints 48 characters in a row.                            |
| `Medium font`                             | n         | Prints 32 characters in a row                             |
| `Large font`                              | l         | Prints 24 characters in a row                             |
| `Small font, width, standard font height` | sn        | Prints small font, small width, and standard font height. |
| `Small font, width and large font height` | sl        | Prints small font, small width, and large font height.    |
| `Standard font width, large font height`  | nl        | Prints standard font, small width, and large font height. |

### Text Alignment

| Type   | Parameter | Description               |
| :----- | :-------- | :------------------------ |
| Left   | l         | Prints text in the left.  |
| Right  | r         | Prints text in the right. |
| Center | c         | Print text in the center. |

***

# Print Text

**Method**: POST

Use this API to print text. If you require to print custom text, use {user["print custom text API"]} instead.

## Request parameter

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
        `handler` Create a handler inner class. This class will return response message.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        DeviceType \
        `mandatory`
      </td>

      <td>
        `string` This parameter is used to Identify the device.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        StringBuffer\
        `mandatory`
      </td>

      <td>
        `stringBuffer` Used to append, concatenate, and manipulate Strings or sequence of characters.
      </td>

      <td>
        `StringBuffer sb=newStringBuffer();`
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```Text JAVA
StringBuffer scriptBuffer = new StringBuffer();
scriptBuffer.append("!hz l\n !asc l\n !gray 5\n");//Set the title font to large
scriptBuffer.append("!yspace 5\n");// Set the line spacing, the value is [0,60], the default is 6
scriptBuffer.append("*text " + alignment + " ++++++++++++++ X ++++++++\n");
scriptBuffer.append("*text " + alignment + " SampleData\n");
scriptBuffer.append("!yspace 10\n");// Set content line spacing
scriptBuffer.append("*text l DATE:25-07-2020 " + "\n");//print text on Right side
scriptBuffer.append("*text l MID:5245678659\n");
scriptBuffer.append("*text l INVOICE:61349\n");
scriptBuffer.append("*text l CARD:441962XXXX1912[CHIP]\n");
scriptBuffer.append("*text l AUTH CODE:61349\n");
scriptBuffer.append("*text r RRN:159566454868\n");//print text on left side
scriptBuffer.append("*text r AID:A0000000031010\n");
scriptBuffer.append("*text l TVR:0000000000\n");
scriptBuffer.append("*text c TC:28EDE192A8837CAA\n");//print text on Center
scriptBuffer.append("*line" + "\n");//Print dotted line
PaymentInitialization initialization = new PaymentInitialization(ScannerViewActivity.this);
initialization.printScript(printerHandler, DeviceType.N910, scriptBuffer);
```

## Sample response

Use this code to fetch the response of this API.

```Text JAVA
@SuppressLint("HandlerLeak")
private final Handler printerHandler = new Handler()
{
	public void handleMessage(android.os.Message msg)
	{
		if (msg.what == SUCCESS)
		{
			Toast.makeText(N910PrinterActivity.this,
				(String) msg.obj, Toast.LENGTH_SHORT).show();
		}
		else
		{
			Toast.makeText(N910PrinterActivity.this,
				(String) msg.obj, Toast.LENGTH_SHORT).show();
		}
	}
};
```

## Print custom text

Use this API to print custom text.

> 📘 Remember
>
> If print characters are more than 32 ,the text will print in the next line.

## Sample request

```Text JAVA
StringBuffer scriptBuffer = new StringBuffer()
scriptBuffer.append("!hz l\n !asc l\n !gray 5\n");//Set font to large
scriptBuffer.append("*text c " + "Print Sample text " + "\n");//set Text center
scriptBuffer.append("*text l " + "Print Sample text " + "\n");//set Text Left
scriptBuffer.append("*text c " + "Print Sample text " + "\n");//Set Text Right
PaymentInitialization initialization = new PaymentInitialization(ScannerViewActivity.this);
initialization.printScript(printerHandler, DeviceType.N910, scriptBuffer);
```

***

# Print Image

Use this API to print image.

## Request parameter

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
        `handler` Create a handler inner class. This class will return response message.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        DeviceType \
        `mandatory`
      </td>

      <td>
        `string` This parameter is used to Identify the device.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Map\<String,Bitmap>\
        `mandatory`
      </td>

      <td>
        `bitmap` This parameter stores the data in a pair such\
        that each element  has a key associated  with it.
      </td>

      <td>
        ```
        Map<String,Bitmap>  
        map=new  
        Map<String,Bitmap>
        ```
      </td>
    </tr>

    <tr>
      <td>
        StringBuffer\
        `mandatory`
      </td>

      <td>
        `stringBuffer` Used to append, concatenate, and manipulate Strings or sequence of characters.
      </td>

      <td>
        `StringBuffer sb=newStringBuffer();`
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```Text JAVA
StringBuffer scriptBuffer = new StringBuffer();
scriptBuffer.append("!hz l\n !asc l\n !gray 5\n");//Set the title font to large
scriptBuffer.append("!yspace 5\n");// Set the line spacing, the value is [0,60], the default is 6
scriptBuffer.append("*text " + alignment + " ++++++++++++++ X ++++++++\n");
scriptBuffer.append("*text " + alignment + " SampleData\n");
scriptBuffer.append("!yspace 10\n");// Set content line spacing
scriptBuffer.append("*text l DATE:25-07-2020 " + "\n");//print text on Right side
scriptBuffer.append("*text l MID:5245678659\n");
scriptBuffer.append("*text l INVOICE:61349\n");
scriptBuffer.append("*text l CARD:441962XXXX1912[CHIP]\n");
scriptBuffer.append("*text l AUTH CODE:61349\n");
scriptBuffer.append("*text r RRN:159566454868\n");//print text on left side
scriptBuffer.append("*text r AID:A0000000031010\n");
scriptBuffer.append("*text l TVR:0000000000\n");
scriptBuffer.append("*text c TC:28EDE192A8837CAA\n");//print text on Center
scriptBuffer.append("*line" + "\n");//Print dotted line
PaymentInitialization initialization = new PaymentInitialization(ScannerViewActivity.this);
initialization.printScript(printerHandler, DeviceType.N910, scriptBuffer);
```

## Sample response

Use this code to fetch the response for this API.

```Text JAVA
@SuppressLint("HandlerLeak")
private final Handler printerHandler = new Handler() {
public void handleMessage(android.os.Message msg) {
if (msg.what == SUCCESS) {
Toast.makeText(N910PrinterActivity.this,
(String) msg.obj, Toast.LENGTH_SHORT).show();
} else {
Toast.makeText(N910PrinterActivity.this,
(String) msg.obj, Toast.LENGTH_SHORT).show();
}
}
};
```

***

# Print QR Code

Use this API to print QR code.

## Request Parameter

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
        `handler` Create a handler inner class. This class will return response message.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        DeviceType \
        `mandatory`
      </td>

      <td>
        `string` This parameter is used to Identify the device.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        StringBuffer\
        `mandatory`
      </td>

      <td>
        `stringBuffer` Used to append, concatenate, and manipulate Strings or sequence of characters.
      </td>

      <td>
        `StringBuffer sb=newStringBuffer();`
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```Text JAVA
//Request
StringBuffer scriptBuffer = new StringBuffer();
scriptBuffer.append("!qrcode "+size+" "+width+"\n*qrcode c Your Text goes here\n");
PaymentInitialization initialization = new PaymentInitialization(ScannerViewActivity.
```

> 👍 Callout
>
> In above sample request maximum range of size can be 50 to 350 and maximum range of width can be 1 to 3.

## Sample response

Use this code to fetch the response of this API.

```Text JAVA
@SuppressLint("HandlerLeak")
private final Handler printerHandler = new Handler() {
public void handleMessage(android.os.Message msg) {
if (msg.what == SUCCESS) {
Toast.makeText(N910PrinterActivity.this,
(String) msg.obj, Toast.LENGTH_SHORT).show();
} else {
Toast.makeText(N910PrinterActivity.this,
(String) msg.obj, Toast.LENGTH_SHORT).show();
}
}
};
```

***

# Multi-language and Special characters

Use this API to print multi-language and special characters.

## Request parameter

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
        `handler` Create a handler inner class. This class will return response message.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        DeviceType \
        `mandatory`
      </td>

      <td>
        `string` Passed for Identification of the device.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Font\
        `mandatory`
      </td>

      <td>
        `string` This parameter prints language other than English and special characters.
      </td>

      <td>
        Roboto.ttf
      </td>
    </tr>

    <tr>
      <td>
        Map\<String,Bitmap>\
        `mandatory`
      </td>

      <td>
        `bitmap` This parameter stores the data in a pair such that each element has a key associated with it.
      </td>

      <td>
        ```
        Map<String,Bitmap>  
        map=new  
        Map<String,Bitmap>
        ```
      </td>
    </tr>

    <tr>
      <td>
        StringBuffer\
        `mandatory`
      </td>

      <td>
        `stringBuffer` Used to append, concatenate, and manipulate Strings or sequence of characters.
      </td>

      <td>
        `StringBuffer sb=newStringBuffer();`
      </td>
    </tr>
  </tbody>
</Table>

> **Notes**:
>
> 1. If Image is not required in print you can pass the Map object as null. The specified font must be available in the application assets folder, else it will print boxes instead. Ensure that you are using proper .ttf file which supports both language and special characters. Example: src/main/assets/Roboto.ttf
> 2. If you are using Locale to get string resources, ensure that you are setting it to English at the end of print.\
>    Example, for Hindi: Context context = LocaleHelper.setLocale(context,”hi”);\
>    Resources resources =context.getResources().getString(R.string.your\_string); You need to set Locale again at the end of print, else the device language will get changed. Example, if you want to change the language to english: Context context = LocaleHelper.setLocale(context,”en”);\
>    Once a transaction is initiated, back button must be disabled until the transaction is completed.

## Sample request

```Text JAVA
Bitmap bitmap = BitmapFactory.decodeResource(getApplicationContext().getResources(),
	R.drawable.payswiff);
Map<String, Bitmap> map = new HashMap<String, Bitmap> ();
String bmp0 = "bmp0;";
map.put(bmp0, bitmap);
StringBuffer buffer = new StringBuffer();
buffer.append("*line\n!yspace 5\n");
buffer.append("*line\n!yspace 5\n");
buffer.append("*image c 200 * 300 path:" + bmp0 + "\n");	//Print image in center
buffer.append("*line\n!yspace 5\n");
buffer.append("*text c आपका पाठ यहाँ जाता है\n");
buffer.append("*line\n!yspace 5\n");
buffer.append("!qrcode 200 2\n*qrcode c ABCDEFG\n");	//Print QR in center
buffer.append("*line\n!yspace 5\n");
buffer.append("*text c € £ $ ¥ ₹\n");	//Special characters
buffer.append("*line\n!yspace 5\n");
buffer.append("!barcode 3 100\n*barcode c 1234567\n");	//Print barcode in center

PaymentInitialization initialization = new PaymentInitialization(N910PrinterActivity.this);
initialization.printImage(printerHandler, DeviceType.N910, buffer, map, "Yantramanav-Medium.ttf");
```

## Sample Response

Use this code to fetch the response of this API.

```Text JAVA
@SuppressLint("HandlerLeak")
private final Handler printerHandler = new Handler() {
public void handleMessage(android.os.Message msg) {
if (msg.what == SUCCESS) {
Toast.makeText(N910PrinterActivity.this,
(String) msg.obj, Toast.LENGTH_SHORT).show();
} else {
Toast.makeText(N910PrinterActivity.this,
(String) msg.obj, Toast.LENGTH_SHORT).show();
}
}
};
```
