---
title: Get Issuing Bank Status API
excerpt: Issuing Bank Status
api:
  file: getIssuingBankStatus.json
  operationId: IssuingBankStatus
hidden: false
metadata:
  title: ' Get Issuing Bank Status API'
  description: >-
    The **Get Issuing Bank Status** API (**getIssuingBankStatus**) helps handle
    credit or debit card issuing bank downtime by providing information on the
    status of the bank.
  keywords:
    - getIssuingBankStatus API Command
    - Issuing Bank of Credit Card Status API
    - Issuing Bank of Debit Card Status API
    - Check issuing bank health that issued credit card API
    - Check issuing bank health that issued debit card API
    - Health check of card issuing bank API
    - Health check of credit card issuing bank API
    - Health check of debit card issuing bank API
    - API Command getIssuingBankStatus
---
The **Get Issuing Bank Status** API (**getIssuingBankStatus**) is used to help you handle the credit card or debit card issuing bank downtime.

| Environment            | URL                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2)         |

<details>
  <summary>Sample request</summary>

  ```
  curl -X POST "https://test.payu.in/merchant/postservice?form=2
  -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
  "key=J****g&command=getIssuingBankStatus&var1=512345&hash=190908741314524c922d9587298eb64a076d058c085c66229f5acfeac4fb8a11dcd41f3f566cdb2e14a12f486a598a4e56943a2390c258384add9aeed1885e9d"
  ```
</details>

<details>
  <summary>Sample response</summary>

  **Success scenario**

  ```plaintext
  {
        "issuing_bank": "HDFC",
        "up_status": "1"
  }
  ```

  * up\_status parameter with the value as 0 signifies that the particular Bank option is down at the moment.
  * up\_status parameter with the value as 1 signifies that the particular Bank Banking option is up at the moment.

  **Failure scenario**

  If issuing bank data is not available for the BIN:

  ```
  {             
   "msg":"No information available",
  "status":0
  }
  ```
</details>

<details>
  <summary>Response parameters</summary>

  The response parameters for a bank code passed in **var1**, it returns a response for the specified bank alone with the parameters as explained in the following table. If the **default** value is passed in **var1**, it returns a array of all the banks in a JSON array format and each JSON has the list of fields similar to the parameter list:

  <table>
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
  </table>
</details>

## Request parameters

<details>
  <summary>Reference information</summary>

  <table align="left">
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

          \- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)

          * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
        </td>
      </tr>

      <tr>
        <td>
          hash
        </td>

        <td>
          Hash logic for this API is:\\

          ```
          sha512(key\|command\|var1\|salt) sha512

          ```
        </td>
      </tr>

      <tr>
        <td>
          var1
        </td>

        <td>
          For JSON fields description, refer to [Additional Info for General APIs](ref:addl-info-general-apis)
        </td>
      </tr>
    </tbody>
  </table>
</details>

Use the following sample values while trying out the API:

**Example values**:

* `var1`(first 6 digit of the card): First six digits of any card (ex- 512345)