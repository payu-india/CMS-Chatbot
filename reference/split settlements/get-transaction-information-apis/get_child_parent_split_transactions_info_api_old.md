---
title: Get Child/Parent Split Transaction Info
excerpt: ''
api:
  file: get-aggregatorparent-transaction-info-3.json
  operationId: GetChildParentSplitTransactionInfo
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get Aggregator Transactions** API is for getting the transaction info of parent merchants in the Aggregator flow.

### Environment

<table style={{ border: "0.1rem solid rgb(242, 242, 242)" }}>
  <tbody>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Test Environment</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>https://uat-onepayuonboarding.payu.in</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Production Environment</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>https://onboarding.payu.in</td>
    </tr>
  </tbody>
</table>

## Response parameters

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>
      <th>
        **Description**
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        status
      </td>
      <td>
        This parameter contains the status of response. It can be any of the following:  
        * **0:** Failed  
        * **1:** Success
      </td>
    </tr>
    <tr>
      <td>
        msg
      </td>
      <td>
        This parameter contains the response or error message.
      </td>
    </tr>
    <tr>
      <td>
        Transaction\_details
      </td>
      <td>
        This parameter contains the transaction details in an array format and it is displayed only when the **status** field returns the value as **1**. For more information on each field in the array, refer to [Additional Info for Split Settlements APIs](ref:additional-info-for-split-settlements-apis).
      </td>
    </tr>
  </tbody>
</Table>

## Request parameters