---
title: Generate Static Hash
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


| Hash Name                                 | Description                                                                                                                         | Hash Formula                                                                                      |
| :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ |

| `eligibleBinsForEMI`                      | It is used to fetch the eligible bins for EMI when EMI is enabled. If not passed, EMI payment will not work.                        | `<key>\\|eligibleBinsForEMI\\|default\\|<salt>`                                                   |
| `getEmiAmount   AccordingToInterest`      | It is used to fetch EMI details like, amount, interest rate, etc when EMI is enabled. If not passed, EMI payment will not work.     | `<key>\\|vas_for_mobile_sdk\\|<amount>\\|<salt>`                                                  |
| `Payment`                                 | It is used for making payment. If not passed, payment will not happen.                                                              | key\|txnid\|amount\|productinfo\|firstname\|email \|udf1\|udf2\| udf3\|udf4\|udf5\|\|\|\|\|\|salt |
| `delete_payment_instrument`               | It is used to delete the Tokenised card                                                                                             | `<key>\\|delete_payment_instrument\\|<userCredential\\| <salt>`                                   |


