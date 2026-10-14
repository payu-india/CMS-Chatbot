---
api:
  file: verify-si-payment.yaml
  operationId: post_merchant-postservice-form-2
hidden: true
link:
  new_tab: false
---
Use the `verify_si_payment` command to check the status of a pre-debit or recurring payment transaction initiated via the [Pre-Debit and Recurring API](ref:subscriptions-pdn-rp). This command uses the same endpoint and request parameters as the standard [Verify Payment](ref:verify-payment) API — the only change is the `command` value and the `var1` input.

<Callout icon="📘" theme="info">
  ### **When to Use This API:**

  Use `verify_si_payment` when:

  - You did not receive the webhook for a pre-debit or recurring event.
  - You want to independently verify the outcome of a debit triggered via the PDN/RP merge API.
  - You are polling for the final status of a transaction that is currently `in progress` (retry state).

  Pass the `rc_` prefixed transaction ID returned by the PDN/RP merge API as `var1`.
</Callout>

***

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /merchant/postservice.php?form=2
  </Card>
</Cards>

***

<GENERALAPIsEnvironment />

***

## Sample Request

<Tabs>
  <Tab title="Request Payload">
    ```curl
    curl --location 'https://info.payu.in/merchant/postservice?form=2' \
    --header 'accept: application/json' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=G2ZB4r' \
    --data-urlencode 'command=verify_si_payment' \
    --data-urlencode 'var1=rc_613345778912516840' \
    --data-urlencode 'hash=e7929823f663946bf9f54a68567901da847e505555e187412cf21a3d8e8fd18b6db1904442f62a07f77e74237398bcbf689353903415bb89d42c2ef0117fff88'
    ```
  </Tab>

  <Tab title="Parameter Description">
    | Parameter                  | Description                                                                                                                              | Example                 |
    | :------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- | :---------------------- |
    | `key`<br />_mandatory_     | `string` Merchant key from the PayU dashboard. For more information, refer to [Check your API Key and Salt](doc:check-api-key-and-salt). | `G2ZB4r`                |
    | `command`<br />_mandatory_ | `string` You should pass the value as `verify_si_payment`.                                                                               | `verify_si_payment`     |
    | `var1`<br />_mandatory_    | `string` The `rc_` prefixed transaction ID returned by the PDN/RP merge API.                                                             | `rc_613345778912516840` |
    | `hash`<br />_mandatory_    | `string` SHA-512 hash for request integrity. Formula: `SHA512(key\|command\|var1\|SALT)`                                                 | `e7929823f663946b...`   |
  </Tab>
</Tabs>

***

## Sample Response

A successful API call returns `status: 1` at the envelope level. The actual transaction outcome is determined by the `status` field inside `transaction_details`. The outer `status: 1` only means the API call was processed — not that the payment succeeded.

<Tabs>
  <Tab title="Response Payload">
    ```json Success
    {
        "status": 1,
        "msg": "1 out of 1 Transactions Fetched Successfully",
        "transaction_details": {
          "rc_613345778912516840": {
            "mihpayid": null,
            "request_id": null,
            "bank_ref_num": null,
            "amt": "1.00",
            "transaction_amount": "1.00",
            "txnid": "rc_613345778912516840",
            "additional_charges": "0.00",
            "productinfo": null,
            "firstname": null,
            "bankcode": null,
            "udf1": null,
            "udf2": null,
            "udf3": null,
            "udf4": null,
            "udf5": null,
            "field2": null,
            "field9": "Request Processed Successfully",
            "error_code": null,
            "addedon": null,
            "payment_source": null,
            "card_type": null,
            "error_Message": null,
            "net_amount_debit": null,
            "disc": "0.00",
            "mode": "null",
            "PG_TYPE": null,
            "card_no": null,
            "status": "pending",
            "unmappedstatus": null,
            "Merchant_UTR": null,
            "Settled_At": null,
            "card_token": null,
            "offerAvailed": null
          }
        }
      }
    ```
  </Tab>

  <Tab title="Parameter Description">

  </Tab>
</Tabs>
