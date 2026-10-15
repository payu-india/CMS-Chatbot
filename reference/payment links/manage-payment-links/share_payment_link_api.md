---
excerpt: ''
api:
  file: payment-link-4.json
  operationId: SharePaymentLinkAPI
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to share a payment link with a list of email IDs and/or phone numbers.

**Environment**

|                        |                                                         |
| :--------------------- | :------------------------------------------------------ |
| Test Environment       | `<redacted URL>`    |
| Production Environment | `<redacted URL>`       |

<Callout icon="📘" theme="info">
  **Note**: The access token with the scope as **read_payment_links** is required on the header. For more information on getting the access token, refer to [Get Access Token](ref:get-token-api-for-payment-links).
</Callout>

<Callout icon="🚧" theme="warn">
  **Important**: The `channelList` must be passed as a **query parameter** in the request URL, not in the request body. Separate multiple email IDs and phone numbers with a comma (`,`) and URL-encode the value (for example, `@` becomes `%40` and `,` becomes `%2C`). This request does not require a request body.
</Callout>

<Accordion title="Sample request" icon="fa-code">
   ```curl
   curl --location --request POST '<redacted URL>' \
     --header 'merchantId: 8235900' \
     --header 'Authorization: Bearer <access_token>'
   ```
   ```python
   import requests

   url = "<redacted URL>"
   headers = {
       "merchantId": "8235900",
       "Authorization": "Bearer <access_token>"
   }
   # requests URL-encodes the query parameter value automatically
   params = {
       "channelList": "abc.example@payu.in,9876543210"
   }
   response = requests.post(url, headers=headers, params=params)
   print(response.json())
   ```
   ```php
   <?php
   $baseUrl = "<redacted URL>";
   // http_build_query URL-encodes the query parameter value
   $query = http_build_query([
       "channelList" => "abc.example@payu.in,9876543210"
   ]);
   $url = $baseUrl . "?" . $query;
   $headers = [
       "merchantId: 8235900",
       "Authorization: Bearer <access_token>"
   ];
   $ch = curl_init($url);
   curl_setopt($ch, CURLOPT_POST, true);
   curl_setopt($ch, CURLOPT_POSTFIELDS, "");
   curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
   curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
   $response = curl_exec($ch);
   curl_close($ch);
   echo $response;
   ?>
   ```
   ```javascript
   const fetch = require('node-fetch');

   const baseUrl = '<redacted URL>';
   // URLSearchParams URL-encodes the query parameter value
   const query = new URLSearchParams({
       channelList: 'abc.example@payu.in,9876543210'
   });
   const url = `${baseUrl}?${query.toString()}`;
   const headers = {
       'merchantId': '8235900',
       'Authorization': 'Bearer <access_token>'
   };

   fetch(url, {
       method: 'POST',
       headers: headers
   })
   .then(response => response.json())
   .then(data => console.log(data))
   .catch(error => console.error('Error:', error));
   ```
   ```java
   import java.net.HttpURLConnection;
   import java.net.URL;
   import java.net.URLEncoder;
   import java.nio.charset.StandardCharsets;
   import java.io.BufferedReader;
   import java.io.InputStreamReader;

   public class SharePaymentLink {
       public static void main(String[] args) throws Exception {
           String baseUrl = "<redacted URL>";
           String channelList = URLEncoder.encode("abc.example@payu.in,9876543210", StandardCharsets.UTF_8.toString());
           URL url = new URL(baseUrl + "?channelList=" + channelList);

           HttpURLConnection conn = (HttpURLConnection) url.openConnection();
           conn.setRequestMethod("POST");
           conn.setRequestProperty("merchantId", "8235900");
           conn.setRequestProperty("Authorization", "Bearer <access_token>");
           conn.setDoOutput(true);
           conn.setFixedLengthStreamingMode(0); // No request body

           try (BufferedReader br = new BufferedReader(
                   new InputStreamReader(conn.getInputStream(), "utf-8"))) {
               StringBuilder response = new StringBuilder();
               String responseLine;
               while ((responseLine = br.readLine()) != null) {
                   response.append(responseLine.trim());
               }
               System.out.println(response.toString());
           }
       }
   }
   ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ```json
    {
      "status": 0,
      "message": "string",
      "result": {},
      "errorCode": 170,
      "guid": "f529e375-739f-4c8a-b5f5-0e67fa3f533f"
    }
  ```
</Accordion>

<Accordion title="Request headers" icon="fa-flask">
  <HTMLBlock>{`
            <table style="width: 100%; border-collapse: collapse;">
            <thead>
            <tr>
              <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
              <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantId<br><strong>mandatory</strong></p>
            </td>
              <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This contains the merchant identifier (MID). For example, 8235900.</p>
            </td>
            </tr>
            <tr>
              <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization<br><strong>mandatory</strong></p>
            </td>
              <td style="border: 1px solid #ddd; padding: 8px;"><p>Bearer <code>String</code> This contains the access token in the <code>Bearer &lt;access_token&gt;</code> format. For getting a token, refer to <a href="http://docs.payu.in/reference/get_token_api">Get Token API</a>.</p>
            </td>
            </tr>
            </tbody>
            </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Path parameters" icon="fa-flask">
  <HTMLBlock>{`
            <table style="width: 100%; border-collapse: collapse;">
            <thead>
            <tr>
              <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameters</strong></th>
              <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
              <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td style="border: 1px solid #ddd; padding: 8px;"><p>id<br><strong>mandatory</strong></p>
            </td>
              <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the payment link invoice number.</p>
            </td>
              <td style="border: 1px solid #ddd; padding: 8px;"><p>INV7444229847726</p>
            </td>
            </tr>
            </tbody>
            </table>
  `}</HTMLBlock>
</Accordion>

## Query parameters

<Accordion title="Reference info for query parameters" icon="fa-flask">
  | Parameter                        | Description                                                                                                                                                                                                                                  | Example                                        |
  | :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------- |
  | channelList<br>**mandatory**     | `String` This parameter must contain the email IDs and/or phone numbers to which the payment link needs to be shared. Pass it as a query parameter in the URL, separate multiple values with a comma (`,`), and URL-encode the value. | `abc.example%40payu.in%2C9876543210`           |
</Accordion>
