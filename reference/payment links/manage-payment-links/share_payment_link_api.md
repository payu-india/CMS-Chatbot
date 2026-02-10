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
         --url https://uatoneapi.payu.in/payment-links/ \
         --header 'authorization: Bearer fjsdkglfd09845084395' \
         --header 'content-type: text/plain' \
         --header 'merchantId: 5016764' \
         --data ashish@gmail.com							
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
