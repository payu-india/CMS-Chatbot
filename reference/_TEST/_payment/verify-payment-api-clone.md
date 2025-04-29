---
title: Verify Payment API Clone
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Verify Payment (**verify\_payment**) API gives you the status of the transaction. PayU recommends using this API to reconcile with PayU’s database after you receive the response, where var1 is your transaction ID.

## Reference information for request parameters

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>
      <th>
        Reference
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        key
      </td>
      <td>
        For more information on how to generate the Key and Salt, refer to any of the following:

        * **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
        * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>
    <tr>
      <td>
        hash
      </td>
      <td>
        Hash logic for this API is: sha512(key|command|var1|salt) sha512
      </td>
    </tr>
  </tbody>
</Table>

<GENERALAPIsEnvironment />

## Response parameters and sample response

For the response parameters and sample response, refer to [Additional Info for General APIs](/reference/addl-info-general-apis#response-parameters-for-verify-payment-api).

To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).

<TutorialTile backgroundColor="#018FF4" emoji="🦉" id="65afb6e90a4e0500389d3886" link="https://docs.payu.in/v1/recipes/parse-the-verify-payment-api-response" slug="parse-the-verify-payment-api-response" title="Parse the Verify Payment API response" />

## Request parameters

**Sample values**

Use the following sample values while trying out the API:

* `var1` (your transaction ID/order ID): 7fa6c4783a363b3da573