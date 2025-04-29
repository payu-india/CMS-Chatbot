---
title: EMI Options for Get Checkout Details API
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
In the request parameters of the **Get Checkout Details **API, you can use the following codes in the JSON array for EMI with the **paymentoption** field of the **filters** parameter. For example, the following can be used for **filters** parameter.

```
{ "paymentOptions": { "emi": { "dc": "SBIN,KKBK,ICIC" } } }
```

## Debit card EMI options

| Bank Name           | Code   |
| ------------------- | ------ |
| Axis                | UTIB   |
| Bank of Baroda      | BARB   |
| HDFC Bank           | HDFCDC |
| Federal Bank        | FDRL   |
| ICICI Bank          | ICIC   |
| Kotak Mahindra Bank | KKBK   |
| State Bank of India | SBIN   |

## Credit card EMI options

| Bank Name               | Code   |
| ----------------------- | ------ |
| AMEX                    | AMEX   |
| AU Small Finance Bank   | AUSF   |
| Axis                    | UTIB   |
| Bank of Baroda          | BARB   |
| CANARA Bank             | CANARA |
| CITI                    | CITI   |
| DBS Bank                | DBSCC  |
| Federal Bank            | FDRL   |
| HDFC Bank               | HDFC   |
| HSBC                    | HSBC   |
| ICICI Bank              | ICIC   |
| IDBI Bank               | IDBI   |
| IDFC FIRST Bank         | IDFC   |
| INDUS                   | INDB   |
| Kotak Mahindra Bank     | KKBK   |
| OneCard                 | ONEC   |
| RBL                     | RATN   |
| State Bank of India     | SBIN   |
| Standard Chartered Bank | SCBL   |
| Yes Bank                | YESB   |

## Cardless EMI options

| Issuer Name   | Code     |
| ------------- | -------- |
| Axio          | AXIO     |
| Bajaj Finance | BAJFIN   |
| HDFC Bank     | HDFC_CL  |
| Homecredit    | HMECDT   |
| ICICI Bank    | ICICI_CL |
| Kotak Bank    | KOTAKC   |
| Kreditbee     | KBEE     |
| Zest Money    | ZESTMON  |