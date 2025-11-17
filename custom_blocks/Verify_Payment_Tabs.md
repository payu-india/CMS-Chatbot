---
name: Verify_Payment_Tabs
---
<br />

<p>Upon receiving the response, PayU recommends you performing a reconciliation step to validate all transaction details.
You can verify your payments using either of the following methods:</p>

<Tabs>
  <Tab title="1. Verify using Webhooks">
    Configure the webhooks to monitor the status of payments.\
    Webhooks enable a server to communicate with another server by sending an HTTP callback or message.\
    These callbacks are triggered by specific events or instances and operate at the server-to-server (S2S) level.

    👉 For more details, refer to [Webhooks for Payments](https://docs.payu.in/reference/webhooks). <br />
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
      ```curl
      curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
      --header 'Content-Type: application/x-www-form-urlencoded' \
      --data-urlencode 'key=JP***g' \
      --data-urlencode 'command=verify_payment' \
      --data-urlencode 'var1=IhfgcZnXR4o4nB' \
      --data-urlencode 'hash=<<calculated_hash_here>>'
      ```
    </Accordion>

    <Accordion title="Sample response" icon="fa-reply">
      <br />

      ```json Success Response
      If credit card payment is made, the response is similar to the following:
      {
      "status": 1,
      "msg": "1 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
         "1733900931584": {
             "mihpayid": "21820644083",
             "request_id": null,
             "bank_ref_num": null,
             "amt": "1.00",
             "transaction_amount": "1.00",
             "txnid": "1733900931584",
             "additional_charges": "0.00",
             "productinfo": "Macbook Pro",
             "firstname": "Abc",
             "bankcode": "MAST",
             "udf1": "udf1",
             "udf2": "udf2",
             "udf3": "udf3",
             "udf4": "udf4",
             "udf5": "udf5",
             "field2": null,
             "field9": "OTP/ATM page expired due to no user action",
             "error_code": "E1602",
             "addedon": "2024-12-11 12:43:03",
             "payment_source": "payu",
             "card_type": "MAST",
             "error_Message": "Bank was unable to authenticate.",
             "net_amount_debit": "0.00",
             "disc": "0.00",
             "mode": "DC",
             "PG_TYPE": "DC-PG",
             "card_no": "XXXXXXXXXXXX7596",
             "status": "failure",
             "unmappedstatus": "dropped",
             "Merchant_UTR": null,
             "Settled_At": null,
             "cardhash": "095d184331be367bb92aa3eeecb57d0728de96cc598dd563d407982d75021149",
             "name_on_card": null,
             "card_token": "4e97156bc2d6320cdfe15",
             "field4": null,
             "threeDSVersion": "2.2.0",
             "offerAvailed": null
         }
      }
      }
      ```

      ```json Failure Response

      If txnID is not found, the response is similar to the following
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
            <th style={{ textAlign: "left" }}>
              **Parameter**
            </th>

            <th style={{ textAlign: "left" }}>
              **Description**
            </th>

            <th style={{ textAlign: "left" }}>
              **Example**
            </th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td style={{ textAlign: "left" }}>
              status
            </td>

            <td style={{ textAlign: "left" }}>
              This parameter returns the status of web service call. The status can be any of the following:

              * 0 - If web service call failed.
              * 1 - If web service call succeeded
            </td>

            <td style={{ textAlign: "left" }}>
              0
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              msg
            </td>

            <td style={{ textAlign: "left" }}>
              This parameter returns the reason string.
            </td>

            <td style={{ textAlign: "left" }}>
              For example, any of the following messages are displayed:

              * Parameter missing
              * Token is empty
              * Amount is empty
              * Transaction not exists
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              transaction\_details
            </td>

            <td style={{ textAlign: "left" }}>
              This parameter contains the response in a JSON format. For more information refer to [JSON fields description for transaction\_details parameter ](#json-field-description-for-transaction_details-parameter).
            </td>

            <td style={{ textAlign: "left" }} />
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              request\_id
            </td>

            <td style={{ textAlign: "left" }}>
              PayU Request ID for a request in a Transaction. For example, a transaction can have a refund request.
            </td>

            <td style={{ textAlign: "left" }}>
              7800456
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              bank\_ref\_num
            </td>

            <td style={{ textAlign: "left" }}>
              This parameter returns the bank reference number. If the bank provides after a successful action.
            </td>

            <td style={{ textAlign: "left" }}>
              204519474956
            </td>
          </tr>
        </tbody>
      </Table>

      To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).
    </Accordion>
  </Tab>
</Tabs>

<br />
