---
title: _payment Request Python Code Walkthrough
description: >-
  This recipe helps you with code walkthrough for PayU Hosted Checkout
  integration _payment request with Python language binding.
hidden: false
recipe:
  color: '#018FF4'
  icon: 🦉
---
```python Python
import requests

url = "https://test.payu.in/_payment"
payload = "key=JP***g&txnid=Dnh8wYimuCRIdv&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=&bankcode=&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=cb4b8bda5677dbe80f53735b1d0ec5d48164c3654627369268cf6bf266db994db39108ce2e0868c953e66c172f6b2d78836b253d3463d0cc40d9b6a93118ed56"
headers = { "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded" }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

```

```json Response Example
{"success":true}
```

# Importing the requests module



The requests module is a popular Python library for making HTTP requests. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application.

# Setting the URL

<!-- python@3 -->

The URL https://test.payu.in/_payment is the endpoint provided by PayU for initiating the payment process. Note that the Test environment is used here.

# Creating the payload



The payload contains the necessary parameters required by PayU to process the payment. These include the merchant key, transaction ID, amount, customer details, product information, success and failure URLs, and a security hash.

# Setting the headers

<!-- python@5 -->

The headers specify that the client expects JSON in response (Accept: application/json) and that the payload is URL-encoded (Content-Type: application/x-www-form-urlencoded).

# Making the request



The requests.request function is used to send a POST request to the specified URL with the given payload and headers.

# Printing the response:



The response from the PayU server is printed out. This will be a JSON string containing the details of the transaction.