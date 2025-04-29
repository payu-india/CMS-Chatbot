---
title: '[Bckup]Get All Refunds from Transaction IDs'
excerpt: 'API Command: **getAllRefundsFromTxnIds**'
api:
  file: get-all-refunds-for-txnid-1.json
  operationId: GetAllRefundsfromTransactionIDs
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get All Refunds for a Transaction ID** API (getAllRefundsFromTxnIds) command is used to retrieve the status of all the refund requests fired for a particular Transaction ID. The output of this API provides the request ID, and the PG used the status of a refund request and the creation of refund date information.

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
        Hash logic for this API is:
        sha512(key|command|var1|salt)
      </td>
    </tr>
  </tbody>
</Table>

## Response parameters description and sample response

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>
      <th>
        **Description**
      </th>
      <th>
        **Example**
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        status
      </td>
      <td>
        The status of the response can be any of the following:

        * **1:** Success  
        * **2:** Failure
      </td>
      <td>
        1
      </td>
    </tr>
    <tr>
      <td>
        msg
      </td>
      <td>
        The description of the response whether the card details were stored successfully or not.
      </td>
      <td>
        Refunds fetched successfully.
      </td>
    </tr>
    <tr>
      <td>
        Refund Details
      </td>
      <td>
        The details are sent by PayU in JSON format for the successful response. For more information, refer to [Additional Info for General APIs](ref:addl-info-general-apis#description-of-the-refund-details-json-fields).
      </td>
      <td>

      </td>
    </tr>
  </tbody>
</Table>

> 📘 Reference:
>
> For sample response, refer to [Additional Info for General APIs](addl-info-general-apis#description-of-the-refund-details-json-fields).

## Request parameters

**Example values**

Use the following sample values while trying out the API:

* `var1` (txnid): db97dd56eff7296e5061