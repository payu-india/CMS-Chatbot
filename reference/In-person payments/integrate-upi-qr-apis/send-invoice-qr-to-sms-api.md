---
title: Send Invoice QR to SMS API
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
The **Send Invoice QR to SMS** API is used to send SMS to provided phoneNumber post transaction. Whenever payment is success/fail via SDK, merchant will call this API to send the payment confirmation SMS to merchant’s executive phone number.

#### Environment

| Environments | URI                                                                                            |
| :----------- | :--------------------------------------------------------------------------------------------- |
| Production   | [https://info.payu.in/merchant/postservice.php](https://info.payu.in/merchant/postservice.php) |

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
        `string` This parameter must include the merchant key that was provided by PayU.  
        Reference: For more information on how to generate the Key and Salt, refer to any of the following:

        Production: Generate Production Merchant Key and Sat.  
        Test: Generate Test Merchant Key and Salt.
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
        `string` The parameter must contain the name of the web service. For this API, send_sdk_message must be posted.
      </td>

      <td>
        send_sdk_message
      </td>
    </tr>

    <tr>
      <td>
        hash  
        `mandatory`
      </td>

      <td>
        string This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:

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
        `string` This parameter must contain the merchant PayU ID that was provided by PayU.
      </td>

      <td>
        412345678912356095
      </td>
    </tr>

    <tr>
      <td>
        var2  
        `mandatory`
      </td>

      <td>
        string This parameter must contain the merchant phone number to which the invoice is sent as SMS.
      </td>

      <td>
        7727820112
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```Text cURL
curl --location --request POST 'https://info.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'command=send_sdk_message' \
--data-urlencode 'key=J****g' \
--data-urlencode 'hash=602a7b58b239e6bdbf762f01cada3652a25b0de0002445dbed69febb652b9c376375b1322b531116cd0a1bee37cdc8ef8a393e066b4c9a836ea4c6c45ff90460' \
--data-urlencode 'var1=13863413996' \
--data-urlencode 'var2=9833208174'
```

## Response parameters

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
        status
      </td>

      <td>
        This parameter returns the status of web service call. The status can be any of the following:

        0 - If web service call failed.  
        1 - If web service call succeeded
      </td>
    </tr>

    <tr>
      <td>
        msg
      </td>

      <td>
        This parameter returns the following message if the SMS was sent successfully:  
        sms request successful
      </td>
    </tr>
  </tbody>
</Table>

## Sample response

#### Success scenario

```Text JSON
a:2:{s:6:"status";i:1;s:3:"msg";s:18:"sms request successful";}
```

#### Failure scenario

* **SMS request failed**

```Text JSON
a:2:{s:6:"status";i:0;s:3:"msg";s:18:"sms request failed";}
```

* **Invalid phone number**

```Text JSON
a:2:{s:6:"status";i:0;s:3:"msg";s:20:"phone is not numeric";}
```

* **Invalid PayU ID**

```
a:2:{s:6:"status";i:0;s:3:"msg";s:59:"There is no success or failed transaction with given payuId";}
```
