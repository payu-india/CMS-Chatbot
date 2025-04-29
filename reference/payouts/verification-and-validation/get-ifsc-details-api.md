---
title: Get IFSC Details API
excerpt: ''
api:
  file: payouts-api-8.json
  operationId: GetIFSCDetailsAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The** Get IFSC Details** API is to get the IFSC Details based on the IFSC code of the bank.

**Environment**

|                            |                                                            |
| -------------------------- | ---------------------------------------------------------- |
| **Test Environment**       | &lt;https://uatoneapi.payu.in/payout/merchant/getIfscDetails&gt; |
| **Production Environment** | &lt;https://www.payumoney.com/payout/merchant/getIfscDetails&gt; |

<details>
  <summary>Sample request</summary>

```curl
curl --location --request GET 'https://test.payumoney.com/payout/merchant/getIfscDetails?ifsc=HDFC0004392' \
--header 'Authorization: Bearer bdbdf325a3bfd9217e7cbc93d0dbe7b40b096bb9ad3aa585d0eab9ac4d30bc3e' \
--header 'payoutMerchantId: 1111270'
```

</details>

<details>
  <summary>Sample response</summary>

**Success scenario**

```
{
    "status": 0,
    "msg": null,
    "code": null,
    "data": {
        "city": "GAUTAM BUDDHA NAGAR, NOIDA",
        "office": "SEC LXII GALAXY IT PARK",
        "district": "GAUTAM BUDDHA NAGAR",
        "ifsc": "HDFC0004392",
        "micr": "110240445",
        "state": "UTTAR PRADESH",
        "contact": "9935903333",
        "branch": "SEC LXII GALAXY IT PARK",
        "address": "HDFC BANK LTD GALAXI IT PARK GROUND FLOOR RETAIL 02 TOWER B PLOT 44 45 GALAXI IT PARK NOIDA GAUTAM BUDH NAGAR UTTAR PRADESH201301",
        "bank": "HDFC BANK"
    }
}

```

**Failure scenario**

```
{
    "status": 1,
    "msg": "IFSC is invalid",
    "code": null,
    "data": null
}
```

</details>

## Header and request parameters

> 📘 Note:
> 
> The payoutMerchantId is different from PayU Merchant Id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your payoutMerchantId.