---
title: Get User Cards API - Model 3
excerpt: ''
api:
  file: storecard-1.json
  operationId: get_payment_instrument
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get User Cards** API is used to fetch all the cards corresponding to the user. In this API, the card number and other sensitive information are not returned.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

## Response parameters

For the response parameters and sample responses, refer to [Additional Info for Model 3 Parameters](ref:additional-info-for-model-3-parameters).

## Reference info for request parameters

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>key</td>
      <td>
        The merchant key provided by PayU while onboarding.
        For more information on how to generate the Key and Salt, refer to any of the following:

        * **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
        * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>
    <tr>
      <td>hash</td>
      <td>
        Hash logic for this API is:
        ```
        sha512(key|command|var1|salt) sha512
        ```
      </td>
    </tr>
  </tbody>
</Table>

## Request parameters