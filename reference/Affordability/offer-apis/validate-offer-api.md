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

|                            |                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://sandbox.payu.in/offers/transactions/validate>](https://sandbox.payu.in/offers/transactions/validate>) |
| **Production Environment** | \<[https://api.payu.in/offers/transactions/validate>](https://api.payu.in/offers/transactions/validate>)         |

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

<Callout icon="📘" theme="info">
  ### **Note**:

  You need to include the current date and time in the **Date** field of the header.
</Callout>

```plaintext
'Date: Tue, 09 Aug 2022 12:14:51 GMT'
'Digest: omlvf5r6yimCxH+TfScrGryCGslY3CIF50/zIt/AMk4='
'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="PojEYoRaldbjj5NgO+B3c8R1Id4Sefm5mYdFN+MYf2E="'
```

## Request parameters

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>float</code> The offer amount is passed to validate whether the offer is applicable.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>10000</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>clientId<br> <code>conditional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>integer</code> You can use this parameter to pass the client ID value.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>8000123</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>mid<br><code>conditional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>integer</code> You can use this parameter to pass the clientId or merchantId.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>7043873219</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>autoApply<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>boolean</code> This parameter contains a flag to specify whether the offer can be automatically applied.<br><strong>Note</strong>: If you had enable the <strong>Enforce Offer</strong> flag with PayU, the best offer out of the all the offers passed will be applied for the customer. While using this API,  the <strong>autoApply</strong> parameter must be set to true if the offer is automatically applied.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantNceParamActive<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>boolean</code> This parameter contains a flag to specify whether the NCE offer needs to be validated. It can contain any of the following:</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offerKeys<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string Array</code> Validate whether offerKey which are passed is valid.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offer@123</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentDetail<br><code>conditional </code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON</code> This parameter is in a JSON format. For the details of fields, refer to the <a href="#description-of-paymentDetail-json-fields">Description of paymentDetail JSON Fields</a>.<br>This parameter is mandatory when the payment method is saved card.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {<br>    &quot;cardNumber&quot;: 5123**789012346,<br>    &quot;cardToken&quot; : null,<br>    &quot;cardTokenType&quot; : null<br>    &quot;cardHash&quot;: &quot;card hash&quot;,<br>    &quot;cardMask&quot;: &quot;card mask&quot;,<br>    &quot;category&quot;: &quot;DEBITCARD&quot;,<br>    &quot;paymentCode&quot;: null,<br>    &quot;vpa&quot;: null<br>  }</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentId<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>integer</code> The transaction ID is submitted using this parameter for logging purpose.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardBin<br><code>conditional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>integer</code>Te card bin for cards used in the transaction.<br>This field is mandatory for credit card /debit card offer transaction</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>category<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code>This parameter must contain any of the following payment category:  </p>
<ul>
<li>CREDITCARD</li>
<li>DEBITCARD</li>
<li>NETBANKING</li>
<li>WALLET</li>
<li>UPI</li>
<li>EMI</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>UPI</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentCode<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The payment code used to identify the particular payment option.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>HDFC</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>vpa<code> conditional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code>The VPA and it is applicable for UPI transactions.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>userDetail<br>  <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON</code> This parameter is in a JSON format. For the details of fields, refer to the <a href="#description-of-userDetails-json-fields">Description of userDetail JSON Fields</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>skuDetail<br><code>  optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>JSON\`  This parameter is in a JSON format. For more information, refer to <a href="#description-of-statusdetails-json-fields">Description of skusDetail JSON Fields</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### Description of paymentDetail JSON fields

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardNumber<br><code>mandatory with card number</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>integer</code> This parameter must contain the card number for which offer needs to be validated.<br><strong>Note</strong>: Either the <strong>cardNumber</strong> or <strong>cardToken</strong> parameter is mandatory for the credit card or debit card offer transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardToken<br><code> mandatory for saved card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> This parameter is used to specify the card token of the saved card.<br><strong>Note</strong>: Either the <strong>cardNumber</strong> or <strong>cardToken</strong> parameter is mandatory for the credit card or debit card offer transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1234 4567 2456 3566</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardTokenType<code> mandatory for save card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>integer</code> This parameter is used to specify the card token type of the saved card. Currently, only network tokens are supported by PayU Offer Engine, so value of this field must be <strong>1</strong>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardHash<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> This parameter is used to specify the cardHash of the saved card.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardMask<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>integer</code> This parameter is used to specify the card mask of the saved card.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>category<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> This parameter is used to specify any of the following payment mode used for the transaction:</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>CREDITCARD</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentCode<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> This parameter used to specify the payment code that is used to identify the particular payment option.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>vpa<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> This parameter is applicable only for UPI transactions to specify the VPA or UPI handle.<br><strong>Note</strong>: This parameter is mandatory in case of UPI collect flow, that is, <strong>isCollect</strong>=true)</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>anything@payu</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>email<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter contains the email ID of the merchant&#39;s customer who is eligible for the offer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="mailto:test123@gmail.com">test123@gmail.com</a></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>phoneNo<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter contains the phone number of the merchant&#39;s customer who is eligible for the offer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>8042296254</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>userToken<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter is used to uniquely identify a user for a client/merchant.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>autoApply<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The flag to specify to automatically apply the offer.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>skuAmount<code> optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The price of one/ single unit of SKU is specified in this field.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offerKeys <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The offer keys to filter at SKU-level is specified in this field.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>quantity <code> optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The quantity for the product is specified in this field.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>skuId<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The product identifier to select offer is specified in this field. For more information on creating a SKU offer, refer to <a href="http://docs.payu.in/docs/collect-payments-with-sku-based-offer-using-merchant-hosted-checkout-offers-integration">SKU-Based Offer using Merchant Hosted Checkout</a>.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Integer</code> This field contains payment ID for the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2500</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>clientId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Integer</code> This field contains reference of the merchant.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>mid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Integer</code>This field contains the unique identifier provided by PayU to each merchant.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Float</code> This field contains the Offer transaction amount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>10000.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentcode</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The payment code that is used to identify the particular payment option.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>HDFC</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>category</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field payment mode used for the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>creditcard</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>isValid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains any of the following values to specify whether the offer is valid or not valid:  </p>
<ul>
<li><strong>true</strong>: Signifies that the offer is a valid offer</li>
<li><strong>false</strong>: Signified that the offer is a valid offer</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offerDiscount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code> This field contains offer discount details in a JSON format. For more information, refer to the <a href="#offerDiscount-field-json-details">offerDiscount Field JSON Details</a> subsection.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Refer to the <a href="#offerDiscount-field-json-details">offerDiscount Field JSON Details</a> subsection.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offerDetail</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code> This field contains offer details in a JSON format. For more information, refer to the <a href="#offerDetail-field-json-details">offerDetail Field JSON Details</a> subsection.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Refer to the <a href="#offerDetail-field-json-details">offerDetail Field JSON Details</a> subsection.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>failureReason</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field is used to display the reason for failure.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;Success&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>skusDetail</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Array</code> This parameter contains the product or SKU offer details. For more information, refer to <a href="#skusParameter-field-description">skusParameter Field Description</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offerKey</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field contains the unique identifier for a particular offer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>SummerSpecialOffer2021@q1Bh0jsogwqP</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offerType</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The field contains any of the following type of offer:  </p>
<ul>

<li>INSTANT </li>
<li>CASHBACK</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>INSTANT</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>discount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the total discount available on the transaction once applied the specific offer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>100.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>discountedAmount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the final Net amount of the transaction after applying the specific offer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>discountType</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains any of the following discount type that were defined:  </p>
<ul>

<li>ABSOLUTE </li>
<li>PERCENTAGE</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ABSOLUTE</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offerId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Integer</code> This field contains the unique identifier to identify an offer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>10005</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offerKey</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field contains the unique identifier for a particular offer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>SummerSpecialOffer2021@q1Bh0jsogwqP</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>anchorOfferKey</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> This field contains the flag to indicate if it is an anchor offer key.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offerType</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field contains the offer owner.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>MERCHANT</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>title</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field contains the title of the offer that will be displayed for customers.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>festive_500</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>description</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field contains the description of offer for the merchant&#39;s reference.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>festive discount</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>validFrom</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The field contains the offer start time.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2021-07-01 17:02:11</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>validTo</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The field contains the offer end time.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2022-08-05 15:53:16</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>tnc</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field contains the Terms &amp; Conditions for applying promo that will be displayed to customers while accessing the link provided in the <strong>tncLink</strong> field.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>abc</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>tncLink</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field contains URL to fetch details on Terms &amp; Conditions and details specified in the <strong>tnc</strong> is displayed.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>abcd</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>discountType</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field contains any of the following discount type that was defined:</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ABSOLUTE</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offerPercentage</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Float</code>This field contains the define the discount percentage for the offer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>10</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>maxDiscountPerTxn</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The field contains the max discount available for a transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>100.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>minTxnAmount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Float</code> The field contains the minimum transaction amount offer will be applicable.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>10.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>maxTxnAmount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Float</code> The field contains the maximum transaction amount offer will be applicable</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>25000.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field contains any of the following current offer status:  </p>
<ul>
<li>DRAFTED</li>
<li>DEACTIVEATED</li>
<li>PAUSED</li>
<li>ACTIVE</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ACTIVE</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>isNce</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code>This field contains any of the following values to specify whether the offer is a no cost EMI offer or not:  </p>
<ul>
<li><strong>true</strong>: The offer is a No Cost EMI offer</li>
<li><strong>false</strong>: The offer is not a No Cost EMI offer</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>disallowTransactionI<br>nvalidOffer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> This field contains any of the following values to specify whether the transaction should continue without offer or with offer:  </p>
<ul>
<li><strong>true</strong>: The transaction should continue without offer</li>
<li><strong>false</strong>: The transaction should continue with offer</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>isSkuOffer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code>This field contains flag to indicate if it is an SKU-based offer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>isSubventedOffer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code>This field contains flag to indicate if it is a subvented offer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>isBaseOffer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code>This field contains flag to indicate if  it is a base offer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Float</code>This field contains the offer amount.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>300</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>discount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Float</code> This field contains the offer amount.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>discountedAmount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Float</code> This field contains the discounted offer amount.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>isValid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code>This field contains flag to indicate if it is a valid offer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>failureReason</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field contains failure reason.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Offer Validated Successfully</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>recordType</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field contains the record type.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>OFFER</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>isGstSubvented</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code>This field contains flag to indicate if it is a GST subvented.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>isCohortOffer</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code>This field contains flag to indicate if it is a cohort offer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>isDpEmi</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code>This field contains flag to indicate if it is a downpayment EMI.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>false</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>minDpRange</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Float</code> This field contains the minimum downpayment amount.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>maxDpRange</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Float</code> This field contains the maximum downpayment amount.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>downPaymentUnit</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Float</code> This field contains the  downpayment unit.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>issuerId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field contains issuer ID.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>issuerName</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field contains issuer name.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>skuAmount<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The price of one/ single unit of SKU is specified in this field.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>skuId<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The product identifier to select offer is specified in this field.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>quantity <br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The quantity for the product is specified in this field.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>offerKeys<br> <strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The offer keys to filter at SKU-level is specified in this field.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

<br />
