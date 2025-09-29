---
title: Card Number Formats
excerpt: 'The cards can be identified by the format as described in following table:'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 📘 Note:
>
> To validate whether the card was issued in India, you must use the **check\_isDomestic** API by posting the first six digits of the card number. For more information, refer to the [BIN APIs](ref:bin-apis).

| **Card Type** | **Card Number Format**                                                              |
| ------------- | ----------------------------------------------------------------------------------- |
| AMEX          | Starting with 34 or 37, length 15 digits.                                           |
| VISA          | Starting with 4, length 16 digits.                                                  |
| Mastercard    | Starting with 51 through 55, length 16 digits.                                      |
| Diners Club   | Starting with 300 through 305, 36, or 38, length 14 digits.                         |
| Discover      | Starting with 6011, length 16 digits or starting with 5, length 15 digits.          |
| JCB           | Starting with 2131 or 1800, length 15 digits or starting with 35, length 16 digits. |

## Validating Card Number using LUHN Algorithm

You can use the LUHN algorithm to validate the card numbers when they enter their card details for payment. The following code block provides function to pass a card number, and receive a boolean value of true or false depending on whether the card is calculated to be valid by the LUHN algorithm.

```javascript
| function luhn \# \<numeric-string\> {  num=\$1  shift 1    len=\${\#num}  is_odd=1  sum=0  for((t = len - 1; t \>= 0; --t)) {  digit=\${num:\$t:1}    if \[[ \$is_odd -eq 1 ]]; then  sum=\$(( sum + \$digit ))  else  sum=\$(( \$sum + ( \$digit != 9 ? ( ( 2 \* \$digit ) % 9 ) : 9 ) ))  fi    is_odd=\$(( ! \$is_odd ))  }    \# NOTE: returning exit status of 0 on success  return \$(( 0 != ( \$sum % 10 ) )) } |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
```
