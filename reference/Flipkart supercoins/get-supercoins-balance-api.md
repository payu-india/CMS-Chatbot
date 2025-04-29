---
title: Get SuperCoins Balance API
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
The **Get SuperCoins Balance** API is used to get the rewards balance for a customer based on their mobile number. In this section, the procedure to get the SuperCoins rewards balance.

#### Endpoints

<table style="border:0.1rem solid rgb(242, 242, 242);"><tbody><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;"><strong>Test Environment</strong></td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">https://test.payu.in/</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;"><strong>Production Environment</strong></td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">&lt;TBD&gt;</td></tr></tbody></table>

## Request Header

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Authorization  \n**mandatory**",
    "0-1": "`String` Specify the access token generated during authentication in this parameter/.",
    "0-2": "Bearer {access\\_token}",
    "1-0": "Content-Type  \n**mandatory**",
    "1-1": "`String` Indicates the format in which the request is sent",
    "1-2": "application/json"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Request Parameters

The request parameters must include the following along with the request header.

| **Parameter**   | **Description**                                                             | **Example**          |
| --------------- | --------------------------------------------------------------------------- | -------------------- |
| mobileNumber    | The customer's mobile number for whom the FKSC balance needs to be fetched. | 9876543210           |
| loyaltyProvider | Passed with the value as **SUPERCOIN** for FKSC.                            | SUPERCOIN            |
| merchantTxnId   | This parameter must contain the transaction ID.                             | dafbe2503deda3c04baa |

## Sample Request

```curl
curl 'https://pp225api.payu.in/loyalty-points/v1/balance' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI4MDc2NDk5MzkzIiwibW9iaWxlTnVtYmVyIjoiODA3NjQ5OTM5MyIsImV4cCI6MTY4NjIyMDE4NiwiaWF0IjoxNjc4NDQ0MTg2fQ.KlUZUOQEMQHq8Ws3nb5qP6ieDeUDAqDZrsy3CBvlN18' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'Origin: https://pp225api.payu.in' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://pp225api.payu.in/public/' \
  -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
  -H 'Cookie: _ga=GA1.2.1104854354.1674121685; _hjSessionUser_2469364=eyJpZCI6ImNjYmFiZTFjLTYyNzgtNTY0Yi1hYzY0LTZlMzFiNjZmZWJiZCIsImNyZWF0ZWQiOjE2NzcyMTUzNjAzMzIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_7CG3P7JYWT=GS1.1.1677215359.3.0.1677215473.0.0.0; PHPSESSID=qd02rs8s93bsqtntsaaun149kj; coherenceToken=0bc22d976fe31c08dddf60ac1b98a17b8dd969d96511cea1d906cda665f0cd64; WZRK_G=f420376eb8fd48c0b10056600106ebbe; WZRK_S_TEST-589-9RZ-ZZ6Z=%7B%22s%22%3A1678682826%2C%22t%22%3A1678682834%2C%22p%22%3A1%7D' \
  --data-raw '{"mobileNumber":"8076499393","loyaltyProvider":"SUPERCOIN","merchantTxnId":"dafbe2503deda3c04baa"}' \
  --compressed Response :    {"usableAmount":9.50,"amount"... by Bobby Sharma
```



## Sample Response

```plaintext
{"usableAmount":9.50,"amount":38,"globalThreshold":true}
```