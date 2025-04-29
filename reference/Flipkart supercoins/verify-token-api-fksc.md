---
title: Verify Token API - FKSC
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Verify Token** API is used to verify the OTP entered by the customer to get the token as a response.

> 📘 Note:
>
> The token received in the response can be used only for getting the reward balance.

#### Endpoints

<table style={{ border: "0.1rem solid rgb(242, 242, 242)" }}>
  <tbody>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>
        <strong>Test Environment</strong>
      </td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>
        https://test.payu.in/
      </td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>
        <strong>Production Environment</strong>
      </td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>
        &lt;TBD&gt;
      </td>
    </tr>
  </tbody>
</table>

## **Request Header**

<Table>
  <thead>
    <tr>
      <th>**Parameter**</th>
      <th>**Description**</th>
      <th>**Example**</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        Content-Type
        **mandatory**
      </td>
      <td>
        Indicates the format in which the request is sent.
      </td>
      <td>
        application/json
      </td>
    </tr>
    <tr>
      <td>
        clientType
      </td>
      <td>
        Pass the type of client making the request and in this case, it is **loyalty**.
      </td>
      <td>
        loyalty
      </td>
    </tr>
    <tr>
      <td>
        Origin
      </td>
      <td>
        Pass the origin URL (the domain) from which the request is being made.
      </td>
      <td>
        [https://staging-rewards-api.payu.in](https://staging-rewards-api.payu.in)
      </td>
    </tr>
    <tr>
      <td>
        Referer
      </td>
      <td>
        Pass the URL that the client was on when the request was done.
      </td>
      <td>
        [https://staging-rewards-api.payu.in/](https://staging-rewards-api.payu.in/)
      </td>
    </tr>
  </tbody>
</Table>

## **Request Parameters**

<Table>
  <thead>
    <tr>
      <th>**Parameter**</th>
      <th>**Description**</th>
      <th>**Example**</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        mobileNumber
        **mandatory**
      </td>
      <td>
        The customer's mobile number for whom the reward balance must be fetched.
      </td>
      <td>
        8076499393
      </td>
    </tr>
    <tr>
      <td>
        otp
        **mandatory**
      </td>
      <td>
        The OTP received by the customer on their mobile.
      </td>
      <td>
        518730
      </td>
    </tr>
    <tr>
      <td>
        merchantTxnId
        **mandatory**
      </td>
      <td>
        The merchant must pass the transaction ID.
      </td>
      <td>
        CL001
      </td>
    </tr>
    <tr>
      <td>
        transactionFlow
        **mandatory**
      </td>
      <td>
        This parameter must be set with the value as "SEAMLESS."
      </td>
      <td>
        SEAMLESS
      </td>
    </tr>
    <tr>
      <td>
        parentPayuTxnId
        **optional**
      </td>
      <td>
        The PayU transaction ID of the transaction.
      </td>
      <td>
        999000000017497
      </td>
    </tr>
    <tr>
      <td>
        uuid
        **mandatory**
      </td>
      <td>
        The UUID (Universally unique identifier) of the customer.
      </td>
      <td>
        1894095170321102220
      </td>
    </tr>
    <tr>
      <td>
        loyaltyProvider
        **mandatory**
      </td>
      <td>
        The loyalty provider name is specified in this parameter. For FKSC, it is SUPERCOIN.
      </td>
      <td>
        SUPERCOIN
      </td>
    </tr>
  </tbody>
</Table>

## Sample Request

```curl
curl -X 'POST' \  
'https://ltest.payu.in/otp/v1?action=verify' \  
-H 'accept: application/json' \  
-H 'Content-Type: application/json' \  
-d '{  "otp": "123123",  "uuid": 123456789,  "merchantTxnId": "123merchantTxnId",  "mobileNumber": "9999999999",  "loyaltyProvider": "SUPERCOIN",  "transactionFlow": "SEAMLESS"}'
```

## Sample Response

```plaintext
{    "token": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI4MDc2NDk5MzkzIiwibW9iaWxlTnVtYmVyIjoiODA3NjQ5OTM5MyIsImV4cCI6MTY4NjQ2NDkyNywiaWF0IjoxNjc4Njg4OTI3fQ.xIpRniWLFa0suN8Cb2ndzX4JVFfXHELCi2bdVSMTdlE"}
```