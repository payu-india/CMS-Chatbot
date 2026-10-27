---
title: PACB Import- Direct Authorization Cards Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
<Banner color="#FFC107">Developer integration required: server-to-server API</Banner>

This page explains how to integrate Direct Authorization for cross-border card payments with the server-to-server (S2S) flow. Use it when you've already completed 3DS authentication through your own MPI (Merchant Plug-In) or 3DS Server, and want PayU to authorize the pre-authenticated transaction.

<Callout icon="📘" theme="info">
  ### **Note**

  **When to use Direct Authorization:** you have your own MPI or 3DS Server and have already authenticated the cardholder. PayU skips its own authentication and authorizes the transaction directly.
</Callout>

<Cards columns="3">
  <Card title="1. Post Parameters to PayU" href="#step-1-post-parameters-to-payu">
    Send the card details and 3DS authentication data.
  </Card>

  <Card title="2. Check the Response from PayU" href="#step-2-check-the-response-from-payu">
    Decode the response and check its hash.
  </Card>

  <Card title="3. Verify the Payment" href="#step-3-verify-the-payment">
    Confirm the final payment status.
  </Card>

  <Card title="4. Update Invoice ID (Conditional)" href="#step-4-update-invoice-id-conditional">
    Add the invoice ID if you didn't send it.
  </Card>

  <Card title="5. Upload Invoices and Shipping Documents" href="#step-5-upload-invoices-and-shipping-documents">
    Required within 10 days of the payment.
  </Card>
</Cards>

***

## Step 1: Post Parameters to PayU

Post the payment parameters and 3DS authentication data to PayU's `_payment` API. Compared with the standard S2S flow:

- Set `txn_s2s_flow` to **3** (Direct Authorization).
- Send the 3DS authentication data from your MPI or 3DS Server in `authentication_info`.
- Send the 3DS version and device channel in `threeDS2RequestData`.

<Callout icon="📘" theme="info">
  ### **Note**

  For more information on the standard Direct Authorization flow, refer to <Anchor target="_blank" href="doc:integrate-with-direct-authorization-s2s">Direct Authorization Integration</Anchor>.
</Callout>

<Accordion title="Environment" icon="fa-server">
  | Environment | URL                               |
  | ----------- | --------------------------------- |
  | Test        | `https://test.payu.in/_payment`   |
  | Production  | `https://secure.payu.in/_payment` |

  **HTTP method:** POST

  **Content type:** `application/x-www-form-urlencoded`
</Accordion>

<Tabs>
  <Tab title="Request Parameters">
    #### Mandatory Parameters

    | Parameter                 | Type          | Description                                                                                                                                                               | Example                                            |
    | ------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
    | <Glossary>key</Glossary>  | `String`      | Merchant key provided by PayU during onboarding.                                                                                                                          | `JPM7Fg`                                           |
    | `txnid`                   | `String`      | Unique transaction ID that you generate for the order.                                                                                                                    | `PACB_DA_12345`                                    |
    | `amount`                  | `String`      | Payment amount.                                                                                                                                                           | `100.00`                                           |
    | `productinfo`             | `String`      | Name or short description of the goods or services. Character limit: 100.                                                                                                 | `Cross-border Product`                             |
    | `firstname`               | `String`      | Customer's first name. Character limit: 60.                                                                                                                               | `Ashish`                                           |
    | `email`                   | `String`      | Customer's email address. Character limit: 50.                                                                                                                            | `test@gmail.com`                                   |
    | `phone`                   | `String`      | Customer's phone number.                                                                                                                                                  | `9876543210`                                       |
    | `pg`                      | `String`      | Payment category. For cards, use `CC`.                                                                                                                                    | `CC`                                               |
    | `bankcode`                | `String`      | Bank code. Use `CC` for credit cards and `DC` for debit cards.                                                                                                            | `CC`                                               |
    | `ccnum`                   | `String`      | Card number: 13–19 digits (15 for AMEX, 13–19 for Maestro). Validate it with the Luhn algorithm.                                                                          | `5123456789012346`                                 |
    | `ccvv`                    | `String`      | <Glossary>CVV</Glossary>: 3 digits (4 for AMEX).                                                                                                                          | `123`                                              |
    | `ccname`                  | `String`      | Cardholder name as entered by the customer.                                                                                                                               | `Ashish Kumar`                                     |
    | `ccexpmon`                | `String`      | Card expiry month in MM format (01–12).                                                                                                                                   | `10`                                               |
    | `ccexpyr`                 | `String`      | Card expiry year in YYYY format.                                                                                                                                          | `2030`                                             |
    | `zipcode`                 | `String`      | Billing postal code. Character limit: 6 digits (India PIN code).                                                                                                          | `110001`                                           |
    | `txn_s2s_flow`            | `String`      | Must be `3` for Direct Authorization. Tells PayU the transaction was already authenticated by your MPI or 3DS Server.                                                     | `3`                                                |
    | `authentication_info`     | `JSON String` | 3DS authentication data from your MPI or 3DS Server. See **authentication_info object** below.                                                                            | See below                                          |
    | `threeDS2RequestData`     | `JSON String` | 3DS version and device channel.                                                                                                                                           | `{"threeDSVersion":"2.2.0","deviceChannel":"BRW"}` |
    | `s2s_client_ip`           | `String`      | IP address of the customer's device. Used for <Glossary>fraud detection</Glossary>.                                                                                       | `10.200.12.12`                                     |
    | `s2s_device_info`         | `String`      | User agent of the customer's device.                                                                                                                                      | `Mozilla/5.0 (Windows NT 10.0; Win64; x64)`        |
    | `surl`                    | `String`      | <Glossary>surl</Glossary> Success URL. Required, but with `txn_s2s_flow=3` no redirect happens and you get the result as an S2S response. You can pass a placeholder URL. | `https://example.com/success`                      |
    | `furl`                    | `String`      | <Glossary>furl</Glossary> Failure URL. Required, but with `txn_s2s_flow=3` no redirect happens. You can pass a placeholder URL.                                           | `https://example.com/failure`                      |
    | `udf5`                    | `String`      | Invoice ID, as shown on the invoice issued to the customer. If you don't have it yet, add it later in Step 4. Character limit: 255.                                       | `INV123456`                                        |
    | `udf4`                    | `String`      | _(Mandatory for payment aggregators)_ End merchant's legal entity name. Character limit: 255.                                                                             | `XYZ Pvt. Ltd.`                                    |
    | <Glossary>hash</Glossary> | `String`      | SHA-512 hash calculated on your server. See **Hash generation** below.                                                                                                    | `YOUR_GENERATED_HASH`                              |

    #### Optional Parameters

    | Parameter             | Type          | Description                                                                                                                                                                                                         | Example                                      |
    | --------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
    | `address1`            | `String`      | _(Recommended for higher approval rate)_ First line of the billing address. Used for billing and <Glossary>fraud</Glossary> prevention. Character limit: 255.                                                       | `123 Main Street`                            |
    | `city`                | `String`      | _(Recommended for higher approval rate)_ Billing city. Character limit: 50.                                                                                                                                         | `New Delhi`                                  |
    | `state`               | `String`      | _(Recommended for higher approval rate)_ Billing state or province. Character limit: 50.                                                                                                                            | `Delhi`                                      |
    | `country`             | `String`      | _(Recommended for higher approval rate)_ Billing country as an ISO 3166-1 alpha-2 code. Character limit: 2.                                                                                                         | `IN`                                         |
    | `udf1`                | `String`      | _(Recommended for higher approval rate)_ Buyer's PAN (Permanent Account Number, India's main tax ID). Character limit: 10.                                                                                          | `ABCDE1234K`                                 |
    | `udf2`                | `String`      | Any extra information about the transaction. Character limit: 255.                                                                                                                                                  | `Additional data`                            |
    | `udf3`                | `String`      | _(Recommended for higher approval rate)_ Buyer's date of birth in DD-MM-YYYY format.                                                                                                                                | `02-02-1980`                                 |
    | `buyer_type_business` | `String`      | _(B2B transactions)_ Send `1` if the buyer is a business. The default is `0`. If you send it, include it in the hash.                                                                                               | `1`                                          |
    | `udf_params`          | `JSON String` | Additional <Glossary>UDFs</Glossary>: `udf7` for the buyer's Import Export Code (IEC) and `udf8` for the airway bill (AWB) or consignment number for goods. If you send it, include it in the hash exactly as sent. | `{"udf7":"0100000029","udf8":"99953729071"}` |

    <Callout icon="📘" theme="info">
      ### **Note**

      - Send `udf1` to `udf5` as separate parameters. Don't send `udf6`; it's reserved.
      - Fields from `udf7` onwards, such as the IEC and AWB number, go only inside `udf_params`. Ask PayU to enable additional UDFs for your account before you send `udf_params`.
    </Callout>

    <Accordion title="authentication_info object" icon="fa-code">
      Send the 3DS authentication data from your MPI or 3DS Server in this JSON format:

      ```json
      {
        "eci": "05",
        "cavv": "AAABAWFlmQAAAABjRWWZEEFgFz+=",
        "flowType": "Frictionless",
        "threeDSTransID": "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
        "threeDSServerTransID": "eea30d14-71cf-41af-b961-f95b7d67dc93",
        "threeDSTransStatus": "Y",
        "threeDSTransStatusReason": "01",
        "acquirer_bin": "401200",
        "additionalinfo": {
          "authudf2": "custom_auth_data"
        }
      }
      ```

      | Field                      | Description                                                                                                                        | Required |
      | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------- |
      | `eci`                      | <Glossary>ECI</Glossary> Electronic Commerce Indicator. `05`/`02` authenticated, `06`/`01` attempted, `07`/`00` not authenticated. | Yes      |
      | `cavv`                     | <Glossary>CAVV</Glossary> Cardholder Authentication Verification Value from the 3DS Server.                                        | Yes      |
      | `flowType`                 | `Frictionless` or `Challenge`.                                                                                                     | Yes      |
      | `threeDSTransID`           | 3DS transaction ID.                                                                                                                | Yes      |
      | `threeDSServerTransID`     | 3DS Server transaction ID.                                                                                                         | Yes      |
      | `threeDSTransStatus`       | `Y` authenticated, `A` attempted, `N` not authenticated, `U` technical error, `R` rejected, `C` challenge required.                | Yes      |
      | `threeDSTransStatusReason` | Status reason code (01–99).                                                                                                        | No       |
      | `acquirer_bin`             | Acquirer BIN.                                                                                                                      | No       |
      | `additionalinfo`           | Extra authentication data as key-value pairs.                                                                                      | No       |
    </Accordion>

    <Accordion title="threeDS2RequestData object" icon="fa-code">
      ```json
      {
        "threeDSVersion": "2.2.0",
        "deviceChannel": "BRW"
      }
      ```

      | Field            | Description                      | Values                               |
      | ---------------- | -------------------------------- | ------------------------------------ |
      | `threeDSVersion` | 3DS protocol version.            | `2.1.0`, `2.2.0`                     |
      | `deviceChannel`  | Channel used for authentication. | `BRW` (browser), `APP` (application) |
    </Accordion>

    <Accordion title="ECI values by card network" icon="fa-info-circle">
      | Network    | Authenticated | Attempted | Not authenticated |
      | ---------- | ------------- | --------- | ----------------- |
      | Visa       | 05            | 06        | 07                |
      | Mastercard | 02            | 01        | 00                |
      | AMEX       | 05            | 06        | 07                |
    </Accordion>

    #### Hashing

    -
    - Notes: use empty strings for missing fields, compute server-side, lowercase hex

    <Accordion title="Sample Code for Hashing" icon="far fa-code">
      <HashingSample />
    </Accordion>
  </Tab>

  <Tab title="Sample Request">
    ```curl
    curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode 'key=JPM7Fg' \
    --data-urlencode 'txnid=PACB_DA_20240101_12345' \
    --data-urlencode 'amount=100.00' \
    --data-urlencode 'firstname=Ashish' \
    --data-urlencode 'lastname=Kumar' \
    --data-urlencode 'email=test@payu.in' \
    --data-urlencode 'phone=9876543210' \
    --data-urlencode 'productinfo=Cross-border Product Purchase' \
    --data-urlencode 'address1=123 Main Street' \
    --data-urlencode 'city=New Delhi' \
    --data-urlencode 'state=Delhi' \
    --data-urlencode 'country=IN' \
    --data-urlencode 'zipcode=110001' \
    --data-urlencode 'surl=https://example.com/success' \
    --data-urlencode 'furl=https://example.com/failure' \
    --data-urlencode 'pg=CC' \
    --data-urlencode 'bankcode=CC' \
    --data-urlencode 'ccnum=5123456789012346' \
    --data-urlencode 'ccname=Ashish Kumar' \
    --data-urlencode 'ccvv=123' \
    --data-urlencode 'ccexpmon=10' \
    --data-urlencode 'ccexpyr=2030' \
    --data-urlencode 'txn_s2s_flow=3' \
    --data-urlencode 'authentication_info={"eci":"05","cavv":"AAABAWFlmQAAAABjRWWZEEFgFz+=","flowType":"Frictionless","threeDSTransID":"67b4c71f-19bf-4d97-bd09-4e3687dc9e42","threeDSServerTransID":"eea30d14-71cf-41af-b961-f95b7d67dc93","threeDSTransStatus":"Y","threeDSTransStatusReason":"01","acquirer_bin":"401200"}' \
    --data-urlencode 'threeDS2RequestData={"threeDSVersion":"2.2.0","deviceChannel":"BRW"}' \
    --data-urlencode 's2s_client_ip=10.200.12.12' \
    --data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
    --data-urlencode 'udf1=ABCDE1234K' \
    --data-urlencode 'udf2=' \
    --data-urlencode 'udf3=02-02-1980' \
    --data-urlencode 'udf4=XYZ Pvt. Ltd.' \
    --data-urlencode 'udf5=INV123456' \
    --data-urlencode 'buyer_type_business=1' \
    --data-urlencode 'udf_params={"udf7":"0100000029","udf8":"99953729071"}' \
    --data-urlencode 'hash=YOUR_GENERATED_HASH'
    ```
    ```python
    import hashlib
    import json
    import os
    import requests

    url = "https://test.payu.in/_payment"
    headers = {"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

    # 3DS authentication data from your MPI or 3DS Server
    authentication_info = {
        "eci": "05",
        "cavv": "AAABAWFlmQAAAABjRWWZEEFgFz+=",
        "flowType": "Frictionless",
        "threeDSTransID": "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
        "threeDSServerTransID": "eea30d14-71cf-41af-b961-f95b7d67dc93",
        "threeDSTransStatus": "Y",
        "threeDSTransStatusReason": "01",
        "acquirer_bin": "401200",
    }
    three_ds2_request_data = {"threeDSVersion": "2.2.0", "deviceChannel": "BRW"}
    udf_params = json.dumps({"udf7": "0100000029", "udf8": "99953729071"}, separators=(",", ":"))

    key = "JPM7Fg"
    salt = os.environ["PAYU_SALT"]  # Keep the salt on your server only
    txnid = "PACB_DA_20240101_12345"
    amount = "100.00"
    productinfo = "Cross-border Product Purchase"
    firstname = "Ashish"
    email = "test@payu.in"
    udf1, udf2, udf3, udf4, udf5 = "ABCDE1234K", "", "02-02-1980", "XYZ Pvt. Ltd.", "INV123456"
    buyer_type_business = "1"

    # udf_params and buyer_type_business are sent, so both go into the hash, after the salt
    hash_string = (f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|"
                   f"{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}|{udf_params}|{buyer_type_business}")
    hash_value = hashlib.sha512(hash_string.encode("utf-8")).hexdigest()

    data = {
        "key": key, "txnid": txnid, "amount": amount,
        "firstname": firstname, "lastname": "Kumar", "email": email, "phone": "9876543210",
        "productinfo": productinfo,
        "address1": "123 Main Street", "city": "New Delhi", "state": "Delhi",
        "country": "IN", "zipcode": "110001",
        "surl": "https://example.com/success", "furl": "https://example.com/failure",
        "pg": "CC", "bankcode": "CC",
        "ccnum": "5123456789012346", "ccname": "Ashish Kumar", "ccvv": "123",
        "ccexpmon": "10", "ccexpyr": "2030",
        "txn_s2s_flow": "3",
        "authentication_info": json.dumps(authentication_info),
        "threeDS2RequestData": json.dumps(three_ds2_request_data),
        "s2s_client_ip": "10.200.12.12",
        "s2s_device_info": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "udf1": udf1, "udf2": udf2, "udf3": udf3, "udf4": udf4, "udf5": udf5,
        "buyer_type_business": buyer_type_business,
        "udf_params": udf_params,
        "hash": hash_value,
    }

    response = requests.post(url, headers=headers, data=data)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
    ```
    ```javascript
    const crypto = require("crypto");

    const SALT = process.env.PAYU_SALT; // Keep the salt on your server only

    const params = {
      key: "JPM7Fg",
      txnid: "PACB_DA_20240101_12345",
      amount: "100.00",
      productinfo: "Cross-border Product Purchase",
      firstname: "Ashish",
      lastname: "Kumar",
      email: "test@payu.in",
      phone: "9876543210",
      address1: "123 Main Street",
      city: "New Delhi",
      state: "Delhi",
      country: "IN",
      zipcode: "110001",
      surl: "https://example.com/success",
      furl: "https://example.com/failure",
      pg: "CC",
      bankcode: "CC",
      ccnum: "5123456789012346",
      ccname: "Ashish Kumar",
      ccvv: "123",
      ccexpmon: "10",
      ccexpyr: "2030",
      txn_s2s_flow: "3",
      authentication_info: JSON.stringify({
        eci: "05",
        cavv: "AAABAWFlmQAAAABjRWWZEEFgFz+=",
        flowType: "Frictionless",
        threeDSTransID: "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
        threeDSServerTransID: "eea30d14-71cf-41af-b961-f95b7d67dc93",
        threeDSTransStatus: "Y",
        threeDSTransStatusReason: "01",
        acquirer_bin: "401200",
      }),
      threeDS2RequestData: JSON.stringify({ threeDSVersion: "2.2.0", deviceChannel: "BRW" }),
      s2s_client_ip: "10.200.12.12",
      s2s_device_info: "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
      udf1: "ABCDE1234K",
      udf2: "",
      udf3: "02-02-1980",
      udf4: "XYZ Pvt. Ltd.",
      udf5: "INV123456",
      buyer_type_business: "1",
      udf_params: '{"udf7":"0100000029","udf8":"99953729071"}',
    };

    const hashFields = ["key", "txnid", "amount", "productinfo", "firstname", "email",
      "udf1", "udf2", "udf3", "udf4", "udf5"];
    const hashString = hashFields.map((f) => params[f]).join("|") + "||||||" + SALT
      + "|" + params.udf_params + "|" + params.buyer_type_business;
    params.hash = crypto.createHash("sha512").update(hashString).digest("hex");

    (async () => {
      const res = await fetch("https://test.payu.in/_payment", {
        method: "POST",
        headers: { accept: "application/json", "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams(params),
      });
      console.log(await res.text());
    })();
    ```
    ```java
    import java.net.URI;
    import java.net.URLEncoder;
    import java.net.http.HttpClient;
    import java.net.http.HttpRequest;
    import java.net.http.HttpResponse;
    import java.nio.charset.StandardCharsets;
    import java.util.LinkedHashMap;
    import java.util.Map;
    import java.util.stream.Collectors;

    public class PACBDirectAuthPayment {
        public static void main(String[] args) throws Exception {
            String url = "https://test.payu.in/_payment";

            // 3DS authentication data from your MPI or 3DS Server
            String authenticationInfo = "{\"eci\":\"05\",\"cavv\":\"AAABAWFlmQAAAABjRWWZEEFgFz+=\",\"flowType\":\"Frictionless\",\"threeDSTransID\":\"67b4c71f-19bf-4d97-bd09-4e3687dc9e42\",\"threeDSServerTransID\":\"eea30d14-71cf-41af-b961-f95b7d67dc93\",\"threeDSTransStatus\":\"Y\",\"threeDSTransStatusReason\":\"01\",\"acquirer_bin\":\"401200\"}";
            String threeDS2RequestData = "{\"threeDSVersion\":\"2.2.0\",\"deviceChannel\":\"BRW\"}";
            String udfParams = "{\"udf7\":\"0100000029\",\"udf8\":\"99953729071\"}";

            Map<String, String> formData = new LinkedHashMap<>();
            formData.put("key", "JPM7Fg");
            formData.put("txnid", "PACB_DA_20240101_12345");
            formData.put("amount", "100.00");
            formData.put("firstname", "Ashish");
            formData.put("lastname", "Kumar");
            formData.put("email", "test@payu.in");
            formData.put("phone", "9876543210");
            formData.put("productinfo", "Cross-border Product Purchase");
            formData.put("address1", "123 Main Street");
            formData.put("city", "New Delhi");
            formData.put("state", "Delhi");
            formData.put("country", "IN");
            formData.put("zipcode", "110001");
            formData.put("surl", "https://example.com/success");
            formData.put("furl", "https://example.com/failure");
            formData.put("pg", "CC");
            formData.put("bankcode", "CC");
            formData.put("ccnum", "5123456789012346");
            formData.put("ccname", "Ashish Kumar");
            formData.put("ccvv", "123");
            formData.put("ccexpmon", "10");
            formData.put("ccexpyr", "2030");
            formData.put("txn_s2s_flow", "3");
            formData.put("authentication_info", authenticationInfo);
            formData.put("threeDS2RequestData", threeDS2RequestData);
            formData.put("s2s_client_ip", "10.200.12.12");
            formData.put("s2s_device_info", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)");
            formData.put("udf1", "ABCDE1234K");
            formData.put("udf3", "02-02-1980");
            formData.put("udf4", "XYZ Pvt. Ltd.");
            formData.put("udf5", "INV123456");
            formData.put("buyer_type_business", "1");
            formData.put("udf_params", udfParams);
            formData.put("hash", "YOUR_GENERATED_HASH"); // generate on your server

            String formBody = formData.entrySet().stream()
                .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "="
                        + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
                .collect(Collectors.joining("&"));

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(formBody))
                .build();

            HttpResponse<String> response = HttpClient.newHttpClient()
                .send(request, HttpResponse.BodyHandlers.ofString());

            System.out.println("Status Code: " + response.statusCode());
            System.out.println("Response: " + response.body());
        }
    }
    ```
    ```php
    <?php
    $url = "https://test.payu.in/_payment";

    // 3DS authentication data from your MPI or 3DS Server
    $authenticationInfo = json_encode([
        "eci" => "05",
        "cavv" => "AAABAWFlmQAAAABjRWWZEEFgFz+=",
        "flowType" => "Frictionless",
        "threeDSTransID" => "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
        "threeDSServerTransID" => "eea30d14-71cf-41af-b961-f95b7d67dc93",
        "threeDSTransStatus" => "Y",
        "threeDSTransStatusReason" => "01",
        "acquirer_bin" => "401200"
    ]);
    $threeDS2RequestData = json_encode(["threeDSVersion" => "2.2.0", "deviceChannel" => "BRW"]);
    $udfParams = json_encode(["udf7" => "0100000029", "udf8" => "99953729071"]);

    $key = "JPM7Fg";
    $salt = getenv('PAYU_SALT'); // Keep the salt on your server only
    $txnid = "PACB_DA_20240101_12345";
    $amount = "100.00";
    $productinfo = "Cross-border Product Purchase";
    $firstname = "Ashish";
    $email = "test@payu.in";
    $udf1 = "ABCDE1234K";
    $udf3 = "02-02-1980";
    $udf4 = "XYZ Pvt. Ltd.";
    $udf5 = "INV123456";
    $buyerTypeBusiness = "1";

    // udf_params and buyer_type_business are sent, so both go into the hash, after the salt
    $hashString = "$key|$txnid|$amount|$productinfo|$firstname|$email|$udf1||$udf3|$udf4|$udf5||||||$salt|$udfParams|$buyerTypeBusiness";
    $hash = hash('sha512', $hashString);

    $data = [
        'key' => $key, 'txnid' => $txnid, 'amount' => $amount,
        'firstname' => $firstname, 'lastname' => 'Kumar', 'email' => $email, 'phone' => '9876543210',
        'productinfo' => $productinfo,
        'address1' => '123 Main Street', 'city' => 'New Delhi', 'state' => 'Delhi',
        'country' => 'IN', 'zipcode' => '110001',
        'surl' => 'https://example.com/success', 'furl' => 'https://example.com/failure',
        'pg' => 'CC', 'bankcode' => 'CC',
        'ccnum' => '5123456789012346', 'ccname' => 'Ashish Kumar', 'ccvv' => '123',
        'ccexpmon' => '10', 'ccexpyr' => '2030',
        'txn_s2s_flow' => '3',
        'authentication_info' => $authenticationInfo,
        'threeDS2RequestData' => $threeDS2RequestData,
        's2s_client_ip' => '10.200.12.12',
        's2s_device_info' => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'udf1' => $udf1, 'udf2' => '', 'udf3' => $udf3, 'udf4' => $udf4, 'udf5' => $udf5,
        'buyer_type_business' => $buyerTypeBusiness,
        'udf_params' => $udfParams,
        'hash' => $hash
    ];

    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => http_build_query($data),
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER => ['accept: application/json', 'Content-Type: application/x-www-form-urlencoded'],
    ]);
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response . "\n";
    ```
  </Tab>
</Tabs>

<Accordion title="Hash generation" icon="fa-lock">
  <PACB_Hashing />

  **Standard formula:**

  ```plaintext
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt)
  ```

  **With buyer_type_business:**

  ```plaintext
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt|buyer_type_business)
  ```

  **With udf_params and buyer_type_business:**

  ```plaintext
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|si_details|salt|udf_params|buyer_type_business)
  ```

  {/* REVIEW (C10 not applied, as requested): the formulas above are kept from the draft. The code samples follow the Confluence order (…|salt|udf_params|buyer_type_business, appended only when sent). */}

  <Callout icon="🚧" theme="warn">
    ### **Critical Rules**

    - If you send `udf_params`, include it in the hash exactly as sent, or the hash check fails.
    - Generate the hash on your server only. Use the [PayU Hash Verification Tool](doc:using-payu-hash-verification-tool) to check it.
  </Callout>
</Accordion>

<Accordion title="Response parameters" icon="fa-table">
  The Direct Authorization response is a base64-encoded JSON string. After decoding, it contains:

  | Parameter               | Description                                                     | Example                     |
  | ----------------------- | --------------------------------------------------------------- | --------------------------- |
  | `status`                | `String` Overall API status: `success` or `failure`.            | `success`                   |
  | `result.mihpayid`       | `String` PayU's unique transaction ID.                          | `16313939584`               |
  | `result.mode`           | `String` Payment mode, for example `CC` for credit card.        | `CC`                        |
  | `result.status`         | `String` Transaction status: `success`, `failure` or `pending`. | `success`                   |
  | `result.txnid`          | `String` Your transaction ID.                                   | `PACB_DA_20240101_12345`    |
  | `result.amount`         | `String` Transaction amount.                                    | `100.00`                    |
  | `result.payment_source` | `String` Always `dirAuthS2S` for Direct Authorization.          | `dirAuthS2S`                |
  | `result.bank_ref_no`    | `String` Bank reference number.                                 | `221130127055`              |
  | `result.bankcode`       | `String` Bank code (card network).                              | `MAST`                      |
  | `result.error`          | `String` Error code. `E000` means no error.                     | `E000`                      |
  | `result.error_Message`  | `String` Error message.                                         | `No Error`                  |
  | `result.unmappedstatus` | `String` Detailed status: `captured`, `auth` or `failed`.       | `captured`                  |
  | `result.card_no`        | `String` Masked card number.                                    | `XXXXXXXXXXXX2346`          |
  | `result.hash`           | `String` Response hash. Check it before you update the order.   | SHA-512 hash                |
  | `result.field7`         | `String` Authorization status.                                  | `AUTHPOSITIVE`              |
  | `result.field8`         | `String` Bank response.                                         | `APPROVED`                  |
  | `result.field9`         | `String` Transaction message.                                   | `Transaction is Successful` |
</Accordion>

***

## Step 2: Check the Response from PayU

PayU sets the transaction status based on the bank's response. For Direct Authorization, the response comes back directly as a base64-encoded JSON string, not through a redirect.

{/* REVIEW (C20): the page says the response is base64-encoded JSON, but the second success sample uses a metaData/result/binData layout and the failure sample was PHP "Array" output (converted to JSON here). Confirm the real response format and replace the samples. All customer and merchant values below are placeholders. */}

<Accordion title="Sample response" icon="fa-reply">
  **Success**

  The decoded response:

  ```json
  {
    "status": "success",
    "result": {
      "mihpayid": "16313939584",
      "mode": "CC",
      "status": "success",
      "key": "JPM7Fg",
      "txnid": "PACB_DA_20240101_12345",
      "amount": "100.00",
      "addedon": "2024-01-01 12:00:00",
      "productinfo": "Cross-border Product Purchase",
      "firstname": "Ashish",
      "lastname": "Kumar",
      "address1": "123 Main Street",
      "city": "New Delhi",
      "state": "Delhi",
      "country": "IN",
      "zipcode": "110001",
      "email": "test@payu.in",
      "phone": "9876543210",
      "udf1": "ABCDE1234K",
      "udf2": "",
      "udf3": "02-02-1980",
      "udf4": "XYZ Pvt. Ltd.",
      "udf5": "INV123456",
      "card_no": "XXXXXXXXXXXX2346",
      "field6": "000",
      "field7": "AUTHPOSITIVE",
      "field8": "APPROVED",
      "field9": "Transaction is Successful",
      "payment_source": "dirAuthS2S",
      "PG_TYPE": "CC-PG",
      "error": "E000",
      "error_Message": "No Error",
      "net_amount_debit": "100",
      "unmappedstatus": "captured",
      "hash": "YOUR_RESPONSE_HASH",
      "bank_ref_no": "240101127055",
      "bank_ref_num": "240101127055",
      "bankcode": "MAST"
    }
  }
  ```

  **Captured, but the card wasn't tokenized (the amount is still debited)**

  ```json
  {
    "metaData": {
      "message": "No Error",
      "referenceId": "0b76e6f43781101972cf69b8e6e95489",
      "statusCode": "E000",
      "txnId": "PACB_DA_20240101_12346",
      "unmappedStatus": "success"
    },
    "result": {
      "mihpayid": "28192801355",
      "mode": "CC",
      "status": "success",
      "key": "JPM7Fg",
      "txnid": "PACB_DA_20240101_12346",
      "amount": "100.00",
      "addedon": "2026-04-16 00:23:53",
      "productinfo": "Direct Authorization",
      "firstname": "Ashish",
      "lastname": "Kumar",
      "address1": "123 Main Street",
      "address2": "",
      "city": "New Delhi",
      "state": "DL",
      "country": "IN",
      "zipcode": "110001",
      "email": "",
      "phone": "",
      "udf1": "",
      "udf2": "",
      "udf3": "",
      "udf4": "",
      "udf5": "INV123456",
      "udf6": "",
      "udf7": "",
      "udf8": "",
      "udf9": "",
      "udf10": "",
      "card_token": "",
      "card_no": "XXXXXXXXXXXX3004",
      "field2": "482380",
      "field6": "00",
      "field7": "AUTHPOSITIVE",
      "field8": "Transaction successful",
      "field9": "Transaction is Successful",
      "payment_source": "dirAuthS2S",
      "cardToken": "",
      "PG_TYPE": "CC-PG",
      "error": "E000",
      "error_Message": "No Error",
      "net_amount_debit": "100",
      "discount": "0.00",
      "unmappedstatus": "captured",
      "hash": "YOUR_RESPONSE_HASH",
      "bank_ref_no": "610600388883",
      "bank_ref_num": "610600388883",
      "bankcode": "CC",
      "surl": "https://example.com/success",
      "furl": "https://example.com/failure"
    },
    "binData": {
      "pureS2SSupported": true,
      "issuingBank": "ICICI",
      "category": "creditcard",
      "cardType": "MAST",
      "isDomestic": true
    }
  }
  ```

  **Failure: declined because of a wrong CVV or expiry, or card validation failed**

  ```json
  {
    "mihpayid": "28192699814",
    "mode": "DC",
    "status": "failure",
    "key": "JPM7Fg",
    "txnid": "PACB_DA_20240101_12347",
    "amount": "1.00",
    "addedon": "2026-04-16 00:05:43",
    "productinfo": "Cross-border Product Purchase",
    "firstname": "Ashish",
    "lastname": "Kumar",
    "city": "New Delhi",
    "state": "DL",
    "country": "IN",
    "zipcode": "110001",
    "udf5": "INV123456",
    "card_no": "XXXXXXXXXXXX0825",
    "field5": "N7",
    "field6": "05",
    "field7": "AUTHNEGATIVE",
    "field8": "N7 | Decline - Invalid Card Verification Number (CVN).",
    "field9": "Transaction declined due to either incorrect cvv/expiry or card validation failure",
    "payment_source": "dirAuthS2S",
    "PG_TYPE": "DC-PG",
    "error": "E1632",
    "error_Message": "Transaction declined due to either incorrect cvv/expiry or card validation failure",
    "net_amount_debit": "0",
    "unmappedstatus": "failed",
    "hash": "YOUR_RESPONSE_HASH",
    "bankcode": "VISA"
  }
  ```
</Accordion>

<Accordion title="Decode the response" icon="fa-code">
  ```python
  import base64
  import json

  response_text = "base64_encoded_response_string"
  data = json.loads(base64.b64decode(response_text).decode("utf-8"))

  print(f"Status: {data['result']['status']}")
  print(f"PayU ID: {data['result']['mihpayid']}")
  ```
</Accordion>

<Accordion title="Verify the response hash" icon="fa-lock">
  Always check the response hash before you accept or reject the transaction.

  ```plaintext
  sha512(salt|status||||||udf10|udf9|udf8|udf7|udf6|udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  <Callout icon="📘" theme="info">
    ### **Note**

    For Direct Authorization, `payment_source` is always `dirAuthS2S`.
  </Callout>
</Accordion>

***

## Step 3: Verify the Payment

<PACB_Verify_Payment />

***

## Step 4: Update Invoice ID (Conditional)

<Update_Invoice_ID />

***

## Step 5: Upload Invoices and Shipping Documents

<Callout icon="🚧" theme="warn">
  ### **Watch Out!**

  - Upload the invoice within **10 days** of the transaction. If you don't, your next settlement is put on hold.
  - Goods merchants must upload the invoice and the airway bill (AWB) separately, so that's two Invoice Upload calls per payment.
</Callout>

<Upload_Invoices />

***

## Error Handling

If you get an error code, refer to [Error Codes](ref:error-codes) for the reason. For errors at each transaction stage, refer to [Transaction Stages - Error References](ref:transaction-stages-error-references-on-field7-field8).

{/* REVIEW (C20): E001–E004 below aren't documented in Confluence. Confirm or remove before publishing. */}

| Error code | Description                    | What to do                                         |
| ---------- | ------------------------------ | -------------------------------------------------- |
| E000       | No error                       | The transaction succeeded.                         |
| E001       | Invalid authentication_info    | Check the JSON structure and all required fields.  |
| E002       | Invalid ECI value              | Check that the ECI value matches the card network. |
| E003       | CAVV validation failed         | Check that the CAVV from your MPI is correct.      |
| E004       | 3DS transaction status invalid | Check that `threeDSTransStatus` is `Y` or `A`.     |

<Callout icon="📘" theme="info">
  ### **Note**

  For the character limit and full description of each parameter, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Callout>

***

## Next Steps

<Cards columns="3">
  <Card title="Plain Cards Integration" href="/docs/plain-cards-integration-one-time-pacb">
    Let PayU handle authentication.
  </Card>

  <Card title="Saved Cards with a Network Token" href="/docs/network-tokens-one-time-payment-pacb">
    Pay with a network token.
  </Card>

  <Card title="FAQs" href="/docs/faqs-for-cross-border-payments">
    Answers about UDFs, invoices and settlement.
  </Card>
</Cards>
