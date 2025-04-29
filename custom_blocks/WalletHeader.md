---
name: Wallet Header
---
### Header

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "x-api-key  \n**mandatory**",
    "0-1": "`String` This is a unique key.",
    "0-2": "7fe1c0de",
    "1-0": "clientId  \n**mandatory**",
    "1-1": "`String` Uniquely identifies the client. During program enrolment each client is provided with a unique client id by Prepaid",
    "1-2": "2000",
    "2-0": "bankId  \n**mandatory**",
    "2-1": "`Numeric` Bank Id is provided by Prepaid Aero during program enrolment to uniquely identify the card issuer.",
    "2-2": "7000",
    "3-0": "entityId  \n**mandatory**",
    "3-1": "`Numeric` Defaults to parent branch i.e., 100",
    "3-2": "100",
    "4-0": "secureCode  \n**mandatory**",
    "4-1": "`String` Uniquely identifies the client on payload level for performing operations.",
    "4-2": "AfYtlO5kqdySIjXyNmGg3F"
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