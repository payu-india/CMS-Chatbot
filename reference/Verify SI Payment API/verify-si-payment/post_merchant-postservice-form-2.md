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

<Accordion title="Pre-Debit Transaction">
  The pre-debit notification was processed successfully. The recurring payment has not yet been executed — it will be attempted on the scheduled recurring date.

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
  ```json Failed
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
          "field9": "Mandate is not Active",
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
          "status": "failure",
          "unmappedstatus": null,
          "Merchant_UTR": null,
          "Settled_At": null,
          "card_token": null,
          "offerAvailed": null
        }
      }
    }
  ```
</Accordion>

<Accordion title="Recurring Transaction">
  ```json Success
  {
      "status": 1,
      "msg": "1 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
        "rc_613345778912516840": {
          "mihpayid": "30141596997",
          "request_id": "",
          "bank_ref_num": "622716418717",
          "amt": "0.00",
          "transaction_amount": "1.00",
          "txnid": "rc_613345778912516840",
          "additional_charges": "0.00",
          "productinfo": "SI",
          "firstname": "",
          "bankcode": "CCSI",
          "udf1": "",
          "udf2": "",
          "udf3": "",
          "udf4": "",
          "udf5": "",
          "field2": "003773",
          "field9": "Transaction Completed",
          "error_code": "E000",
          "addedon": "2026-08-15 22:00:04",
          "payment_source": "sirecurring",
          "card_type": "MAST",
          "error_Message": "NO ERROR",
          "net_amount_debit": 1.00,
          "disc": "0.00",
          "mode": "SI",
          "PG_TYPE": "SI-PG",
          "card_no": "XXXXXXXXXXXXXXXX",
          "status": "success",
          "unmappedstatus": "captured",
          "Merchant_UTR": null,
          "Settled_At": null,
          "card_token": null,
          "offerAvailed": null
        }
      }
    }
  ```
  ```json Failed
  {
      "status": 1,
      "msg": "1 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
        "rc_613345778912516840": {
          "mihpayid": "30025956801",
          "request_id": null,
          "bank_ref_num": null,
          "amt": "1.00",
          "transaction_amount": "1.00",
          "txnid": "rc_613345778912516840",
          "additional_charges": "0.00",
          "productinfo": "SI",
          "firstname": "",
          "bankcode": "CCSI",
          "udf1": "",
          "udf2": "",
          "udf3": "",
          "udf4": "",
          "udf5": "",
          "field2": null,
          "field9": "Authorization failed at Bank",
          "error_code": "E1903",
          "addedon": "2026-08-09 19:00:04",
          "payment_source": "sirecurring",
          "card_type": "VISA",
          "error_Message": "Unable to process the request.",
          "net_amount_debit": 0.00,
          "disc": "0.00",
          "mode": "SI",
          "PG_TYPE": "SI-PG",
          "card_no": "XXXXXXXXXXXXXXXX",
          "status": "failure",
          "unmappedstatus": "failed",
          "Merchant_UTR": null,
          "Settled_At": null,
          "card_token": null,
          "offerAvailed": null
        }
      }
    }
  ```
  ```json Retry in Progress
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
          "field9": "Transaction Retry is in progress",
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
          "status": "in progress",
          "unmappedstatus": null,
          "Merchant_UTR": null,
          "Settled_At": null,
          "card_token": null,
          "offerAvailed": null
        }
      }
    }
  ```
</Accordion>

<Accordion title="Response Parameter Description">
  <Table align={["left","left"]}>
    <thead>
      <tr>
        <th>
          Parameter
        </th>

        <th>
          Description
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          `status`
        </td>

        <td>
          `integer` The status of the API call. This does **not** indicate payment success. You can check `transaction_details` for the actual outcome. Possible values:

          - `1`: API call processed
          - `0`: API call failed
        </td>
      </tr>

      <tr>
        <td>
          `msg`
        </td>

        <td>
          `string` Human-readable outcome message, e.g. `1 out of 1 Transactions Fetched Successfully`.
        </td>
      </tr>

      <tr>
        <td>
          `transaction_details`
        </td>

        <td>
          `object` Map of `rc_` prefixed transaction ID → transaction detail object.
        </td>
      </tr>
    </tbody>
  </Table>

  ### `transaction_details` Parameter Description

  | Parameter            | Description                                                                                                                                                                                                                                                                                                            |
  | :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `mihpayid`           | `string/null` PayU's unique transaction ID. Populated only after the recurring charge is processed; `null` for pre-debit and retry states.                                                                                                                                                                             |
  | `request_id`         | `string/null` Internal PayU request identifier.                                                                                                                                                                                                                                                                        |
  | `bank_ref_num`       | `string/null `Bank reference number assigned to the transaction. Populated on successful recurring charges.                                                                                                                                                                                                            |
  | `amt`                | `string `Mandate amount as registered during SI creation.                                                                                                                                                                                                                                                              |
  | `transaction_amount` | `string` Actual debit amount for this billing cycle.                                                                                                                                                                                                                                                                   |
  | `txnid`              | `string` The `rc_` prefixed transaction ID, echoed back.                                                                                                                                                                                                                                                               |
  | `additional_charges` | `string` Flat surcharge applied to the debit. `0.00` if none.                                                                                                                                                                                                                                                          |
  | `productinfo`        | `string/null` Product description. `SI` for recurring transactions; `null` for pre-debit states.                                                                                                                                                                                                                       |
  | `firstname`          | `string/null` Customer first name. Populated on recurring transactions.                                                                                                                                                                                                                                                |
  | `bankcode`           | `string/null` Bank or card code. `CCSI` for card SI recurring transactions.                                                                                                                                                                                                                                            |
  | `udf1` – `udf5`      | `string/null` Merchant user-defined fields passed during the debit request.                                                                                                                                                                                                                                            |
  | `field2`             | `string/null` Bank authorisation code. Populated on successful recurring transactions.                                                                                                                                                                                                                                 |
  | `field9`             | `string/null` Human-readable status message from PayU. Key values: `Request Processed Successfully` (pre-debit success), `Mandate is not Active` (pre-debit failed), `Transaction Completed` (recurring success), `Authorization failed at Bank` (recurring failed), `Transaction Retry is in progress` (retry state). |
  | `error_code`         | `string/null` PayU error code. `E000` on success; non-null on failure (e.g. `E1903` for bank authorisation failure).                                                                                                                                                                                                   |
  | `addedon`            | `string/null` Transaction creation timestamp (`YYYY-MM-DD HH:MM:SS`). `null` until the recurring charge is processed.                                                                                                                                                                                                  |
  | `payment_source`     | `string/null` Payment source identifier. `sirecurring` confirms a recurring SI charge; `null` for pre-debit states.                                                                                                                                                                                                    |
  | `card_type`          | `string/null` Card network. Common values: `VISA`, `MAST`. `null` for pre-debit states.                                                                                                                                                                                                                                |
  | `error_Message`      | `string/null` Human-readable error description from the bank. `NO ERROR` on success.                                                                                                                                                                                                                                   |
  | `net_amount_debit`   | `number/null` Net amount debited after discounts. `0.00` on failure; `null` when not yet processed.                                                                                                                                                                                                                    |
  | `disc`               | `string` Discount amount applied. `0.00` if none.                                                                                                                                                                                                                                                                      |
  | `mode`               | `string` Payment mode. `SI` for recurring transactions; `"null"` (string) for pre-debit and retry states.                                                                                                                                                                                                              |
  | `PG_TYPE`            | `string/null` Payment gateway type. `SI-PG` for recurring SI transactions.                                                                                                                                                                                                                                             |
  | `card_no`            | `string/null` Masked card number. Populated on recurring transactions.                                                                                                                                                                                                                                                 |
  | `status`             | `string` Transaction outcome. See [Transaction Status Mapping](#transaction-status-mapping) below.                                                                                                                                                                                                                     |
  | `unmappedstatus`     | `string/null` Granular payment status. `captured` on recurring success; `failed` on recurring failure; `null` for pre-debit and retry states.                                                                                                                                                                          |
  | `Merchant_UTR`       | `string/null` Merchant UTR for settlement reconciliation. Populated post-settlement.                                                                                                                                                                                                                                   |
  | `Settled_At`         | `string/null` Settlement timestamp. Populated post-settlement.                                                                                                                                                                                                                                                         |
  | `card_token`         | `string/null` Network card token, if applicable.                                                                                                                                                                                                                                                                       |
  | `offerAvailed`       | `string/null` Offer or discount details, if applicable.                                                                                                                                                                                                                                                                |
</Accordion>

<Accordion title="Error Responses">
  These are returned when the API call itself fails (envelope `status: 0`).

  **Missing or empty&#x20;**`var1`

  ```json
  {
    "status": 0,
    "msg": "Invalid txnId: cannot be null or empty"
  }
  ```

  **Transaction ID not found**

  ```json
  {
    "status": 0,
    "msg": "0 out of 1 Transactions Fetched Successfully",
    "transaction_details": {
      "PZT2608142058W69KM01-001": {
        "mihpayid": "Not Found",
        "status": "Not Found"
      }
    }
  }
  ```
</Accordion>

***

## Transaction Status Mapping

Use the combination of `status` and `unmappedstatus` inside `transaction_details` to determine the outcome:

| Transaction State  | `status`      | `unmappedstatus` | `field9` (sample)                  |
| :----------------- | :------------ | :--------------- | :--------------------------------- |
| Pre-Debit Success  | `pending`     | `null`           | `Request Processed Successfully`   |
| Pre-Debit Failed   | `failure`     | `null`           | `Mandate is not Active`            |
| Recurring Success  | `success`     | `captured`       | `Transaction Completed`            |
| Recurring Failed   | `failure`     | `failed`         | `Authorization failed at Bank`     |
| Recurring Retrying | `in progress` | `null`           | `Transaction Retry is in progress` |

<Callout icon="📘" theme="info">
  The `field9` value contains a human-readable status message. For the complete list of `error_code` and `field9` combinations, refer to the PayU error code reference.
</Callout>
