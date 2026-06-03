---
title: Check Mandate Status
deprecated: false
hidden: true
metadata:
  robots: index
---
Use this endpoint to check the mandate status of the following payment methods:

- Cards
- NetBanking
- UPI

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /merchant/postservice.php
  </Card>
</Cards>

<GENERALAPIsEnvironment />

## Sample Request

<Accordion title="Request Payload" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
    --header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642' \
    --form 'form="2"' \
    --form 'key="BmTY3G"' \
    --form 'command="check_mandate_status"' \
    --form 'var1="{\"authPayuId\":\"25599222315\",\"requestId\":\"403993715532527858_check_3\",\"endDate\":\"2025-11-15\",\"amount\":\"1\"}"' \
    --form 'hash="YOUR_HASH_VALUE"'
  ```
</Accordion>

<br />
