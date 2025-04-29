---
title: Create Smart Send Link API
excerpt: ''
api:
  file: new-payouts-api-collection-5.json
  operationId: CreateSmartSendLinkAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The** Create Smart Send Link** API is used to create and send the Smart Send link to beneficiary phone number or Email Id. This method is used when the beneficiary bank details or VPA is not available.

**Environment**:

|                            |                                                         |
| -------------------------- | ------------------------------------------------------- |
| **Test Environment**       | <https://uatoneapi.payu.in/payout/v2/smartSend/link>    |
| **Production Environment** | <https://payout.payumoney.com/payout/v2/smartSend/link> |

<details>
  <summary>Sample request</summary>

```curl
curl --location --request POST 'https://oneapi.payu.in/payout/v2/smartSend/link' \
--header 'authorization: Bearer f596252f5ccfeb775071b1202a80328d40bf58cf0c468f150220d16dce9deeee' \
--header 'pid: 1111312' \
--header 'Content-Type: application/json' \
--data-raw '{
    "amount": "1",
    "merchantRefId": "TEST00020",
    "custName": "DIVIK",
    "custMobile": "9868888568",
    "description": "TEST",
    "expiryDate": "2021-07-23T10:00:49.778Z"
}'
```

</details>

<details>
  <summary>Sample response</summary>

**Success scenario**

```
{
	"status": 0,
	"msg": "Success",
	"code": null,
	"data": {
		"link": "https://test.payumoney.com/url/1IOrXuzqo5KH",
		"linkId": "D9tCcL3ICHYsby5Op1BXv9vETLDvfiExyXAC9jf/lQ2xTIIUAyREa2ZN3VbrMmFx",
		"expiryDate": "2021-07-21T12:19:04.882+0000"
	}
}
```

**Failure scenario**

**Access Denied**

```
{
  "timestamp": "2024-01-30T09:03:39.698+0000",
  "status": 401,
  "error": "Unauthorized",
  "message": "Access is denied",
  "path": "/payout/v2/smartSend/link"
}
```

</details>

## Request header and parameters

> 📘 Notes:
> 
> - The **pid** is **payoutMerchantId**, however it is different from the PayU merchant id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your **payoutsMerchantID**.
> - The mobile number or email is required for creating a smart send link, so either the `custMobile` or `custEmail` parameters must have values. If both mobile and email are passed in the request, then Smart Send link will go to both email and mobile.