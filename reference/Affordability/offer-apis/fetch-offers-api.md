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

<Callout icon="📘" theme="info">
  ###

  **Note**: If the amount is received in the request, the discount calculation for each offer is also sent as part of the response. If the amount is not received, the response does not contain the discount calculation fields.
</Callout>

**Endpoints**

|                            |                                                                                                |
| -------------------------- | ---------------------------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://sandbox.payu.in/offers/transactions>](https://sandbox.payu.in/offers/transactions>) |
| **Production Environment** | \<[https://api.payu.in/offers/transactions>](https://api.payu.in/offers/transactions>)         |

## Request Headers

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Date
        `mandatory`
      </td>

      <td>
        The date and time should be in the GMT time conversion(not the IST). For example, current time in India is 18:00:00 IST, the time in the date header should be 12:30:00 GMT.
      </td>

      <td>
        Thu, 17 Feb 2022 08:17:59 GMT
      </td>
    </tr>

    <tr>
      <td>
        Digest
        `mandatory`
      </td>

      <td>
        Base 64 encode of (sha256 hash of the JSON data (post to server).
      </td>

      <td>
        vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=
      </td>
    </tr>

    <tr>
      <td>
        Authorization
        `mandatory`
      </td>

      <td>
        This field is in the following format: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4=" Where the above format includes the following: • username: The merchant key of the merchant. • algorithm: This must have the value as hmac-sha256 that is used for this API • headers: This must have the value as date digest • signature: This must contain the hmacsha256 of (signing\_string, merchant\_secret), where: • signing\_string: This is in the "Date"+"\n"+"Digest" format. Here, the Date and Digest is the same values in the fields listed in this table For example, "Thu, 17 Feb 2022 08:17:59 GMT""\n"+"vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=" • merchant\_secret: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to Generate Merchant Key and Salt on PayU Dashboard
      </td>

      <td>
        hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI="
      </td>
    </tr>

    <tr>
      <td>
        platformId
        `mandatory`
      </td>

      <td>
        This field contains the platform ID and must include the value as 1.
      </td>

      <td>
        1
      </td>
    </tr>
  </tbody>
</Table>

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

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Amount
        `optional`
      </td>

      <td>
        `float` The offer transaction amount
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        offerKeys
        `optional`
      </td>

      <td>
        `String Array` This field contains list of keys to filter the offer in an array format.
      </td>

      <td>
        `SummerSpecialOffer2021@q1Bh0jsogwqP`
      </td>
    </tr>

    <tr>
      <td>
        paymentId
        `optional`
      </td>

      <td>
        `Long` Unique reference ID for a transaction which is generated by merchant and sent in the request
      </td>

      <td>
        `110`
      </td>
    </tr>

    <tr>
      <td>
        userToken
        `optional`
      </td>

      <td>
        `String Long` This parameter is used to uniquely identify a user for a client/merchant.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        skusDetail
        `optional`
      </td>

      <td>
        `String Array` The skusDetail is in an array format and contains the SKU offer details. For more information, refer to
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        autoApply
        `optional`
      </td>

      <td>
        `Boolean` This parameter must be set to true if the offer is automatically applied.
      </td>

      <td>
        `true`
      </td>
    </tr>
  </tbody>
</Table>

<br />

<Callout icon="📘" theme="info">
  ### Notes:

  - If you had enable the **Enforce Offer** flag with PayU, the best offer out of the all the offers passed will be applied for the customer. While using this API,  the **autoApply** parameter must be set to true if the offer is automatically applied.
  - All the parameters are optional, but the header is mandatory.
</Callout>

### skusDetail Parameter Description

In addition to the request parameters listed in the [Fetch Offers API](ref:fetch-offers-api) section, the **skusDetail** parameter is posted with the following fields are posted in an array:

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        skuAmount
        `optional`
      </td>

      <td>
        `String` The price of one/ single unit of SKU is specified in this field.
      </td>
    </tr>

    <tr>
      <td>
        skuId
        `mandatory`
      </td>

      <td>
        `String` The product identifier to select offer is specified in this field.
      </td>
    </tr>

    <tr>
      <td>
        quantity
        `optional`
      </td>

      <td>
        `String` The quantity for the product is specified in this field.
      </td>
    </tr>

    <tr>
      <td>
        offerKeys
        `optional`
      </td>

      <td>
        `String` The offer keys to filter at SKU-level is specified in this field.
      </td>
    </tr>
  </tbody>
</Table>

## Sample request and response for a normal transactional offer

### With autoApply=true

**Sample request**

```curl
curl --location 'https://sandbox.payu.in/offers/transactions' \
--header 'Content-Type: application/json' \
--header 'Date: {{generated_date}}' \
--header 'Digest: {{generated_digest}}' \
--header 'Authorization: {{generated_authorization}}' \
--header 'platformId: 1' \
--data '{
    "amount": 500,
    "autoApply": true,
    "userToken": "merchant_key:unique_user_id"
}'
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

- For Base No-Cost EMI  (NCE) with Instant Discount Offer

```json
{
    "code": "200",
    "message": "Offer Retrieved Successfully",
    "status": 1,
    "result": {
        "failureReason": null,
        "clientId": 154400,
        "mid": 8406928,
        "amount": null,
        "couponsAvailable": false,
        "isUserPersonalizedOffersAvailable": false,
        "offers": [
            {
                "failureReason": null,
                "stepSize": null,
                "externalOfferType": null,
                "recordSubType": null,
                "offerKey": "CashbackTest@FnarpOmjdeLL",
                "type": "MERCHANT",
                "title": "Cashback Test",
                "description": "Get Rs.10 Flat cashback",
                "tnc": "TnC",
                "tncLink": null,
                "minTxnAmount": 100.00,
                "maxTxnAmount": 10000.00,
                "offerType": "CASHBACK",
                "minRangeDiscount": null,
                "maxRangeDiscount": null,
                "validFrom": "2026-02-04 00:00:00",
                "validTo": "2026-02-05 23:59:59",
                "discountDetail": {
                    "discountType": "ABSOLUTE",
                    "discountPercentage": null,
                    "discount": null,
                    "discountedAmount": null,
                    "maxDiscount": 10.00
                },
                "isNoCostEmi": false,
                "isSubvented": false,
                "isSkuOffer": false,
                "creditCard": null,
                "debitCard": null,
                "netBanking": null,
                "wallet": null,
                "clw": null,
                "upi": [
                    {
                        "title": "CRED",
                        "paymentCode": "CRED",
                        "handle": [
                            "axisb"
                        ]
                    },
                    {
                        "title": "Bhim",
                        "paymentCode": "bhim",
                        "handle": [
                            "upi"
                        ]
                    },
                    {
                        "title": "Paytm",
                        "paymentCode": "paytm",
                        "handle": [
                            "paytm"
                        ]
                    },
                    {
                        "title": "Amazon Pay",
                        "paymentCode": "amazonpay",
                        "handle": [
                            "apl",
                            "yapl"
                        ]
                    },
                    {
                        "title": "Groww",
                        "paymentCode": "Groww",
                        "handle": [
                            "yesg"
                        ]
                    },
                    {
                        "title": "Freecharge",
                        "paymentCode": "Freecharge",
                        "handle": [
                            "freecharge"
                        ]
                    },
                    {
                        "title": "WhatsApp",
                        "paymentCode": "whatsapp",
                        "handle": [
                            "wahdfcbank",
                            "waicici",
                            "wasbi",
                            "waaxis"
                        ]
                    },
                    {
                        "title": "Jupiter Money",
                        "paymentCode": "jupiter",
                        "handle": [
                            "jupiteraxis"
                        ]
                    },
                    {
                        "title": "Mobikwik",
                        "paymentCode": "Mobikwik",
                        "handle": [
                            "ikwik"
                        ]
                    },
                    {
                        "title": "Google Pay",
                        "paymentCode": "googlepay",
                        "handle": [
                            "okaxis",
                            "oksbi",
                            "okicici",
                            "okhdfcbank"
                        ]
                    },
                    {
                        "title": "PhonePe",
                        "paymentCode": "phonepe",
                        "handle": [
                            "axl",
                            "ibl",
                            "ybl"
                        ]
                    }
                ],
                "emi": null,
                "bnpl": null,
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
                "isNudgeOnlyOffer": false,
                "offerMilestone": null,
                "userMilestone": null,
                "userDetail": null,
                "isUserVerificationRequired": false,
                "isPersonalisedUniqueCoupon": false,
                "isLockOffer": false,
                "currencyDescription": null,
                "cashbackDestination": null
            }
        ],
        "skusDetail": null,
        "flagToFail": false,
        "isSkuOffer": false,
        "paymentId": null
    },
    "traceId": "10.248.157.222-8081-1-748685-167-1770198363.779"
}

Base NCEMI;
offerkey: BaseNCETest@1Xu25kZyv6nH
Offerkey: TestInstantDiscountN@NrjyL6571jbW

Request:
{
    "amount": "2500",
    "offerKeys": ["BaseNCETest@1Xu25kZyv6nH",
    "TestInstantDiscountN@NrjyL6571jbW"]  
}

Response;

{
    "code": "200",
    "message": "Offer Retrieved Successfully",
    "status": 1,
    "result": {
        "failureReason": null,
        "clientId": 154400,
        "mid": 8406928,
        "amount": 2500,
        "couponsAvailable": false,
        "isUserPersonalizedOffersAvailable": false,
        "offers": [
            {
                "failureReason": null,
                "stepSize": null,
                "externalOfferType": null,
                "recordSubType": null,
                "offerKey": "TestInstantDiscountN@NrjyL6571jbW",
                "type": "MERCHANT",
                "title": "Test Instant Discount NON EMI",
                "description": "Get Flat 10% off",
                "tnc": "TnC",
                "tncLink": null,
                "minTxnAmount": 1000.00,
                "maxTxnAmount": 10000.00,
                "offerType": "INSTANT",
                "minRangeDiscount": null,
                "maxRangeDiscount": null,
                "validFrom": "2026-02-04 00:00:00",
                "validTo": "2026-02-05 23:59:59",
                "discountDetail": {
                    "discountType": "ABSOLUTE",
                    "discountPercentage": null,
                    "discount": 100.00,
                    "discountedAmount": 2400.00,
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
                                "code": "HDFC",
                                "title": "Hdfc Bank"
                            },
                            {
                                "code": "ICICI",
                                "title": "ICICI"
                            }
                        ],
                        "title": null,
                        "paymentCode": null,
                        "handle": null
                    }
                ],
                "debitCard": [
                    {
                        "networks": [],
                        "banks": [
                            {
                                "code": "HDFC",
                                "title": "Hdfc Bank"
                            }
                        ],
                        "title": null,
                        "paymentCode": null,
                        "handle": null
                    }
                ],
                "netBanking": null,
                "wallet": null,
                "clw": null,
                "upi": null,
                "emi": {
                    "debitCard": {
                        "banks": [
                            {
                                "bankCode": "HDFC",
                                "bankName": "HDFC Bank Debit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "HDFCD06",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": [
                                            "BaseNCETest@1Xu25kZyv6nH"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "HDFCD03",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": [
                                            "BaseNCETest@1Xu25kZyv6nH"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "HDFCD12",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": [
                                            "BaseNCETest@1Xu25kZyv6nH"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "HDFCD09",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": [
                                            "BaseNCETest@1Xu25kZyv6nH"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "HDFCD18",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": [
                                            "BaseNCETest@1Xu25kZyv6nH"
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    "creditCard": {
                        "banks": [
                            {
                                "bankCode": "HDFC",
                                "bankName": "HDFC Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "EMI12",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": [
                                            "BaseNCETest@1Xu25kZyv6nH"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "EMI18",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMI6",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": [
                                            "BaseNCETest@1Xu25kZyv6nH"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "EMI9",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": [
                                            "BaseNCETest@1Xu25kZyv6nH"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "36 Months",
                                        "paymentCode": "EMI36",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMI",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": [
                                            "BaseNCETest@1Xu25kZyv6nH"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "24 Months",
                                        "paymentCode": "EMI24",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    }
                                ]
                            }
                        ]
                    },
                    "cardLess": null,
                    "other": null
                },
                "bnpl": null,
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
                "isNudgeOnlyOffer": false,
                "offerMilestone": null,
                "userMilestone": null,
                "userDetail": null,
                "isUserVerificationRequired": false,
                "isPersonalisedUniqueCoupon": false,
                "isLockOffer": false,
                "currencyDescription": null,
                "cashbackDestination": null
            },
            {
                "failureReason": null,
                "stepSize": null,
                "externalOfferType": null,
                "recordSubType": null,
                "offerKey": "BaseNCETest@1Xu25kZyv6nH",
                "type": "MERCHANT",
                "title": "Base NCE Test",
                "description": "Get 15% off",
                "tnc": "TnCs",
                "tncLink": null,
                "minTxnAmount": 1000.00,
                "maxTxnAmount": 10000.00,
                "offerType": "INSTANT",
                "minRangeDiscount": null,
                "maxRangeDiscount": null,
                "validFrom": "2026-02-04 00:00:00",
                "validTo": "2026-02-05 23:59:59",
                "discountDetail": null,
                "isNoCostEmi": true,
                "isSubvented": false,
                "isSkuOffer": false,
                "creditCard": null,
                "debitCard": null,
                "netBanking": null,
                "wallet": null,
                "clw": null,
                "upi": null,
                "emi": {
                    "debitCard": {
                        "banks": [
                            {
                                "bankCode": "HDFC",
                                "bankName": "HDFC Bank Debit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "HDFCD06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 112.64,
                                            "discountedAmount": 2387.36
                                        },
                                        "linkedOffers": [
                                            "TestInstantDiscountN@NrjyL6571jbW"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "HDFCD12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 203.83,
                                            "discountedAmount": 2296.17
                                        },
                                        "linkedOffers": [
                                            "TestInstantDiscountN@NrjyL6571jbW"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "HDFCD18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 290.38,
                                            "discountedAmount": 2209.62
                                        },
                                        "linkedOffers": [
                                            "TestInstantDiscountN@NrjyL6571jbW"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "HDFCD03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 65.21,
                                            "discountedAmount": 2434.79
                                        },
                                        "linkedOffers": [
                                            "TestInstantDiscountN@NrjyL6571jbW"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "HDFCD09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 158.83,
                                            "discountedAmount": 2341.17
                                        },
                                        "linkedOffers": [
                                            "TestInstantDiscountN@NrjyL6571jbW"
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    "creditCard": {
                        "banks": [
                            {
                                "bankCode": "SBIN",
                                "bankName": "State Bank of India Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 months",
                                        "paymentCode": "SBI03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.5,
                                            "discount": 67.21,
                                            "discountedAmount": 2432.79
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "ICIC",
                                "bankName": "ICICI Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMIIC6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.99,
                                            "discount": 105.76,
                                            "discountedAmount": 2394.24
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMIIC3",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.99,
                                            "discount": 61.18,
                                            "discountedAmount": 2438.82
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "HDFC",
                                "bankName": "HDFC Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMI",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 65.21,
                                            "discountedAmount": 2434.79
                                        },
                                        "linkedOffers": [
                                            "TestInstantDiscountN@NrjyL6571jbW"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "EMI9",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 158.83,
                                            "discountedAmount": 2341.17
                                        },
                                        "linkedOffers": [
                                            "TestInstantDiscountN@NrjyL6571jbW"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMI6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 112.64,
                                            "discountedAmount": 2387.36
                                        },
                                        "linkedOffers": [
                                            "TestInstantDiscountN@NrjyL6571jbW"
                                        ]
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "EMI12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 203.83,
                                            "discountedAmount": 2296.17
                                        },
                                        "linkedOffers": [
                                            "TestInstantDiscountN@NrjyL6571jbW"
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    "cardLess": null,
                    "other": null
                },
                "bnpl": null,
                "skuDetail": null,
                "isAcrossSkuQuantity": false,
                "offerCategory": "NO_COST_EMI",
                "isBaseOffer": true,
                "recordType": "OFFER",
                "toDisplay": true,
                "disallowTransactionInvalidOffer": false,
                "isAllPaymentMethodsAvailable": false,
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
                "isPersonalisedUniqueCoupon": false,
                "isLockOffer": false,
                "currencyDescription": null,
                "cashbackDestination": null
            }
        ],
        "skusDetail": null,
        "flagToFail": false,
        "isSkuOffer": false,
        "paymentId": null
    },
    "traceId": "10.248.157.222-8081-1-772954-339-1770199777.284"
}
              
Low cost EMI
Request;
{
    "amount": "2500",
    "offerKeys": ["LCETestOffer@Ou6Fnq8uPf2O"]  
}

Response;
{
    "code": "200",
    "message": "Offer Retrieved Successfully",
    "status": 1,
    "result": {
        "failureReason": null,
        "clientId": 154400,
        "mid": 8406928,
        "amount": 2500,
        "couponsAvailable": false,
        "isUserPersonalizedOffersAvailable": false,
        "offers": [
            {
                "failureReason": null,
                "stepSize": null,
                "externalOfferType": null,
                "recordSubType": null,
                "offerKey": "LCETestOffer@Ou6Fnq8uPf2O",
                "type": "MERCHANT",
                "title": "LCE Test Offer",
                "description": "Get Instant LCE off",
                "tnc": "TnC",
                "tncLink": null,
                "minTxnAmount": 1000.00,
                "maxTxnAmount": 100000.00,
                "offerType": "INSTANT",
                "minRangeDiscount": null,
                "maxRangeDiscount": null,
                "validFrom": "2026-02-04 00:00:00",
                "validTo": "2026-02-05 23:59:59",
                "discountDetail": null,
                "isNoCostEmi": false,
                "isSubvented": false,
                "isSkuOffer": false,
                "creditCard": null,
                "debitCard": null,
                "netBanking": null,
                "wallet": null,
                "clw": null,
                "upi": null,
                "emi": {
                    "debitCard": null,
                    "creditCard": {
                        "banks": [
                            {
                                "bankCode": "AMEX",
                                "bankName": "American Express Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 months",
                                        "paymentCode": "EMIAMEX3",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 12.00,
                                            "discountedAmount": 2488.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 months",
                                        "paymentCode": "EMIAMEX6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 12.00,
                                            "discountedAmount": 2488.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "INDB",
                                "bankName": "IndusInd Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMIIND6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMIIND3",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "CITI",
                                "bankName": "Citi Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMI06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMI03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "KKBK",
                                "bankName": "Kotak Mahindra Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMIK6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMIK3",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "HSBC",
                                "bankName": "HSBC Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMIHS03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMIHS06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "RATN",
                                "bankName": "RBL Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMIRBL3",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMIRBL6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "YESB",
                                "bankName": "Yes Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMIY06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMIY03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "SBIN",
                                "bankName": "State Bank of India Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 months",
                                        "paymentCode": "SBI03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 months",
                                        "paymentCode": "SBI06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "ICIC",
                                "bankName": "ICICI Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMIIC6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMIIC3",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "ONEC",
                                "bankName": "One Card Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "ONEC03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "ONEC06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "HDFC",
                                "bankName": "HDFC Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMI6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMI",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "IDFC",
                                "bankName": "Idfc Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 months",
                                        "paymentCode": "IDFC03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 months",
                                        "paymentCode": "IDFC06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "SCBL",
                                "bankName": "Standard Chartered Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMISCB6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMISCB3",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "UTIB",
                                "bankName": "Axis Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 months",
                                        "paymentCode": "EMIA6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 months",
                                        "paymentCode": "EMIA3",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": 11.00,
                                            "discountedAmount": 2489.00
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            }
                        ]
                    },
                    "cardLess": null,
                    "other": null
                },
                "bnpl": null,
                "skuDetail": null,
                "isAcrossSkuQuantity": false,
                "offerCategory": "LOW_COST_EMI",
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
                "isNudgeOnlyOffer": false,
                "offerMilestone": null,
                "userMilestone": null,
                "userDetail": null,
                "isUserVerificationRequired": false,
                "isPersonalisedUniqueCoupon": false,
                "isLockOffer": false,
                "currencyDescription": null,
                "cashbackDestination": null
            }
        ],
        "skusDetail": null,
        "flagToFail": false,
        "isSkuOffer": false,
        "paymentId": null
    },
    "traceId": "10.248.157.222-8081-1-774731-57-1770199898.382"
}

Nocost EMI
Request;
{
    "amount": "2500",
    "offerKeys": ["NCETestOffer@eHb7ESUPH8ls"]  
}

Response;
{
    "code": "200",
    "message": "Offer Retrieved Successfully",
    "status": 1,
    "result": {
        "failureReason": null,
        "clientId": 154400,
        "mid": 8406928,
        "amount": 2500,
        "couponsAvailable": false,
        "isUserPersonalizedOffersAvailable": false,
        "offers": [
            {
                "failureReason": null,
                "stepSize": null,
                "externalOfferType": null,
                "recordSubType": null,
                "offerKey": "NCETestOffer@eHb7ESUPH8ls",
                "type": "MERCHANT",
                "title": "NCE Test Offer",
                "description": "Get 5% off",
                "tnc": "Tnc",
                "tncLink": null,
                "minTxnAmount": 1000.00,
                "maxTxnAmount": 10000.00,
                "offerType": "INSTANT",
                "minRangeDiscount": null,
                "maxRangeDiscount": null,
                "validFrom": "2026-02-04 00:00:00",
                "validTo": "2026-02-05 23:59:59",
                "discountDetail": null,
                "isNoCostEmi": true,
                "isSubvented": false,
                "isSkuOffer": false,
                "creditCard": null,
                "debitCard": null,
                "netBanking": null,
                "wallet": null,
                "clw": null,
                "upi": null,
                "emi": {
                    "debitCard": {
                        "banks": [
                            {
                                "bankCode": "BARB",
                                "bankName": "Bank of Baroda Debit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "BOBD18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 290.38,
                                            "discountedAmount": 2209.62
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "BOBD03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 65.21,
                                            "discountedAmount": 2434.79
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "BOBD09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 158.83,
                                            "discountedAmount": 2341.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "BOBD12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 203.83,
                                            "discountedAmount": 2296.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "BOBD06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 112.64,
                                            "discountedAmount": 2387.36
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "SBIN",
                                "bankName": "State Bank of India Debit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "SBID09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 18.45,
                                            "discount": 181.83,
                                            "discountedAmount": 2318.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "SBID18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 18.45,
                                            "discount": 330.56,
                                            "discountedAmount": 2169.44
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "SBID12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 18.45,
                                            "discount": 232.90,
                                            "discountedAmount": 2267.10
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "SBID06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 18.45,
                                            "discount": 129.20,
                                            "discountedAmount": 2370.80
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "ICIC",
                                "bankName": "ICICI Bank Debit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "ICICID06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 112.64,
                                            "discountedAmount": 2387.36
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "ICICID12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 203.83,
                                            "discountedAmount": 2296.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "ICICID03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 65.21,
                                            "discountedAmount": 2434.79
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "ICICID09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 158.83,
                                            "discountedAmount": 2341.17
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "HDFC",
                                "bankName": "HDFC Bank Debit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "HDFCD12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 203.83,
                                            "discountedAmount": 2296.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "HDFCD18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 290.38,
                                            "discountedAmount": 2209.62
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "HDFCD09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 158.83,
                                            "discountedAmount": 2341.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "HDFCD03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 65.21,
                                            "discountedAmount": 2434.79
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "HDFCD06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 112.64,
                                            "discountedAmount": 2387.36
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "FDRL",
                                "bankName": "Federal Bank Debit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "FEDED09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 15.0,
                                            "discount": 149.35,
                                            "discountedAmount": 2350.65
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "FEDED03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 15.0,
                                            "discount": 61.22,
                                            "discountedAmount": 2438.78
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "FEDED12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 15.0,
                                            "discount": 191.81,
                                            "discountedAmount": 2308.19
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "FEDED06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 15.0,
                                            "discount": 105.83,
                                            "discountedAmount": 2394.17
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "KKBK",
                                "bankName": "Kotak Mahindra Bank Debit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "KOTAKD09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 19.0,
                                            "discount": 186.95,
                                            "discountedAmount": 2313.05
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "1 Month",
                                        "paymentCode": "KOTAKD01",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 20.0,
                                            "discount": 40.98,
                                            "discountedAmount": 2459.02
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "2 Months",
                                        "paymentCode": "KOTAKD02",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 20.0,
                                            "discount": 61.14,
                                            "discountedAmount": 2438.86
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "KOTAKD03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 19.0,
                                            "discount": 77.13,
                                            "discountedAmount": 2422.87
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "KOTAKD06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 19.0,
                                            "discount": 132.89,
                                            "discountedAmount": 2367.11
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "KOTAKD12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 19.0,
                                            "discount": 239.35,
                                            "discountedAmount": 2260.65
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "UTIB",
                                "bankName": "Axis Debit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "AXISD06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.0,
                                            "discount": 98.99,
                                            "discountedAmount": 2401.01
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "AXISD03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.0,
                                            "discount": 57.22,
                                            "discountedAmount": 2442.78
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "AXISD09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 158.83,
                                            "discountedAmount": 2341.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "AXISD18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 290.38,
                                            "discountedAmount": 2209.62
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "24 Months",
                                        "paymentCode": "AXISD24",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 372.55,
                                            "discountedAmount": 2127.45
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "AXISD12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 203.83,
                                            "discountedAmount": 2296.17
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            }
                        ]
                    },
                    "creditCard": {
                        "banks": [
                            {
                                "bankCode": "BARB",
                                "bankName": "Bank of Baroda Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "BOBCC06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 112.64,
                                            "discountedAmount": 2387.36
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "BOBCC03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 65.21,
                                            "discountedAmount": 2434.79
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "BOBCC12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 203.83,
                                            "discountedAmount": 2296.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "36 Months",
                                        "paymentCode": "BOBCC36",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 524.74,
                                            "discountedAmount": 1975.26
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "BOBCC18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 290.38,
                                            "discountedAmount": 2209.62
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "BOBCC09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 158.83,
                                            "discountedAmount": 2341.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "24 Months",
                                        "paymentCode": "BOBCC24",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 372.55,
                                            "discountedAmount": 2127.45
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "AMEX",
                                "bankName": "American Express Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 months",
                                        "paymentCode": "EMIAMEX9",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.0,
                                            "discount": 139.81,
                                            "discountedAmount": 2360.19
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 months",
                                        "paymentCode": "EMIAMEX6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.0,
                                            "discount": 98.99,
                                            "discountedAmount": 2401.01
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 months",
                                        "paymentCode": "EMAMEX12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": null,
                                            "discountedAmount": null
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 months",
                                        "paymentCode": "EMIAMEX3",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.0,
                                            "discount": 57.22,
                                            "discountedAmount": 2442.78
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "YESB",
                                "bankName": "Yes Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMIY06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 112.64,
                                            "discountedAmount": 2387.36
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "EMIY18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 290.38,
                                            "discountedAmount": 2209.62
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "EMIY09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 158.83,
                                            "discountedAmount": 2341.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMIY03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 65.21,
                                            "discountedAmount": 2434.79
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "EMIY12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 203.83,
                                            "discountedAmount": 2296.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "24 Months",
                                        "paymentCode": "EMIY24",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 372.55,
                                            "discountedAmount": 2127.45
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "SBIN",
                                "bankName": "State Bank of India Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 months",
                                        "paymentCode": "SBI06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 15.0,
                                            "discount": 105.83,
                                            "discountedAmount": 2394.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 months",
                                        "paymentCode": "SBI12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 15.0,
                                            "discount": 191.81,
                                            "discountedAmount": 2308.19
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 months",
                                        "paymentCode": "SBI09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 15.0,
                                            "discount": 149.35,
                                            "discountedAmount": 2350.65
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "24 months",
                                        "paymentCode": "SBI24",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 15.75,
                                            "discount": 367.35,
                                            "discountedAmount": 2132.65
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 months",
                                        "paymentCode": "SBI18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 15.5,
                                            "discount": 282.05,
                                            "discountedAmount": 2217.95
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 months",
                                        "paymentCode": "SBI03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.5,
                                            "discount": 67.21,
                                            "discountedAmount": 2432.79
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "ICIC",
                                "bankName": "ICICI Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "24 Months",
                                        "paymentCode": "EMIIC24",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.99,
                                            "discount": 351.43,
                                            "discountedAmount": 2148.57
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "EMIIC18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.99,
                                            "discount": 273.51,
                                            "discountedAmount": 2226.49
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "EMIIC9",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.99,
                                            "discount": 149.25,
                                            "discountedAmount": 2350.75
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMIIC3",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.99,
                                            "discount": 61.18,
                                            "discountedAmount": 2438.82
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMIIC6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.99,
                                            "discount": 105.76,
                                            "discountedAmount": 2394.24
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "EMIIC12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.99,
                                            "discount": 191.69,
                                            "discountedAmount": 2308.31
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "HDFC",
                                "bankName": "HDFC Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "EMI12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 203.83,
                                            "discountedAmount": 2296.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMI",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 65.21,
                                            "discountedAmount": 2434.79
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMI6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 112.64,
                                            "discountedAmount": 2387.36
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "EMI9",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 158.83,
                                            "discountedAmount": 2341.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "36 Months",
                                        "paymentCode": "EMI36",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 524.74,
                                            "discountedAmount": 1975.26
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "24 Months",
                                        "paymentCode": "EMI24",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 372.55,
                                            "discountedAmount": 2127.45
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "EMI18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 290.38,
                                            "discountedAmount": 2209.62
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "IDFC",
                                "bankName": "Idfc Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "15 months",
                                        "paymentCode": "IDFC15",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 247.67,
                                            "discountedAmount": 2252.33
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "24 months",
                                        "paymentCode": "IDFC24",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 372.55,
                                            "discountedAmount": 2127.45
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 months",
                                        "paymentCode": "IDFC06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 15.0,
                                            "discount": 105.83,
                                            "discountedAmount": 2394.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 months",
                                        "paymentCode": "IDFC09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 15.0,
                                            "discount": 149.35,
                                            "discountedAmount": 2350.65
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 months",
                                        "paymentCode": "IDFC03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 65.21,
                                            "discountedAmount": 2434.79
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 months",
                                        "paymentCode": "IDFC12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 203.83,
                                            "discountedAmount": 2296.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 months",
                                        "paymentCode": "IDFC18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 290.38,
                                            "discountedAmount": 2209.62
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "36 months",
                                        "paymentCode": "IDFC36",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 524.74,
                                            "discountedAmount": 1975.26
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "KKBK",
                                "bankName": "Kotak Mahindra Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMIK6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 112.64,
                                            "discountedAmount": 2387.36
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "24 Months",
                                        "paymentCode": "EMIK24",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 372.55,
                                            "discountedAmount": 2127.45
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "EMIK18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 290.38,
                                            "discountedAmount": 2209.62
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMIK3",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 65.21,
                                            "discountedAmount": 2434.79
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "EMIK12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 203.83,
                                            "discountedAmount": 2296.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "EMIK9",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 158.83,
                                            "discountedAmount": 2341.17
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "UTIB",
                                "bankName": "Axis Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 months",
                                        "paymentCode": "EMIA9",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 15.0,
                                            "discount": 149.35,
                                            "discountedAmount": 2350.65
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 months",
                                        "paymentCode": "EMIA12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 15.0,
                                            "discount": 191.81,
                                            "discountedAmount": 2308.19
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 months",
                                        "paymentCode": "EMIA6",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.0,
                                            "discount": 98.99,
                                            "discountedAmount": 2401.01
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 months",
                                        "paymentCode": "EMIA18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 290.38,
                                            "discountedAmount": 2209.62
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 months",
                                        "paymentCode": "EMIA3",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 14.0,
                                            "discount": 57.22,
                                            "discountedAmount": 2442.78
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "24 months",
                                        "paymentCode": "EMIA24",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 372.55,
                                            "discountedAmount": 2127.45
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            }
                        ]
                    },
                    "cardLess": {
                        "banks": [
                            {
                                "bankCode": "KBEE",
                                "bankName": "Kredibee Card Less ",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 months",
                                        "paymentCode": "KBEE12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 18.0,
                                            "discount": 227.60,
                                            "discountedAmount": 2272.40
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 months",
                                        "paymentCode": "KBEE09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 18.0,
                                            "discount": 177.63,
                                            "discountedAmount": 2322.37
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 months",
                                        "paymentCode": "KBEE18",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 18.0,
                                            "discount": 323.26,
                                            "discountedAmount": 2176.74
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 months",
                                        "paymentCode": "KBEE06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 18.0,
                                            "discount": 126.17,
                                            "discountedAmount": 2373.83
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 months",
                                        "paymentCode": "KBEE03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 18.0,
                                            "discount": 73.17,
                                            "discountedAmount": 2426.83
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
                            {
                                "bankCode": "ICICI_CL",
                                "bankName": "Icici Card Less ",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 months",
                                        "paymentCode": "ICICIC09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 18.0,
                                            "discount": 177.63,
                                            "discountedAmount": 2322.37
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 months",
                                        "paymentCode": "ICICIC12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 18.0,
                                            "discount": 227.60,
                                            "discountedAmount": 2272.40
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 months",
                                        "paymentCode": "ICICIC06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 18.0,
                                            "discount": 126.17,
                                            "discountedAmount": 2373.83
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 months",
                                        "paymentCode": "ICICIC03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 18.0,
                                            "discount": 73.17,
                                            "discountedAmount": 2426.83
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            },
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
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 290.38,
                                            "discountedAmount": 2209.62
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 months",
                                        "paymentCode": "HDFCCL12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 203.83,
                                            "discountedAmount": 2296.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 months",
                                        "paymentCode": "HDFCCL03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 65.21,
                                            "discountedAmount": 2434.79
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 months",
                                        "paymentCode": "HDFCCL09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 158.83,
                                            "discountedAmount": 2341.17
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 months",
                                        "paymentCode": "HDFCCL06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": 16.0,
                                            "discount": 112.64,
                                            "discountedAmount": 2387.36
                                        },
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
                                        "title": "6 months",
                                        "paymentCode": "BAJFIN06",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": null,
                                            "discountedAmount": null
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 months",
                                        "paymentCode": "BAJFIN12",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": null,
                                            "discountedAmount": null
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 months",
                                        "paymentCode": "BAJFIN03",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": null,
                                            "discountedAmount": null
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "2 months",
                                        "paymentCode": "BAJFIN02",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": null,
                                            "discountedAmount": null
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 months",
                                        "paymentCode": "BAJFIN09",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": null,
                                            "discountedAmount": null
                                        },
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "8 months",
                                        "paymentCode": "BAJFIN08",
                                        "handle": null,
                                        "discountDetail": {
                                            "discountPercentage": null,
                                            "discount": null,
                                            "discountedAmount": null
                                        },
                                        "linkedOffers": []
                                    }
                                ]
                            }
                        ]
                    }
                },
                "bnpl": null,
                "skuDetail": null,
                "isAcrossSkuQuantity": false,
                "offerCategory": "NO_COST_EMI",
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
                "isNudgeOnlyOffer": false,
                "offerMilestone": null,
                "userMilestone": null,
                "userDetail": null,
                "isUserVerificationRequired": false,
                "isPersonalisedUniqueCoupon": false,
                "isLockOffer": false,
                "currencyDescription": null,
                "cashbackDestination": null
            }
        ],
        "skusDetail": null,
        "flagToFail": false,
        "isSkuOffer": false,
        "paymentId": null
    },
    "traceId": "10.248.157.222-8081-1-777090-138-1770200042.151"
}

Instant discount;
Request;
{
    "amount": "2500",
    "offerKeys": ["TestInstantDiscountN@NrjyL6571jbW"]  
}


Response;
{
    "code": "200",
    "message": "Offer Retrieved Successfully",
    "status": 1,
    "result": {
        "failureReason": null,
        "clientId": 154400,
        "mid": 8406928,
        "amount": 2500,
        "couponsAvailable": false,
        "isUserPersonalizedOffersAvailable": false,
        "offers": [
            {
                "failureReason": null,
                "stepSize": null,
                "externalOfferType": null,
                "recordSubType": null,
                "offerKey": "TestInstantDiscountN@NrjyL6571jbW",
                "type": "MERCHANT",
                "title": "Test Instant Discount NON EMI",
                "description": "Get Flat 10% off",
                "tnc": "TnC",
                "tncLink": null,
                "minTxnAmount": 1000.00,
                "maxTxnAmount": 10000.00,
                "offerType": "INSTANT",
                "minRangeDiscount": null,
                "maxRangeDiscount": null,
                "validFrom": "2026-02-04 00:00:00",
                "validTo": "2026-02-05 23:59:59",
                "discountDetail": {
                    "discountType": "ABSOLUTE",
                    "discountPercentage": null,
                    "discount": 100.00,
                    "discountedAmount": 2400.00,
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
                                "code": "HDFC",
                                "title": "Hdfc Bank"
                            },
                            {
                                "code": "ICICI",
                                "title": "ICICI"
                            }
                        ],
                        "title": null,
                        "paymentCode": null,
                        "handle": null
                    }
                ],
                "debitCard": [
                    {
                        "networks": [],
                        "banks": [
                            {
                                "code": "HDFC",
                                "title": "Hdfc Bank"
                            }
                        ],
                        "title": null,
                        "paymentCode": null,
                        "handle": null
                    }
                ],
                "netBanking": null,
                "wallet": null,
                "clw": null,
                "upi": null,
                "emi": {
                    "debitCard": {
                        "banks": [
                            {
                                "bankCode": "HDFC",
                                "bankName": "HDFC Bank Debit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "HDFCD06",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "HDFCD12",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "HDFCD03",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "HDFCD09",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "HDFCD18",
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
                                "bankCode": "HDFC",
                                "bankName": "HDFC Bank Credit Card",
                                "tenureOption": [
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "9 Months",
                                        "paymentCode": "EMI9",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "24 Months",
                                        "paymentCode": "EMI24",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "6 Months",
                                        "paymentCode": "EMI6",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "12 Months",
                                        "paymentCode": "EMI12",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "3 Months",
                                        "paymentCode": "EMI",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "18 Months",
                                        "paymentCode": "EMI18",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    },
                                    {
                                        "minDpRange": null,
                                        "maxDpRange": null,
                                        "isDpEmi": false,
                                        "downPaymentUnit": null,
                                        "title": "36 Months",
                                        "paymentCode": "EMI36",
                                        "handle": null,
                                        "discountDetail": null,
                                        "linkedOffers": []
                                    }
                                ]
                            }
                        ]
                    },
                    "cardLess": null,
                    "other": null
                },
                "bnpl": null,
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
                "isNudgeOnlyOffer": false,
                "offerMilestone": null,
                "userMilestone": null,
                "userDetail": null,
                "isUserVerificationRequired": false,
                "isPersonalisedUniqueCoupon": false,
                "isLockOffer": false,
                "currencyDescription": null,
                "cashbackDestination": null
            }
        ],
        "skusDetail": null,
        "flagToFail": false,
        "isSkuOffer": false,
        "paymentId": null
    },
    "traceId": "10.248.157.222-8081-1-778857-89-1770200118.972"
}

```

<br />

### With autoApply=false

**Sample request**

```curl
curl --location 'https://sandbox.payu.in/offers/transactions' \
--header 'Content-Type: application/json' \
--header 'Date: {{generated_date}}' \
--header 'Digest: {{generated_digest}}' \
--header 'Authorization: {{generated_authorization}}' \
--header 'platformId: 1' \
--data '{
    "amount": 500,
    "autoApply": false,
    "offerKeys": ["flat150Off@03q62aqtF34n", "TestOffer@fY6HdoP7da8L"]
}'
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

```json
curl --location 'https://sandbox.payu.in/offers/transactions' \
--header 'Content-Type: application/json' \
--header 'Date: {{generated_date}}' \
--header 'Digest: {{generated_digest}}' \
--header 'Authorization: {{generated_authorization}}' \
--header 'platformId: 1' \
--data '{
    "amount": 500,
    "autoApply": true,
    "userToken": "merchant_key:unique_user_id",
    "skusDetail": [
        {
            "skuAmount": 300,
            "quantity": 1,
            "skuId": "sampleProductId",
            "offerKeys": []
        }
    ]
}'
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

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>code</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the HTTP status code based on .</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>200</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>message</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter is the result message which contains information about the result</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Offer Validated Successfull</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the status of web service call. The status can be any of the following:  </p>
<ul>
<li>0 - If web service call failed.</li>
<li>1 - If web service call succeeded</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code> This parameter gives the information about the result of the API response in a JSON format. For more information, refer to the <a href="#result-parameter-json-details">result Parameter JSON Details</a> subsection.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Refer to the <a href="#result-parameter-json-details">result Field JSON Details</a> subsection.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        skuAmount
        `optional`
      </td>

      <td>
        `String` The price of one/ single unit of SKU is specified in this field.
      </td>
    </tr>

    <tr>
      <td>
        skuId
        `mandatory`
      </td>

      <td>
        `String` The product identifier to select offer is specified in this field.
      </td>
    </tr>

    <tr>
      <td>
        quantity
        `optional`
      </td>

      <td>
        `String` The quantity for the product is specified in this field.
      </td>
    </tr>

    <tr>
      <td>
        offerKeys
        `optional`
      </td>

      <td>
        `String` The offer keys to filter at SKU-level is specified in this field.
      </td>
    </tr>
  </tbody>
</Table>

The changes made:
• Removed bold formatting from field names
• Removed the `<br>` tags
• Kept the mandatory/optional status in backticks
• Preserved all other content and structure

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

<br />
