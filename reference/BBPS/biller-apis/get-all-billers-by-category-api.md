---
title: Get All Billers By Category API
excerpt: ''
api:
  file: bbps-apis-agent-share-3.json
  operationId: GetAllBillersByCategory
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get All Billers by Category** API fetches all the billers from PayU based on the biller category name passed in the request.

<BBPSEnvironment />

> 📘 Note:
> 
> Send the scope of the Get Token API as **read_billers** to obtain the access_token for this request. For more information refer to [Get Token API - BBPS](ref:get-token-api-bbps).

<details><summary>Sample request</summary>

```
curl --location --request GET 'https://<hostName>/payu-nbc/v1/nbc/getBillerByBillerCategory?billerCategoryName=&agentId=&pageNumber=&pageSize=' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <token>'
```

</details>

<details><summary>Response parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Field Name**",
    "h-1": "**Description**",
    "0-0": "code",
    "0-1": "The global response code and can be any of the following:  \n  \n- **0**: If web service call failed\n- **1**: if web service call succeeded",
    "1-0": "status",
    "1-1": "The status of the API command and can be any of the following:  \n  \n- SUCCESS\n- FAILURE",
    "2-0": "payload",
    "2-1": "It will contain a list of biller categories. For more information, refer to the [payload](#payload) table."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


### payload

[block:parameters]
{
  "data": {
    "h-0": "**Field Name**",
    "h-1": "**Description**",
    "0-0": "**Success Scenarios**",
    "0-1": "",
    "1-0": "billerCategories",
    "1-1": "This field contains the biller categories in an array format.",
    "2-0": "billerName",
    "2-1": "This field contains the biller name.",
    "3-0": "billerCategory",
    "3-1": "This field contains the biller category.",
    "4-0": "",
    "4-1": "",
    "5-0": "**Failure Scenarios**",
    "5-1": "",
    "6-0": "refId",
    "6-1": "For failure scenarios, This parameter contains the reference ID.  \n**Note**: In case of category fetch refId will be null.",
    "7-0": "type",
    "7-1": "For failure scenarios, this field contains the type of error.",
    "8-0": "code",
    "8-1": "The global response code",
    "9-0": "payload",
    "9-1": "It will contain payload with error messages.",
    "10-0": "status",
    "10-1": "The status of the response. Example, SUCCESS/FAILURE",
    "11-0": "message",
    "11-1": "For failure scenarios, this field contains the description of error type for failure or success.",
    "12-0": "errors",
    "12-1": "For failure scenarios, this field contains the following in the response:  \n  \n- **reason**: The error description if the request has failed.\n- **errorCode**: The error code of the error if the request has failed",
    "13-0": "additionalParams",
    "13-1": "For failure scenarios, this field contains the additional fields (if any) related to billers in an array format."
  },
  "cols": 2,
  "rows": 14,
  "align": [
    null,
    null
  ]
}
[/block]


</details>

<details><summary>Sample response</summary>

### Success scenario

```
{
   "code":200,
   "status":"SUCCESS",
   "payload":{
      "billers":[
         {
            "billerId":"<billerId1>",
            "billerName":"<billerId2>",
            "customerParams":[
               {
                  "dataType":"ALPHANUMERIC",
                  "optional":false,
                  "paramName":"Customer Code",
                  "minLength":"2",
                  "maxLength":"10",
                  "regex":"<regex for biller>",
                  "values":"< values comma separated supported by a biller customer param >",
                  "requiredIn":"fetch/payment"
               }
            ],
            "isAdhoc":false,
            "fetchOption":"OPTIONAL/MANDATORY/NOT_SUPPORTED",
            "category":"<Name of the category>",
            "region":"<region name>",
            "flowType":"BBPS/NON-BBPS",
            "paymentModesAllowed":[
               {
                  "paymentMode":"Internet Banking",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"Debit Card",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"Credit Card",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"Prepaid Card",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"IMPS",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"Cash",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"UPI",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"Wallet",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"NEFT",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"AEPS",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"Account Transfer",
                  "minLimit":"0.01"
               }
            ],
            "paymentChannelsAllowed":[
               {
                  "paymentMode":"INT",
                  "maxLimit":"50000",
                  "minLimit":"1"
               },
               {
                  "paymentMode":"INTB",
                  "maxLimit":"50000",
                  "minLimit":"1"
               },
               {
                  "paymentMode":"MOB",
                  "maxLimit":"50000",
                  "minLimit":"1"
               },
               {
                  "paymentMode":"MOBB",
                  "maxLimit":"50000",
                  "minLimit":"1"
               },
               {
                  "paymentMode":"POS",
                  "maxLimit":"50000",
                  "minLimit":"1"
               },
               {
                  "paymentMode":"MPOS",
                  "maxLimit":"50000",
                  "minLimit":"1"
               },
               {
                  "paymentMode":"ATM",
                  "maxLimit":"50000",
                  "minLimit":"1"
               },
               {
                  "paymentMode":"BNKBRNCH",
                  "maxLimit":"50000",
                  "minLimit":"1"
               },
               {
                  "paymentMode":"KIOSK",
                  "maxLimit":"50000",
                  "minLimit":"1"
               },
               {
                  "paymentMode":"AGT",
                  "maxLimit":"50000",
                  "minLimit":"1"
               },
               {
                  "paymentMode":"BSC",
                  "maxLimit":"50000",
                  "minLimit":"1"
               }
            ],
            "billerOwnerShp":"PSU",
            "status":"ACTIVE",
            "billerEffctvFrom":"2020-04-20",
            "billerEffctvTo":null,
            "interchangeFee":[
               {
                  "feeDesc":"Customer_Convenience_Fee",
                  "feeCode":"CCF1",
                  "feeDirection":"C_2_B",
                  "interchangeFeeDetails":[
                     {
                        "effctvTo":"",
                        "tranAmtRangeMax":9223372036854776000,
                        "effctvFrom":"2019-08-01",
                        "percentFee":0,
                        "tranAmtRangeMin":0,
                        "flatFee":0
                     }
                  ]
               },
               {
                  "feeDesc":"Physical_Biller_Fee",
                  "feeCode":"PBF",
                  "feeDirection":"B_2_C",
                  "interchangeFeeDetails":[
                     {
                        "effctvTo":"",
                        "tranAmtRangeMax":9223372036854776000,
                        "effctvFrom":"2019-08-01",
                        "percentFee":0,
                        "tranAmtRangeMin":0,
                        "flatFee":225
                     }
                  ]
               },
               {
                  "feeDesc":"Electronic_Biller_Fee",
                  "feeCode":"EBF",
                  "feeDirection":"B_2_C",
                  "interchangeFeeDetails":[
                     {
                        "effctvTo":"",
                        "tranAmtRangeMax":9223372036854776000,
                        "effctvFrom":"2019-08-01",
                        "percentFee":0,
                        "tranAmtRangeMin":0,
                        "flatFee":225
                     }
                  ]
               }
            ],
            "interchangeFeeConf":[
               {
                  "fees":[
                     "CCF1",
                     "EBF"
                  ],
                  "mti":"PAYMENT",
                  "defaultFee":true,
                  "effctvFrom":"20190801",
                  "responseCode":"000"
               },
               {
                  "fees":[
                     "CCF1",
                     "PBF"
                  ],
                  "mti":"PAYMENT",
                  "defaultFee":false,
                  "effctvFrom":"20190801",
                  "responseCode":"000"
               },
               {
                  "fees":[
                     "CCF1",
                     "PBF"
                  ],
                  "mti":"PAYMENT",
                  "defaultFee":false,
                  "effctvFrom":"20190801",
                  "responseCode":"000"
               },
               {
                  "fees":[
                     "CCF1",
                     "PBF"
                  ],
                  "mti":"PAYMENT",
                  "defaultFee":false,
                  "effctvFrom":"20190801",
                  "responseCode":"000"
               }
            ],
            "supportBillValidation":"NOT_SUPPORTED/OPTIONAL/MANDATORY",
            "blrResponseParams":{
               "amountOptions":[
                  {
                     "amountBreakupSet":[
                        "BASE_BILL_AMOUNT"
                     ]
                  }
               ],
               "params":[
                  
               ]
            },
            "blrAdditionalInfo":[
               
            ],
            "billerMode":"ONLINE/OFFLINEA/OFFLINEB"
         },
         {
            "billerId":"<billerId2>",
            "billerName":"<biller Name 2>",
            "customerParams":[
               {
                  "dataType":"ALPHANUMERIC",
                  "optional":false,
                  "paramName":"<param Name>",
                  "minLength":"2",
                  "maxLength":"10",
                  "regex":"<regex for biller>",
                  "values":"< values comma separated supported by a biller customer param>",
                  "requiredIn":"fetch/payment"
               }
            ],
            "isAdhoc":false,
            "fetchOption":"OPTIONAL/MANDATORY/NOT_SUPPORTED",
            "category":"<Name of Category>",
            "region":"<Region Name>",
            "flowType":"BBPS",
            "paymentModesAllowed":[
               {
                  "paymentMode":"Internet Banking",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"Debit Card",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"Credit Card",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"Prepaid Card",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"IMPS",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"Cash",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"UPI",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"Wallet",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"NEFT",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"AEPS",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"Account Transfer",
                  "minLimit":"0.01"
               }
            ],
            "paymentChannelsAllowed":[
               {
                  "paymentMode":"INT",
                  "maxLimit":"0",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"INTB",
                  "maxLimit":"0",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"MOB",
                  "maxLimit":"0",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"MOBB",
                  "maxLimit":"0",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"POS",
                  "maxLimit":"0",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"MPOS",
                  "maxLimit":"0",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"ATM",
                  "maxLimit":"0",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"BNKBRNCH",
                  "maxLimit":"0",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"KIOSK",
                  "maxLimit":"0",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"AGT",
                  "maxLimit":"0",
                  "minLimit":"0.01"
               },
               {
                  "paymentMode":"BSC",
                  "maxLimit":"0",
                  "minLimit":"0.01"
               }
            ],
            "billerOwnerShp":"Private",
            "status":"ACTIVE",
            "billerEffctvFrom":"2020-04-19",
            "billerEffctvTo":null,
            "interchangeFee":[
               {
                  "feeDesc":"Customer_Convenience_Fee",
                  "feeCode":"CCF1",
                  "feeDirection":"C_2_B",
                  "interchangeFeeDetails":[
                     {
                        "effctvTo":"",
                        "tranAmtRangeMax":9223372036854776000,
                        "effctvFrom":"2019-08-01",
                        "percentFee":0,
                        "tranAmtRangeMin":0,
                        "flatFee":0
                     }
                  ]
               },
               {
                  "feeDesc":"Physical_Biller_Fee",
                  "feeCode":"PBF",
                  "feeDirection":"B_2_C",
                  "interchangeFeeDetails":[
                     {
                        "effctvTo":"",
                        "tranAmtRangeMax":9223372036854776000,
                        "effctvFrom":"2019-08-01",
                        "percentFee":0,
                        "tranAmtRangeMin":0,
                        "flatFee":225
                     }
                  ]
               },
               {
                  "feeDesc":"Electronic_Biller_Fee",
                  "feeCode":"EBF",
                  "feeDirection":"B_2_C",
                  "interchangeFeeDetails":[
                     {
                        "effctvTo":"",
                        "tranAmtRangeMax":9223372036854776000,
                        "effctvFrom":"2019-08-01",
                        "percentFee":0,
                        "tranAmtRangeMin":0,
                        "flatFee":225
                     }
                  ]
               }
            ],
            "interchangeFeeConf":[
               {
                  "fees":[
                     "CCF1",
                     "EBF"
                  ],
                  "mti":"PAYMENT",
                  "defaultFee":true,
                  "effctvFrom":"20190801",
                  "responseCode":"000"
               },
               {
                  "fees":[
                     "CCF1",
                     "PBF"
                  ],
                  "mti":"PAYMENT",
                  "defaultFee":false,
                  "effctvFrom":"20190801",
                  "responseCode":"000"
               },
               {
                  "fees":[
                     "CCF1",
                     "PBF"
                  ],
                  "mti":"PAYMENT",
                  "defaultFee":false,
                  "effctvFrom":"20190801",
                  "responseCode":"000"
               },
               {
                  "fees":[
                     "CCF1",
                     "PBF"
                  ],
                  "mti":"PAYMENT",
                  "defaultFee":false,
                  "effctvFrom":"20190801",
                  "responseCode":"000"
               }
            ],
            "supportBillValidation":"NOT_SUPPORTED/MANDATORY/OPTIONAL",
            "blrResponseParams":{
               "amountOptions":[
                  {
                     "amountBreakupSet":[
                        "BASE_BILL_AMOUNT"
                     ]
                  }
               ],
               "params":[
                  
               ]
            },
            "blrAdditionalInfo":[
               
            ],
            "billerMode":"ONLINE/OFFLINEA/OFFLINEB"
         }
      ]
   }
}
```

### Failure scenario

```
{ 
  "code": 600, 
  "status": "FAILURE", 
  "payload": { 
    "errors": [ 
      { 
        "reason": "<error reason>", 
        "errorCode": "<error code>" 
      } 
    ], 
    "refId": null, 
    "type": "biller_info_response", 
    "message": "biller_info_response_failure", 
    "additionalParams": { 
      "Key1": "value1", 
      "Key2": "value2", 
      "Key3": "value3" 
    } 
  } 
} 
```

</details>

## Request parameters