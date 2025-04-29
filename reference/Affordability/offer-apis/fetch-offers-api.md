---
title: Fetch Offers API
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
The **fetch\_offers** API fetches all active (with the **Live** status on Dashboard) offers for this Merchant ID.

> 📘 **Note**:
> 
> If the amount are received in the request, the discount calculation for each offer is also sent as part of the response. If the amount is not received, the response does not contain the discount calculation fields.

**Endpoints**

|                            |                                               |
| -------------------------- | --------------------------------------------- |
| **Test Environment**       | <https://sandbox.payu.in/offers/transactions> |
| **Production Environment** | <https://api.payu.in/offers/transactions>     |

## Request Headers

The request header contains the following fields:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Date  \n**mandatory**",
    "0-1": "The date and time should be in the GMT time conversion(not the IST). For example, current time in India is 18:00:00 IST, the time in the date header should be 12:30:00 GMT.",
    "0-2": "Thu, 17 Feb 2022 08:17:59 GMT",
    "1-0": "Digest  \n**mandatory**",
    "1-1": "Base 64 encode of (sha256 hash of the JSON data (post to server).",
    "1-2": "`vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=`",
    "2-0": "Authorization  \n**mandatory**",
    "2-1": "This field is in the following format:  \n`hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4=\"`  \nWhere the above format includes the following:  \n  \n- **username**: The merchant key of the merchant.\n- **algorithm**: This must have the value as **hmac-sha256** that is used for this API\n- **headers**: This must have the value as **date digest**\n- **signature**: This must contain the hmacsha256 of (signing\\_string, merchant\\_secret), where:\n  - **signing\\_string**: This is in the \"**Date**\"+\"\\\\n\"+\"**Digest**\" format. Here, the Date and Digest is the same values in the fields listed in this table For example, \"Thu, 17 Feb 2022 08:17:59 GMT\"\"\\\\n\"+“vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=“\n  - **merchant\\_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)",
    "2-2": " hmac username=\"smsplus\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI=\"",
    "3-0": "platformId  \n**mandatory**",
    "3-1": "This field contains the platform ID and include the value as **1**.",
    "3-2": "1"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


The following sample Java code contains the logic used to encrypt as described in the above table:

```java
import com.google.gson.Gson;
import com.google.gson.JsonObject;
import org.apache.commons.codec.binary.Base64;
import org.joda.time.DateTime;
import org.joda.time.format.DateTimeFormat;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class HmacAuth {

    public static String getSha256(String input) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] digest = md.digest(input.getBytes());
            return Base64.encodeBase64String(digest);
        } catch (NoSuchAlgorithmException ignored) {}
        return null;
    }

    public static JsonObject getRequestBody(){
        JsonObject requestJson = new JsonObject();
        requestJson.addProperty("firstname","John");
        requestJson.addProperty("lastname","Doe");
        return requestJson;
    }

    public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException {
        String key = "smsplus";
        String secret = "admin";
        Gson gson = new Gson();
        String date = DateTimeFormat.forPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'").withZoneUTC().print(new DateTime());
        System.out.println(date);
        JsonObject requestJson = getRequestBody();
        String digest = getSha256(gson.toJson(requestJson));
        System.out.println(digest);
        String signingString = new StringBuilder()
            .append("date: " + date)
            .append("\ndigest: " + digest).toString();
        Mac sha256_HMAC = Mac.getInstance("HmacSHA256");
        SecretKeySpec secret_key = new SecretKeySpec(secret.getBytes(), "HmacSHA256");
        sha256_HMAC.init(secret_key);
        String signature = Base64.encodeBase64String(sha256_HMAC.doFinal(signingString.getBytes()));
        String authorization = new StringBuilder()
            .append("hmac username=\"")
            .append(key)
            .append("\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"")
            .append(signature)
            .append("\"").toString();
        System.out.println(authorization);
    }
}
```

## Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Amount  \n`optional`",
    "0-1": "`float`The offer transaction amount",
    "0-2": "",
    "1-0": "offerKeys  \n`optional`",
    "1-1": "`String Array`This field contains list of keys to filter the offer in an array format.",
    "1-2": "SummerSpecialOffer2021@q1Bh0jsogwqP",
    "2-0": "paymentId  \n`optional`",
    "2-1": "`Long`Unique reference ID for a transaction which is generated by merchant and sent in the request",
    "2-2": "110",
    "3-0": "userToken  \n`optional`",
    "3-1": "`String Long`This parameter is used to uniquely identify a user for a client/merchant.",
    "3-2": "",
    "4-0": "skusDetail  \n`optional`",
    "4-1": "`String Array`The skusDetail is in an array format and contains the SKU offer details. For more information, refer to",
    "4-2": "",
    "5-0": "autoApply  \n`optional`",
    "5-1": "`Boolean` This parameter must be set to true if the offer is automatically applied.",
    "5-2": "true"
  },
  "cols": 3,
  "rows": 6,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


> 📘 Notes:
> 
> - If you had enable the **Enforce Offer** flag with PayU, the best offer out of the all the offers passed will be applied for the customer. While using this API,  the **autoApply** parameter must be set to true if the offer is automatically applied.
> - All the parameters are optional, but the header is mandatory.

### **skusDetail Parameter Description**

In addition to the request parameters listed in the [Fetch Offers API](ref:fetch-offers-api) section, the **skusDetail** parameter is posted with the following fields are posted in an array:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "skuAmount  \n`optional`",
    "0-1": "`String` The price of one/ single unit of SKU is specified in this field.",
    "1-0": "skuId  \n`mandatory`",
    "1-1": "`String` The product identifier to select offer is specified in this field.",
    "2-0": "quantity   \n`optional`",
    "2-1": "`String` The quantity for the product is specified in this field.",
    "3-0": "offerKeys  \n` optional`",
    "3-1": "`String`The offer keys to filter at SKU-level is specified in this field."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    null,
    null
  ]
}
[/block]


## Sample request and response for a normal transactional offer

### With autoApply=true

**Sample request**

```
{
    "amount": 300,
    "offerKeys": [],
    "paymentId": 12332345,
    "autoApply": true,
    "userToken": "token"
}
```

**Sample response**

```
{
    "code": "200",
    "message": "Offer Retrieved Successfully",
    "status": 1,
    "result": {
        "failureReason": null,
        "clientId": 42693,
        "mid": 180012,
        "amount": 300,
        "couponsAvailable": true,
        "isUserPersonalizedOffersAvailable": true,
        "offers": [
            {
                "failureReason": null,
                "stepSize": null,
                "externalOfferType": null,
                "valid": true,
                "offerKey": "Test@A0RwlqkXSPkK",
                "type": "MERCHANT",
                "title": "Test",
                "description": "Test",
                "tnc": "Test",
                "tncLink": null,
                "minTxnAmount": 100.00,
                "maxTxnAmount": 1000.00,
                "offerType": "INSTANT",
                "minRangeDiscount": null,
                "maxRangeDiscount": null,
                "validFrom": "2024-10-14 00:00:00",
                "validTo": "2024-10-15 23:59:59",
                "discountDetail": {
                    "discountType": "ABSOLUTE",
                    "discountPercentage": null,
                    "discount": 100.00,
                    "discountedAmount": 200.00,
                    "maxDiscount": 100.00
                },
                "isNoCostEmi": false,
                "isSubvented": false,
                "isSkuOffer": false,
                "creditCard": [
                    {
                        "networks": [],
                        "banks": [
                            {
                                "code": "AIRP",
                                "title": "Airtel Payments bank"
                            }
                        ],
                        "title": null,
                        "paymentCode": null,
                        "handle": null
                    }
                ],
                "debitCard": [
                    {
                        "networks": [
                            {
                                "code": "AMEX",
                                "title": "Amex CreditCard"
                            }
                        ],
                        "banks": [],
                        "title": null,
                        "paymentCode": null,
                        "handle": null
                    }
                ],
                "netBanking": [
                    {
                        "title": "Kotak Mahindra Bank",
                        "paymentCode": "162B",
                        "handle": null
                    }
                ],
                "wallet": [
                    {
                        "title": "Amazon Pay",
                        "paymentCode": "AMZPAY",
                        "handle": null
                    }
                ],
                "clw": null,
                "upi": [
                    {
                        "title": "SamsungPay",
                        "paymentCode": "SamsungPay",
                        "handle": [
                            "pingpay"
                        ]
                    }
                ],
                "emi": {
                    "debitCard": {
                        "banks": [
                            {
                                "bankCode": "UTIB",
                                "bankName": "Axis Debit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "AXISD09",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    }
                                ]
                            }
                        ]
                    },
                    "creditCard": {
                        "banks": [
                            {
                                "bankCode": "AUSF",
                                "bankName": "AU Small Finance Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "AUSF03",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    }
                                ]
                            }
                        ]
                    },
                    "cardLess": {
                        "banks": [
                            {
                                "bankCode": "HDFC_CL",
                                "bankName": "Hdfc Card Less ",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 months",
                                        "paymentCode": "HDFCCL18",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    }
                                ]
                            }
                        ]
                    },
                    "other": {
                        "banks": [
                            {
                                "bankCode": "BAJFIN",
                                "bankName": "Bajaj Finance Card Less ",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 months",
                                        "paymentCode": "BAJFIN09",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    }
                                ]
                            }
                        ]
                    }
                },
                "bnpl": [
                    {
                        "title": "LazyPay",
                        "paymentCode": "LAZYPAY",
                        "handle": null,
                        "tenureOption": null
                    },
                    {
                        "title": "HDFC Bank FlexiPay",
                        "paymentCode": "HDFCF",
                        "handle": null,
                        "tenureOption": [
                            {
                                "title": "HDFC Bank FlexiPay - 15 Days",
                                "paymentCode": "HDFCF15",
                                "handle": null
                            }
                        ]
                    }
                ],
                "skuDetail": null,
                "isAcrossSkuQuantity": false,
                "offerCategory": null,
                "isBaseOffer": false,
                "recordType": "OFFER",
                "toDisplay": true,
                "disallowTransactionInvalidOffer": false,
                "isAllPaymentMethodsAvailable": false,
                "isCohortOffer": false,
                "isGstSubvented": false,
                "isExternalOffer": false,
                "issuerId": null,
                "issuerName": null,
                "isNudgeOnlyOffer": false
            }
        ],
        "skusDetail": null,
        "flagToFail": false,
        "isSkuOffer": false
    },
    "traceId": "1efe4312-d59c-4706-978c-2180a5c2e956"
}
```

### With autoApply=false

**Sample request **

```
{
    "amount": 300,
    "autoApply": false,
    "offerKeys": [
        "TestOffer@fY6HdoP7da8L"
    ]
}
```

**Sample response**

```
{
    "code": "200",
    "message": "Offer Retrieved Successfully",
    "status": 1,
    "result": {
        "failureReason": null,
        "clientId": 42693,
        "mid": 180012,
        "amount": 300,
        "couponsAvailable": true,
        "isUserPersonalizedOffersAvailable": false,
        "offers": [
            {
                "failureReason": null,
                "stepSize": null,
                "externalOfferType": null,
                "recordSubType": null,
                "valid": true,
                "offerKey": "TestOffer@fY6HdoP7da8L",
                "type": "MERCHANT",
                "title": "TestOffer",
                "description": "offer",
                "tnc": "tnc",
                "tncLink": null,
                "minTxnAmount": 101.00,
                "maxTxnAmount": 111111.00,
                "offerType": "INSTANT",
                "minRangeDiscount": null,
                "maxRangeDiscount": null,
                "validFrom": "2024-10-14 00:00:00",
                "validTo": "2024-11-30 23:59:00",
                "discountDetail": {
                    "discountType": "ABSOLUTE",
                    "discountPercentage": null,
                    "discount": 100.00,
                    "discountedAmount": 200.00,
                    "maxDiscount": 100.00
                },
                "isNoCostEmi": false,
                "isSubvented": false,
                "isSkuOffer": false,
                "creditCard": null,
                "debitCard": null,
                "netBanking": null,
                "wallet": null,
                "clw": null,
                "upi": null,
                "emi": null,
                "bnpl": null,
                "skuDetail": null,
                "isAcrossSkuQuantity": false,
                "offerCategory": null,
                "isBaseOffer": false,
                "recordType": "OFFER",
                "toDisplay": true,
                "disallowTransactionInvalidOffer": false,
                "isAllPaymentMethodsAvailable": true,
                "isCohortOffer": false,
                "isGstSubvented": false,
                "isExternalOffer": false,
                "issuerId": null,
                "issuerName": null,
                "isNudgeOnlyOffer": false,
                "offerMilestone": null,
                "userMilestone": null,
                "userDetail": null,
                "isUserVerificationRequired": false,
                "isPersonalisedUniqueCoupon": false
            }
        ],
        "skusDetail": null,
        "flagToFail": false,
        "isSkuOffer": false,
        "paymentId": null
    },
    "traceId": "4c6603a3-3fed-4a13-a44d-7e59e3df11d3"
}
```

### Failure scenarios

- Merchant ID does not exists

Merchant ID does not exists

```plaintext
{
    "code": "404",
    "message": "Merchant with merchant Id :1800122 does not exists",
    "status": 0,
    "exceptionId": "9cf201ab-2ad3-439e-a7a6-f707d2f76e48"
}
```

- The platform for client mismatch or does not exists

```plaintext
{
    "code": "404",
    "message": "client with clientId :4 , platformId :12 does not exists.",
    "status": 0,
    "exceptionId": "6985749b-9de4-4d39-9242-d19d35a82d0c"
}
```

- Service unavailable

```plaintext
{
    "code": "500",
    "message": "Service Unavailable",
    "status": 0,
    "exceptionId": "65466805-5be1-4fa4-912d-d28cf620d687"
}
```

- Invalid request

```
{
    "code": "400",
    "message": "Invalid Request",
    "status": 0,
    "exceptionId": "252e1602-2a9a-449a-8f17-f55fe1f0949a"
}
```

## Sample request and response for a SKU-based offer

### With autoApply=true

Sample request

```curl
{
    "amount": 300,
    "autoApply": true,
    "paymentId": 12332345,
    "userToken": "token"
    "skusDetail": [
        {
            "skuAmount": 300,
            "quantity": 1,
            "skuId": "sampleProductId",
            "offerKeys": []
        }
    ]
}
```

#### Sample response

```
{
    "code": "200",
    "message": "Offer Retrieved Successfully",
    "status": 1,
    "result": {
        "failureReason": null,
        "clientId": 42693,
        "mid": 180012,
        "amount": 300,
        "couponsAvailable": true,
        "isUserPersonalizedOffersAvailable": false,
        "offers": [
            {
                "failureReason": null,
                "stepSize": null,
                "externalOfferType": null,
                "recordSubType": null,
                "valid": true,
                "offerKey": "TestOffer@fY6HdoP7da8L",
                "type": "MERCHANT",
                "title": "TestOffer",
                "description": "offer",
                "tnc": "tnc",
                "tncLink": null,
                "minTxnAmount": 101.00,
                "maxTxnAmount": 111111.00,
                "offerType": "INSTANT",
                "minRangeDiscount": null,
                "maxRangeDiscount": null,
                "validFrom": "2024-10-14 00:00:00",
                "validTo": "2024-11-30 23:59:00",
                "discountDetail": {
                    "discountType": "ABSOLUTE",
                    "discountPercentage": null,
                    "discount": 100.00,
                    "discountedAmount": 200.00,
                    "maxDiscount": 100.00
                },
                "isNoCostEmi": false,
                "isSubvented": false,
                "isSkuOffer": false,
                "creditCard": null,
                "debitCard": null,
                "netBanking": null,
                "wallet": null,
                "clw": null,
                "upi": null,
                "emi": null,
                "bnpl": null,
                "skuDetail": null,
                "isAcrossSkuQuantity": false,
                "offerCategory": null,
                "isBaseOffer": false,
                "recordType": "OFFER",
                "toDisplay": true,
                "disallowTransactionInvalidOffer": false,
                "isAllPaymentMethodsAvailable": true,
                "isCohortOffer": false,
                "isGstSubvented": false,
                "isExternalOffer": false,
                "issuerId": null,
                "issuerName": null,
                "isNudgeOnlyOffer": false,
                "offerMilestone": null,
                "userMilestone": null,
                "userDetail": null,
                "isUserVerificationRequired": false,
                "isPersonalisedUniqueCoupon": false
            }
        ],
        "skusDetail": {
            "skus": [
                {
                    "skuId": "sampleProductId",
                    "skuCategory": null,
                    "quantity": 1,
                    "skuAmount": 300,
                    "offers": [
                        {
                            "failureReason": null,
                            "stepSize": null,
                            "externalOfferType": null,
                            "recordSubType": null,
                            "valid": true,
                            "offerKey": "hellosku@rFTxczzbDmj6",
                            "type": "MERCHANT",
                            "title": "hello sku",
                            "description": "qwe4",
                            "tnc": "123e",
                            "tncLink": null,
                            "minTxnAmount": 11.00,
                            "maxTxnAmount": 1000000.00,
                            "offerType": "INSTANT",
                            "minRangeDiscount": null,
                            "maxRangeDiscount": null,
                            "validFrom": "2024-10-15 00:00:00",
                            "validTo": "2024-10-16 23:59:59",
                            "discountDetail": {
                                "discountType": "ABSOLUTE",
                                "discountPercentage": null,
                                "discount": 10.00,
                                "discountedAmount": 290.00,
                                "maxDiscount": 10.00
                            },
                            "isNoCostEmi": false,
                            "isSubvented": false,
                            "isSkuOffer": true,
                            "creditCard": null,
                            "debitCard": null,
                            "netBanking": null,
                            "wallet": null,
                            "clw": null,
                            "upi": null,
                            "emi": null,
                            "bnpl": null,
                            "skuDetail": {
                                "skuId": "sampleProductId",
                                "skuCategory": null,
                                "skuName": "sampleProductName",
                                "minQuantity": 1,
                                "maxQuantity": 5,
                                "minAmount": 10.00,
                                "maxAmount": 100000.00,
                                "quantity": 1,
                                "skuAmount": 300
                            },
                            "isAcrossSkuQuantity": false,
                            "offerCategory": null,
                            "isBaseOffer": false,
                            "recordType": "OFFER",
                            "toDisplay": true,
                            "disallowTransactionInvalidOffer": false,
                            "isAllPaymentMethodsAvailable": true,
                            "isCohortOffer": false,
                            "isGstSubvented": false,
                            "isExternalOffer": false,
                            "issuerId": null,
                            "issuerName": null,
                            "isNudgeOnlyOffer": false,
                            "offerMilestone": null,
                            "userMilestone": null,
                            "userDetail": null,
                            "isUserVerificationRequired": false,
                            "isPersonalisedUniqueCoupon": false
                        }
                    ]
                }
            ]
        },
        "flagToFail": false,
        "isSkuOffer": false,
        "paymentId": null
    },
    "traceId": "1b565184-43dc-4be3-9e61-c6f8b324f476"
}
```

### With autoApply=false

**Sample request**

```
{
    "amount": 300,
    "autoApply": false,
    "skusDetail": [
        {
            "skuAmount": 300,
            "quantity": 1,
            "skuId": "sampleProductId",
            "offerKeys": ["hellosku@rFTxczzbDmj6"]
        }
    ]
}
```

**Sample response**

```
{
    "code": "200",
    "message": "Offer Retrieved Successfully",
    "status": 1,
    "result": {
        "failureReason": null,
        "clientId": 42693,
        "mid": 180012,
        "amount": 300,
        "couponsAvailable": true,
        "isUserPersonalizedOffersAvailable": false,
        "offers": [
            {
                "failureReason": null,
                "stepSize": null,
                "externalOfferType": null,
                "recordSubType": null,
                "valid": true,
                "offerKey": "TestOffer@fY6HdoP7da8L",
                "type": "MERCHANT",
                "title": "TestOffer",
                "description": "offer",
                "tnc": "tnc",
                "tncLink": null,
                "minTxnAmount": 101.00,
                "maxTxnAmount": 111111.00,
                "offerType": "INSTANT",
                "minRangeDiscount": null,
                "maxRangeDiscount": null,
                "validFrom": "2024-10-14 00:00:00",
                "validTo": "2024-11-30 23:59:00",
                "discountDetail": {
                    "discountType": "ABSOLUTE",
                    "discountPercentage": null,
                    "discount": 100.00,
                    "discountedAmount": 200.00,
                    "maxDiscount": 100.00
                },
                "isNoCostEmi": false,
                "isSubvented": false,
                "isSkuOffer": false,
                "creditCard": null,
                "debitCard": null,
                "netBanking": null,
                "wallet": null,
                "clw": null,
                "upi": null,
                "emi": null,
                "bnpl": null,
                "skuDetail": null,
                "isAcrossSkuQuantity": false,
                "offerCategory": null,
                "isBaseOffer": false,
                "recordType": "OFFER",
                "toDisplay": true,
                "disallowTransactionInvalidOffer": false,
                "isAllPaymentMethodsAvailable": true,
                "isCohortOffer": false,
                "isGstSubvented": false,
                "isExternalOffer": false,
                "issuerId": null,
                "issuerName": null,
                "isNudgeOnlyOffer": false,
                "offerMilestone": null,
                "userMilestone": null,
                "userDetail": null,
                "isUserVerificationRequired": false,
                "isPersonalisedUniqueCoupon": false
            }
        ],
        "skusDetail": {
            "skus": [
                {
                    "skuId": "sampleProductId",
                    "skuCategory": null,
                    "quantity": 1,
                    "skuAmount": 300,
                    "offers": [
                        {
                            "failureReason": null,
                            "stepSize": null,
                            "externalOfferType": null,
                            "recordSubType": null,
                            "valid": true,
                            "offerKey": "hellosku@rFTxczzbDmj6",
                            "type": "MERCHANT",
                            "title": "hello sku",
                            "description": "qwe4",
                            "tnc": "123e",
                            "tncLink": null,
                            "minTxnAmount": 11.00,
                            "maxTxnAmount": 1000000.00,
                            "offerType": "INSTANT",
                            "minRangeDiscount": null,
                            "maxRangeDiscount": null,
                            "validFrom": "2024-10-15 00:00:00",
                            "validTo": "2024-10-16 23:59:59",
                            "discountDetail": {
                                "discountType": "ABSOLUTE",
                                "discountPercentage": null,
                                "discount": 10.00,
                                "discountedAmount": 290.00,
                                "maxDiscount": 10.00
                            },
                            "isNoCostEmi": false,
                            "isSubvented": false,
                            "isSkuOffer": true,
                            "creditCard": null,
                            "debitCard": null,
                            "netBanking": null,
                            "wallet": null,
                            "clw": null,
                            "upi": null,
                            "emi": null,
                            "bnpl": null,
                            "skuDetail": {
                                "skuId": "sampleProductId",
                                "skuCategory": null,
                                "skuName": "sampleProductName",
                                "minQuantity": 1,
                                "maxQuantity": 5,
                                "minAmount": 10.00,
                                "maxAmount": 100000.00,
                                "quantity": 1,
                                "skuAmount": 300
                            },
                            "isAcrossSkuQuantity": false,
                            "offerCategory": null,
                            "isBaseOffer": false,
                            "recordType": "OFFER",
                            "toDisplay": true,
                            "disallowTransactionInvalidOffer": false,
                            "isAllPaymentMethodsAvailable": true,
                            "isCohortOffer": false,
                            "isGstSubvented": false,
                            "isExternalOffer": false,
                            "issuerId": null,
                            "issuerName": null,
                            "isNudgeOnlyOffer": false,
                            "offerMilestone": null,
                            "userMilestone": null,
                            "userDetail": null,
                            "isUserVerificationRequired": false,
                            "isPersonalisedUniqueCoupon": false
                        }
                    ]
                }
            ]
        },
        "flagToFail": false,
        "isSkuOffer": false,
        "paymentId": null
    },
    "traceId": "131b13ad-4655-437e-82cd-0db2908c379d"
}
```

### Failure scenarios

- Merchant ID does not exists

Merchant ID does not exists

```plaintext
{
    "code": "404",
    "message": "Merchant with merchant Id :1800122 does not exists",
    "status": 0,
    "exceptionId": "9cf201ab-2ad3-439e-a7a6-f707d2f76e48"
}
```

- The platform for client mismatch or does not exists

```plaintext
{
    "code": "404",
    "message": "client with clientId :4 , platformId :12 does not exists.",
    "status": 0,
    "exceptionId": "6985749b-9de4-4d39-9242-d19d35a82d0c"
}
```

- Service unavailable

```plaintext
{
    "code": "500",
    "message": "Service Unavailable",
    "status": 0,
    "exceptionId": "65466805-5be1-4fa4-912d-d28cf620d687"
}
```

- Invalid request

```
{
    "code": "400",
    "message": "Invalid Request",
    "status": 0,
    "exceptionId": "252e1602-2a9a-449a-8f17-f55fe1f0949a"
}
```

- Offer key is mandatory when autoApply=false

```
{
    "code": "400",
    "message": "Offer key is mandatory when offer is not auto applied",
    "status": 0,
    "exceptionId": "0e2012e76b4347f48d58808bf3c39122",
    "traceId": "4baa1329-b3c5-479c-b98e-b3f2a99f0158"
}
```

## Response Parameters

The response involves the following parameters and the **result** parameter contains the offer results:

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "code",
    "0-1": "This parameter returns the HTTP status code based on .",
    "0-2": "200",
    "1-0": "message",
    "1-1": "`String` This parameter is the result message which contains information about the result",
    "1-2": "Offer Validated Successfull",
    "2-0": "status",
    "2-1": "This parameter returns the status of web service call. The status can be any of the following:  \n  \n- 0 - If web service call failed.\n- 1 - If web service call succeeded",
    "2-2": "1",
    "3-0": "result",
    "3-1": "`JSON Object` This parameter gives the information about the result of the API response in a JSON format. For more information, refer to the [result Parameter JSON Details](#result-parameter-json-details) subsection.",
    "3-2": "Refer to the [result Field JSON Details](#result-parameter-json-details) subsection."
  },
  "cols": 3,
  "rows": 4,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### result Parameter JSON Details

The **result** parameter contains the result in a JSON format and the fields in the JSON are described in the following table. The **offers** field in this JSON contains the offer details as described in the following table:

| **Field**                         | **Description**                                                                                                                                                                           | **Example**                                                                      |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| failureReason                     | `String` This field contains reason for offer failure.                                                                                                                                    |                                                                                  |
| clientId                          | `Integer` This field contains reference of the merchant.                                                                                                                                  | 5861                                                                             |
| mid                               | `Integer`This field contains the unique identifier provided by PayU to each merchant.                                                                                                     | 1                                                                                |
| amount                            | `Float` This field contains the Offer transaction amount                                                                                                                                  | 15000                                                                            |
| couponsAvailable                  | `Boolean` This field contains the flag to indicate whether the coupons are available.                                                                                                     | true                                                                             |
| isUserPersonalizedOffersAvailable | `Boolean` This field contains the flag to indicate whether the personalized offers available.                                                                                             | false                                                                            |
| offers                            | `JSON Object` This field contains the list of offer with details in a JSON format. For more information, refer to the [offers Field JSON Details](#offers-field-json-details) subsection. | Refer to the [offers Field JSON Details](#offers-field-json-details) subsection. |

The sample value for the **result** parameter in a JSON format is similar to the following:

```plaintext
{
    "code": "200",
    "message": "Offer Retrieved Successfully",
    "status": 1,
    "result": {
        "failureReason": null,
        "clientId": 42693,
        "mid": 180012,
        "amount": 300,
        "couponsAvailable": true,
        "isUserPersonalizedOffersAvailable": false,
        "offers": [
            {
                "failureReason": null,
                "stepSize": null,
                "externalOfferType": null,
                "recordSubType": null,
                "valid": true,
                "offerKey": "TestOffer@fY6HdoP7da8L",
                "type": "MERCHANT",
                "title": "TestOffer",
                "description": "offer",
                "tnc": "tnc",
                "tncLink": null,
                "minTxnAmount": 101.00,
                "maxTxnAmount": 111111.00,
                "offerType": "INSTANT",
                "minRangeDiscount": null,
                "maxRangeDiscount": null,
                "validFrom": "2024-10-14 00:00:00",
                "validTo": "2024-11-30 23:59:00",
                "discountDetail": {
                    "discountType": "ABSOLUTE",
                    "discountPercentage": null,
                    "discount": 100.00,
                    "discountedAmount": 200.00,
                    "maxDiscount": 100.00
                },
                "isNoCostEmi": false,
                "isSubvented": false,
                "isSkuOffer": false,
                "creditCard": null,
                "debitCard": null,
                "netBanking": null,
                "wallet": null,
                "clw": null,
                "upi": null,
                "emi": null,
                "bnpl": null,
                "skuDetail": null,
                "isAcrossSkuQuantity": false,
                "offerCategory": null,
                "isBaseOffer": false,
                "recordType": "OFFER",
                "toDisplay": true,
                "disallowTransactionInvalidOffer": false,
                "isAllPaymentMethodsAvailable": true,
                "isCohortOffer": false,
                "isGstSubvented": false,
                "isExternalOffer": false,
                "issuerId": null,
                "issuerName": null,
                "isNudgeOnlyOffer": false,
                "offerMilestone": null,
                "userMilestone": null,
                "userDetail": null,
                "isUserVerificationRequired": false,
                "isPersonalisedUniqueCoupon": false
            }
        ],
        "skusDetail": {
            "skus": [
                {
                    "skuId": "sampleProductId",
                    "skuCategory": null,
                    "quantity": 1,
                    "skuAmount": 300,
                    "offers": [
                        {
                            "failureReason": null,
                            "stepSize": null,
                            "externalOfferType": null,
                            "recordSubType": null,
                            "valid": true,
                            "offerKey": "hellosku@rFTxczzbDmj6",
                            "type": "MERCHANT",
                            "title": "hello sku",
                            "description": "qwe4",
                            "tnc": "123e",
                            "tncLink": null,
                            "minTxnAmount": 11.00,
                            "maxTxnAmount": 1000000.00,
                            "offerType": "INSTANT",
                            "minRangeDiscount": null,
                            "maxRangeDiscount": null,
                            "validFrom": "2024-10-15 00:00:00",
                            "validTo": "2024-10-16 23:59:59",
                            "discountDetail": {
                                "discountType": "ABSOLUTE",
                                "discountPercentage": null,
                                "discount": 10.00,
                                "discountedAmount": 290.00,
                                "maxDiscount": 10.00
                            },
                            "isNoCostEmi": false,
                            "isSubvented": false,
                            "isSkuOffer": true,
                            "creditCard": null,
                            "debitCard": null,
                            "netBanking": null,
                            "wallet": null,
                            "clw": null,
                            "upi": null,
                            "emi": null,
                            "bnpl": null,
                            "skuDetail": {
                                "skuId": "sampleProductId",
                                "skuCategory": null,
                                "skuName": "sampleProductName",
                                "minQuantity": 1,
                                "maxQuantity": 5,
                                "minAmount": 10.00,
                                "maxAmount": 100000.00,
                                "quantity": 1,
                                "skuAmount": 300
                            },
                            "isAcrossSkuQuantity": false,
                            "offerCategory": null,
                            "isBaseOffer": false,
                            "recordType": "OFFER",
                            "toDisplay": true,
                            "disallowTransactionInvalidOffer": false,
                            "isAllPaymentMethodsAvailable": true,
                            "isCohortOffer": false,
                            "isGstSubvented": false,
                            "isExternalOffer": false,
                            "issuerId": null,
                            "issuerName": null,
                            "isNudgeOnlyOffer": false,
                            "offerMilestone": null,
                            "userMilestone": null,
                            "userDetail": null,
                            "isUserVerificationRequired": false,
                            "isPersonalisedUniqueCoupon": false
                        }
                    ]
                }
            ]
        },
        "flagToFail": false,
        "isSkuOffer": false,
        "paymentId": null
    },
    "traceId": "131b13ad-4655-437e-82cd-0db2908c379d"
}
```

#### offers Field JSON Details

The **offers** field in the **result** JSON contains the offer details and details for each payment mode in a JSON format as described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "failureReason",
    "0-1": "`String` This field contains reason for offer failure.",
    "0-2": "",
    "1-0": "stepSize",
    "1-1": "`String` This field contains step size.",
    "1-2": "",
    "2-0": "externalOfferType",
    "2-1": "`String` This field contains the external offer type.",
    "2-2": "",
    "3-0": "recordSubType",
    "3-1": "`String` This field contains the record sub-type.",
    "3-2": "",
    "4-0": "valid",
    "4-1": "`String `This field contains flag whether the is valid.",
    "4-2": "",
    "5-0": "offerKey",
    "5-1": "`String` This field contains the unique identifier for a particular offer.",
    "5-2": "SummerSpecialOffer2021@q1Bh0jsogwqP",
    "6-0": "type",
    "6-1": "`String` This field contains the offer owner.",
    "6-2": "MERCHANT",
    "7-0": "title",
    "7-1": "`String` This field contains the title of the offer that will be displayed for customers.",
    "7-2": "festive\\_500",
    "8-0": "description",
    "8-1": "`String` This field contains the description of offer for the merchant's reference.",
    "8-2": "festive discount",
    "9-0": "tnc",
    "9-1": "`String` This field contains the Terms & Conditions for applying promo that will be displayed to customers while accessing the link provided in the **tncLink** field.",
    "9-2": "abc",
    "10-0": "tncLink",
    "10-1": "`String` This field contains URL to fetch details on Terms & Conditions and details specified in the **tnc** is displayed.",
    "10-2": "abcd",
    "11-0": "minTxnAmount",
    "11-1": "`Float` The field contains the minimum transaction amount offer will be applicable.",
    "11-2": "10.00",
    "12-0": "maxTxnAmount",
    "12-1": "`Float` The field contains the maximum transaction amount offer will be applicable",
    "12-2": "25000.00",
    "13-0": "offerType",
    "13-1": "`String` The field contains any of the following type of offer:  \n  \n- INSTANT \n- CASHBACK",
    "13-2": "INSTANT",
    "14-0": "validFrom",
    "14-1": "`String` The field contains the offer start time.",
    "14-2": "2021-07-01 17:02:11",
    "15-0": "validTo",
    "15-1": "`String` The field contains the offer end time.",
    "15-2": "2022-08-05 15:53:16",
    "16-0": "discountDetail",
    "16-1": "`JSON Object` This field contains the discount detail of the offer in a JSON format. This field contain the following fields in a JSON format:  \n  \n- **discountType**: This field contains any of the following discount type that was defined:\n  - ABSOLUTE \n  - PERCENTAGE\n- **discountPercentage**: This field contains the define the discount percentage.\n- **discount**: This field contains the total discount available on the transaction once applied the specific offer.\n- **discountedAmount**: This field contains the final Net amount of the transaction after applying the specific offer.\n- **maxDiscount**: The field contains the max discount available on an offer.",
    "16-2": " ",
    "17-0": "isNoCostEmi",
    "17-1": "`Boolean`This field contains any of the following values to specify whether th_e offer is no cost EMI offer or normal offer.",
    "17-2": "true",
    "18-0": "creditCard",
    "18-1": "`JSON Object` The field contains the offer configuration details for credit card with the fields in a JSON format:  \n  \n- **networks**: The list of card networks for which the offer is supported similar to the example.\n- **banks**: The list of banks with codes supported are listed similar to the example.\n- **title**: This parameter contains the payment title that is used to identify the particular payment option.\n- **paymentCode**: the payment code that is used to identify the particular payment option.\n- **discountDetail**: The discount detail an array format as in the example.",
    "18-2": "networks:  \n{  \n\"code\": \"MAST\",  \n\"title\": \"Master Network\"  \n},  \n{  \n\"code\": \"VISA\",  \n\"title\": \"VIsa Network\"  \n}  \nbanks:  \n{  \n\"code\": \"ICICI\",  \n\"title\": \"ICICI credit card\"  \n},  \n{  \n\"code\": \"HDFC\",  \n\"title\": \"HDFC credit card\"  \n}",
    "19-0": "debitCard",
    "19-1": "`JSON Object`The field contains the offer configuration details for debit card in a JSON format with the following fields:  \n  \n- **networks**: The list of card networks for which the offer is supported similar to the example.\n- **banks**: The list of banks with codes supported are listed similar to the example.\n- **title**: This parameter contains the payment title that is used to identify the particular payment option.\n- **paymentCode**: the payment code that is used to identify the particular payment option.",
    "19-2": "networks:  \n{  \n\"code\": \"MAST\",  \n\"title\": \"Master Network\"  \n},  \n{  \n\"code\": \"VISA\",  \n\"title\": \"Visa Network\"  \n}  \n  \nbanks:  \n{  \n\"code\": \"ICICI\",  \n\"title\": \"ICICI debit card\"  \n},  \n{  \n\"code\": \"HDFC\",  \n\"title\": \"HDFC debit card\"  \n}",
    "20-0": "netBanking",
    "20-1": "`JSON Object` The field contains the offer configuration details for NetBanking in JSON format similar to the example.",
    "20-2": "{  \n\"title\": \"axis bank\",  \n\"paymentCode\": \"AXIB1\"  \n},  \n{  \n\"title\": \"Bank of India\",  \n\"paymentCode\": \"BOIB\"  \n},  \n{  \n\"title\": \"Canara Bank\",  \n\"paymentCode\": \"CABB\"  \n}  \n} ",
    "21-0": "wallet",
    "21-1": "`JSON Object`The field contains the offer configuration details for Wallet in a JSON format similar to the example.",
    "21-2": "{  \n\"title\": \"freecharge\",  \n\"paymentCode\": \"FREC\"  \n} ",
    "22-0": "upi",
    "22-1": "`JSON Object`The field contains the offer configuration details for UPI in JSON format similar to the example.",
    "22-2": " {  \n\"title\": \"upi\",  \n\"paymentCode\": \"UPI\"  \n}",
    "23-0": "emi",
    "23-1": "`JSON Object` The field contains the offer configuration details for EMI in a JSON format with the following fields:  \n  \n- **debitCard**: Contains the list of banks and tenure option similar to the example.\n- **creditCard**: Contains the list of banks and tenure option similar to the example.",
    "23-2": "DebitCard:  \n{  \n\"banks\": \\[  \n{  \n\"bankCode\": \"CITI\",  \n\"tenureOption\": [  \n{  \n\"title\": \"CITI Bank 3EMI\",  \n\"paymentCode\": \"EMI03\",  \n\"discountDetail\": null  \n},  \n{  \n\"title\": \"CITI Bank 6 EMI\",  \n\"paymentCode\": \"EMI06\",  \n\"discountDetail\": null  \n}  \n]  \n},  \n{  \n\"bankCode\": \"AXIS\",  \n\"tenureOption\": [  \n{  \n\"title\": \"AXIS Bank 3 EMI\",  \n\"paymentCode\": \"EMI3\",  \n\"discountDetail\": null  \n}  \n]  \n}  \n]  \n}  \n  \ncreditCard:  \n{  \n\"banks\": \\[  \n{  \n\"bankCode\": \"CITI\",  \n\"tenureOption\": [  \n{  \n\"title\": \"CITI Bank 9 EMI\",  \n\"paymentCode\": \"EMI09\",  \n\"discountDetail\": null  \n}  \n]  \n},  \n{  \n\"bankCode\": \"AXIS\",  \n\"tenureOption\": [  \n{  \n\"title\": \"AXIS Bank 12 EMI\",  \n\"paymentCode\": \"EMI12\",  \n\"discountDetail\": null  \n}  \n]  \n}  \n]  \n}  \n}"
  },
  "cols": 3,
  "rows": 24,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


The sample value for **offers** field in a JSON is similar to the following:

```plaintext
"offers": [
            {
                "offerKey": "SummerSpecialOffer2021@q1Bh0jsogwqP",
                "type": "MERCHANT",
                "title": "festive_500",
                "description": "festive discount",
                "tnc": "abc",
                "tncLink": "abcd",
                "minTxnAmount": 10.00,
                "maxTxnAmount": 25000.00,
                "offerType": "INSTANT",
                "validFrom": "2021-07-01 17:02:11",
                "validTo": "2022-08-05 15:53:16",
                "discountDetail": {
                    "discountType": "PERCENTAGE",
                    "discountPercentage": 10.00,
                    "discount": 100.00,
                    "discountedAmount": 14900,
                    "maxDiscount": 100.00
                },
                "isNoCostEmi": false,
                "creditCard": [
                    {
                        "networks": [
                            {
                                "code": "MAST",
                                "title": "Master Network"
                            },
                            {
                                "code": "VISA",
                                "title": "VIsa Network"
                            }
                        ],
                        "banks": [
                            {
                                "code": "ICICI",
                                "title": "ICICI debit card"
                            },
                            {
                                "code": "HDFC",
                                "title": "HDFC debit card"
                            }
                        ],
                        "title": null,
                        "paymentCode": null
                    }
                ],
                "debitCard": [
                    {
                        "networks": [
                            {
                                "code": "MAST",
                                "title": "Master Network"
                            }
                        ],
                        "banks": [
                            {
                                "code": "HDFC",
                                "title": "HDFC debit card"
                            }
                        ],
                        "title": null,
                        "paymentCode": null
                    }
                ],
                "netBanking": [
                    {
                        "title": "axis bank",
                        "paymentCode": "AXIB1"
                    },
                    {
                        "title": "Bank of India",
                        "paymentCode": "BOIB"
                    },
                    {
                        "title": "Canara Bank",
                        "paymentCode": "CABB"
                    }
                ],
                "wallet": [
                    {
                        "title": "freecharge",
                        "paymentCode": "FREC"
                    }
                ],
                "upi": [
                    {
                        "title": "upi",
                        "paymentCode": "UPI"
                    }
                ],
                "emi": {
                    "debitCard": {
                        "banks": [
                            {
                                "bankCode": "CITI",
                                "tenureOption": [
                                    {
                                        "title": "CITI Bank 3EMI",
                                        "paymentCode": "EMI03",
                                        "discountDetail": null
                                    },
                                    {
                                        "title": "CITI Bank 6 EMI",
                                        "paymentCode": "EMI06",
                                        "discountDetail": null
                                    }
                                ]
                            },
                            {
                                "bankCode": "AXIS",
                                "tenureOption": [
                                    {
                                        "title": "AXIS Bank 3 EMI",
                                        "paymentCode": "EMI3",
                                        "discountDetail": null
                                    }
                                ]
                            }
                        ]
                    },
                    "creditCard": {
                        "banks": [
                            {
                                "bankCode": "CITI",
                                "tenureOption": [
                                    {
                                        "title": "CITI Bank  9 EMI",
                                        "paymentCode": "EMI09",
                                        "discountDetail": null
                                    }
                                ]
                            },
                            {
                                "bankCode": "AXIS",
                                "tenureOption": [
                                    {
                                        "title": "AXIS Bank 12 EMI",
                                        "paymentCode": "EMI12",
                                        "discountDetail": null
                                    }
                                ]
                            }
                        ]
                    }
                }
            },
            {
                "offerKey": "SummerSpecialOffer2021@oi7gMfLOobVZ",
                "type": "MERCHANT",
                "title": "Summer Special Offer 2021",
                "description": "20% Instant discount",
                "tnc": "Discount will be applied instantly after applying coupon code",
                "tncLink": "www.icicibank/offer/t&c",
                "minTxnAmount": 500.00,
                "maxTxnAmount": 100000.00,
                "offerType": "CASHBACK",
                "validFrom": "2020-12-31 15:53:16",
                "validTo": "2022-02-28 15:53:16",
                "discountDetail": null,
                "isNoCostEmi": true,
                "creditCard": null,
                "debitCard": null,
                "netBanking": null,
                "wallet": null,
                "upi": null,
                "emi": {
                    "debitCard": {
                        "banks": [
                            {
                                "bankCode": "CITI",
                                "tenureOption": [
                                    {
                                        "title": "CITI Bank 6 EMI",
                                        "paymentCode": "EMI06",
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 835.12,
                                            "discountedAmount": 15000
                                        }
                                    },
                                    {
                                        "title": "CITI Bank 3EMI",
                                        "paymentCode": "EMI03",
                                        "discountDetail": {
                                            "discountPercentage": 15.0,
                                            "discount": 444.33,
                                            "discountedAmount": 15000
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    "creditCard": {
                        "banks": [
                            {
                                "bankCode": "AXIS",
                                "tenureOption": [
                                    {
                                        "title": "AXIS Bank 12 EMI",
                                        "paymentCode": "EMI12",
                                        "discountDetail": {
                                            "discountPercentage": 14.5,
                                            "discount": 1420.79,
                                            "discountedAmount": 15000
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        ]
```