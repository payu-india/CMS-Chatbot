---
title: Fetch Balance API – Sodexo Integration
excerpt: 'API Command: **check\_balance**'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Fetch Balance **check\_balance** API command is used to check the balance of a Sodexo card. When using Seamless Integration, integrate this API and display the balance on the Checkout page to your customers.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

## Request parameters

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
        key
        `mandatory`
      </td>

      <td>
        This parameter must contain your merchant key shared by PayU during onboarding.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        command
        `mandatory`
      </td>

      <td>
        This parameters must contain the API command as **check\_balance**.
      </td>

      <td>
        check\_balance
      </td>
    </tr>

    <tr>
      <td>
        hash
        `mandatory`
      </td>

      <td>
        This parameter contains the hash. Use the following hash generation format:
        `sha512(key\|command\|var1\|salt) sha512`
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        var1
        `mandatory`
      </td>

      <td>
        This parameter must contain the Sodexo Source ID in JSON format as provided in the example.
      </td>

      <td>
        `{"sodexoSourceId":"src_81e2c860-631b-4b01-aefa-19cfa9c63415"}`
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Notes:
>
> * **var1** is in a JSON format. All the sub fields are to be sent as a json in var1. The whole JSON string should be used for hash generation.
> * **sourceId** is shared by PayU with merchants in the field3 parameter in any of the following API responses for all successful transactions wherever customer has provided permission to save their card.
>   * ws\_callback
>   * [Verify Payment API](ref:verify_payment_api)

## Sample request

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&command=check_balance&var1={\"sodexoSourceId\":\"src_81e2c860-631b-4b01-aefa-19cfa9c63415\"}&hash=fbd44e564f49aaa271250df4fc9fdc5a7eff98d961d6ca8e8049ae0f830d7ee7ff73a4b74c69c9742ccfe0c0478e737c4c685a3fe614ba5ef7edf706097e3346"
```

## Response parameters

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th><strong>Parameter</strong></th>
      <th><strong>Description</strong></th>
      <th><strong>Example</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>status</td>
      <td>
        This parameter returns the status of web service call. The status can be any of the following:
        <ul>
          <li>0 - If web service call failed.</li>
          <li>1 - If web service call succeeded.</li>
        </ul>
      </td>
      <td>1</td>
    </tr>
    <tr>
      <td>cardNo</td>
      <td>This parameter contains the Sodexo card number.</td>
      <td>637513XXXXXX9318</td>
    </tr>
    <tr>
      <td>cardBalance</td>
      <td>This parameter returns the card balance (in rupees).</td>
      <td>3000.00</td>
    </tr>
    <tr>
      <td>cardName</td>
      <td>This parameter contains name of the customer as on the Sodexo card.</td>
      <td>test</td>
    </tr>
    <tr>
      <td>msg</td>
      <td>This parameter contains the message, that is successful or failure.</td>
      <td>success</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

<br />

## Sample response

### Success scenario

```plaintext
{"status":1,"cardNo":"637513XXXXXX9318","cardBalance":".82","cardName":"test","msg":"success"}
```

### Failure scenarios

* Hash is invalid

```plaintext
{"status":0,"msg":"Invalid Hash."}
```

* Unable to fetch balance

```plaintext
{"status":0,"msg":"Unable to fetch balance"}
```

* Sodexo Source ID is not found

```plaintext
{"status":0,"msg":"Source not found."}
```