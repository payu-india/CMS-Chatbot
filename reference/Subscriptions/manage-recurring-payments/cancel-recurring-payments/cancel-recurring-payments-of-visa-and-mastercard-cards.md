---
title: Cancel Recurring Payments of VISA and Mastercard Cards
excerpt: >-
  Cancel recurring payment mandates created using VISA and Mastercard cards with
  PayU APIs. Learn the card mandate cancellation flow, request parameters,
  response handling, and recurring payment management.
deprecated: false
hidden: true
metadata:
  robots: index
---
Use this API to cancel card mandates registered using VISA and Mastercard card networks. You cannot restore a cancelled mandate. You should ask customers to register a new mandate.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /merchant/postservice.php?form=2
  </Card>
</Cards>

## Environment

| **Environment**            | **URL**                                                |
| :------------------------- | :----------------------------------------------------- |
| **Test Environment**       | `https://test.payu.in/merchant/postservice.php?form=2` |
| **Production Environment** | `https://info.payu.in/merchant/postservice.php?form=2` |

## Sample Request

<Accordion title="Request Payload" icon="fa-code">

```curl
curl --location 'https://info.payu.in/merchant/postservice.php' \
  --header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642' \
  --form 'form="2"' \
  --form 'key="BmTY3G"' \
  --form 'command="mandate_revoke"' \
  --form 'var1="{\"authpayuid\":\"19504273314\",\"requestId\":\"test000212\"}"' \
  --form 'hash="YOUR_HASH_VALUE"' \
  --form 'salt="YOUR_SALT_VALUE"'
```

</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">

```json Success Response
{
  "status":1,
  "message":"Mandate Revoked Successfully",
  "action":"MANDATE_REVOKE"
}
```
```json Error Response
{
  "status":0,
  "message":"Mandate not in appropriate state to perform action",
  "action":"MANDATE_REVOKE"
}
```


</Accordion>
