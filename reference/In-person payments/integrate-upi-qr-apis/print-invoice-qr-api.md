---
title: Print Invoice QR API
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
The **Print Invoice QR** API is used to generate Dynamic UPI QR which can be printed on merchant Invoice. Each QR can be associated to respective Amount and Order no which can be used to accept unique payments. GST details can also be captured and linked during QR code generation.

**Example**

The Print Invoice QR API can be used by large distributors who accept payments from their buyers by raising periodic Invoice and payment is made by the buyers post receipt of the Invoice. Here these distributors can generate Print Invoice QR and print it in the Invoice which basically gives the buyers an option to scan and make UPI based payments against the invoice. Since the QR will have invoice details embedded during generation transactions are automatically reconciled.

This API generate UPI or BQR QR. This API returns either Base64, string or image format of the QR based on the request type.

| Environment | URI                                             |
| :---------- | :---------------------------------------------- |
| Production  | <https://info.payu.in/merchant/postservice.php> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Sample Value",
    "0-0": "key  \n`mandatory`",
    "0-1": "string This parameter must include the merchant key that was provided by PayU.  \nReference: For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n**Production**: Generate Production Merchant Key and Sat.  \n**Test**: Generate Test Merchant Key and Salt.",
    "0-2": "Your Test Key",
    "1-0": "command  \n`mandatory`",
    "1-1": "`string` The parameter must contain the name of the web service. For this API, generate_invoice_qr must be posted.",
    "1-2": "generate_invoice_qr",
    "2-0": "hash  \n`mandatory`",
    "2-1": "`string` This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:  \n  \nsha512(key|command|var1|salt)  \n  \nsha512 is the encryption method used here.",
    "2-2": "ajh84babvav",
    "3-0": "var1  \n`mandatory`",
    "3-1": "`json` This parameter will include a JSON format of the transaction details. For more information, refer to the >.",
    "3-2": "Refer the <<var Sample>> section."
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


### Fields in var1 Parameter Description

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "transactionId  \n`mandatory`",
    "0-1": "`string` This must contain the merchant transaction Identifier. This must be unique (after a successful transaction) & alphanumeric special (less than 40 characters & excluding >,\\<, &, ‘)",
    "0-2": "1234_abcdedf",
    "1-0": "transactionAmount  \n`mandatory`",
    "1-1": "`float` This must contain the amount for which QR needs to be generated. This must be greater than or equal to 1.00.",
    "1-2": "1005, 1042.23, 95494.4, 10000.00",
    "2-0": "merchantVpa  \n`optional`",
    "2-1": "`string` This must contain the merchant's VPA in which payment will be collected. If not sent, VPA registered against given merchant Key is used.",
    "2-2": "yellowqr. payu@hdfc",
    "3-0": "expiryTime  \n`optional`",
    "3-1": "`numeric` This must contain the  time in seconds for which the QR is active. If empty, merchant level expiry is used. If there is no merchant level value, the global value is used.",
    "3-2": "3600",
    "4-0": "qrName  \nmerchantVpa  \n`optional`",
    "4-1": "`string` This field is used to post the merchant's name to be embedded in the QR. If the value is not posted, the merchant’s name registered during the onboarding process will be used.",
    "4-2": "PayU",
    "5-0": "qrCity  \nmerchantVpa  \n`optional`",
    "5-1": "`string` This parameter is used to post the merchant's city that will be embedded in the QR. If the value not posted, merchant’s city registered during the onboarding process will be used.",
    "5-2": "Gurgaon",
    "6-0": "qrPinCode  \n`optional`",
    "6-1": "`string` This field is used to post the merchant's PIN code to be embedded in the QR. If not sent, merchant’s PIN code registered during the onboarding process will be used.",
    "6-2": "122001",
    "7-0": "customerName  \n`optional`",
    "7-1": "`string` This field must contain the customer name.",
    "7-2": "Ravi",
    "8-0": "customerCity  \n`optional`",
    "8-1": "`string` This field must contain the customer city.",
    "8-2": "122001",
    "9-0": "customerPhone  \n`optional`",
    "9-1": "`string` This field must contain the customer phone number.",
    "9-2": "9833207164",
    "10-0": "customerEmail  \n`optional`",
    "10-1": "`string` This field must contain the customer email address.",
    "10-2": "[hello@payu.in](mailto:hello@payu.in)",
    "11-0": "customerAddress  \n`optional`",
    "11-1": "`string` This field contains the customer's address.It can be up to 100 characters. Anything after the first 100 characters will be ignored",
    "11-2": "Payu, Bestech Business Tower, Gurgaon",
    "12-0": "udf3 - udf5  \n`optional`",
    "12-1": "`string` This field must contain the user-defined fields such as udf3, udf4 and udf5 can be sent in request to include any transactional information.",
    "12-2": "-",
    "13-0": "qrType  \n`optional`",
    "13-1": "`string` This field is used to indicate whether BQR or UPI QR need to be generated and can contain any of the following values:  \n  \nbqr  \nupi",
    "13-2": "upi or bqr",
    "14-0": "outputType  \n`optional`",
    "14-1": "`string` This field is used to indicate the QR output format and contain any of the following:  \n  \nbase64  \nstring  \nimage format",
    "14-2": "base64, string, image",
    "15-0": "gst  \n`optional`",
    "15-1": "`string` This must contain the applicable GST amount for that transaction. Only applicable in case you want to embed gst specific details in the QR.",
    "15-2": "100.25",
    "16-0": "cgst  \n`optional`",
    "16-1": "`string` This is the applicable CFST amount for that transaction. Only applicable in case you want to embed GST specific details.",
    "16-2": "25.45",
    "17-0": "sgst  \n`optional`",
    "17-1": "`string` This must contain the SGST amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.",
    "17-2": "25.45",
    "18-0": "igst  \n`optional`",
    "18-1": "`string` This must contain the IGST amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.",
    "18-2": "50.9",
    "19-0": "cess  \n`optional`",
    "19-1": "`string` This must contain the cess amount for that transaction. Only applicable in case you want to embed gst specific details in the QR.",
    "19-2": "10.2",
    "20-0": "gstIncentive  \n`optional`",
    "20-1": "`string` This must contain the GST Incentive amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.",
    "20-2": "10.2",
    "21-0": "gstPercentage  \n`optional`",
    "21-1": "`string` This must contain the GST percentage for that transaction. Only applicable in case you want to embed GST specific details in the QR.",
    "21-2": "18",
    "22-0": "gstIn  \n`optional`",
    "22-1": "`string` This is the GSTIN of the legal entity of the merchant. Only applicable in case you want to embed GST specific details in the QR.",
    "22-2": "24AAACC1206D1ZM",
    "23-0": "invoiceName  \n`optional`",
    "23-1": "`string` This is the name of the invoice for which QR will be used. Only applicable in case you want to embed GST specific details in the QR.",
    "23-2": "Bill",
    "24-0": "invoiceNo  \n`optional`",
    "24-1": "`string` This is the invoice number for which QR will be used. Only applicable in case you want to embed GST specific details in the QR.",
    "24-2": "78457637",
    "25-0": "invoiceDate  \n`optional`",
    "25-1": "`string` This is the invoice date for which QR will be used. It should always be in GMT format. Only applicable in case you want to embed GST specific details in the QR.",
    "25-2": "2021-05-21T13:21:50+05:30",
    "26-0": "purpose  \n`optional`",
    "26-1": "`string` This is the purpose for which QR will be used. This param will have fixed values basis your business type. Please take the value from our integration team.",
    "26-2": "3",
    "27-0": "refUrl  \n`optional`",
    "27-1": "string This field can be used to share invoice copy or any other transaction related information/documents to customer for their reference.",
    "27-2": "<https://payu.in/>",
    "28-0": "category  \n`optional`",
    "28-1": "string This field is mandatory when refUrl is passed. Use any of the following based on the purpose:  \n  \n01 for advertisement  \n02 for invoice.",
    "28-2": "01 or 02",
    "29-0": "txnNote  \n`optional`",
    "29-1": "`string` This field is used if any transaction remarks should be shown to customer.",
    "29-2": "Loan Repayment"
  },
  "cols": 3,
  "rows": 30,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### var1 sample

The var1 parameter is similar to the following JSON format and description of fields in the JSON is described in the following table:

```Text JSON
{
  "transactionId": "delhivery_1",
  "transactionAmount": "1",
  "merchantVpa": "yellowqr.payutestdynamicqr@hdfcbank",
  "expiryTime": "3600",
  "qrName": "ronaldo",
  "qrCity": "gurugram",
  "qrPinCode": "122001",
  "customerName": "Messi",
  "customerCity": "hyderabad",
  "customerPinCode": "500072",
  "customerPhoneNumber": "7060334501",
  "customerEmail": "messi10@gmail.com",
  "customerAddress": "bestech business tower, sohna road, sector 48, gurgaon,122001",
  "gst": "110",
  "cgst": "25",
  "sgst": "25",
  "igst": "50",
  "cess": "10",
  "gstIncentive": "10",
  "gstPercentage": "18",
  "gstIn": "24AAACC1206D1ZM",
  "invoiceName": "Javed H",
  "invoiceNo": "78457637",
  "invoiceDate": "2021-05 21T13:21:50+05:30",
  "purpose": "03",
  "refUrl": "https://payu.in/",
  "category": "02",
  "txnNote": "Loan Payment"
}
```

## Sample request

```Text cURL
curl --location --request POST 'https://info.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'command=generate_invoice_qr' \
--data-urlencode 'key =J****g' \
--data-urlencode 'hash =c0110b439987304598edc8871e4b134262dbbd6b3b64532fa2731d50aadf03c5dec0958de560a2011b35f01a719ab8ca246bfd6dcfa6ecf4b4100b07e0635322' \
--data-urlencode 'var1 ={"transactionId":"DBQR000479","transactionAmount":"1","outputType":"string","qrType":"upi"}'
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "OutputType",
    "h-1": "Description",
    "0-0": "image",
    "0-1": "Image of the QR code will be returned, either BQR or UPI QR  \nstring",
    "1-0": "string",
    "1-1": "Qr String is plain text will be returned in response along with QR ID & VPA associated to the QR, the QR string can be converted into image and used for accepting transactions",
    "2-0": "base64",
    "2-1": "Base 64 encoded string will be returned in response along with QR ID & VPA associated to the QR, the encoded string provides a layer of security which can be eventually converted into image and used for accepting transactions"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


### Sample response

- UPI

```Text JSON
{
  "qrString": "upi://pay?pa=gauravdua1.payu@indus&pn=J****g&mc=7399&tr=P-424951&ver=01&mode=15&orgid=000000&qrMedium=06&cu=INR&purpose=02&pinCode=122002&am=1.00&QRexpire=2021-08-25T21:58:08+05:30",
  "msg": null
}
```

- BQR

```Text JSON
{
  "qrString": "000201010211021644038470007469080415522024070007469061661000307000746960825HDFC00006225020001855322626470010A0000005240129yellowqr.payutest.94@hdfcbank27370010A0000005240119STQ9y45z1cv3z5450925204569153033565802IN5910vendorName6010vendorCity610650017262350519STQ9y45z1cv3z545092070870007469630417EF",
  "msg": null
}
```