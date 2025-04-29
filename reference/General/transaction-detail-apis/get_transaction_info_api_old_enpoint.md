---
title: '[Bckup]Get Transaction Info API'
excerpt: 'API Command: **get_transaction_info**'
api:
  file: get-transaction-info-2.json
  operationId: GetTransactionInfo
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: endpoint
      slug: get_transaction_details_api
      title: Get Transaction Details API
    - type: endpoint
      slug: verify_payment_api
      title: Verify Payment API
---
The **Get Transaction Info** API (get *transaction\_info) can take input as the exact time in terms of minutes and seconds the output would be in the same format as\**[get\_Transaction\_Details\*](ref:get_transaction_details_api)\_ API output.

<GENERALAPIsEnvironment />

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
        Hash logic for this API is: sha512(key\|command\|var1\|salt) sha512
      </td>
    </tr>
  </tbody>
</Table>

## Response parameters and sample response

* For the response details in the **transaction\_details** parameter, refer to [Additional Info for General APIs](ref:addl-info-general-apis#json-field-description-for-transaction_details-parameter).
* For sample response, refer to [Additional Info for General APIs](ref:addl-info-general-apis#sample-response-for-get-transaction-details).

To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).

## Request parameters

**Sample values**

Use the following sample values while trying out the API:

* `var1`: 2020-10-20 16:00:00
* `var2`: 2020-10-26 18:00:00