---
title: REST API Format
excerpt: >-
  PayU has created many REST APIs and each REST API has a specific function. You
  can use them to automate different features. The basic format and execution of
  all web services remain the same. Each REST API is a server-to-server call
  from your server to PayU’s server.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
REST API can be accessed by making a server-to-server call on the following PayU URLs:

> 📘 Reference:
> 
> Refer to the following recipe for a walkthrough of a cURL request for a REST API.
> 
> [block:tutorial-tile]{"backgroundColor":"#018FF4","emoji":"🦉","id":"65084edbb1c590100cf1243e","link":"https://payu-hosted-checkout.readme.io/v1/recipes/curl-walkthrough","slug":"curl-walkthrough","title":"CURL Walkthrough"}[/block]

## URLs for Test and Production environment

### Base URLs

<table style="border:0.1rem solid rgb(242, 242, 242);"><tbody><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Test</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">https://test.payu.in/merchant/postservice.php?form=2&nbsp;</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Production</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">https://info.payu.in/merchant/postservice.php?form=2</td></tr></tbody></table>

> 📘 Note:
> 
> The above base URLs are for the General APIs. Refer to the specific API reference page to get the exact endpoints. For the \_payment APIs, refer to any of the following:
> 
> - [Collect Payment API for PayU Hosted Checkout integration](ref:_payment_payu_hosted_checkout)
> - [Collect Payment API for Merchant Hosted Checkout integration](ref:_payment_merchant_hosted)
> - [Collect Payment API for S2S integration](ref:_payment_server_to_server)

## Request format

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Sample Value**",
    "0-0": "key",
    "0-1": "Merchant key provided by PayU. For more information on checking your key and Salt, refer to [Generate Merchant Key and Salt on PayU Dashboard](https://devguide.payu.in/api/integration-apis/generate-api-key-and-salt/).",
    "0-2": "Ibibo",
    "1-0": "command",
    "1-1": "This parameter must have name of the web-service. ",
    "1-2": "save\\_card",
    "2-0": "hash",
    "2-1": "This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:  \nsha512(key|command|var1|salt) sha512 is the encryption method used.  \n**Note**:  For \\_payment APIs, refer to [Generate Hash](doc:hashing-request-and-response)",
    "2-2": "ajh84ba8abvav",
    "3-0": "var1, var2, var3 ... up to var15",
    "3-1": "These are the variable parameters, whose values depend on the particular web-service. The definition of these parameters will be covered in the (Read command explanations mentioned later - separate for all the actions/commands.)",
    "3-2": "Read specific commands."
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Response format

> 📘 Note:
> 
> To get the response in JSON, you need to append **form=2** along with the endpoint similar to the following:

<https://test.payu.in/merchant/postservice.php?form=2>

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "This parameter returns the any of the following status of web service call:  \n_  1 - If web service call succeeded  \n_  0 - if web service call failed",
    "0-2": "0",
    "1-0": "msg",
    "1-1": "Reason String",
    "1-2": "Parameter missing or token is empty or amount is empty or transaction not exists",
    "2-0": "transaction\\_details",
    "2-1": "This parameter may or may not be return response depending on the web service being called.",
    "2-2": "mihpayid,request\\_id, bank\\_ref\\_num etc",
    "3-0": "request\\_id",
    "3-1": "PayU Request ID for a request in a Transaction. eg. A transaction can have a refund request.",
    "3-2": "7800456",
    "4-0": "bank\\_ref\\_num",
    "4-1": "Bank Reference Number. If bank provides after a successful action.",
    "4-2": "204519474956"
  },
  "cols": 3,
  "rows": 5,
  "align": [
    null,
    null,
    null
  ]
}
[/block]