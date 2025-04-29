---
title: Validate Offer API
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
The **validate\_offer** API validates the payment request against an offer key. This API doesn’t apply the offer and only validates the request.

**Endpoints**

|                            |                                                        |
| -------------------------- | ------------------------------------------------------ |
| **Test Environment**       | <https://sandbox.payu.in/offers/transactions/validate> |
| **Production Environment** | <https://api.payu.in/offers/transactions/validate>     |

## Request headers

The request header contains the following fields:

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

The sample header is similar to the following:

> 📘 **Note**:
> 
> You need to include the current date and time in the **Date** field of the header.

```plaintext
'Date: Tue, 09 Aug 2022 12:14:51 GMT'
'Digest: omlvf5r6yimCxH+TfScrGryCGslY3CIF50/zIt/AMk4='
'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="PojEYoRaldbjj5NgO+B3c8R1Id4Sefm5mYdFN+MYf2E="'
```

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "amount  \n `optional`",
    "0-1": "`float` The offer amount is passed to validate whether the offer is applicable.",
    "0-2": "10000",
    "1-0": "clientId  \n `conditional`",
    "1-1": "`integer` You can use this parameter to pass the client ID value.",
    "1-2": "8000123",
    "2-0": "mid  \n`conditional`",
    "2-1": "`integer` You can use this parameter to pass the clientId or merchantId.",
    "2-2": "7043873219",
    "3-0": "autoApply  \n `optional`",
    "3-1": "`boolean` This parameter contains a flag to specify whether the offer can be automatically applied.  \n**Note**: If you had enable the **Enforce Offer** flag with PayU, the best offer out of the all the offers passed will be applied for the customer. While using this API,  the **autoApply** parameter must be set to true if the offer is automatically applied.",
    "3-2": "false",
    "4-0": "merchantNceParamActive  \n `mandatory`",
    "4-1": "`boolean` This parameter contains a flag to specify whether the NCE offer needs to be validated. It can contain any of the following:",
    "4-2": "false",
    "5-0": "offerKeys  \n`mandatory`",
    "5-1": "`string Array` Validate whether offerKey which are passed is valid.",
    "5-2": "offer@123",
    "6-0": "paymentDetail  \n`conditional `",
    "6-1": "`JSON` This parameter is in a JSON format. For the details of fields, refer to the [Description of paymentDetail JSON Fields](#description-of-paymentDetail-json-fields).  \nThis parameter is mandatory when the payment method is saved card.",
    "6-2": " {  \n    \"cardNumber\": 5123\\*\\*789012346,  \n    \"cardToken\" : null,  \n    \"cardTokenType\" : null  \n    \"cardHash\": \"card hash\",  \n    \"cardMask\": \"card mask\",  \n    \"category\": \"DEBITCARD\",  \n    \"paymentCode\": null,  \n    \"vpa\": null  \n  }",
    "7-0": "paymentId  \n `optional`",
    "7-1": "`integer` The transaction ID is submitted using this parameter for logging purpose.",
    "7-2": "",
    "8-0": "cardBin  \n`conditional`",
    "8-1": "`integer`Te card bin for cards used in the transaction.  \nThis field is mandatory for credit card /debit card offer transaction",
    "8-2": "",
    "9-0": "category  \n`mandatory`",
    "9-1": "`string`This parameter must contain any of the following payment category:  \n  \n- CREDITCARD\n- DEBITCARD\n- NETBANKING\n- WALLET\n- UPI\n- EMI",
    "9-2": "UPI",
    "10-0": "paymentCode  \n`mandatory`",
    "10-1": "`string` The payment code used to identify the particular payment option.",
    "10-2": "HDFC",
    "11-0": "vpa`\nconditional`",
    "11-1": "`string`The VPA and it is applicable for UPI transactions.",
    "11-2": "",
    "12-0": "userDetail  \n  `mandatory`",
    "12-1": "`JSON` This parameter is in a JSON format. For the details of fields, refer to the [Description of userDetail JSON Fields](#description-of-userDetails-json-fields).",
    "12-2": "",
    "13-0": "skuDetail  \n`  optional`",
    "13-1": "JSON\\`  This parameter is in a JSON format. For more information, refer to [Description of skusDetail JSON Fields](#description-of-statusdetails-json-fields).",
    "13-2": ""
  },
  "cols": 3,
  "rows": 14,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### Description of paymentDetail JSON fields

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "cardNumber  \n`mandatory with card number`",
    "0-1": "`integer` This parameter must contain the card number for which offer needs to be validated.  \n**Note**: Either the **cardNumber** or **cardToken** parameter is mandatory for the credit card or debit card offer transaction.",
    "0-2": " ",
    "1-0": "cardToken  \n` mandatory for saved card`",
    "1-1": "`string` This parameter is used to specify the card token of the saved card.  \n**Note**: Either the **cardNumber** or **cardToken** parameter is mandatory for the credit card or debit card offer transaction.",
    "1-2": "1234 4567 2456 3566",
    "2-0": "cardTokenType`\nmandatory for save card`",
    "2-1": "`integer` This parameter is used to specify the card token type of the saved card. Currently, only network tokens are supported by PayU Offer Engine, so value of this field must be **1**.",
    "2-2": "1",
    "3-0": "cardHash  \n`optional`",
    "3-1": "`string` This parameter is used to specify the cardHash of the saved card.",
    "3-2": " ",
    "4-0": "cardMask  \n`optional`",
    "4-1": "`integer` This parameter is used to specify the card mask of the saved card.",
    "4-2": " ",
    "5-0": "category  \n`mandatory`",
    "5-1": "`string` This parameter is used to specify any of the following payment mode used for the transaction:",
    "5-2": "CREDITCARD",
    "6-0": "paymentCode  \n`mandatory`",
    "6-1": "`string` This parameter used to specify the payment code that is used to identify the particular payment option.",
    "6-2": " ",
    "7-0": "vpa  \n`optional`",
    "7-1": "`string` This parameter is applicable only for UPI transactions to specify the VPA or UPI handle.  \n**Note**: This parameter is mandatory in case of UPI collect flow, that is, **isCollect**\\=true)",
    "7-2": "anything@payu"
  },
  "cols": 3,
  "rows": 8,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


#### Sample paymentDetail JSON

```plaintext
"paymentDetail": {
    "cardNumber": 5123**789012346,
    "cardToken" : null,
    "cardTokenType" : null
    "cardHash": "card hash",
    "cardMask": "card mask",
    "category": "DEBITCARD",
    "paymentCode": null,
    "vpa": null
  }
```

### Description of userDetail JSON Fields

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "email  \n`optional`",
    "0-1": "`String`This parameter contains the email ID of the merchant's customer who is eligible for the offer",
    "0-2": "[test123@gmail.com](mailto:test123@gmail.com)",
    "1-0": "phoneNo  \n`optional`",
    "1-1": "`String` This parameter contains the phone number of the merchant's customer who is eligible for the offer.",
    "1-2": "8042296254",
    "2-0": "userToken  \n`mandatory`",
    "2-1": "`String` This parameter is used to uniquely identify a user for a client/merchant.",
    "2-2": ""
  },
  "cols": 3,
  "rows": 3,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


#### Sample userDetail JSON

```plaintext
 "userDetail": {
    "email": "string",
    "phoneNo": "string",
    "userToken": "useToken123456"
  }
```

### Description of skusDetails JSON fields

In addition to the request parameters listed in this section, the **skusDetail** parameter with **skus** in an JSON array is posted, where each **skus** contain the following fields are posted in an array:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "autoApply  \n`mandatory`",
    "0-1": "The flag to specify to automatically apply the offer.",
    "1-0": "skuAmount`\noptional`",
    "1-1": "The price of one/ single unit of SKU is specified in this field.",
    "2-0": "offerKeys `optional`",
    "2-1": "The offer keys to filter at SKU-level is specified in this field.",
    "3-0": "quantity `\noptional`",
    "3-1": "The quantity for the product is specified in this field.",
    "4-0": "skuId  \n`mandatory`",
    "4-1": "The product identifier to select offer is specified in this field. For more information on creating a SKU offer, refer to [SKU-Based Offer using Merchant Hosted Checkout](doc:collect-payments-with-sku-based-offer-using-merchant-hosted-checkout-offers-integration)."
  },
  "cols": 2,
  "rows": 5,
  "align": [
    null,
    null
  ]
}
[/block]


#### Sample skusDetails

```plaintext
"skusDetail": {
    "skus": [
      {
        "skuAmount": 1000,
        "autoApply": true,
        "offerKeys": [
          "SummerSpecialOffer2021@q1Bh0jsogwqP"
        ],
        "quantity": 1,
        "skuId": "1"
      }
    ]
  }
```

## Sample request and response for normal transactional offers

### With autoApply=true

**Sample request**

```curl
{
    "amount": 300,
    "autoApply": true,
    "offerKeys": [],
    "paymentDetail": {
        "cardNumber": 1234567890123456,
        "cardToken": null,
        "cardTokenType": null,
        "category": "CREDITCARD",
        "paymentCode": "CC",
        "vpa": null
    },
    "paymentId": 11111135,
    "platformId": 1,
    "userDetail": {
        "email": "string",
        "phoneNo": "string",
        "userToken": "sds"
    }
}
```

**Sample response**

```
{
    "code": "200",
    "message": "Offer Validated Successfully",
    "status": 1,
    "result": {
        "flagToFail": false,
        "paymentId": 11111135,
        "clientId": 42693,
        "mid": 180012,
        "amount": 300,
        "downPaymentAmount": null,
        "emiAmount": null,
        "paymentCode": "CC",
        "category": "CREDITCARD",
        "isValid": true,
        "offerDiscount": {
            "offerKey": "TestOffer@fY6HdoP7da8L",
            "offerType": "INSTANT",
            "discount": 100.00,
            "discountedAmount": 200.00,
            "discountType": "ABSOLUTE"
        },
        "offerDetail": {
            "offerId": 66057,
            "offerKey": "TestOffer@fY6HdoP7da8L",
            "anchorOfferKey": null,
            "offerType": "INSTANT",
            "offerCategory": null,
            "title": "TestOffer",
            "description": "offer",
            "validFrom": "2024-10-14 00:00:00",
            "validTo": "2024-11-30 23:59:00",
            "tnc": "tnc",
            "tncLink": null,
            "discountType": "ABSOLUTE",
            "offerPercentage": null,
            "maxDiscountPerTxn": 100.00,
            "minTxnAmount": 101.00,
            "maxTxnAmount": 111111.00,
            "minRangeDiscount": null,
            "maxRangeDiscount": null,
            "status": "ACTIVE",
            "isNce": false,
            "disallowTransactionInvalidOffer": null,
            "isSkuOffer": false,
            "isSubventedOffer": false,
            "isBaseOffer": false,
            "amount": 300,
            "discount": 100.00,
            "discountedAmount": 200.00,
            "isValid": true,
            "failureReason": "Offer Validated Successfully",
            "recordType": "OFFER",
            "isGstSubvented": false,
            "isCohortOffer": false,
            "isDpEmi": false,
            "minDpRange": null,
            "maxDpRange": null,
            "downPaymentUnit": null,
            "issuerId": null,
            "issuerName": null
        },
        "totalDiscountDetail": {
            "totalCashbackDiscount": 0,
            "totalInstantDiscount": 100.00,
            "totalDiscountedAmount": 200.00
        },
        "offers": [
            {
                "offerId": 66057,
                "offerKey": "TestOffer@fY6HdoP7da8L",
                "anchorOfferKey": null,
                "offerType": "INSTANT",
                "offerCategory": null,
                "title": "TestOffer",
                "description": "offer",
                "validFrom": "2024-10-14 00:00:00",
                "validTo": "2024-11-30 23:59:00",
                "tnc": "tnc",
                "tncLink": null,
                "discountType": "ABSOLUTE",
                "offerPercentage": null,
                "maxDiscountPerTxn": 100.00,
                "minTxnAmount": 101.00,
                "maxTxnAmount": 111111.00,
                "minRangeDiscount": null,
                "maxRangeDiscount": null,
                "status": "ACTIVE",
                "isNce": false,
                "disallowTransactionInvalidOffer": null,
                "isSkuOffer": false,
                "isSubventedOffer": false,
                "isBaseOffer": false,
                "amount": 300,
                "discount": 100.00,
                "discountedAmount": 200.00,
                "isValid": true,
                "failureReason": "Offer Validated Successfully",
                "recordType": "OFFER",
                "isGstSubvented": false,
                "isCohortOffer": false,
                "isDpEmi": false,
                "minDpRange": null,
                "maxDpRange": null,
                "downPaymentUnit": null,
                "issuerId": null,
                "issuerName": null
            }
        ],
        "skusDetail": null,
        "failureReason": "Offer Validated Successfully",
        "failureReasonsBreakup": [
            {
                "offerKey": "title@xsSMQwiE5wcq",
                "failureCode": "ERR6014"
            }
        ],
        "autoApply": true,
        "isSkuOffer": false
    },
    "traceId": "59bd685f-2923-459c-ab06-5edaf8e0ee50"
}
```

### With  autoApply=false

**Sample request**

```
{
    "amount": 300,
    "autoApply": false,
    "offerKeys": ["TestOffer@fY6HdoP7da8L"],
    "paymentDetail": {
        "cardNumber": 1234567890123456,
        "cardToken": null,
        "cardTokenType": null,
        "category": "CREDITCARD",
        "paymentCode": "CC",
        "vpa": null
    },
    "paymentId": 11111135,
    "platformId": 1,
    "userDetail": {
        "email": "string",
        "phoneNo": "string",
        "userToken": "sds"
    }
}
```

**Sample response**

```
{
    "code": "200",
    "message": "Offer Validated Successfully",
    "status": 1,
    "result": {
        "flagToFail": false,
        "paymentId": 11111135,
        "clientId": 42693,
        "mid": 180012,
        "amount": 300,
        "downPaymentAmount": null,
        "emiAmount": null,
        "paymentCode": "CC",
        "category": "CREDITCARD",
        "isValid": true,
        "offerDiscount": {
            "offerKey": "TestOffer@fY6HdoP7da8L",
            "offerType": "INSTANT",
            "discount": 100.00,
            "discountedAmount": 200.00,
            "discountType": "ABSOLUTE"
        },
        "offerDetail": {
            "offerId": 66057,
            "offerKey": "TestOffer@fY6HdoP7da8L",
            "anchorOfferKey": null,
            "offerType": "INSTANT",
            "offerCategory": null,
            "title": "TestOffer",
            "description": "offer",
            "validFrom": "2024-10-14 00:00:00",
            "validTo": "2024-11-30 23:59:00",
            "tnc": "tnc",
            "tncLink": null,
            "discountType": "ABSOLUTE",
            "offerPercentage": null,
            "maxDiscountPerTxn": 100.00,
            "minTxnAmount": 101.00,
            "maxTxnAmount": 111111.00,
            "minRangeDiscount": null,
            "maxRangeDiscount": null,
            "status": "ACTIVE",
            "isNce": false,
            "disallowTransactionInvalidOffer": null,
            "isSkuOffer": false,
            "isSubventedOffer": false,
            "isBaseOffer": false,
            "amount": 300,
            "discount": 100.00,
            "discountedAmount": 200.00,
            "isValid": true,
            "failureReason": "Offer Validated Successfully",
            "recordType": "OFFER",
            "isGstSubvented": false,
            "isCohortOffer": false,
            "isDpEmi": false,
            "minDpRange": null,
            "maxDpRange": null,
            "downPaymentUnit": null,
            "issuerId": null,
            "issuerName": null
        },
        "totalDiscountDetail": {
            "totalCashbackDiscount": 0,
            "totalInstantDiscount": 100.00,
            "totalDiscountedAmount": 200.00
        },
        "offers": [
            {
                "offerId": 66057,
                "offerKey": "TestOffer@fY6HdoP7da8L",
                "anchorOfferKey": null,
                "offerType": "INSTANT",
                "offerCategory": null,
                "title": "TestOffer",
                "description": "offer",
                "validFrom": "2024-10-14 00:00:00",
                "validTo": "2024-11-30 23:59:00",
                "tnc": "tnc",
                "tncLink": null,
                "discountType": "ABSOLUTE",
                "offerPercentage": null,
                "maxDiscountPerTxn": 100.00,
                "minTxnAmount": 101.00,
                "maxTxnAmount": 111111.00,
                "minRangeDiscount": null,
                "maxRangeDiscount": null,
                "status": "ACTIVE",
                "isNce": false,
                "disallowTransactionInvalidOffer": null,
                "isSkuOffer": false,
                "isSubventedOffer": false,
                "isBaseOffer": false,
                "amount": 300,
                "discount": 100.00,
                "discountedAmount": 200.00,
                "isValid": true,
                "failureReason": "Offer Validated Successfully",
                "recordType": "OFFER",
                "isGstSubvented": false,
                "isCohortOffer": false,
                "isDpEmi": false,
                "minDpRange": null,
                "maxDpRange": null,
                "downPaymentUnit": null,
                "issuerId": null,
                "issuerName": null
            }
        ],
        "skusDetail": null,
        "failureReason": "Offer Validated Successfully",
        "failureReasonsBreakup": [],
        "autoApply": false,
        "isSkuOffer": false
    },
    "traceId": "9bfb1312-d154-4160-acc6-415b0c78c974"
}
```

### Failure scenarios

- Merchant ID does not exists

```plaintext
{
    "code": "404",
    "message": "Merchant with merchant Id :1800122 does not exists",
    "status": 0,
    "exceptionId": "9cf201ab-2ad3-439e-a7a6-f707d2f76e48"
}
```

- Client ID does not exist or not matching with platform ID

```plaintext
{
    "code": "404",
    "message": "client with clientId :4 , platformId :12 does not exists.",
    "status": 0,
    "exceptionId": "6985749b-9de4-4d39-9242-d19d35a82d0c"
}
```

- Service Unavailable

```plaintext

{
    "code": "500",
    "message": "Service Unavailable",
    "status": 0,
    "exceptionId": "65466805-5be1-4fa4-912d-d28cf620d687"
}
```

## Sample request and response for SKU-based offers

### With autoApply=true

**Sample request**

```
{
    "amount": 300,
    "autoApply": false,
    "offerKeys": [],
    "paymentDetail": {
        "cardNumber": 1234567890123456,
        "cardToken": null,
        "cardTokenType": null,
        "category": "CREDITCARD",
        "paymentCode": "CC",
        "vpa": null
    },
    "paymentId": 11111135,
    "platformId": 1,
    "userDetail": {
        "email": "string",
        "phoneNo": "string",
        "userToken": "sds"
    },
    "skusDetail": {
        "skus": [
            {
                "skuCategory": "sku_only",
                "skuAmount": 300,
                "quantity": 1,
                "autoApply": true,
                "skuId": "sampleProductId",
                "offerKeys": []
            }
        ]
    }
}
```

**Sample response**

```
{
    "code": "200",
    "message": "Offer Validated Successfully",
    "status": 1,
    "result": {
        "flagToFail": false,
        "paymentId": 11111135,
        "clientId": 42693,
        "mid": 180012,
        "amount": null,
        "downPaymentAmount": null,
        "emiAmount": null,
        "paymentCode": "CC",
        "category": "CREDITCARD",
        "isValid": false,
        "offerDiscount": null,
        "offerDetail": null,
        "totalDiscountDetail": null,
        "offers": null,
        "skusDetail": {
            "skusDiscountDetail": {
                "totalCashbackDiscount": 0,
                "totalInstantDiscount": 50.00,
                "totalDiscountedAmount": 250.00
            },
            "skus": [
                {
                    "skuId": "sampleProductId",
                    "skuCategory": "sku_only",
                    "skuName": "sampleProductName",
                    "quantity": 1,
                    "skuAmount": 300,
                    "isValid": true,
                    "discountDetail": {
                        "offerKey": "hellosku@rFTxczzbDmj6",
                        "offerType": "INSTANT",
                        "discount": 50.00,
                        "discountedAmount": 250.00,
                        "discountType": "ABSOLUTE"
                    },
                    "skuTotalDiscountDetail": {
                        "totalCashbackDiscount": 0,
                        "totalInstantDiscount": 50.00,
                        "totalDiscountedAmount": 250.00
                    },
                    "offerDetail": {
                        "offerId": 66067,
                        "offerKey": "hellosku@rFTxczzbDmj6",
                        "anchorOfferKey": null,
                        "offerType": "INSTANT",
                        "offerCategory": null,
                        "title": "hello sku",
                        "description": "qwe4",
                        "validFrom": "2024-10-15 00:00:00",
                        "validTo": "2024-10-16 23:59:59",
                        "tnc": "123e",
                        "tncLink": null,
                        "discountType": "ABSOLUTE",
                        "offerPercentage": null,
                        "maxDiscountPerTxn": 50.00,
                        "minTxnAmount": 11.00,
                        "maxTxnAmount": 1000000.00,
                        "minRangeDiscount": null,
                        "maxRangeDiscount": null,
                        "status": "ACTIVE",
                        "isNce": false,
                        "disallowTransactionInvalidOffer": null,
                        "isSkuOffer": true,
                        "isSubventedOffer": false,
                        "isBaseOffer": false,
                        "amount": 300,
                        "discount": 50.00,
                        "discountedAmount": 250.00,
                        "isValid": true,
                        "failureReason": "Offer Validated Successfully",
                        "recordType": "OFFER",
                        "isGstSubvented": false,
                        "isCohortOffer": false,
                        "isDpEmi": false,
                        "minDpRange": null,
                        "maxDpRange": null,
                        "downPaymentUnit": null,
                        "issuerId": null,
                        "issuerName": null
                    },
                    "offers": [
                        {
                            "offerId": 66067,
                            "offerKey": "hellosku@rFTxczzbDmj6",
                            "anchorOfferKey": null,
                            "offerType": "INSTANT",
                            "offerCategory": null,
                            "title": "hello sku",
                            "description": "qwe4",
                            "validFrom": "2024-10-15 00:00:00",
                            "validTo": "2024-10-16 23:59:59",
                            "tnc": "123e",
                            "tncLink": null,
                            "discountType": "ABSOLUTE",
                            "offerPercentage": null,
                            "maxDiscountPerTxn": 50.00,
                            "minTxnAmount": 11.00,
                            "maxTxnAmount": 1000000.00,
                            "minRangeDiscount": null,
                            "maxRangeDiscount": null,
                            "status": "ACTIVE",
                            "isNce": false,
                            "disallowTransactionInvalidOffer": null,
                            "isSkuOffer": true,
                            "isSubventedOffer": false,
                            "isBaseOffer": false,
                            "amount": 300,
                            "discount": 50.00,
                            "discountedAmount": 250.00,
                            "isValid": true,
                            "failureReason": "Offer Validated Successfully",
                            "recordType": "OFFER",
                            "isGstSubvented": false,
                            "isCohortOffer": false,
                            "isDpEmi": false,
                            "minDpRange": null,
                            "maxDpRange": null,
                            "downPaymentUnit": null,
                            "issuerId": null,
                            "issuerName": null
                        }
                    ],
                    "statusMessage": "Offer Validated Successfully",
                    "autoApply": true
                }
            ]
        },
        "failureReason": null,
        "failureReasonsBreakup": [],
        "autoApply": false,
        "isSkuOffer": false
    },
    "traceId": "d2851fa2-cf37-4669-b316-41b7143282f4"
}
```

### With autoApply=false

**Sample request**

```
{
    "amount": 300,
    "autoApply": false,
    "offerKeys": [],
    "paymentDetail": {
        "cardNumber": 1234567890123456,
        "cardToken": null,
        "cardTokenType": null,
        "category": "CREDITCARD",
        "paymentCode": "CC",
        "vpa": null
    },
    "paymentId": 11111135,
    "platformId": 1,
    "userDetail": {
        "email": "string",
        "phoneNo": "string",
        "userToken": "sds"
    },
    "skusDetail": {
        "skus": [
            {
                "skuCategory": "sku_only",
                "skuAmount": 300,
                "quantity": 1,
                "autoApply": false,
                "skuId": "sampleProductId",
                "offerKeys": [
                    "hellosku@rFTxczzbDmj6"
                ]
            }
        ]
    }
}
```

**Sample response**

```
{
    "code": "200",
    "message": "Offer Validated Successfully",
    "status": 1,
    "result": {
        "flagToFail": false,
        "paymentId": 11111135,
        "clientId": 42693,
        "mid": 180012,
        "amount": null,
        "downPaymentAmount": null,
        "emiAmount": null,
        "paymentCode": "CC",
        "category": "CREDITCARD",
        "isValid": false,
        "offerDiscount": null,
        "offerDetail": null,
        "totalDiscountDetail": null,
        "offers": null,
        "skusDetail": {
            "skusDiscountDetail": {
                "totalCashbackDiscount": 0,
                "totalInstantDiscount": 50.00,
                "totalDiscountedAmount": 250.00
            },
            "skus": [
                {
                    "skuId": "sampleProductId",
                    "skuCategory": "sku_only",
                    "skuName": "sampleProductName",
                    "quantity": 1,
                    "skuAmount": 300,
                    "isValid": true,
                    "discountDetail": {
                        "offerKey": "hellosku@rFTxczzbDmj6",
                        "offerType": "INSTANT",
                        "discount": 50.00,
                        "discountedAmount": 250.00,
                        "discountType": "ABSOLUTE"
                    },
                    "skuTotalDiscountDetail": {
                        "totalCashbackDiscount": 0,
                        "totalInstantDiscount": 50.00,
                        "totalDiscountedAmount": 250.00
                    },
                    "offerDetail": {
                        "offerId": 66067,
                        "offerKey": "hellosku@rFTxczzbDmj6",
                        "anchorOfferKey": null,
                        "offerType": "INSTANT",
                        "offerCategory": null,
                        "title": "hello sku",
                        "description": "qwe4",
                        "validFrom": "2024-10-15 00:00:00",
                        "validTo": "2024-10-16 23:59:59",
                        "tnc": "123e",
                        "tncLink": null,
                        "discountType": "ABSOLUTE",
                        "offerPercentage": null,
                        "maxDiscountPerTxn": 50.00,
                        "minTxnAmount": 11.00,
                        "maxTxnAmount": 1000000.00,
                        "minRangeDiscount": null,
                        "maxRangeDiscount": null,
                        "status": "ACTIVE",
                        "isNce": false,
                        "disallowTransactionInvalidOffer": null,
                        "isSkuOffer": true,
                        "isSubventedOffer": false,
                        "isBaseOffer": false,
                        "amount": 300,
                        "discount": 50.00,
                        "discountedAmount": 250.00,
                        "isValid": true,
                        "failureReason": "Offer Validated Successfully",
                        "recordType": "OFFER",
                        "isGstSubvented": false,
                        "isCohortOffer": false,
                        "isDpEmi": false,
                        "minDpRange": null,
                        "maxDpRange": null,
                        "downPaymentUnit": null,
                        "issuerId": null,
                        "issuerName": null
                    },
                    "offers": [
                        {
                            "offerId": 66067,
                            "offerKey": "hellosku@rFTxczzbDmj6",
                            "anchorOfferKey": null,
                            "offerType": "INSTANT",
                            "offerCategory": null,
                            "title": "hello sku",
                            "description": "qwe4",
                            "validFrom": "2024-10-15 00:00:00",
                            "validTo": "2024-10-16 23:59:59",
                            "tnc": "123e",
                            "tncLink": null,
                            "discountType": "ABSOLUTE",
                            "offerPercentage": null,
                            "maxDiscountPerTxn": 50.00,
                            "minTxnAmount": 11.00,
                            "maxTxnAmount": 1000000.00,
                            "minRangeDiscount": null,
                            "maxRangeDiscount": null,
                            "status": "ACTIVE",
                            "isNce": false,
                            "disallowTransactionInvalidOffer": null,
                            "isSkuOffer": true,
                            "isSubventedOffer": false,
                            "isBaseOffer": false,
                            "amount": 300,
                            "discount": 50.00,
                            "discountedAmount": 250.00,
                            "isValid": true,
                            "failureReason": "Offer Validated Successfully",
                            "recordType": "OFFER",
                            "isGstSubvented": false,
                            "isCohortOffer": false,
                            "isDpEmi": false,
                            "minDpRange": null,
                            "maxDpRange": null,
                            "downPaymentUnit": null,
                            "issuerId": null,
                            "issuerName": null
                        }
                    ],
                    "statusMessage": "Offer Validated Successfully",
                    "autoApply": false
                }
            ]
        },
        "failureReason": null,
        "failureReasonsBreakup": [],
        "autoApply": false,
        "isSkuOffer": false
    },
    "traceId": "c80dde13-cfcb-473a-b200-b3be788ac7f2"
}
```

### Failure scenarios

- Merchant ID does not exists

```plaintext
{
    "code": "404",
    "message": "Merchant with merchant Id :1800122 does not exists",
    "status": 0,
    "exceptionId": "9cf201ab-2ad3-439e-a7a6-f707d2f76e48"
}
```

- Client ID does not exist or not matching with platform ID

```plaintext
{
    "code": "404",
    "message": "client with clientId :4 , platformId :12 does not exists.",
    "status": 0,
    "exceptionId": "6985749b-9de4-4d39-9242-d19d35a82d0c"
}
```

- Service Unavailable

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

### Sample request with Using a saved card

```curl
curl --location --request POST 'https://sandbox.payu.in/offers/transactions/validate' \
--header 'Date: Tue, 09 Aug 2022 12:14:51 GMT' \
--header 'Digest: omlvf5r6yimCxH+TfScrGryCGslY3CIF50/zIt/AMk4=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="PojEYoRaldbjj5NgO+B3c8R1Id4Sefm5mYdFN+MYf2E="' \
--header 'Content-Type: application/json' \
--header 'Cookie: PHPSESSID=fucavghe82bnd1baej5mdgmaem' \
--data-raw '{
{
  "amount": 500,
  "offerKeys": [
    "SummerSpecialOffer2021@07qIdabo1AHl"
  ],
  "paymentDetail": {
    "cardToken": 1234 4567 2456 3566,
    "cardTokenType": 1,
    "cardHash": "card hash",
    "cardMask": "card mask",
    "category": "DEBITCARD",
    "paymentCode": null,
    "vpa": null,
  },
  "paymentId": 2500,
  "userDetail": {
    "email": "string",
    "phoneNo": "string",
    "userToken": "userToken"
  }
}
}'
```

## Response parameters

The response involves the following parameters and the **result** parameter contains the offer results:

### result parameter JSON Details

The **result** parameter contains the result in a JSON format and the fields in the JSON are described in the following table. The **offerDiscount** and **offerDetail** fields in this JSON contains the offer details as described in the following subsections:

This field contains any of the following values to specify whether the offer is valid or not valid:  

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "paymentid",
    "0-1": "`Integer` This field contains payment ID for the transaction.",
    "0-2": "2500",
    "1-0": "clientId",
    "1-1": "`Integer` This field contains reference of the merchant.",
    "1-2": "1",
    "2-0": "mid",
    "2-1": "`Integer`This field contains the unique identifier provided by PayU to each merchant.",
    "2-2": "1",
    "3-0": "amount",
    "3-1": "`Float` This field contains the Offer transaction amount",
    "3-2": "10000.00",
    "4-0": "paymentcode",
    "4-1": "`String`The payment code that is used to identify the particular payment option.",
    "4-2": "HDFC",
    "5-0": "category",
    "5-1": "`String`This field payment mode used for the transaction.",
    "5-2": "creditcard",
    "6-0": "isValid",
    "6-1": "This field contains any of the following values to specify whether the offer is valid or not valid:  \n  \n- **true**: Signifies that the offer is a valid offer\n- **false**: Signified that the offer is a valid offer",
    "6-2": "true",
    "7-0": "offerDiscount",
    "7-1": "`JSON Object` This field contains offer discount details in a JSON format. For more information, refer to the [offerDiscount Field JSON Details](#offerDiscount-field-json-details) subsection.",
    "7-2": "Refer to the [offerDiscount Field JSON Details](#offerDiscount-field-json-details) subsection.",
    "8-0": "offerDetail",
    "8-1": "`JSON Object` This field contains offer details in a JSON format. For more information, refer to the [offerDetail Field JSON Details](#offerDetail-field-json-details) subsection.",
    "8-2": "Refer to the [offerDetail Field JSON Details](#offerDetail-field-json-details) subsection.",
    "9-0": "failureReason",
    "9-1": "`String` This field is used to display the reason for failure.",
    "9-2": "\"Success\"",
    "10-0": "skusDetail",
    "10-1": "`Array` This parameter contains the product or SKU offer details. For more information, refer to [skusParameter Field Description](#skusParameter-field-description).",
    "10-2": " "
  },
  "cols": 3,
  "rows": 11,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


The sample value for **result** parameter in a JSON is similar to the following:

```plaintext
"result": {
        "paymentId": 2500,
        "clientId": 1,
        "mid": 1,
        "amount": 500,
        "paymentCode": null,
        "category": "DEBITCARD",
        "isValid": true,
        "offerDiscount": {
            "offerKey": "SummerSpecialOffer2021@07qIdabo1AHl",
            "offerType": "INSTANT",
            "discount": 100.00,
            "discountedAmount": 400.00,
            "discountType": "ABSOLUTE"
        },
        "offerDetail": {
            "offerId": 10005,
            "offerKey": "SummerSpecialOffer2021@07qIdabo1AHl",
            "offerType": "INSTANT",
            "title": "SummerSpecialOffer",
            "description": "SummerSpecialOffer discount",
            "validFrom": "2021-07-01 17:02:11",
            "validTo": "2022-08-05 15:53:16",
            "tnc": "abc",
            "tncLink": "abcd",
            "discountType": "ABSOLUTE",
            "offerPercentage": null,
            "maxDiscountPerTxn": 100.00,
            "minTxnAmount": 10.00,
            "maxTxnAmount": 25000.00,
            "status": "ACTIVE",
            "isNce": false,
            "disallowTransactionInvalidOffer":true
        },
        "failureReason": "Success"
    }
```

#### offerDiscount Field JSON Details

The **offerDiscount** field in the **result** JSON contains the offer discount details in a JSON format as described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "offerKey",
    "0-1": "`String` This field contains the unique identifier for a particular offer.",
    "0-2": "SummerSpecialOffer2021@q1Bh0jsogwqP",
    "1-0": "offerType",
    "1-1": "`String` The field contains any of the following type of offer:  \n  \n- INSTANT \n- CASHBACK",
    "1-2": "INSTANT",
    "2-0": "discount",
    "2-1": "This field contains the total discount available on the transaction once applied the specific offer.",
    "2-2": "100.00",
    "3-0": "discountedAmount",
    "3-1": "This field contains the final Net amount of the transaction after applying the specific offer.",
    "3-2": "400.00",
    "4-0": "discountType",
    "4-1": "This field contains any of the following discount type that were defined:  \n  \n- ABSOLUTE \n- PERCENTAGE",
    "4-2": "ABSOLUTE"
  },
  "cols": 3,
  "rows": 5,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


The sample value for **offerDiscount** field in a JSON is similar to the following:

```plaintext
"offerDiscount": {
            "offerKey": "SummerSpecialOffer2021@07qIdabo1AHl",
            "offerType": "INSTANT",
            "discount": 100.00,
            "discountedAmount": 400.00,
            "discountType": "ABSOLUTE"
        },
```

#### offerDetail Field JSON Details

The **offerDetail** field in the **result** JSON contains the offer details in a JSON format as described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "offerId",
    "0-1": "`Integer` This field contains the unique identifier to identify an offer.",
    "0-2": "10005",
    "1-0": "offerKey",
    "1-1": "`String` This field contains the unique identifier for a particular offer.",
    "1-2": "SummerSpecialOffer2021@q1Bh0jsogwqP",
    "2-0": "anchorOfferKey",
    "2-1": "`Boolean` This field contains the flag to indicate if it an anchor offer key.",
    "2-2": "",
    "3-0": "offerType",
    "3-1": "`String` This field contains the offer owner.",
    "3-2": "MERCHANT",
    "4-0": "title",
    "4-1": "`String` This field contains the title of the offer that will be displayed for customers.",
    "4-2": "festive\\_500",
    "5-0": "description",
    "5-1": "`String` This field contains the description of offer for the merchant's reference.",
    "5-2": "festive discount",
    "6-0": "validFrom",
    "6-1": "`String` The field contains the offer start time.",
    "6-2": "2021-07-01 17:02:11",
    "7-0": "validTo",
    "7-1": "`String` The field contains the offer end time.",
    "7-2": "2022-08-05 15:53:16",
    "8-0": "tnc",
    "8-1": "`String` This field contains the Terms & Conditions for applying promo that will be displayed to customers while accessing the link provided in the **tncLink** field.",
    "8-2": "abc",
    "9-0": "tncLink",
    "9-1": "`String` This field contains URL to fetch details on Terms & Conditions and details specified in the **tnc** is displayed.",
    "9-2": "abcd",
    "10-0": "discountType",
    "10-1": "`String`This field contains any of the following discount type that was defined:",
    "10-2": "ABSOLUTE",
    "11-0": "offerPercentage",
    "11-1": "`Float`This field contains the define the discount percentage for the offer.",
    "11-2": "10",
    "12-0": "maxDiscountPerTxn",
    "12-1": "`String` The field contains the max discount available for a transaction.",
    "12-2": "100.00",
    "13-0": "minTxnAmount",
    "13-1": "`Float` The field contains the minimum transaction amount offer will be applicable.",
    "13-2": "10.00",
    "14-0": "maxTxnAmount",
    "14-1": "`Float` The field contains the maximum transaction amount offer will be applicable",
    "14-2": "25000.00",
    "15-0": "status",
    "15-1": "`String`This field contains any of the following current offer status:  \n  \n- DRAFTED\n- DEACTIVEATED\n- PAUSED\n- ACTIVE",
    "15-2": "ACTIVE",
    "16-0": "isNce",
    "16-1": "`Boolean`This field contains any of the following values to specify whether the offer is a no cost EMI offer or not:  \n  \n- **true**: The offer is a No Cost EMI offer\n- **false**: The offer is not a No Cost EMI offer",
    "16-2": "",
    "17-0": "disallowTransactionI  \nnvalidOffer",
    "17-1": "`Boolean` This field contains any of the following values to specify whether the transaction should continue without offer or with offer:  \n  \n- **true**: The transaction should continue without offer\n- **false**: The transaction should continue with offer",
    "17-2": "true",
    "18-0": "isSkuOffer",
    "18-1": "`Boolean`This field contains flag to indicate if it is an SKU-based offer.",
    "18-2": "true",
    "19-0": "isSubventedOffer",
    "19-1": "`Boolean`This field contains flag to indicate if it is a subvented offer.",
    "19-2": "false",
    "20-0": "isBaseOffer",
    "20-1": "`Boolean`This field contains flag to indicate if  it a base offer.",
    "20-2": "false",
    "21-0": "amount",
    "21-1": "`Float`This field contains the offer amount.",
    "21-2": "300",
    "22-0": "discount",
    "22-1": "`Float` This field contains the offer amount.",
    "22-2": "",
    "23-0": "discountedAmount",
    "23-1": "`Float` This field contains the discounted offer amount.",
    "23-2": "true",
    "24-0": "isValid",
    "24-1": "`Boolean`This field contains flag to indicate if it is a valid offer.",
    "24-2": "",
    "25-0": "failureReason",
    "25-1": "`String`This field contains failure reason.",
    "25-2": "Offer Validated Successfully",
    "26-0": "recordType",
    "26-1": "`String`This field contains the record type.",
    "26-2": "OFFER",
    "27-0": "isGstSubvented",
    "27-1": "`Boolean`This field contains flag to indicate if it is a GST subvented.",
    "27-2": "false",
    "28-0": "isCohortOffer",
    "28-1": "`Boolean`This field contains flag to indicate if it is a cohort offer.",
    "28-2": "false",
    "29-0": "isDpEmi",
    "29-1": "`Boolean`This field contains flag to indicate if it is a downpayment EMI.",
    "29-2": "false",
    "30-0": "minDpRange",
    "30-1": "`Float` This field contains the minimum downpayment amount.",
    "30-2": "",
    "31-0": "maxDpRange",
    "31-1": "`Float` This field contains the maximum downpayment amount.",
    "31-2": "",
    "32-0": "downPaymentUnit",
    "32-1": "`Float` This field contains the  downpayment unit.",
    "32-2": "",
    "33-0": "issuerId",
    "33-1": "`String`This field contains issuer ID.",
    "33-2": "",
    "34-0": "issuerName",
    "34-1": "`String`This field contains issuer name.",
    "34-2": ""
  },
  "cols": 3,
  "rows": 35,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


The sample value for **offerDetail** field in a JSON is similar to the following:

```plaintext
"offerDetail" {
            "offerId": 66057,
            "offerKey": "TestOffer@fY6HdoP7da8L",
            "anchorOfferKey": null,
            "offerType": "INSTANT",
            "offerCategory": null,
            "title": "TestOffer",
            "description": "offer",
            "validFrom": "2024-10-14 00:00:00",
            "validTo": "2024-11-30 23:59:00",
            "tnc": "tnc",
            "tncLink": null,
            "discountType": "ABSOLUTE",
            "offerPercentage": null,
            "maxDiscountPerTxn": 100.00,
            "minTxnAmount": 101.00,
            "maxTxnAmount": 111111.00,
            "minRangeDiscount": null,
            "maxRangeDiscount": null,
            "status": "ACTIVE",
            "isNce": false,
            "disallowTransactionInvalidOffer": null,
            "isSkuOffer": false,
            "isSubventedOffer": false,
            "isBaseOffer": false,
            "amount": 300,
            "discount": 100.00,
            "discountedAmount": 200.00,
            "isValid": true,
            "failureReason": "Offer Validated Successfully",
            "recordType": "OFFER",
            "isGstSubvented": false,
            "isCohortOffer": false,
            "isDpEmi": false,
            "minDpRange": null,
            "maxDpRange": null,
            "downPaymentUnit": null,
            "issuerId": null,
            "issuerName": null
        }
```

#### skusDetail Parameter Description

In addition to the request parameters listed in the [Fetch Offers API](ref:fetch-offers-api) section, the **skusDetail** parameter is posted with the following fields are posted in an array:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "skuAmount  \n**optional**",
    "0-1": "`String` The price of one/ single unit of SKU is specified in this field.",
    "1-0": "skuId  \n**mandatory**",
    "1-1": "`String` The product identifier to select offer is specified in this field.",
    "2-0": "quantity   \n**optional**",
    "2-1": "`String` The quantity for the product is specified in this field.",
    "3-0": "offerKeys  \n **optional**",
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