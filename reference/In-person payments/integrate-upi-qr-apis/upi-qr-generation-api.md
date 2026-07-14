---
title: 'UPI QR Generation API '
deprecated: false
hidden: true
metadata:
  robots: index
---
The UPI QR Generation API initiates a payment transaction and generates a QR code for UPI payments. The QR format (base64 or URL) is determined by the `sendqrimage` merchant parameter.

Earlier, you received only the intent URL and had to convert it to QR using their own libraries. With this feature, PayU can now send the QR code directly as:

- **Base64-encoded image** for immediate display
- **Image URL** for hosted QR rendering

This API supports both online (Intent-based) and offline (DBQR) QR modes for seamless S2S integrations (`txn_s2s_flow = 4`).

<Callout icon="📘" theme="info">
  ### Note:

  Contact your PayU Key Account manager to enable the **sendqrimage** parameter to use the QR generation feature.
</Callout>

***

## Environment

| Environment    | URL                               | Methor |
| -------------- | --------------------------------- | ------ |
| **Production** | `https://secure.payu.in/_payment` | POST   |
| **Sandbox**    | `https://test.payu.in/_payment`   | POST   |

<br />

## Authentication

Include your merchant key and authorization token in the request headers.

***

## Request Headers

<div>
  

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Header</th>
      <th style="width: 75%; white-space: normal; word-break: break-word;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Content-Type<br><code>mandatory</code></td>
      <td style="white-space: normal; word-break: break-word;">
        <code>application/x-www-form-urlencoded; charset=UTF-8</code>
      </td>
    </tr>
    <tr>
      <td>Accept<br><code>mandatory</code></td>
      <td style="white-space: normal; word-break: break-word;">
        <code>application/json</code>
      </td>
    </tr>
    <tr>
      <td>Authorization<br><code>optional</code></td>
      <td style="white-space: normal; word-break: break-word;">
        Bearer token or API key as per your integration type
      </td>
    </tr>
  </tbody>
</table>


</div>

***

## Request Parameters

<div>
  

<table>
  <thead>
    <tr>
      <th style="width: 15%;">Parameter</th>
      <th style="width: 65%; white-space: normal; word-break: break-word;">Type & Description</th>
      <th style="width: 20%;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        key<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>String</code> Your merchant key provided by PayU during onboarding.
      </td>
      <td>JP***g</td>
    </tr>
    <tr>
      <td>
        txnid<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>String</code> Unique transaction ID for this payment request.
      </td>
      <td>T123456789</td>
    </tr>
    <tr>
      <td>
        amount<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>Decimal</code> Payment amount in INR.
      </td>
      <td>100.00</td>
    </tr>
    <tr>
      <td>
        productinfo<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>String</code> Description of the product or service being purchased.
      </td>
      <td>Mobile Recharge</td>
    </tr>
    <tr>
      <td>
        firstname<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>String</code> First name of the customer.
      </td>
      <td>Ashish</td>
    </tr>
    <tr>
      <td>
        email<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>String</code> Email address of the customer.
      </td>
      <td>test@payu.in</td>
    </tr>
    <tr>
      <td>
        phone<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>String</code> Phone number of the customer.
      </td>
      <td>9876543210</td>
    </tr>
    <tr>
      <td>
        surl<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>String</code> Success return URL where customers are redirected after successful payment.
      </td>
      <td>https://yoursite.com/success</td>
    </tr>
    <tr>
      <td>
        furl<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>String</code> Failure return URL where customers are redirected after failed payment.
      </td>
      <td>https://yoursite.com/failure</td>
    </tr>
    <tr>
      <td>
        pg<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>String</code> Payment mode. For online QR use <code>UPI</code>; for offline QR use <code>DBQR</code> (SDK) or <code>QR</code> (mobile web).
      </td>
      <td>UPI</td>
    </tr>
    <tr>
      <td>
        bankcode<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>String</code> Payment gateway code. Use <code>INTENT</code> for online QR, <code>UPIDBQR</code> for offline QR (SDK), or <code>UPIQR</code> for offline QR (mobile web).
      </td>
      <td>INTENT</td>
    </tr>
    <tr>
      <td>
        upiAppName<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>String</code> Must be set to <code>MQR</code> for mobile/SDK QR transactions. This value is stored in field8 for tracking purposes.
      </td>
      <td>MQR</td>
    </tr>
    <tr>
      <td>
        txn_s2s_flow<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>Integer</code> S2S flow identifier. Must be <code>4</code> for SDK-based QR flows. Not required for mobile web.
      </td>
      <td>4</td>
    </tr>
    <tr>
      <td>
        hash<br>
        <code>mandatory</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>String</code> SHA-512 hash for request validation. Formula: <code>sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)</code>. See <a href="https://docs.payu.in/docs/generate-hash" target="_blank">hash generation guide</a>.
      </td>
      <td>5C4F...</td>
    </tr>
    <tr>
      <td>
        isMobileUPIQR<br>
        <code>optional</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>Integer</code> QR mode preference. <code>1</code> = Offline DBQR primary; <code>2</code> = Online Intent primary; <code>0</code> = Disable QR. If passed in the request, this takes precedence over the merchant_param configuration.
      </td>
      <td>2</td>
    </tr>
    <tr>
      <td>
        sendqrimage<br>
        <code>optional</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>String</code> Determines the QR image format in the response. <code>base64</code> returns a base64-encoded image; <code>url</code> returns an image URL; if not set, only the intent string is returned (existing behavior). 
      </td>
      <td>base64</td>
    </tr>
    <tr>
      <td>
        expiryTime<br>
        <code>optional</code>
      </td>
      <td style="white-space: normal; word-break: break-word;">
        <code>Integer</code> QR code expiry duration in seconds. If not provided, defaults to 300 seconds (5 minutes).
      </td>
      <td>600</td>
    </tr>
  </tbody>
</table>


</div>

***

## QR Mode Configuration

The QR mode (Online Intent vs Offline DBQR) is determined by the `isMobileUPIQR` parameter, which can be configured at the merchant level or passed in the `_payment` request:

**Online QR (isMobileUPIQR = 2):**

- **Mobile Web:** `mode=UPI`, `ibibo-code=INTENT`, `upiAppName=MQR`
- **SDK:** `mode=UPI`, `ibibo-code=INTENT`, `upiAppName=MQR`, `txn_s2s_flow=4`

**Offline DBQR (isMobileUPIQR = 1):**

- **Mobile Web:** `mode=QR`, `ibibo-code=UPIQR`, `upiAppName=MQR`
- **SDK:** `mode=DBQR`, `ibibo-code=UPIDBQR`, `upiAppName=MQR`, `txn_s2s_flow=4`

<Note>
If `isMobileUPIQR` is passed in the `_payment` request, it takes **precedence** over the merchant_param configuration, provided the requested mode is valid and enabled for your merchant account.
</Note>

***

## sendqrimage Parameter Options

The `sendqrimage` parameter controls how the QR code is returned:

| Value                 | Behavior                                                                                                                                                                                                                                           |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Not set (default)** | Returns only the `intentURIData` or `qrString`. No QR image is generated. Merchant must generate QR code on their end.                                                                                                                             |
| **base64**            | PayU generates the QR image, converts it to base64, and includes it in the response under `qrImage.base64.value`. The temporary image file is deleted after encoding.                                                                              |
| **url**               | PayU generates the QR image, uploads it to S3 with a 5-minute expiry, and returns the image URL under `qrImage.url.value`. The URL format is `https://secure.payu.in/<token>/ShowQrImage`. The temporary local image file is deleted after upload. |

<Warning>
The `sendqrimage` parameter must be enabled in your merchant_param configuration before use. Contact your PayU account manager to enable this feature for your merchant ID.
</Warning>

***


## Sample Request

### Request with base64 QR (S2S Flow)

```bash
curl --location 'https://secure.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
--header 'Accept: application/json' \
--data-urlencode 'key=JP***g' \
--data-urlencode 'txnid=T123456789' \
--data-urlencode 'amount=100.00' \
--data-urlencode 'productinfo=Mobile Recharge' \
--data-urlencode 'firstname=Ashish' \
--data-urlencode 'email=test@payu.in' \
--data-urlencode 'phone=9876543210' \
--data-urlencode 'surl=https://yoursite.com/success' \
--data-urlencode 'furl=https://yoursite.com/failure' \
--data-urlencode 'mode=UPI' \
--data-urlencode 'ibibo-code=INTENT' \
--data-urlencode 'upiAppName=MQR' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'isMobileUPIQR=2' \
--data-urlencode 'sendqrimage=base64' \
--data-urlencode 'hash=5C4F3E2D1A0B9C8D7E6F5A4B3C2D1E0F...'
```

> **Note:** Replace all placeholder values (key, hash, URLs, etc.) before making the request.

## Sample Response
### base64 QR

```json
{
  "metaData": {
    "message": null,
    "referenceId": "29483752703",
    "statusCode": null,
    "txnId": "fM8KPzqvyWZ1KUeAf5OC",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": "294837527031",
    "merchantName": "ARTHVIT 1809 TECH PRIVATE LIMITED",
    "merchantVpa": "goodscore.payu@axisbank",
    "amount": "1360.00",
    "intentURIData": "pa=goodscore.payu@axisbank&pn=ARTHVIT 1809 TECH PRIVATE LIMITED&tr=29483752703&tid=PPPL294837527031007260922316a506c7f&am=1360.00&cu=INR&tn=UPIIntent",
    "qrImage": {
      "base64": {
        "value": "iVBORw0KGgoAAAANSUhEUgAAAR0AAAEdAQMAAAALpCE4AAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAADU0lEQVRoge1ZQa6rMBC1..."
      }
    },
    "otpPostUrl": "https://secure.payu.in/ResponseHandler.php"
  }
}
```

### URL QR

```json
{
  "metaData": {
    "message": null,
    "referenceId": "29483752703",
    "statusCode": null,
    "txnId": "fM8KPzqvyWZ1KUeAf5OC",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": "294837527031",
    "merchantName": "ARTHVIT 1809 TECH PRIVATE LIMITED",
    "merchantVpa": "goodscore.payu@axisbank",
    "amount": "1360.00",
    "intentURIData": "pa=goodscore.payu@axisbank&pn=ARTHVIT 1809 TECH PRIVATE LIMITED&tr=29483752703&tid=PPPL294837527031007260922316a506c7f&am=1360.00&cu=INR&tn=UPIIntent",
    "qrImage": {
      "url": {
        "value": "https://secure.payu.in/7b17b5d3babc2e2998c61e3d63e1f81b/ShowQrImage"
      }
    },
    "otpPostUrl": "https://secure.payu.in/ResponseHandler.php"
  }
}
```

### Offline DBQR

```json
{
  "metaData": {
    "message": null,
    "referenceId": "6d36c537a8ff8e3dced4bc5f698df91c",
    "statusCode": null,
    "txnId": "3d30aff07ecf1f5357fa",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": "28579212177",
    "merchantName": "ESAFSMALLFINANCEBANKLIMITED",
    "merchantVpa": "ESAFSMALLdbqr.payu@icici",
    "amount": "10.00",
    "qrString": "upi://pay?pa=ESAFSMALLdbqr.payu@icici&pn=ESAF SMALL FINANCE BANKLIMITED&tr=EZV2026051317273063952330&tid=PPPL285792121771305261727306a04672a&am=10.00&cu=INR&tn=UPI Transaction",
    "otpPostUrl": "https://secure.payu.in/ResponseHandler.php"
  }
}
```

***

## Error Codes

<div>
  

<table>
  <thead>
    <tr>
      <th style="width: 15%;">Error Code</th>
      <th style="width: 50%; white-space: normal; word-break: break-word;">Description</th>
      <th style="width: 35%; white-space: normal; word-break: break-word;">Recommended Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>400</td>
      <td style="white-space: normal; word-break: break-word;">
        <strong>Bad Request</strong><br>Invalid or missing required parameters. Check the request payload for missing or incorrectly formatted fields.
      </td>
      <td style="white-space: normal; word-break: break-word;">
        Verify all mandatory parameters are present and correctly formatted. Ensure <code>sendqrimage</code> value is either <code>base64</code> or <code>url</code> if set.
      </td>
    </tr>
    <tr>
      <td>403</td>
      <td style="white-space: normal; word-break: break-word;">
        <strong>Forbidden</strong><br>The <code>sendqrimage</code> parameter is not enabled for your merchant account, or the requested QR mode (online/offline) is not enabled for your merchant.
      </td>
      <td style="white-space: normal; word-break: break-word;">
        Contact your PayU account manager to enable <code>sendqrimage</code> in your merchant_param configuration and verify that DBQR or UPI Intent is enabled based on your <code>isMobileUPIQR</code> value.
      </td>
    </tr>
    <tr>
      <td>500</td>
      <td style="white-space: normal; word-break: break-word;">
        <strong>Internal Server Error</strong><br>QR generation failed due to a server-side issue. This could be due to S3 upload failure, image generation failure, or payment gateway error.
      </td>
      <td style="white-space: normal; word-break: break-word;">
        Retry the request after a brief delay. If the issue persists, display error message: "QR unavailable. Retry or choose another payment method." Log the error and contact PayU support if it continues.
      </td>
    </tr>
  </tbody>
</table>


</div>

***
