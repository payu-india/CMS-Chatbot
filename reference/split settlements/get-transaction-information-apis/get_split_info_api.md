---
title: Get Split Info API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Get Split Info API
  description: ''
  keywords:
    - Get Split Info API
    - ' Split Information API for Split Settlemements'
    - Get Information on Split Transactions
    - Information on Split Transactions
    - Split Transaction Information
  robots: index
next:
  description: ''
---
The **Get Split Info** API is used for getting split info of the parent transaction in the aggregator flow.

<GENERALAPIsEnvironment />

## Request parameters

The request body contains the following parameters:

<Table>
  <thead>
    <tr>
      <th>
        **Params**
      </th>
      <th>
        **Description**
      </th>
      <th>
        Example
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        key
        `mandatory`
      </td>
      <td>
        Merchant key provided by PayU
      </td>
      <td>
        JPM\*\*\*g
      </td>
    </tr>
    <tr>
      <td>
        command\
        `mandatory`
      </td>
      <td>
        This parameter must contain the API Command for getting Transaction. It should be `get_split_info` for **Get Split Info** API.
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        var1\
        `mandatory`
      </td>
      <td>
        This parameter must contain the PayU ID
      </td>
      <td>
         403993715532325577
      </td>
    </tr>
    <tr>
      <td>
        hash\
        `mandatory`
      </td>
      <td>
        This parameter must contain the hash value to be calculated at your end. Hash logic for this API is:
        ```
        sha512(key|command|payuId|salt) sha512
        ```
      </td>
      <td>
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```
curl --location 'https://test.payu.in/merchant/postservice.php?form=1' \
--header 'Cookie: PHPSESSID=j601h8g2u1cofo4u5it8v1lk8r; PHPSESSID=670cf11080b74' \
--form 'key="JPM***g"' \
--form 'command="get_split_info"' \
--form 'var1="403993715532325577"' \
--form 'hash="49fa996d81f66374fbe2eedfc494b48149f1abb9555afa0b0c03d671d7a769efd07e40eabee6571fba124966b1a2d219b8118ff9500456effb1e0ae63d94a3e2"' \
```

## Response parameters

<Table>
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
        payuId
      </td>
      <td>
        This parameter returns the parent merchant PayU ID that was posted in the API request.
      </td>
      <td>
        403993715532325577
      </td>
    </tr>
    <tr>
      <td>
        splitStatus
      </td>
      <td>
        This parameter returns the reason string. For a list of error codes for failure scenarios, refer to [Error codes for failure scenario](#error-codes-for-failure-scenario)
      </td>
      <td>
        success
      </td>
    </tr>
    <tr>
      <td>
        splits
      </td>
      <td>
        This parameter contains the response in a JSON array format. Each JSON object contains the following:  
        * merchant key
        * aggregator sub-transaction ID
        * amount
        * Transaction\_details field.
      </td>
      <td>
        ```
        {
                    "merchantKey": "iC***G",
                    "aggregatorSubTxnId": "dkjgfrfgnfm",
                    "amount": 900.00,
                    "splitType": "split"
          }
        ```
      </td>
    </tr>
  </tbody>
</Table>

<br />

## Sample response

### Success scenario

```
{
    "status": 1,
    "payuId": 403993715532325577,
    "splitStatus": "success",
    "splits": [
        {
            "merchantKey": "iC***G",
            "aggregatorSubTxnId": "dkjgfrfgnfm",
            "amount": 900.00,
            "splitType": "split"
        },
        {
            "merchantKey": "ut***U",
            "aggregatorSubTxnId": "dkfhdgfcdcddfn",
            "amount": 100.00,
            "splitType": "commission"
        }
    ]
}
```

## Error codes for failure scenario

<Table>
  <thead>
    <tr>
      <th>
        **Condition**
      </th>
      <th>
        **error\_code**
      </th>
      <th>
        **error\_message**
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        Hash validation failed
      </td>
      <td>
        AGG-300
      </td>
      <td>
        Hash validation failed
      </td>
    </tr>
    <tr>
      <td>
        invalid parent transaction Payu ID:  
        * non-existent PayuID
        * PayuID is not a parent transaction of aggregator flow
        * Payu ID belongs to some other merchant.
      </td>
      <td>
        AGG-301
      </td>
      <td>
        Invalid PayuID
      </td>
    </tr>
    <tr>
      <td>
        Split doesn’t exist for the transaction
      </td>
      <td>
        AGG-302
      </td>
      <td>
        Split doesn't exist for this transaction
      </td>
    </tr>
  </tbody>
</Table>