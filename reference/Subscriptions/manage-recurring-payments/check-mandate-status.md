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

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Cards - Success Response 
  {
    "status":"active",
    "action":"check_mandate_status",
    "authpayuid":25599222315,
    "amount":"1",
    "mandateStartDate":"2025-10-14",
    "mandateEndDate":"2027-12-01"
  }
  ```
  ```json NetBanking - Success Response
  {
  	"status": "SUCCESS", // INITIATED/SUCCESS/FAILED/CANCEL_INITIATED/CANCEL_PENDING/CANCEL_FAILED/CANCEL_INITIATION_FAILED
  	"action": "NB_mandate_status",
  	"authpayuid": "10731087875",
  	"amount": "100.00",
  	"mandateStartDate": "2022-07-19",
  	"mandateEndDate": "2023-12-20"
  }
  ```
  ```json UPI - Success Response
  {
      "status": "active",
      "action": "MANDATE_STATUS",
      "authpayuid": "25600438037",
      "amount": "1.00",
      "mandateStartDate": "2025-10-14 00:00:00",
      "mandateEndDate": "2027-12-01 00:00:00"
  }
  ```
</Accordion>

<br />
