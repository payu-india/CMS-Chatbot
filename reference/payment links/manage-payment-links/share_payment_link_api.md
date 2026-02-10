---
title: Share Payment Link API
excerpt: ''
api:
  file: payment-link-4.json
  operationId: SharePaymentLinkAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to share the payment link in the given list of email IDs.

**Environment**

|                        |                                                                                                                    |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------- |
| Test Environment       | \<[https://uatoneapi.payu.in/payment-links/`\{id}`/share>](https://uatoneapi.payu.in/payment-links/`\{id}`/share>) |
| Production Environment | \<[https://oneapi.payu.in/payment-links/`\{id}`/share>](https://oneapi.payu.in/payment-links/`\{id}`/share>)       |

<Callout icon="📘" theme="info">
  **Note**: The access token with the scope as **read_payment_links** is required on the header. For more information on getting the access token, refer to [Get Access Token](ref:get-token-api-for-payment-links).
</Callout>

<Accordion title="Sample request" icon="fa-code">
   ```curl
   curl --request POST \
     --url https://uatoneapi.payu.in/payment-links/INV8446471886220/share \
     --header 'authorization: Bearer fjsdkglfd09845084395' \
     --header 'content-type: application/json' \
     --header 'mid: 5016764' \
     --data '{"channelList": ["ashish@gmail.com", "+919876543210"]}'
   ```
   ```python
   import requests
   import json

   url = "https://uatoneapi.payu.in/payment-links/INV8446471886220/share"
   headers = {
       "authorization": "Bearer fjsdkglfd09845084395",
       "content-type": "application/json",
       "mid": "5016764"
   }
   data = {
       "channelList": ["ashish@gmail.com", "+919876543210"]
   }
   response = requests.post(url, headers=headers, data=json.dumps(data))
   print(response.json())
   ```
   ```php
   <?php
   $url = "https://uatoneapi.payu.in/payment-links/INV8446471886220/share";
   $data = json_encode([
       "channelList" => ["ashish@gmail.com", "+919876543210"]
   ]);
   $headers = [
       "authorization: Bearer fjsdkglfd09845084395",
       "content-type: application/json",
       "mid: 5016764"
   ];
   $ch = curl_init($url);
   curl_setopt($ch, CURLOPT_POST, true);
   curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
   curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
   curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
   $response = curl_exec($ch);
   curl_close($ch);
   echo $response;
   ?>
   ```
   ```javascript
   const fetch = require('node-fetch');

   const url = 'https://uatoneapi.payu.in/payment-links/INV8446471886220/share';
   const headers = {
       'authorization': 'Bearer fjsdkglfd09845084395',
       'content-type': 'application/json',
       'mid': '5016764'
   };
   const body = JSON.stringify({
       channelList: ['ashish@gmail.com', '+919876543210']
   });

   fetch(url, {
       method: 'POST',
       headers: headers,
       body: body
   })
   .then(response => response.json())
   .then(data => console.log(data))
   .catch(error => console.error('Error:', error));
   ```
   ```java
   import java.net.HttpURLConnection;
   import java.net.URL;
   import java.io.OutputStream;
   import java.io.BufferedReader;
   import java.io.InputStreamReader;
   import com.google.gson.Gson;
   import java.util.Arrays;
   import java.util.HashMap;
   import java.util.Map;

   public class SharePaymentLink {
       public static void main(String[] args) throws Exception {
           URL url = new URL("https://uatoneapi.payu.in/payment-links/INV8446471886220/share");
           HttpURLConnection conn = (HttpURLConnection) url.openConnection();
           conn.setRequestMethod("POST");
           conn.setRequestProperty("authorization", "Bearer fjsdkglfd09845084395");
           conn.setRequestProperty("content-type", "application/json");
           conn.setRequestProperty("mid", "5016764");
           conn.setDoOutput(true);
           
           Map<String, Object> requestBody = new HashMap<>();
           requestBody.put("channelList", Arrays.asList("ashish@gmail.com", "+919876543210"));
           
           Gson gson = new Gson();
           String jsonInputString = gson.toJson(requestBody);
           
           try (OutputStream os = conn.getOutputStream()) {
               byte[] input = jsonInputString.getBytes("utf-8");
               os.write(input, 0, input.length);
           }
           
           try (BufferedReader br = new BufferedReader(
                   new InputStreamReader(conn.getInputStream(), "utf-8"))) {
               StringBuilder response = new StringBuilder();
               String responseLine = null;
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
              <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantid<br><strong>mandatory</strong></p>
            </td>
              <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This contains the merchant identifier.</p>
            </td>
            </tr>
            <tr>
              <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization<br><strong>mandatory</strong></p>
            </td>
              <td style="border: 1px solid #ddd; padding: 8px;"><p>Bearer <code>String</code> This contains the client_token. For getting a token, refer to <a href="http://docs.payu.in/reference/get_token_api">Get Token API</a></p>
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
              <td style="border: 1px solid #ddd; padding: 8px;"><p>Id<br><strong>mandatory</strong></p>
            </td>
              <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the payment link invoice number.</p>
            </td>
              <td style="border: 1px solid #ddd; padding: 8px;"><p>INV8446471886220</p>
            </td>
            </tr>
            </tbody>
            </table>
  `}</HTMLBlock>
</Accordion>

## Query parameters

<Accordion title="Reference info for request parameters" icon="fa-flask">
  | Parameter   | Reference                                                                                                         |
  | :---------- | :---------------------------------------------------------------------------------------------------------------- |
  | channelList | `String` This parameter must contain all the emails & phone numbers to which the payment link needs to be shared. |
</Accordion>
