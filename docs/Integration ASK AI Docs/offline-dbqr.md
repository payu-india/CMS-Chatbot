---
title: 'Offline DBQR '
deprecated: false
hidden: false
metadata:
  robots: index
---
Overview

The offline Dynamic QR Generation API allows merchants to generate UPI QR Codes with pre-

filled amount for collecting payments.

API Endpoint:

Production URL:

Request Structure

Mandatory Parameters:

• key: Merchant's unique key

• txnid: Unique transaction ID

• amount: Payment amount

• productinfo: Description of the product

• firstname, email, phone: Customer's personal details

• pg: "DBQR" indicating Dynamic QR transactions

• bankcode: "UPIDBQR"

• hash: SHA-512 hash for security

• s2s\_client\_ip: Customer's IP address

• s2s\_device\_info: Device information

• txn\_s2s\_flow: Set to 4 for S2S transactions

Optional Parameters:

• expiry\_time: Duration QR is valid (default 30 minutes)

• Address and User Fields (udf1-udf5): As needed for additional transaction details.

Security: Hashing Calculation

• Formula:

sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)

A) Indus Flow (Depreciated)

Sample Request

curl --location

\--header 'Content-Type: application/x-www-form-urlencoded'

\--data-urlencode 'key=smsplus'

\--data-urlencode 'command=generate\_dynamic\_bharat\_qr'

\--data-urlencode
'hash=08854d3193ba66224c688e201b2a3376262d938c059437777a4a103ca7a9feb28e88f7cf4de 8d7aafeb2bfd6cd53ad6f23cc62f5f42451bd10d731d0a53ab69e'

\--data-urlencode
'var1={"transactionId":"dbqr098","transactionAmount":"1","outputType":"base64","qrType":"bq r"}'

Sample Response

Case : "outputType":"base64"

{

"qrString":
"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZUAAAGVAQAAAAAeIFGW AAACUklEQVR4Xu3UwYrcQAyEYYPf/31zMDhTf6nb3kAIS0DaQ/XM2t1SfX0Rs8f97fXr+ LPy7xUToxUToxUToxXzP+Y6WCfvk8r5+XwKp5vuVC+m3VTOX9K+iT3PlYgZMa9OUTF N1fWViJk1eivr3xdVtjE/wlDWOHfCY40ZNu+ns0RVW1ftREy70W/MU/3bpxIxE+ZZGqRGy A2+hec7E9NtiPBrU7f+RP0BPTam3ZAA124nGe+x5hszYw6yrmuLWl9uc4YV0288ML3Vsax6 dTeJ6TduvYTDnM11QW1i2o1+bryNhVyqzboLFNNuDIhdighR02D93bWYdiNw8lCvzrqj9rp G13GM6TeOwKpfRW00Tc3aImbAuK8mGE7Rc/SjqjEzpooXG6fZcxnvmCnjYqnb04X4uvrKx kyZVdND5qhUFVXgxph2U+l6r5BjjupQPGbCaIJ0+Y3ZauPfor/qxkyYndaWTsX4mvONmTC KKIz1VhU/9HIVEdNvXOYP/jjXyW8V022cVMVAZ5+00VKxOjH9pqIapMI7S8ZJajEzptDnQ 45eHWpf+Zgh82Q56PQ6nkIuxvQbTdNRpHuXkrX3gV1Mv5HyBJ88NS4SZVsspt1c+v/Hqn+E JEmxrQ4kpt/UWlV2xlLi65o7Rr1ec9U82eyMh+j3tScaM2A4XhohIa4hx00u60ZyMf3mYpY3M xXwifFKy7oVM2j8Jkt1tdRU3ShmzNQDxeH+Mt+YKbOlyzqx9QV64ejEtBv9rA4GSg9YcXd XK2bCfG/FxGjFxGjFxGjF/HDzG9tVoDkHEUxvAAAAAElFTkSuQmCC"

}

Case : "outputType":"String" { 
  "qrString": "upi://pay?pa=mayank@hdfcbank&pn=smsplus-
Test%20MID&mc=7399&tr=DYQ21362224903&cu=INR&am=1.00&QRexpire=2024-10-24T12:50:32+05:30" 
}

Case : "outputType":"Image"

<br />

B) ICICI Flow (Standard)
Doc:
Configuration
For ICICI flow the bank code ICICI and the txn\_s2s\_flow flag must be enabled (i.e. 1) Sample Request
curl --location ' \\
\--header 'accept: application/json' \\

\--header 'Content-Type: application/x-www-form-urlencoded' \\
\--data-urlencode 'key=smsplus' \\
\--data-urlencode 'txnid=qr\_12321111' \\
\--data-urlencode 'amount=10.00' \\
\--data-urlencode 'firstname=Navnath' \\
\--data-urlencode  \\
\--data-urlencode 'phone=8693817260' \\
\--data-urlencode 'productinfo=iPhone' \\
\--data-urlencode 'pg=DBQR' \\
\--data-urlencode 'bankcode=UPIDBQR' \\
\--data-urlencode 'surl=[https://test.payu.in/admin/test\_response](https://test.payu.in/admin/test_response)' \\
\--data-urlencode 'furl=[https://test.payu.in/admin/test\_response](https://test.payu.in/admin/test_response)' \\
\--data-urlencode
'hash=530f58deb1ba39fc6139b86fe364f65443807257b5468dd60f04337479c54dbf38087b0eead e48ed958ddb9b9d54d61f158708629fd9519a09a59b0af7beac1c' \\
\--data-urlencode 'txn\_s2s\_flow=4'

Sample Response
{
  "metaData": {<br />  "message": null,<br />  "referenceId": "d4d6e3e3a269def6439529cee2b7c43b",    "statusCode": null,<br />  "txnId": "qr\_12321111",

  "txnStatus": "pending",<br />  "unmappedStatus": "pending"<br />  },<br />  "result": {  
": "21546726668",  
ame": "smsplus-TestMID",  
pa": "testqr002.2.333@indus",  
"10.00",  
: "upi://pay?pa=testqr002.2.333@indus&pn=TEST 
726668&tid=PPPL21546726668121124181233&am=10.00&cu=INR&tn=UPI Transaction", 
k": {  
"71AF83D3-87EA-3A2C-0A4A-CF139E67387E",  
 "10.00",  
": "d4d6e3e3a269def6439529cee2b7c43b",  
": "testqr002.2.333@indus",  
e": "smsplus-TestMID",  
ionFee": "10.00"  
 <br />}

QrString To QR code :

<br />

Next Steps
1.Transaction Status Verification: Use the Verify Payment API.

2.S2S Callbacks Management: Handle server callbacks for transaction updates.
