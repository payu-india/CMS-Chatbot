---
name: siDetails v2 object
---
### siDetails object fields description

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "billingCycle  \n`mandatory`",
    "0-1": "The frequency of the billing, indicating how often the payment occurs.",
    "0-2": "MONTHLY",
    "1-0": "billingAmount  \n`mandatory`",
    "1-1": "The amount to be billed for each cycle.",
    "1-2": "1.00",
    "2-0": "billingCurrency  \n`mandatory`",
    "2-1": "The currency in which the billing amount is denominated.",
    "2-2": "INR",
    "3-0": "billingInterval  \n`mandatory`",
    "3-1": "The interval between billing cycles, specified in terms of the cycle frequency.",
    "3-2": "1",
    "4-0": "paymentStartDate  \n`mandatory`",
    "4-1": "The date when the payment cycle begins.",
    "4-2": "2020-09-16",
    "5-0": "paymentEndDate  \n`mandatory`",
    "5-1": "The date when the payment cycle ends.",
    "5-2": "2020-10-16",
    "6-0": "siTokenRequestor  \n`optional`",
    "6-1": "This is optional and is only needed before 30th September, 2022 to activate new mandate setups in a controlled manner than activating it completely on all users. This involves creating token at the time of susbcription set. You can include any of the following values::  \n1 : PayU will tokenise the card and share it in same subscription setup call with issuers for subscription setup.  \n2: PayU will do the authorization on plain card. Later, the same response will be shared to merchant.",
    "6-2": "1",
    "7-0": "authpayuid  \n`mandatory for modifying subscription`",
    "7-1": "An identifier used for the authorization of payments via PayU.",
    "7-2": "",
    "8-0": "action  \n`mandatory for cards`",
    "8-1": "This field is used to modify or delete an existing subscription.",
    "8-2": ""
  },
  "cols": 3,
  "rows": 9,
  "align": [
    null,
    null,
    null
  ]
}
[/block]