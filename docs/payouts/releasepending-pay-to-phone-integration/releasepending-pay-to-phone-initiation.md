---
title: Pay to Phone Initiation
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can choose to initiate pay to phone using the Payouts API integration, Payout Dashboard or File Upload mediums as per your convenience.  

## Pay to Phone from API  

You can initiate single payouts to phone API requests using the Initiate Transfer API which can also be used for any other payouts modes too. For more information, refer to [Initiate Transfer API](https://docs.payu.in/reference/initiate-transfer-api).

### Required parameters

- beneficiaryName
- mobileNumber
- amount
- purpose
- paymentType as **PHONE** .

### Sample request

```curl
curl --location 'https://uatoneapi.payu.in/payout/v2/payment' \
--header 'accept: application/json, text/plain, */*' \
--header 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
--header 'authorization: Bearer 35a2ad7249ad1ec2f13a3cb8a41ed3faf16451ed659a0f479b744f57182dab25' \
--header 'content-type: application/json;charset=UTF-8' \
--header 'mid: 127172' \
--header 'origin: https://dashboard-staging.payu.in' \
--header 'pid: 2225335' \
--header 'product: PAYUBIZ' \
--header 'referer: https://dashboard-staging.payu.in/' \
--header 'sec-ch-ua: "Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "macOS"' \
--header 'sec-fetch-dest: empty' \
--header 'sec-fetch-mode: cors' \
--header 'sec-fetch-site: same-site' \
--header 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '[
    {
        "beneficiaryName": "CC",
        "beneficiaryMobile": 7754927986,
        "paymentType": "phone",
        "purpose": "Payout",
        "amount": "1",
        "batchId": "",
        "merchantRefId": "",
        "vpa": "",
        "scheduledTime": ""
    }
]'
```

### Sample response

```
{
    "status": 0,
    "msg": "Requests are in process. Will send response of individual request on webhooks set by you",
    "code": null,
    "data": []
}
```

## Single Payouts to Phone from Dashboard   

You can initiate single payouts to phone request from the Dashboard in the ‘[Make A Transfer](https://docs.payu.in/docs/make-a-transfer)’ journey, by clicking on ‘**PHONE**’ and providing the beneficiary’s name, mobile, purpose and amount.  

- You can also schedule the payout for future dates.   
- Before submission, you can set the merchant reference id as per your internal mapping. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2687448-image.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


### Bulk Payouts to Phone from Dashboard  

You can initiate multiple payouts to phone requests from the Dashboard in the ‘[Make A Transfer](https://docs.payu.in/docs/make-a-transfer)’ journey, by clicking on ‘Pay to Phone’ in ‘BULK TRANSFERS’ and uploading a csv file with the beneficiary name, beneficiary mobile, amount, purpose without providing the beneficiary account number, IFSC or VPA details.  

- Each row entry in csv file will be processed as a single payout to the beneficiary. 
- Max 10,000 payouts to phone can be initiated in a single csv file upload 
- Required Values – Beneficiary Name, Mobile Number, Amount, Purpose and payment type as ‘PHONE’ 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1f26904-image.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]