---
title: '[OLD]Refund Transaction API'
excerpt: 'API Command: **cancel_refund_transaction**'
api:
  file: cancel_refund_tranasaction-8.json
  operationId: cancel_refund_transaction
deprecated: false
hidden: true
metadata:
  title: Refund Transaction API
  description: >-
    The Refund Transaction API allows users to cancel or refund transactions in
    different states, with specific parameters required for each action. Sample
    requests and responses are provided for successful and failed scenarios.
  keywords:
    - cancel_refund_transaction command
    - ' Refund Transaction API'
    - ' Cancel a Refund API'
    - ' API for Refund Transaction'
  robots: index
next:
  description: ''
---
The Refund Transaction API (**cancel_refund_transaction**) can be used for the following purposes:

- Cancel a transaction that is in ‘`auth`’ state at the moment. 
- Refund a transaction that is in a ‘`captured`’ state at the moment.

To learn more about different payment states, refer to [Payment States Explanations](https://docs.payu.in/reference/payment-state-explanations). 

In this API: **var1** is the Payu ID (mihpayid) of the transaction, **var2** should contain the Token ID (unique token from the merchant), and **var3** parameter should contain the amount that needs to be refunded.

<GENERALAPIsEnvironment />

<details><summary>Sample request</summary>

**Simple sample request**

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

"key=JP***g&command=cancel_refund_transaction&var1=403993715521937565&var2=20201105secrettokenaturend&hash=10"
```

**Sample request with split information JSON**

```
curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g&command=cancel_refund_transaction&var1=403993715521937565&var2=20201105secrettokenaturend&hash=10&var9=child_merchant_key_1:{\"amount\": 100,\"aggregatorRefundAmount\": 40 }"

```

</details>

<details>  <summary>Sample response</summary>

**Success Scenarios**

- On successful processing from PayU, the response is similar to the following:

```plaintext
Array 
(
      [status] => 1
      [msg] => Cancel Request Queued 
      [txn_update_id] => <Request ID> 
      [bank_ref_num] => <Bank Reference Number> 
      [mihpayid] => <PayU Transaction ID>
)
```

- On successful processing from PayU end for captured transactions, the response is similar to the following:

```plaintext
Array 
(
     [status] => 1
     [msg] => Refund Request Queued 
     [request_id] => Request ID 
     [bank_ref_num] => <Bank Reference Number> 
     [mihpayid] => <PayU Transaction ID>
)
```

On successful processing at PayU end for auth transactions, the response is similar to the following:

```plaintext
Array 
(
    [status] => 1
    [msg] => Cancel Request Queued 
    [txn_update_id] => <Request ID> 
    [bank_ref_num] => <Bank Reference Number>
)
```

**Failure scenarios**

- If token is missing, the response is similar to the following:

```plaintext
{
      "status": 0,
      "msg": "token is empty",
      "mihpayid": "403993715521937565"
}
```

- If amount is missing, the response is similar to the following:

```plaintext
Array 
(
[status] => 0
[msg] => amount is empty 
)
```

- If the transaction is not found, the response is similar to the following:

```plaintext
Array 
(
[status] => 0
[msg] => transaction not exists 
)
```

- If failed to refund, the response is similar to the following:

```plaintext
Array 
(
       [status] => 0
       [msg] => Refund request failed
)
```

- If capture is done on the same day, the response is similar to the following:

```plaintext
Array 
(
    [status] => 1
    [msg]=> Capture is done today, please check for refund status tomorrow 
    [request_id] => Request ID
    [bank_ref_num] => Bank Reference Number
    [mihpayid] => PayU ID
)
```

- If the token is invalid, the response is similar to the following:

```plaintext
(
    [status] => 0
    [msg] => token already used or request pending 
)
```

- If failed to cancel a transaction, the response is similar to the following:

```plaintext
Array 
(
     [status] => 0
     [msg] => Cancel request failed
)
```

> 📘 Notes:
> 
> - The response for Refund Transaction API in Test Environment is similar to the following as it is the limitation with Test Environment:
>   - Regular Merchant
>     ```
>     (
>         [status] => 1
>         [msg] => Refund Request Queued
>         [request_id] => 136409872
>         [bank_ref_num] => 
>         [mihpayid] => 403993715530925893
>         [error_code] => 102
>     )
>     ```
>   - Merchant with Split transaction enabled
> 
> ```
> {
>   "status": 236,
>   "msg": "Refund Split Info must be of JSON format",
>   "mihpayid": "403993715521937565"
> }
> ```
> 
> - The error_code ​value 102​ should be treated as success; the rest are failures. For the list of error codes, refer to [Error Codes for Refund Initiation](ref:error-codes-for-refund-initiation).

</details>

<details>  <summary>Response parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Fields**",
    "h-2": "**Sample Value**",
    "0-0": "status",
    "0-1": "The status can be any of the following:  \n_ **1** if API call is a success  \n_ **0** if the API has failed",
    "0-2": "1",
    "1-0": "msg",
    "1-1": "This parameter contains a response message description.",
    "1-2": "Refund Request Queued",
    "2-0": "request\\_id",
    "2-1": "This parameter contains a unique refund ID generated by PayU.",
    "2-2": "6582898821",
    "3-0": "bank\\_ref\\_num",
    "3-1": "This parameter contains a bank reference number is returned from bank.",
    "3-2": "IRN6601148",
    "4-0": "mihpayid",
    "4-1": "This parameter contains a unique transaction ID generated by PayU during sale.",
    "4-2": "7043873219",
    "5-0": "error\\_code",
    "5-1": "This parameter contains the code for response. For a list of error codes and their description, refer to Refund Error Codes.",
    "5-2": "102"
  },
  "cols": 3,
  "rows": 6,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


> 📘 Note:
> 
> The error_code ​value 102​ should be treated as success; the rest are failures. To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).

The **Refund Details** parameter of the response is in JSON format and the parameters in this JSON are described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "**JSON Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Payu\\_ID",
    "0-1": "This field contains a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.",
    "0-2": "403993715521937565",
    "1-0": "RequestID",
    "1-1": "This field contains the request ID value posted by the merchant during the transaction request.  \n  \n- **failure** - If the API command failed. \n- **success** - If the API command succeeded.",
    "1-2": "131278422",
    "2-0": "RefundToken",
    "2-1": "This field contains the refund token from bank.",
    "2-2": "20201105secrettokenatur",
    "3-0": "Payment Gateway",
    "3-1": "This parameter gives information on the payment gateway used for the transaction.",
    "3-2": "AXISPG",
    "4-0": "Amount",
    "4-1": "This parameter contains the original amount which was sent in the transaction request by the merchant.",
    "4-2": "10.00",
    "5-0": "Status",
    "5-1": "This parameter contains any of the the following status based on whether the API command was successful or failed to get response:",
    "5-2": "success",
    "6-0": "Refund\\_CreationDate",
    "6-1": "This parameter contains the time stamp of refund initiation from PayU when the merchant requested. The format of the time stamp is YYYY-MM-DD HH:MM:SS.",
    "6-2": "2020-11-05 01:23:19",
    "7-0": "bank\\_ref\\_num",
    "7-1": "For each successful transaction – this parameter contains the bank reference number generated by the bank.",
    "7-2": "527013524405",
    "8-0": "bank\\_arn",
    "8-1": "This parameter contains the Acquirer Reference Number (ARN) is a unique number is generated by the bank. This ARN is generated within 24-72 business hours of initiating the refund.",
    "8-2": "0084129821",
    "9-0": "settled\\_at",
    "9-1": "This parameter contains the transaction settlement time stamp. The format of the time stamp is YYYY-MM-DD HH:MM:SS.",
    "9-2": "2020-11-05 01:24:04"
  },
  "cols": 3,
  "rows": 10,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


</details>

## Request parameters

<details>  <summary>Reference information and other request parameters</summary>

<KeyHashForGeneralParametersDescription />

### Other request parameters

Other request parameters used for **Refund Transaction **API (which are not in the below form for Try It experience) are listed in the following table:

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "var2",
    "0-1": "This parameter must contain the Token ID (unique token from the merchant) for the refund request. Token ID has to be generated at your end for each new refund request. It is an identifier for each new refund request which can be used for tracking it. It must be unique for every new refund request generated – otherwise the refund request would not be generated successfully. Token ID length should not be greater than 23 characters.",
    "1-0": "var3",
    "1-1": "For captured transaction: This parameter must contain the amount which needs to be refunded. Both partial and full refunds are allowed.   \nFor a partial refund, this var3 value would be less than the amount with which the transaction was made.  \n  \n- **For a full refund**: The var3 value would be equal to the amount with which the transaction was made.  \n- **For pre-auth transaction**:  If the transaction is in a pre-auth state currently, the full cancellation is allowed. The amount must be the same as the auth amount. A partial amount would not be allowed.",
    "2-0": "var5",
    "2-1": "If a refund callback for a transaction is required on a specific URL, the URL must be specified in this parameter.",
    "3-0": "var8:  \n`mandatory for split`",
    "3-1": "Refund split information provided by merchant in a JSON format. This is applicable only with the Split transactions. The JSON format is described in the next able."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


The **var8** parameter is in a JSON format that contains the fields described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Split 1 Details",
    "0-1": "The child merchant key, amount and aggregator refund amount is specified in the following format:  \nchild\\_merchant\\_key\\_1\":{ \"amount\": 100, aggregatorRefundAmount: 40 }  \n**Note**: The aggregator refund amount is optional in this field.",
    "0-2": "child\\_merchant\\_key\\_1\": { \"amount\": 100, aggregatorRefundAmount: 40 }",
    "1-0": "Split 2 Details",
    "1-1": "The child merchant key, amount and aggregator refund amount is specified similar to Split 1 details.",
    "1-2": "child\\_merchant\\_key\\_2\": {\"amount\": 20, aggregatorRefundAmount: 0 }"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


**Sample JSON for var8**

```
{ "child_merchant_key_1": { "amount": 100, aggregatorRefundAmount: 40 }, "child_merchant_key_2": {"amount": 20, aggregatorRefundAmount: 0 }}
```

</details>

> 📘 Reference:
> 
> var5 and var8 are optional parameters and not included in the following **Try It** experience. For more information on description with examples, refer to the [Other request parameters](#other-request-parameters) subsection.

**Example values **

Use the following sample values while trying out the API:

- `var1` (mihpayid): 403993715521937565
- `var2` (reference number for a refund provided by merchant): 20201105secrettokenaturend