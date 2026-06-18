---
api:
  file: pdn-rp-api.yaml
  operationId: post_merchant-webservice-service-php
hidden: true
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /merchant/postservice.php?form=2
  </Card>
</Cards>

<GENERALAPIsEnvironment />

## Sample Request

<Accordion title="Request Payload" icon="fa-code">
```curl
curl -X POST "https://info.payu.in/merchant/postservice.php?form=2" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=test" \
  -d "hash=YOUR_HASH_VALUE" \
  -d 'var1={
  "authPayuId": "403993715529787",
  "txnId": "TXN_20240415_002",
  "amount": "999.00",
  "debitDate": "2024-04-22",
  "debitType": "PREDEBIT_AND_RECURRING",
  "currency": "INR",
  "planId": "PLAN_MONTHLY_999",
  "mandateSeqNo": "2",
  "additional_charges": "CCSI:10,DCSI:20,HDFCDCSI:30,AMEXSI:40",
  "percentage_additional_charges": "CCSI:10,DCSI:20,HDFCDCSI:30,AMEXSI:40",
  "udf2": "renewal",
  "udf3": "premium",
  "udf4": "auto_pay",
  "udf5": "cycle_2",
  "email": "customer@example.com",
  "phone": "9999999999",
  "firstname": "John",
  "lastname": "Doe",
  "address1": "123 Main Street",
  "address2": "Apt 4B",
  "city": "Mumbai",
  "state": "Maharashtra",
  "country": "India",
  "zipcode": "400001",
  "more_info": [
    {
      "wtParams": [
        {
          "type": "mutual_fund",
          "plan": "GD",
          "folio": "9104927822",
          "amount": "100",
          "option": "G",
          "scheme": "LT",
          "receipt": "12345",
          "mf_member_id": "12345",
          "mf_user_id": "7740",
          "mf_partner": "cams",
          "mf_investment_type": "L",
          "mf_amc_code": ""
        }
      ]
    }
  ]
}'
```
</Accordion>

> 📘 **Request Parameter Description**
>
> Refer to the Form Data section for request parameter description.

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "status":1,
  "message":"Debit Scheduled successfully",
  "details":[
    
  ],
  "predebitDetails":[
    
  ]
}
```json Error Response
{
  "status":0,
  "message":"debitDate is mandatory",
  "errorCode":"SIR004",
  "action":"SI_RECURRING"
}
```
</Accordion>

```json Success Response
{
  "status":1,
  "message":"Debit Scheduled successfully",
  "details":[
    
  ],
  "predebitDetails":[
    
  ]
}
```
```json Error Response
{
  "status":0,
  "message":"debitDate is mandatory",
  "errorCode":"SIR004",
  "action":"SI_RECURRING"
}
```

> 📘 **Response Parameter Description**
>
> Refer to the Responses section for response parameter description.

<br />
