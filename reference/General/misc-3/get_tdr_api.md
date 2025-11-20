---
title: Get TDR API
api:
  file: get_tdr_corrected.json
  operationId: get_TDR
hidden: false
link:
  new_tab: false
metadata:
  title: Get TDR API
---
The Get TDR API (**get_TDR** API) is used to get the Transaction Discount Rate (TDR) value of a transaction with PayU. It is a simple API for which you need to provide the PayU ID of the transaction as input and the TDR value is returned in the output, var1 is Payu id (mihpayid) of the transaction.

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=get_TDR&var1=403993715521891555&hash=a0cf2d4ed3fb551388bd9e078f7ace8fb565d3240e06735cfc83330bb604b0f97a26a31160f1987af4ba5f78e126f400826a62d71337395e6e127b28a62b860d"
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  **Success scenario**

  ```json
  {
    "status": 1,
    "msg": "Transaction Fetched Successfully",
    "TDR_details": {
      "TDR": 0
    }
  }
  ```

  **Failure scenario**

  If mihpayid is not found:

  ```json
  {
    "status": 0,
    "msg": "Invalid PayU ID"
  }
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  <HTMLBlock>{`
        <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
          <thead>
            <tr style="background-color: #f5f5f5;">
              <th style="padding: 10px; border: 1px solid #ddd; font-weight: bold; text-align: left;">Parameter</th>
              <th style="padding: 10px; border: 1px solid #ddd; font-weight: bold; text-align: left;">Description</th>
              <th style="padding: 10px; border: 1px solid #ddd; font-weight: bold; text-align: left;">Example</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">status</td>
              <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">
                This parameter returns the status of web service call. The status can be any of the following: 
                <ul style="padding-left: 20px; margin-top: 5px;">
                  <li>0 - If web service call failed.</li>
                  <li>1 - If web service call succeeded</li>
                </ul>
              </td>
              <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">0</td>
            </tr>
            <tr>
              <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">msg</td>
              <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">This parameter returns the reason string.</td>
              <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">
                For example, any of the following messages are displayed:
                <ul style="padding-left: 20px; margin-top: 5px;">
                  <li>Parameter missing</li>
                  <li>Token is empty</li>
                  <li>Amount is empty</li>
                  <li>Transaction not exists</li>
                </ul>
              </td>
            </tr>
            <tr>
              <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">TDR_details</td>
              <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">This parameter contains the TDR information in JSON format.</td>
              <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;"><code>{"TDR": 0}</code></td>
            </tr>
            <tr>
              <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">TDR_details.TDR</td>
              <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">The Transaction Discount Rate value for the given transaction.</td>
              <td style="padding: 10px; border: 1px solid #ddd; vertical-align: top;">0</td>
            </tr>
          </tbody>
        </table>
  `}</HTMLBlock>
</Accordion>

## Request parameters

<Accordion title="Sample values" icon="fa-flask">
  Use the following sample values while trying out the API:

  * var1 (Payu ID/mihpayid): 403993715521891555
</Accordion>
