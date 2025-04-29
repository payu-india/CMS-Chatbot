---
title: _payment Request PHP Code Walkthrough
description: >-
  This recipe provides code walkthrough of _payment request with PayU Hosted
  Integration with the PHP language binding.
hidden: false
recipe:
  color: '#018FF4'
  icon: 🦉
---
```php PHP
<?php

$url = "https://test.payu.in/_payment";

$req = req_init($url);

req_setopt($req, CURLOPT_URL, $url);
req_setopt($req, CURLOPT_POST, true); 
req_setopt($req, CURLOPT_RETURNTRANSFER, true);

$headers = array(
    "Content-Type: application/x-www-form-urlencoded",
); 

req_setopt($curl, CURLOPT_HTTPHEADER, $headers);

$data = "key=JP***g&txnid=Dnh8wYimuCRIdv&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=&bankcode=&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=&ccexpmon=&ccexpyr=&ccvv=&ccname=&txn_s2s_flow=&hash=cb4b8bda5677dbe80f53735b1d0ec5d48164c3654627369268cf6bf266db994db39108ce2e0868c953e66c172f6b2d78836b253d3463d0cc40d9b6a93118ed56";

req_setopt($curl, CURLOPT_POSTFIELDS, $data);

$resp = req_exec($req);

req_close($req);

var_dump($resp);

?>
```

```json Response Example
{"success":true}
```

# Setting the URL

<!-- php@3 -->

The URL https://test.payu.in/_payment is the endpoint provided by PayU for initiating the payment process.

# Initializing the cURL session

<!-- php@5 -->

The req_init() function is used to initialize a new session and return a cURL handle for use with the req_setopt(), req_exec(), and req_close() functions.

# Setting the cURL options

<!-- php@7-9 -->

The req_setopt() function is used to set an option on a cURL session handle. Here it’s used to set the URL, the HTTP method to POST, and to return the transfer as a string.

# Setting the headers

<!-- php@11-12 -->

The headers specify that the payload is URL-encoded (Content-Type: application/x-www-form-urlencoded).

# Creating the data

<!-- php@15-19 -->

The data contains the necessary parameters required by PayU to process the payment. These include the merchant key, transaction ID, amount, customer details, product information, success and failure URLs, and a security hash.

# Executing the cURL session

<!-- php@21 -->

The req_exec() function is used to perform a cURL session.

# Closing the cURL session

<!-- php@23 -->

The req_close() function is used to close a cURL session and free all resources. The cURL handle, req, is also deleted.

# Printing the response

<!-- php@25 -->

The response from the PayU server is printed out. This will be a string containing the details of the transaction.