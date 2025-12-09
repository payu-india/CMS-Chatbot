---
title: Basics of cURL
description: Recipe Description
hidden: true
recipe:
  color: '#018FF4'
  icon: 🦉
---
```shell Shell
curl -X POST "https://test.payu.in/_payment" \
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d \
"key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00 \
&firstname=PayU User&email=test@gmail.com&phone=9876543210 \
&productinfo=iPhone&surl= \
https://apiplayground-response.herokuapp.com/ \
&furl=https://apiplayground-response.herokuapp.com/ \
&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
```

```json Response Example
{"success":true}
```

# Endpoint

<!-- shell@1 -->

It contains the server endpoint with the path and also path parameters if any or query parameters appended after a question mark("?"). 

# Header

<!-- shell@2 -->

Contains the format of the form data or regular parameters. In general, it contains the authentication.

# Body Params

<!-- shell@3-8 -->

It contains the body parameters or form data.