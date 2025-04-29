---
title: Capture a Pre-Authorized API
excerpt: ''
api:
  file: emi-apis-6.json
  operationId: CapturePreAuth
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
To capture a pre-authorized payment, use the following command. After the API command is successful, the transaction would be captured and settled to you.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

<details>
  <summary>Sample request</summary>

### Cards

```curl
curl --location --request POST 'https://info.payu.in/merchant/postservice.php?form=2' \ 
--header 'Content-Type: application/x-www-form-urlencoded' \ 
--form 'key="JF***g"' \ 
--form 'command="capture_transaction"' \ 
--form 'hash="67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019"' \ 
--form 'var1="15246574846"' \ 
--form 'var2="authorizeTransaction123"' \ 
--form 'var3="1"' 
```

### UPI

```curl
curl --location --request POST 'https://info.payu.in/merchant/postservice.php?form=2' \   
 --header 'Content-Type: application/x-www-form-urlencoded' \   
 --form 'key="JF***g"' \   
 --form 'command="capture_transaction"' \   
 --form 'hash="67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019"' \   
 --form 'var1="15246574846"' \   
 --form 'var2="authorizeTransaction123"' \   
 --form 'var3="1"'  
```

</details>

<details>
  <summary>Sample response</summary>

### Cards

```plaintext
{ 
    "status": 1, 
    "msg": "Capture Request Queued", 
    "request_id": "Request ID", 
    "bank_ref_num": "Bank Reference Number" 
} 
```

### UPI

```
{
    "msg": "Transaction Processed successfully",
    "status": 1,
    "result": {
        "payuid": 613345678912399031,
        "txnId": "upiAuthCapture_12",
        "amount": 10000.00,
        "merchantId": 3,
        "authpayuid": "3975",
        "status": "in progress",
        "mode": "UPIOTM",
        "bankRefNumber": "410700457030",
        "payerVpa": "surya@icici",
        "field5": "3159219e58ed45eda39e8914b998401a@icici",
        "field9": "0|Transaction Successful"
    }
}
```

</details>

<details>
  <summary>Response parameters</summary>

<Table>
  <thead>
    <tr>
      <th>**Parameter**</th>
      <th>**Description**</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>status</td>
      <td>This parameter returns the status of web service call. The status can be any of the following:</td>
    </tr>
    <tr>
      <td></td>
      <td>* 0 - If web service call failed</td>
    </tr>
    <tr>
      <td></td>
      <td>* 1 - If web service call succeeded</td>
    </tr>
    <tr>
      <td>msg</td>
      <td>This parameter returns the following message if the pre-auth transaction was successful: Capture Request Queued</td>
    </tr>
    <tr>
      <td>request_id</td>
      <td>This parameter returns the request ID for the transaction.</td>
    </tr>
    <tr>
      <td>bank_ref_num</td>
      <td>This parameter returns the bank reference number for the transaction.</td>
    </tr>
  </tbody>
</Table>

</details>

## Request parameters

<KeyHashForGeneralParametersDescription />