---
title: Refund Transaction API
excerpt: ''
api:
  file: cancel_refund_tranasaction-10.json
  operationId: cancel_refund_transaction
deprecated: false
hidden: false
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
The Refund Transaction API (**cancel\_refund\_transaction**) can be used for the following purposes:

* Cancel a transaction that is in ‘`auth`’ state at the moment. 
* Refund a transaction that is in a ‘`captured`’ state at the moment.

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

* On successful processing from PayU, the response is similar to the following:

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

* On successful processing from PayU end for captured transactions, the response is similar to the following:

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

* If token is missing, the response is similar to the following:

```plaintext
{
      "status": 0,
      "msg": "token is empty",
      "mihpayid": "403993715521937565"
}
```

* If amount is missing, the response is similar to the following:

```plaintext
Array 
(
[status] => 0
[msg] => amount is empty 
)
```

* If the transaction is not found, the response is similar to the following:

```plaintext
Array 
(
[status] => 0
[msg] => transaction not exists 
)
```

* If failed to refund, the response is similar to the following:

```plaintext
Array 
(
       [status] => 0
       [msg] => Refund request failed
)
```

* If capture is done on the same day, the response is similar to the following:

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

* If the token is invalid, the response is similar to the following:

```plaintext
(
    [status] => 0
    [msg] => token already used or request pending 
)
```

* If failed to cancel a transaction, the response is similar to the following:

```plaintext
Array 
(
     [status] => 0
     [msg] => Cancel request failed
)
```

> 📘 Notes:
>
> * The response for Refund Transaction API in Test Environment is similar to the following as it is the limitation with Test Environment:
>   * Regular Merchant
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
>   * Merchant with Split transaction enabled
>
> ```
> {
>   "status": 236,
>   "msg": "Refund Split Info must be of JSON format",
>   "mihpayid": "403993715521937565"
> }
> ```
>
> * The error\_code ​value 102​ should be treated as success; the rest are failures. For the list of error codes, refer to [Error Codes for Refund Initiation](ref:error-codes-for-refund-initiation).

</details>

<details>  <summary>Response parameters</summary>

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Fields**
      </th>

      <th>
        **Sample Value**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        status
      </td>

      <td>
        The status can be any of the following:  

        * **1** if API call is a success  
        * **0** if the API has failed
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        msg
      </td>

      <td>
        This parameter contains a response message description.
      </td>

      <td>
        Refund Request Queued
      </td>
    </tr>

    <tr>
      <td>
        request\_id
      </td>

      <td>
        This parameter contains a unique refund ID generated by PayU.
      </td>

      <td>
        6582898821
      </td>
    </tr>

    <tr>
      <td>
        bank\_ref\_num
      </td>

      <td>
        This parameter contains a bank reference number is returned from bank.
      </td>

      <td>
        IRN6601148
      </td>
    </tr>

    <tr>
      <td>
        mihpayid
      </td>

      <td>
        This parameter contains a unique transaction ID generated by PayU during sale.
      </td>

      <td>
        7043873219
      </td>
    </tr>

    <tr>
      <td>
        error\_code
      </td>

      <td>
        This parameter contains the code for response. For a list of error codes and their description, refer to Refund Error Codes.
      </td>

      <td>
        102
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Note:
>
> The error\_code ​value 102​ should be treated as success; the rest are failures. To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).

</details>

## Request parameters

<details>  <summary>Reference information and other request parameters</summary>

<KeyHashForGeneralParametersDescription />

### Other request parameters

Other request parameters used for **Refund Transaction** API (which are not in the below form for Try It experience) are listed in the following table:

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
        var2
      </td>

      <td>
        This parameter must contain the Token ID (unique token from the merchant) for the refund request. Token ID has to be generated at your end for each new refund request. It is an identifier for each new refund request which can be used for tracking it. It must be unique for every new refund request generated – otherwise the refund request would not be generated successfully. Token ID length should not be greater than 23 characters.
      </td>
    </tr>

    <tr>
      <td>
        var3
      </td>

      <td>
        For captured transaction: This parameter must contain the amount which needs to be refunded. Both partial and full refunds are allowed. \
        For a partial refund, this var3 value would be less than the amount with which the transaction was made.  

        * **For a full refund**: The var3 value would be equal to the amount with which the transaction was made.  
        * **For pre-auth transaction**:  If the transaction is in a pre-auth state currently, the full cancellation is allowed. The amount must be the same as the auth amount. A partial amount would not be allowed.
      </td>
    </tr>

    <tr>
      <td>
        var5
      </td>

      <td>
        If a refund callback for a transaction is required on a specific URL, the URL must be specified in this parameter.
      </td>
    </tr>

    <tr>
      <td>
        var8:\
        `mandatory for split`
      </td>

      <td>
        Refund split information provided by merchant in a JSON format. This is applicable only with the Split transactions. The JSON format is described in the next able.
      </td>
    </tr>
  </tbody>
</Table>

The **var8** parameter is in a JSON format that contains the fields described in the following table:

<Table>
  <thead>
    <tr>
      <th>
        **Field**
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
        Split 1 Details
      </td>

      <td>
        The child merchant key, amount and aggregator refund amount is specified in the following format:\
        child\_merchant\_key\_1":\{ "amount": 100, aggregatorRefundAmount: 40 }  

        * \*Note\*\*: The aggregator refund amount is optional in this field.
      </td>

      <td>
        child\_merchant\_key\_1": \{ "amount": 100, aggregatorRefundAmount: 40 }
      </td>
    </tr>

    <tr>
      <td>
        Split 2 Details
      </td>

      <td>
        The child merchant key, amount and aggregator refund amount is specified similar to Split 1 details.
      </td>

      <td>
        child\_merchant\_key\_2": \{"amount": 20, aggregatorRefundAmount: 0 }
      </td>
    </tr>
  </tbody>
</Table>

**Sample JSON for var8**

```
{ "child_merchant_key_1": { "amount": 100, aggregatorRefundAmount: 40 }, "child_merchant_key_2": {"amount": 20, aggregatorRefundAmount: 0 }}
```

</details>

> 📘 Reference:
>
> var5 and var8 are optional parameters and not included in the following **Try It** experience. For more information on description with examples, refer to the [Other request parameters](#other-request-parameters) subsection.

**Example values**

Use the following sample values while trying out the API:

* `var1` (mihpayid): 403993715521937565
* `var2` (reference number for a refund provided by merchant): 20201105secrettokenaturend
