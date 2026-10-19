---
name: Verify_Payment_Tabs
---
Upon receiving the response, PayU recommends you performing a reconciliation step to validate all transaction details.<br/>

You can verify your payments using either of the following methods:<br/>

<Tabs>
  <Tab title="1. Verify using Webhooks">
    Configure the webhooks to monitor the status of payments.<br />Webhooks enable a server to communicate with another server by sending an HTTP callback or message.<br />These callbacks are triggered by specific events or instances and operate at the server-to-server (S2S) level.

    <br />

    Know how to manage [Webhooks for Payments](https://docs.payu.in/reference/webhooks).
  </Tab>

  <Tab title="2. Verify using Verify Payments API">
    **Environment**

    |                        |                                                                                                              |
    | :--------------------- | :----------------------------------------------------------------------------------------------------------- |
    | Test Environment       | [https://test.payu.in/merchant/postservice.php?form=2](https://test.payu.in/merchant/postservice.php?form=2) |
    | Production Environment | [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2) |

    > Note: The hash logic for Verify Payment API is:
    > `sha512(key|command|var1|salt)
    > sha512`

    <Accordion title="Sample request" icon="fa-code">
      curl --request POST <br />--url '[https://test.payu.in/merchant/postservice?form=2](https://test.payu.in/merchant/postservice?form=2)' <br />--header 'Content-Type: application/x-www-form-urlencoded' <br />--data key=JPM7Fg <br />--data command=verify_payment <br />--data var1=IhfgcZnXR4o4nB <br />--data hash=a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9
    </Accordion>

    <Accordion title="Sample response" icon="fa-reply">
      <br />

      If credit card payment is made, the response is similar to the following:

      ```json Success Response
      {
        "status":0,
        "msg":"0 out of 1 Transactions Fetched Successfully",
        "transaction_details":
      {
      "IhfgcZnXR4o4nB":
      {
      "mihpayid":"Not Found",
      "status":"Not Found"
      }
      }
      }
      ```

      If txnID is not found, the response is similar to the following:

      ```json Failure Response

      {
          "status":0,
          "msg":"0 out of 1 Transactions Fetched Successfully",
            "transaction_details":
            {	
                            "IhfgcZnXR4o4nB":
              {
                                    "mihpayid":"Not Found",
                  "status":"Not Found"
                }
                            }
      }
      ```
    </Accordion>

    <Accordion title="Response parameters" icon="fa-list">
      <Table align={["left","left","left"]}>
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
              This parameter returns the status of web service call. The status can be any of the following:

              * 0 - If web service call failed.
              * 1 - If web service call succeeded
            </td>

            <td>
              0
            </td>
          </tr>

          <tr>
            <td>
              msg
            </td>

            <td>
              This parameter returns the reason string.
            </td>

            <td>
              For example, any of the following messages are displayed:

              * Parameter missing
              * Token is empty
              * Amount is empty
              * Transaction not exists
            </td>
          </tr>

          <tr>
            <td>
              transaction_details
            </td>

            <td>
              This parameter contains the response in a JSON format. For more information refer to [JSON fields description for transaction_details parameter ](ref:addl-info-general-apis).
            </td>

            <td>

            </td>
          </tr>

          <tr>
            <td>
              request_id
            </td>

            <td>
              PayU Request ID for a request in a Transaction. For example, a transaction can have a refund request.
            </td>

            <td>
              7800456
            </td>
          </tr>

          <tr>
            <td>
              bank_ref_num
            </td>

            <td>
              This parameter returns the bank reference number. If the bank provides after a successful action.
            </td>

            <td>
              204519474956
            </td>
          </tr>
        </tbody>
      </Table>

      To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).
    </Accordion>
  </Tab>
</Tabs>
