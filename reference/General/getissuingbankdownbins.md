---
title: Get Issuing Bank Down BINs API
api:
  file: updated_gettingissuingbankdownbins.json
  operationId: GetIssuingBankDownBINs
hidden: false
---
The **Getting Issuing Bank Down Bins** API (**gettingIssuingBankDownBins**) is used to retrieve the card BINs for all the banks that are observing either full downtime or partial downtime at an instance.

| Environment            | URL                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2)         |

<details>
  <summary>Sample request</summary>

  ```
  curl -X POST "https://test.payu.in/merchant/postservice?form=2
  -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

  "key=JP***g&command=getIssuingBankDownBins&var1=ALLBD&var2=1&hash=efc4452469091d4d6061fcf6bce45c8116675972a89ddcba6bdd27dce613ca6e48e703e3ba7f6015ef128eda60ed61a3307795c5dd7e284a7691f0c6dc3812a8"
  ```
</details>

<details>
  <summary>Sample response</summary>

  ```
  [
        {
              "issuing_bank": "ALLBD",
              "status": 2,
              "title": "ALLAHABAD BANK",
              "bins_arr": [
                    "421337",
                    "608219",
                    "608218",
                    "608171",
                    "608102",
                    "607352",
                    "607137",
                    "607038",
                    "607091",
                    "607016",
                    "607117",
                    "430450",
                    "652204"
              ]
        }
  ]
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

<details>
  <summary>Reference information for request parameters</summary>

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
          sha512(key\|command\|var1\|salt) sha512
          ```
        </td>
      </tr>
    </tbody>
  </Table>
</details>

Use the following sample values while trying out the API:

**Example values**:

* `var1`: Pass "default" to get the downtime status of all banks or pass the bank codes (ex-AXISB) to get the downtime status of a specific bank.