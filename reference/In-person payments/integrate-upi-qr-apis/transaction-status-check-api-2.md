---
title: Transaction Status Check API
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
The **Transaction Status Check** API is used to check the status of the transaction based on the status of the transaction in PayU system further course of action is determined. If the transaction status is pending in PayU then we hit bank API to get the transaction’s status. Based on the bank response, we mark transaction success, fail, or pending in our system and provide a response.

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
        `string` This parameter must include the Merchant key that was provided by PayU.  
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
        `string` The parameter must contain the name of the web service.
      </td>

      <td>
        check_bqr_txn_status
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
        var1: transactionId  
        `mandatory`
      </td>

      <td>
        `string` (alphanumeric) This parameter will include the transaction Identifier of the transaction for which the status is being checked.
      </td>

      <td>
        1234abcd
      </td>
    </tr>

    <tr>
      <td>
        var2: paymentmode  
        `optional`
      </td>

      <td>
        `string` This parameter will include any of the following values to specify the mode of transaction:

        CARD: Debit/Credit Card

        UPI: UPI
      </td>

      <td>
        CARD
      </td>
    </tr>

    <tr>
      <td>
        var3: productype  
        `optional`
      </td>

      <td>
        `string` This parameter will include any of the following values to specify the product type:  
        ‘’ or ‘’.

        DBQR: DBQR  
        ISBQR: ISBQR
      </td>

      <td>
        DBQR
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```Text cURL
curl --location --request POST 'https://info.payu.in/merchant/postservice.php' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=vDy3i7' \
--data-urlencode 'command=check_bqr_txn_status' \
--data-urlencode 'hash=8bb33d0ed43485019eab261cc5f73838149e3bbc1d253e63ca829ff05975c173ec9f308bafe022605aa7fce31821ea3b18df3752accd8a7f50658a96552a0860' \
--data-urlencode 'var1=980' \
--data-urlencode 'var2=UPI' \
--data-urlencode 'var3=Optional'
```
```Text Python
import http.client

conn = http.client.HTTPSConnection("info.payu.in")
payload = 'key=vDy3i7&command=check_bqr_txn_status&hash=8bb33d0ed43485019eab261cc5f73838149e3bbc1d253e63ca829ff05975c173ec9f308bafe022605aa7fce31821ea3b18df3752accd8a7f50658a96552a0860&var1=980&var2=UPI&var3=Optional'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
conn.request("POST", "/merchant/postservice.php", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```Text php
curl --location --request POST 'https://info.payu.in/merchant/postservice.php' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=vDy3i7' \
--data-urlencode 'command=check_bqr_txn_status' \
--data-urlencode 'hash=8bb33d0ed43485019eab261cc5f73838149e3bbc1d253e63ca829ff05975c173ec9f308bafe022605aa7fce31821ea3b18df3752accd8a7f50658a96552a0860' \
--data-urlencode 'var1=980' \
--data-urlencode 'var2=UPI' \
--data-urlencode 'var3=Optional'
```
```Text Java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "key=vDy3i7&command=check_bqr_txn_status&hash=8bb33d0ed43485019eab261cc5f73838149e3bbc1d253e63ca829ff05975c173ec9f308bafe022605aa7fce31821ea3b18df3752accd8a7f50658a96552a0860&var1=980&var2=UPI&var3=Optional");
Request request = new Request.Builder()
  .url("https://info.payu.in/merchant/postservice.php")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .build();
Response response = client.newCall(request).execute();
```

## Response parmeters

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
        result
      </td>
    </tr>

    <tr>
      <td>
        result
      </td>

      <td>
        Encoded transaction and status details.
      </td>
    </tr>
  </tbody>
</Table>

## Sample response

* **Success**

```Text JSON
{
  "status": 1,
  "msg": "Transaction has been already\nCompleted.",
  "result": "eyJtaWhwYXlpZCI6NDAzOTkzNzE1NTExODQxNjcwLCJtb2RlIjoiREJRUiIsInN0YXR1cyI6InN1Y2Nlc3MiLCJrZXkiOiJ2RHkzaTciLCJ0eG5pZCI6Ijk4MCIsImFtb3VudCI6IjEuMDAiLCJhZGRlZG9uIjoiMjAxOS0wNS0yMyAxODoyMzozMiIsInByb2R1Y3RpbmZvIjoiT2ZmbGluZSBEeW5hbWljIFFSIiwiZmlyc3RuYW1lIjoicm9uYWxkbyIsImxhc3RuYW1lIjoiIiwiYWRkcmVzczEiOiJiZXN0ZWNoIGJ1c2luZXNzIHRvd2VyICBzb2huYSByb2FkICBzZWN0b3IgNDggIGd1cmdhb24gMTIyMDAxIiwiYWRkcmVzczIiOiIiLCJjaXR5IjoiaHlkZXJhYmFkIiwic3RhdGUiOiIiLCJjb3VudHJ5IjoiIiwiemlwY29kZSI6IjUwMDA3MiIsImVtYWlsIjoibW52c2s5N0BnbWFpbC5jb20iLCJwaG9uZSI6IjcwNjAzMzQ1MDEiLCJ1ZGYxIjoiMTgwIiwidWRmMiI6IiIsInVkZjMiOiIiLCJ1ZGY0IjoiIiwidWRmNSI6IiIsInVkZjYiOiIiLCJ1ZGY3IjoiIiwidWRmOCI6IiIsInVkZjkiOiIiLCJ1ZGYxMCI6IiIsImNhcmRfdG9rZW4iOiIiLCJjYXJkX25vIjoiIiwiZmllbGQwIjoiRFlROTgwMTM2MjI3NiIsImZpZWxkMSI6IiIsImZpZWxkMiI6IjUyOTgzNzQ2NDAiLCJmaWVsZDMiOiI3ODI3MDU3NjA0QHlibCIsImZpZWxkNCI6IiIsImZpZWxkNSI6InllbGxvd3FyLnBheXV0ZXN0ZHluYW1pY3FyQGhkZmNiYW5rIXBheXV0ZXN0ZHluYW1pY3FyIU5BIiwiZmllbGQ2IjoiS290YWsgTWFoaW5kcmEgQmFuayE5MTEyMTI0MTg1IUtLQkswMDAwMjU1ITkxNzgyNzA1NzYwNCIsImZpZWxkNyI6IlRyYW5zYWN0aW9uIHN1Y2Nlc3MiLCJmaWVsZDgiOiIiLCJmaWVsZDkiOiJTVUNDRVNTfENvbXBsZXRlZCBVc2luZyBDYWxsYmFjayIsInBheW1lbnRfc291cmNlIjoicGF5dSIsIlBHX1RZUEUiOiJCUVIiLCJlcnJvciI6IkUwMDAiLCJlcnJvcl9NZXNzYWdlIjoiTm8gRXJyb3IiLCJuZXRfYW1vdW50X2RlYml0IjoxLCJ1bm1hcHBlZHN0YXR1cyI6ImNhcHR1cmVkIiwiaGFzaCI6ImQzMGQ0MzY2MWFkYjQ0NGMxNDgyYzkzODMwZTA5OGJmZTY1ZTVjZjgzOWEwMWRiMTlhZDU2MzYxZjM5M2FkZDdhODUyNTZlNDM4M2E2MDZjY2M4MTM0OTZkZTAwN2M1N2QyZGNkYTlkMjI5ZTBlNTk4MjE1MDkwNDdmZTJhNjM2IiwiYmFua19yZWZfbm8iOiI5MTM3Mzk5NTMyMTYiLCJiYW5rX3JlZl9udW0iOiI5MTM3Mzk5NTMyMTYiLCJiYW5rY29kZSI6IlVQSUJRUiIsInN1cmwiOiJodHRwOlwvXC8xMC41MC4yMy4zNSIsImN1cmwiOiJodHRwOlwvXC8xMC41MC4yMy4zNSIsImZ1cmwiOiJodHRwOlwvXC8xMC41MC4yMy4zNSJ9"
}
```

* **Pending**

```Text JSON
{
  "status": 1,
  "msg": "Transaction is Pending",
  "result": "eyJtaWhwYXlpZCI6NDAzOTkzNzE1NTExODQxNjcwLCJtb2RlIjoiREJRUiIsInN0YXR1cyI6InBlbmRpbmciLCJrZXkiOiJ2RHkzaTciLCJ0eG5pZCI6Ijk4MCIsImFtb3VudCI6IjEuMDAiLCJhZGRlZG9uIjoiMjAxOS0wNS0yMyAxODoyMzozMiIsInByb2R1Y3RpbmZvIjoiT2ZmbGluZSBEeW5hbWljIFFSIiwiZmlyc3RuYW1lIjoicm9uYWxkbyIsImxhc3RuYW1lIjoiIiwiYWRkcmVzczEiOiJiZXN0ZWNoIGJ1c2luZXNzIHRvd2VyICBzb2huYSByb2FkICBzZWN0b3IgNDggIGd1cmdhb24gMTIyMDAxIiwiYWRkcmVzczIiOiIiLCJjaXR5IjoiaHlkZXJhYmFkIiwic3RhdGUiOiIiLCJjb3VudHJ5IjoiIiwiemlwY29kZSI6IjUwMDA3MiIsImVtYWlsIjoibW52c2s5N0BnbWFpbC5jb20iLCJwaG9uZSI6IjcwNjAzMzQ1MDEiLCJ1ZGYxIjoiMTgwIiwidWRmMiI6IiIsInVkZjMiOiIiLCJ1ZGY0IjoiIiwidWRmNSI6IiIsInVkZjYiOiIiLCJ1ZGY3IjoiIiwidWRmOCI6IiIsInVkZjkiOiIiLCJ1ZGYxMCI6IiIsImNhcmRfdG9rZW4iOiIiLCJjYXJkX25vIjoiIiwiZmllbGQwIjoiRFlROTgwMTM2MjI3NiIsImZpZWxkMSI6IiIsImZpZWxkMiI6IjUyOTgzNzQ2NDAiLCJmaWVsZDMiOiI3ODI3MDU3NjA0QHlibCIsImZpZWxkNCI6IiIsImZpZWxkNSI6InllbGxvd3FyLnBheXV0ZXN0ZHluYW1pY3FyQGhkZmNiYW5rIXBheXV0ZXN0ZHluYW1pY3FyIU5BIiwiZmllbGQ2IjoiS290YWsgTWFoaW5kcmEgQmFuayE5MTEyMTI0MTg1IUtLQkswMDAwMjU1ITkxNzgyNzA1NzYwNCIsImZpZWxkNyI6IlRyYW5zYWN0aW9uIHN1Y2Nlc3MiLCJmaWVsZDgiOiIiLCJmaWVsZDkiOiJBbW91bnQgb3IgdHJhbnNhY3Rpb24gZG9lc250IG1hdGNofENvbXBsZXRlZCBVc2luZyBDYWxsYmFjayIsInBheW1lbnRfc291cmNlIjoicGF5dSIsIlBHX1RZUEUiOiJCUVIiLCJlcnJvciI6IkUyMjAiLCJlcnJvcl9NZXNzYWdlIjoiQW1vdW50IG9yIHRyYW5zYWN0aW9uIGRvZXNudCBtYXRjaCIsIm5ldF9hbW91bnRfZGViaXQiOjAsInVubWFwcGVkc3RhdHVzIjoiaW4gcHJvZ3Jlc3MiLCJoYXNoIjoiY2YyMjUwNTNhYWZkMDJiYjE0ZWVlMTFhZTQxMWM4NTgzODQyMzdmMjg4MjE4MzE0ZDkzM2UyNzVkOWM3ODUzMDA0M2FjMjFjMTQ0MTU0N2VmYzdkYWM3NjM1N2ZkYzI5NWFkYjA3YWMxZWE2Yzk2YTk1ZDFiNmQ5OWYxNWM3MDQiLCJiYW5rX3JlZl9ubyI6IjkxMzczOTk1MzIxNiIsImJhbmtfcmVmX251bSI6IjkxMzczOTk1MzIxNiIsImJhbmtjb2RlIjoiVVBJQlFSIiwic3VybCI6Imh0dHA6XC9cLzEwLjUwLjIzLjM1IiwiY3VybCI6Imh0dHA6XC9cLzEwLjUwLjIzLjM1IiwiZnVybCI6Imh0dHA6XC9cLzEwLjUwLjIzLjM1In0="
}
```

* **Failed at backend**

```Text JSON
{
  "status": 1,
  "msg": "Transaction is Failed",
  "result": "eyJtaWhwYXlpZCI6NDAzOTkzNzE1NTExODQxNjcwLCJtb2RlIjoiREJRUiIsInN0YXR1cyI6ImZhaWx1cmUiLCJrZXkiOiJ2RHkzaTciLCJ0eG5pZCI6Ijk4MCIsImFtb3VudCI6IjEwLjAwIiwiYWRkZWRvbiI6IjIwMTktMDUtMjMgMTg6MjM6MzIiLCJwcm9kdWN0aW5mbyI6Ik9mZmxpbmUgRHluYW1pYyBRUiIsImZpcnN0bmFtZSI6InJvbmFsZG8iLCJsYXN0bmFtZSI6IiIsImFkZHJlc3MxIjoiYmVzdGVjaCBidXNpbmVzcyB0b3dlciAgc29obmEgcm9hZCAgc2VjdG9yIDQ4ICBndXJnYW9uIDEyMjAwMSIsImFkZHJlc3MyIjoiIiwiY2l0eSI6Imh5ZGVyYWJhZCIsInN0YXRlIjoiIiwiY291bnRyeSI6IiIsInppcGNvZGUiOiI1MDAwNzIiLCJlbWFpbCI6Im1udnNrOTdAZ21haWwuY29tIiwicGhvbmUiOiI3MDYwMzM0NTAxIiwidWRmMSI6IjE4MCIsInVkZjIiOiIiLCJ1ZGYzIjoiIiwidWRmNCI6IiIsInVkZjUiOiIiLCJ1ZGY2IjoiIiwidWRmNyI6IiIsInVkZjgiOiIiLCJ1ZGY5IjoiIiwidWRmMTAiOiIiLCJjYXJkX3Rva2VuIjoiIiwiY2FyZF9ubyI6IiIsImZpZWxkMCI6IkRZUTk4MDEzNjIyNzYiLCJmaWVsZDEiOiIiLCJmaWVsZDIiOiI1Mjk4Mzc0NjQwIiwiZmllbGQzIjoiNzgyNzA1NzYwNEB5YmwiLCJmaWVsZDQiOiIiLCJmaWVsZDUiOiJ5ZWxsb3dxci5wYXl1dGVzdGR5bmFtaWNxckBoZGZjYmFuayFwYXl1dGVzdGR5bmFtaWNxciFOQSIsImZpZWxkNiI6IktvdGFrIE1haGluZHJhIEJhbmshOTExMjEyNDE4NSFLS0JLMDAwMDI1NSE5MTc4MjcwNTc2MDQiLCJmaWVsZDciOiJUcmFuc2FjdGlvbiBzdWNjZXNzIiwiZmllbGQ4IjoiIiwiZmllbGQ5IjoiQW1vdW50IG9yIHRyYW5zYWN0aW9uIGRvZXNudCBtYXRjaCIsInBheW1lbnRfc291cmNlIjoicGF5dSIsIlBHX1RZUEUiOiJCUVIiLCJlcnJvciI6IkUyMjAiLCJlcnJvcl9NZXNzYWdlIjoiQW1vdW50IG9yIHRyYW5zYWN0aW9uIGRvZXNudCBtYXRjaCIsIm5ldF9hbW91bnRfZGViaXQiOjAsInVubWFwcGVkc3RhdHVzIjoiZmFpbGVkIiwiaGFzaCI6ImQ0OTc5MDdmZjFlZjY5ODg2NTlkZWUzMDA2M2UyMWVlZWVhYTNlOTJlZTZiMWM0MzdmMmU2ZDhjODZhNzliZDJjYTg4Njk5ODgxOTIwOWRmNWZlMzA3YjdlMjJmNjFiNDc1ODE2ZWExYmNlN2U3ZDBjNGZkYmJhNDZjMDZlZTg0IiwiYmFua19yZWZfbm8iOiI5MTM3Mzk5NTMyMTYiLCJiYW5rX3JlZl9udW0iOiI5MTM3Mzk5NTMyMTYiLCJiYW5rY29kZSI6IlVQSUJRUiIsInN1cmwiOiJodHRwOlwvXC8xMC41MC4yMy4zNSIsImN1cmwiOiJodHRwOlwvXC8xMC41MC4yMy4zNSIsImZ1cmwiOiJodHRwOlwvXC8xMC41MC4yMy4zNSJ9"
}
```

* **Pending Status at PayU but Success at Backend**

```Text JSON
{
  "status": 1,
  "msg": "Transaction is Successful",
  "result": "eyJtaWhwYXlpZCI6NDAzOTkzNzE1NTExODQxNjcwLCJtb2RlIjoiREJRUiIsInN0YXR1cyI6InN1Y2Nlc3MiLCJrZXkiOiJ2RHkzaTciLCJ0eG5pZCI6Ijk4MCIsImFtb3VudCI6IjEuMDAiLCJhZGRlZG9uIjoiMjAxOS0wNS0yMyAxODoyMzozMiIsInByb2R1Y3RpbmZvIjoiT2ZmbGluZSBEeW5hbWljIFFSIiwiZmlyc3RuYW1lIjoicm9uYWxkbyIsImxhc3RuYW1lIjoiIiwiYWRkcmVzczEiOiJiZXN0ZWNoIGJ1c2luZXNzIHRvd2VyICBzb2huYSByb2FkICBzZWN0b3IgNDggIGd1cmdhb24gMTIyMDAxIiwiYWRkcmVzczIiOiIiLCJjaXR5IjoiaHlkZXJhYmFkIiwic3RhdGUiOiIiLCJjb3VudHJ5IjoiIiwiemlwY29kZSI6IjUwMDA3MiIsImVtYWlsIjoibW52c2s5N0BnbWFpbC5jb20iLCJwaG9uZSI6IjcwNjAzMzQ1MDEiLCJ1ZGYxIjoiMTgwIiwidWRmMiI6IiIsInVkZjMiOiIiLCJ1ZGY0IjoiIiwidWRmNSI6IiIsInVkZjYiOiIiLCJ1ZGY3IjoiIiwidWRmOCI6IiIsInVkZjkiOiIiLCJ1ZGYxMCI6IiIsImNhcmRfdG9rZW4iOiIiLCJjYXJkX25vIjoiIiwiZmllbGQwIjoiRFlROTgwMTM2MjI3NiIsImZpZWxkMSI6IiIsImZpZWxkMiI6IjUyOTgzNzQ2NDAiLCJmaWVsZDMiOiI3ODI3MDU3NjA0QHlibCIsImZpZWxkNCI6IiIsImZpZWxkNSI6InllbGxvd3FyLnBheXV0ZXN0ZHluYW1pY3FyQGhkZmNiYW5rIXBheXV0ZXN0ZHluYW1pY3FyIU5BIiwiZmllbGQ2IjoiS290YWsgTWFoaW5kcmEgQmFuayE5MTEyMTI0MTg1IUtLQkswMDAwMjU1ITkxNzgyNzA1NzYwNCIsImZpZWxkNyI6IlRyYW5zYWN0aW9uIHN1Y2Nlc3MiLCJmaWVsZDgiOiIiLCJmaWVsZDkiOiJjYXB0dXJlZCB1c2luZyBWZXJpZnkgQXBpIiwicGF5bWVudF9zb3VyY2UiOiJwYXl1IiwiUEdfVFlQRSI6IkJRUiIsImVycm9yIjoiRTAwMCIsImVycm9yX01lc3NhZ2UiOiJObyBFcnJvciIsIm5ldF9hbW91bnRfZGViaXQiOjEsInVubWFwcGVkc3RhdHVzIjoiY2FwdHVyZWQiLCJoYXNoIjoiZDMwZDQzNjYxYWRiNDQ0YzE0ODJjOTM4MzBlMDk4YmZlNjVlNWNmODM5YTAxZGIxOWFkNTYzNjFmMzkzYWRkN2E4NTI1NmU0MzgzYTYwNmNjYzgxMzQ5NmRlMDA3YzU3ZDJkY2RhOWQyMjllMGU1OTgyMTUwOTA0N2ZlMmE2MzYiLCJiYW5rX3JlZl9ubyI6IjkxMzczOTk1MzIxNiIsImJhbmtfcmVmX251bSI6IjkxMzczOTk1MzIxNiIsImJhbmtjb2RlIjoiVVBJQlFSIiwic3VybCI6Imh0dHA6XC9cLzEwLjUwLjIzLjM1IiwiY3VybCI6Imh0dHA6XC9cLzEwLjUwLjIzLjM1IiwiZnVybCI6Imh0dHA6XC9cLzEwLjUwLjIzLjM1In0="
}
```
