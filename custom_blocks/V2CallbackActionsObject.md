---
name: v2 callbackActions object
---
### callbackActions object fields description

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "successAction  \n `mandatory`",
    "0-1": "`String`URL to redirect to upon successful payment.",
    "1-0": "failureAction  \n `mandatory`",
    "1-1": "`String`URL to redirect to if the payment is failed.",
    "2-0": "cancelAction  \n `mandatory`",
    "2-1": "`String`URL to redirect to if the transaction is cancelled.",
    "3-0": "codAction  \n `optional`",
    "3-1": "`String`URL to handle Cash on Delivery actions.",
    "4-0": "termAction  \n `optional`",
    "4-1": "`String`URL for completing terms and conditions actions.",
    "5-0": "returnAction  \n `optional`",
    "5-1": "`String`URL to return to after successful payment action is completed."
  },
  "cols": 2,
  "rows": 6,
  "align": [
    null,
    null
  ]
}
[/block]