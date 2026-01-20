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

The **Print Invoice QR** API generate UPI or BQR QR. This API returns either Base64, string or image format of the QR based on the request type.

#### Environment

| Environment | URI                                                                                            |
| :---------- | :--------------------------------------------------------------------------------------------- |
| Production  | [https://info.payu.in/merchant/postservice.php](https://info.payu.in/merchant/postservice.php) |

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
        Sample Value
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
        `mandatory`
      </td>

      <td>
        string This parameter must include the merchant key that was provided by PayU.  
        Reference: For more information on how to generate the Key and Salt, refer to any of the following:

        * *Production**: Generate Production Merchant Key and Sat.
        * *Test**: Generate Test Merchant Key and Salt.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        command  
        `mandatory`
      </td>

      <td>
        `string` The parameter must contain the name of the web service. For this API, generate_invoice_qr must be posted.
      </td>

      <td>
        generate_invoice_qr
      </td>
    </tr>

    <tr>
      <td>
        hash  
        `mandatory`
      </td>

      <td>
        `string` This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:

        sha512(key|command|var1|salt)

        sha512 is the encryption method used here.
      </td>

      <td>
        ajh84babvav
      </td>
    </tr>

    <tr>
      <td>
        var1  
        `mandatory`
      </td>

      <td>
        `json` This parameter will include a JSON format of the transaction details. For more information, refer to the [Fields in var1 Parameter Description](#fields-in-var1-parameter-description)  section .
      </td>

      <td>
        Refer the [Fields in var1 Parameter Description](#fields-in-var1-parameter-description) section.
      </td>
    </tr>
  </tbody>
</Table>

### Fields in var1 Parameter Description

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
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
        transactionId
        `mandatory`
      </td>

      <td>
        `string` This must contain the merchant transaction Identifier. This must be unique (after a successful transaction) & alphanumeric special (less than 40 characters & excluding >,\<, &, ‘)
      </td>

      <td>
        1234_abcdedf
      </td>
    </tr>

    <tr>
      <td>
        transactionAmount  
        `mandatory`
      </td>

      <td>
        `float` This must contain the amount for which QR needs to be generated. This must be greater than or equal to 1.00.
      </td>

      <td>
        1005, 1042.23, 95494.4, 10000.00
      </td>
    </tr>

    <tr>
      <td>
        merchantVpa  
        `optional`
      </td>

      <td>
        `string` This must contain the merchant's VPA in which payment will be collected. If not sent, VPA registered against given merchant Key is used.
      </td>

      <td>
        yellowqr. payu@hdfc
      </td>
    </tr>

    <tr>
      <td>
        expiryTime  
        `optional`
      </td>

      <td>
        `numeric` This must contain the  time in seconds for which the QR is active. If empty, merchant level expiry is used. If there is no merchant level value, the global value is used.
      </td>

      <td>
        3600
      </td>
    </tr>

    <tr>
      <td>
        qrName  
        merchantVpa  
        `optional`
      </td>

      <td>
        `string` This field is used to post the merchant's name to be embedded in the QR. If the value is not posted, the merchant’s name registered during the onboarding process will be used.
      </td>

      <td>
        PayU
      </td>
    </tr>

    <tr>
      <td>
        qrCity  
        merchantVpa  
        `optional`
      </td>

      <td>
        `string` This parameter is used to post the merchant's city that will be embedded in the QR. If the value not posted, merchant’s city registered during the onboarding process will be used.
      </td>

      <td>
        Gurgaon
      </td>
    </tr>

    <tr>
      <td>
        qrPinCode  
        `optional`
      </td>

      <td>
        `string` This field is used to post the merchant's PIN code to be embedded in the QR. If not sent, merchant’s PIN code registered during the onboarding process will be used.
      </td>

      <td>
        122001
      </td>
    </tr>

    <tr>
      <td>
        customerName  
        `optional`
      </td>

      <td>
        `string` This field must contain the customer name.
      </td>

      <td>
        Ravi
      </td>
    </tr>

    <tr>
      <td>
        customerCity  
        `optional`
      </td>

      <td>
        `string` This field must contain the customer city.
      </td>

      <td>
        122001
      </td>
    </tr>

    <tr>
      <td>
        customerPhone  
        `optional`
      </td>

      <td>
        `string` This field must contain the customer phone number.
      </td>

      <td>
        9833207164
      </td>
    </tr>

    <tr>
      <td>
        customerEmail  
        `optional`
      </td>

      <td>
        `string` This field must contain the customer email address.
      </td>

      <td>
        [hello@payu.in](mailto:hello@payu.in)
      </td>
    </tr>

    <tr>
      <td>
        customerAddress  
        `optional`
      </td>

      <td>
        `string` This field contains the customer's address.It can be up to 100 characters. Anything after the first 100 characters will be ignored
      </td>

      <td>
        Payu, Bestech Business Tower, Gurgaon
      </td>
    </tr>

    <tr>
      <td>
        udf3 - udf5  
        `optional`
      </td>

      <td>
        `string` This field must contain the user-defined fields such as udf3, udf4 and udf5 can be sent in request to include any transactional information.
      </td>

      <td>
        * <br />
      </td>
    </tr>

    <tr>
      <td>
        qrType  
        `optional`
      </td>

      <td>
        `string` This field is used to indicate whether BQR or UPI QR need to be generated and can contain any of the following values:

        bqr  
        upi
      </td>

      <td>
        upi or bqr
      </td>
    </tr>

    <tr>
      <td>
        outputType  
        `optional`
      </td>

      <td>
        `string` This field is used to indicate the QR output format and contain any of the following:

        base64  
        string  
        image format
      </td>

      <td>
        base64, string, image
      </td>
    </tr>

    <tr>
      <td>
        gst  
        `optional`
      </td>

      <td>
        `string` This must contain the applicable GST amount for that transaction. Only applicable in case you want to embed gst specific details in the QR.
      </td>

      <td>
        100.25
      </td>
    </tr>

    <tr>
      <td>
        cgst  
        `optional`
      </td>

      <td>
        `string` This is the applicable CFST amount for that transaction. Only applicable in case you want to embed GST specific details.
      </td>

      <td>
        25.45
      </td>
    </tr>

    <tr>
      <td>
        sgst  
        `optional`
      </td>

      <td>
        `string` This must contain the SGST amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        25.45
      </td>
    </tr>

    <tr>
      <td>
        igst  
        `optional`
      </td>

      <td>
        `string` This must contain the IGST amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        50.9
      </td>
    </tr>

    <tr>
      <td>
        cess  
        `optional`
      </td>

      <td>
        `string` This must contain the cess amount for that transaction. Only applicable in case you want to embed gst specific details in the QR.
      </td>

      <td>
        10.2
      </td>
    </tr>

    <tr>
      <td>
        gstIncentive  
        `optional`
      </td>

      <td>
        `string` This must contain the GST Incentive amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        10.2
      </td>
    </tr>

    <tr>
      <td>
        gstPercentage  
        `optional`
      </td>

      <td>
        `string` This must contain the GST percentage for that transaction. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        18
      </td>
    </tr>

    <tr>
      <td>
        gstIn  
        `optional`
      </td>

      <td>
        `string` This is the GSTIN of the legal entity of the merchant. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        24AAACC1206D1ZM
      </td>
    </tr>

    <tr>
      <td>
        invoiceName  
        `optional`
      </td>

      <td>
        `string` This is the name of the invoice for which QR will be used. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        Bill
      </td>
    </tr>

    <tr>
      <td>
        invoiceNo  
        `optional`
      </td>

      <td>
        `string` This is the invoice number for which QR will be used. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        78457637
      </td>
    </tr>

    <tr>
      <td>
        invoiceDate  
        `optional`
      </td>

      <td>
        `string` This is the invoice date for which QR will be used. It should always be in GMT format. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        2021-05-21T13:21:50+05:30
      </td>
    </tr>

    <tr>
      <td>
        purpose  
        `optional`
      </td>

      <td>
        `string` This is the purpose for which QR will be used. This param will have fixed values basis your business type. Please take the value from our integration team.
      </td>

      <td>
        3
      </td>
    </tr>

    <tr>
      <td>
        refUrl  
        `optional`
      </td>

      <td>
        string This field can be used to share invoice copy or any other transaction related information/documents to customer for their reference.
      </td>

      <td>
        [https://payu.in/](https://payu.in/)
      </td>
    </tr>

    <tr>
      <td>
        category  
        `optional`
      </td>

      <td>
        string This field is mandatory when refUrl is passed. Use any of the following based on the purpose:

        01 for advertisement  
        02 for invoice.
      </td>

      <td>
        01 or 02
      </td>
    </tr>

    <tr>
      <td>
        txnNote  
        `optional`
      </td>

      <td>
        `string` This field is used if any transaction remarks should be shown to customer.
      </td>

      <td>
        Loan Repayment
      </td>
    </tr>
  </tbody>
</Table>

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

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        OutputType
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        image
      </td>

      <td>
        Image of the QR code will be returned, either BQR or UPI QR  
        string
      </td>
    </tr>

    <tr>
      <td>
        string
      </td>

      <td>
        Qr String is plain text will be returned in response along with QR ID & VPA associated to the QR, the QR string can be converted into image and used for accepting transactions
      </td>
    </tr>

    <tr>
      <td>
        base64
      </td>

      <td>
        Base 64 encoded string will be returned in response along with QR ID & VPA associated to the QR, the encoded string provides a layer of security which can be eventually converted into image and used for accepting transactions
      </td>
    </tr>
  </tbody>
</Table>

### Sample response

* UPI

```Text JSON
{
  "qrString": "upi://pay?pa=gauravdua1.payu@indus&pn=J****g&mc=7399&tr=P-424951&ver=01&mode=15&orgid=000000&qrMedium=06&cu=INR&purpose=02&pinCode=122002&am=1.00&QRexpire=2021-08-25T21:58:08+05:30",
  "msg": null
}
```

* BQR

```Text JSON
{
  "qrString": "000201010211021644038470007469080415522024070007469061661000307000746960825HDFC00006225020001855322626470010A0000005240129yellowqr.payutest.94@hdfcbank27370010A0000005240119STQ9y45z1cv3z5450925204569153033565802IN5910vendorName6010vendorCity610650017262350519STQ9y45z1cv3z545092070870007469630417EF",
  "msg": null
}
```
