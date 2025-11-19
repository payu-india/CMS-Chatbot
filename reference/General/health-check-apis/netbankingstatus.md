---
title: Get Net Banking Status API
api:
  file: getNetBankingStatus.json
  operationId: NetBankingStatus
hidden: false
metadata:
  title: Get Net Banking Status API
  description: >-
    The Get Net Banking Status API  or getNetbankingStatus API command is used
    to check the status of Net Banking options, indicating whether they are up
    or down. The API can provide the status of a specific bank or all banks.
  keywords:
    - getNetbankingStatus API Command
    - Net Banking health check API
    - Check Net Banking health status
    - Net Banking health check
    - Online bank Health check
    - NetBanking health check API
    - Check NetBanking health status
    - NetBanking health check
    - API Command getNetbankingStatus
---
The Get Net Banking Status API (**getNetbankingStatus**) is used to help you in handling the NetBanking Downtime. A few times, one or more Net Banking options may be facing downtime due to issues observed at the bank’s end. This API is used to tell the status of one or all the Net Banking options. The status can be either up or down. If you want to know the status of a specific Net Banking option, the input parameter should contain the corresponding ibibo_code. If you want to know the status of all the Net Banking options, the input parameter should contain the value as default.

This API helps you in handling the Net Banking downtime.

| Environment            | URL                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2)         |

<details>
  <summary>Sample request</summary>

  ```
  curl -X POST "https://test.payu.in/merchant/postservice?form=2"-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&command=getNetbankingStatus&var1=AXIB&hash=11f17a5b7b3a93bd0391a0447706ebebd37ab11d8ec8aff18e7d0ca6267f44d6b0b56c4bee6a8b8998acec1491be17047d43ad3ef1b4677bf2504f48d3e779ea"
  ```
</details>

<details>
  <summary>Sample response</summary>

  ```plaintext
  {
        "ibibo_code": "AXIB",
        "title": "AXIS Bank NetBanking",
        "up_status": 0,
        "mode": "NB"
  }
  ```

  To get the status of all Net Banking options pass (value “**default**” is passed in input):

  ```
  {
        "AXIB": {
              "ibibo_code": "AXIB",
              "title": "AXIS Bank NetBanking",
              "up_status": 0,
              "mode": "NB"
        },
        "SBIB": {
              "ibibo_code": "SBIB",
              "title": "State Bank of India",
              "up_status": 1,
              "mode": "NB"
        },
        "TESTPGNB": {
              "ibibo_code": "TESTPGNB",
              "title": "Test Net Banking",
              "up_status": 1,
              "mode": "NB"
        },
        "UPI": {
              "ibibo_code": "UPI",
              "title": "Test UPI",
              "up_status": 1,
              "mode": "UPI"
        },
        "CASH": {
              "ibibo_code": "CASH",
              "title": "Test Wallet",
              "up_status": 1,
              "mode": "CASH"
        }
  }
  ```
</details>

<details>
  <summary>Response parameters</summary>

  The response parameters for a bank code passed in **var1**, it returns a response for the specified bank alone with the parameters as explained in the following table. If the **default** value is passed in **var1**, it returns a array of all the banks in a JSON array format and each JSON has the list of fields similar to the parameter list:

  <Table>
    <thead>
      <tr>
        <th>
          **Parameter/JSON Field**
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
          ibibo\_code
        </td>

        <td>
          This parameter contains the bank code for which the Net Banking status is displayed.
        </td>

        <td>
          AXIB
        </td>
      </tr>

      <tr>
        <td>
          title
        </td>

        <td>
          This parameter contains the bank name and service.
        </td>

        <td>
          AXIS Bank NetBanking
        </td>
      </tr>

      <tr>
        <td>
          up\_status
        </td>

        <td>
          This parameter contains the status of the NetBanking service and can be any of the following:

          * 0 - signifies that the particular Bank option is down at the moment
          * 1 - signifies that the particular Banking option is up at the moment
        </td>

        <td>
          1
        </td>
      </tr>

      <tr>
        <td>
          mode
        </td>

        <td>
          This parameter contains the mode of payment for which the status is displayed.
        </td>

        <td>
          NB
        </td>
      </tr>
    </tbody>
  </Table>
</details>

## Request parameters

Use the following sample values while trying out the API:

<details>
  <summary>Reference information</summary>

  <Table align={["left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          Parameter
        </th>

        <th style={{ textAlign: "left" }}>
          Reference
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          key
        </td>

        <td style={{ textAlign: "left" }}>
          For more information on how to generate the Key and Salt, refer to any of the following:

          \- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)

          * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          hash
        </td>

        <td style={{ textAlign: "left" }}>
          Hash logic for this API is:

          ```
          sha512(key|command|var1|salt) sha512
          ```
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          var1
        </td>

        <td style={{ textAlign: "left" }}>
          For JSON fields description, refer to [Additional Info for General APIs](ref:addl-info-general-apis)
        </td>
      </tr>
    </tbody>
  </Table>
</details>

**Example values**:

* `var1`: Pass "**default**" to get the status of all banks or specify the net banking code (ex, AXISB) of the respective bank to get the uptime status. See [Net Banking Codes](https://docs.payu.in/docs/net-banking-codes).