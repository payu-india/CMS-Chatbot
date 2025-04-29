---
title: OLD-Get Payment Details (Cryptogram)
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to get the payment details of an existing card stored on PayU Vault so that you can use it with third-party tokenization. The payment details include the cryptogram, PAR, card number, card token, issuer token details and network token details as listed in the [Response Parameters table](#response-parameters) of this section.

HTTP Method: **POST**

**Environment**

| Test Environment       | [https://test.payu.in/merchant](https://test.payu.in/merchant)   |
| :--------------------- | :--------------------------------------------------------------- |
| Production Environment | [https://info.payu.in/merchant/](https://info.payu.in/merchant/) |

## Request parameters

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
        key
        **mandatory**
      </td>

      <td>
        For more information on how to generate the Key and Salt, refer to any of the following:\
        \- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)\
        \- **Test**:: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>

      <td>
        JF\*\*\*g
      </td>
    </tr>

    <tr>
      <td>
        command\
        **mandatory**
      </td>

      <td>
        `varchar` The command name for this REST API call must be included in this parameter. For getting user cards details, use **get\_payment\_details** here.
      </td>

      <td>
        get\_payment\_details
      </td>
    </tr>

    <tr>
      <td>
        hash\
        **mandatory**
      </td>

      <td>
        `varchar` The hash must be included in this parameter. The hash logic for is:\
        sha512(key|command|var1|salt) sha512
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        var1\
        **mandatory**
      </td>

      <td>
        `varchar` The user credentials is posted in this parameter in the following format: MerchantKey:UserId
      </td>

      <td>
        J\*\*\*G:abc
      </td>
    </tr>

    <tr>
      <td>
        var2\
        **mandatory**
      </td>

      <td>
        `varchar` The card token of the card (cardToken) is specified in this parameter.
      </td>

      <td>
        745d72e2fd9b7e88824fef4e7ed7dac1f
      </td>
    </tr>

    <tr>
      <td>
        var3\
        **mandatory**
      </td>

      <td>
        `float` The amount of the transaction
      </td>

      <td>
        10.00
      </td>
    </tr>

    <tr>
      <td>
        var4\
        **optional**
      </td>

      <td>
        `varchar` The currency used for the transaction.  

        * \*Note\*\*: If this parameter is left blank, the currency is considered as INR by default.
      </td>

      <td>
        INR
      </td>
    </tr>

    <tr>
      <td>
        var5\
        **optional**
      </td>

      <td>
        `varchar` The cardToken type is specified in this parameter and can be any of the following:  

        * \*Note\*\*: If this parameter is left blank, the default value will be PAYU.
      </td>

      <td>
        PAYU
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
“key=T****T&command=get_payment_details&var1=“merchant:user”&var2=60ac1025f09d1965b7dae2&var2=My_card&var3=10&var4=INR&
hash=e2f11b3818772b1851937ad6181c70b25f1dd296cb55ab507f0199c32239b76440889254e7f33c3fd111d87553d17ab4ee7a191e9cbb5d3484915ad00f4711e2”
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
        The status of the response can be any of the following:  

        * 1: Success  
        * . 2: Failure
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
        The description of the response whether the card details were stored successfully or not stored.
      </td>

      <td>
        Instrument details
      </td>
    </tr>

    <tr>
      <td>
        card details
      </td>

      <td>
        (Array format) | The details are sent by PayU in Array format for the successful response. The next table describes the details in the Array format.
      </td>

      <td>
        Refer the [sample response](#sample_response).
      </td>
    </tr>
  </tbody>
</Table>

The details on the Array format for a successful response is described in the following table:

<Table>
  <thead>
    <tr>
      <th>
        **Array Parameter**
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
        cryptogram
      </td>

      <td>
        The cryptogram used for encryption is returned in this parameter. This can be also a TAVV. TAVV is a 20-byte Base64-encoded binary value that is used with tokens.
      </td>

      <td>
        `0c186bdb8c0ebda30ab9d92816772cbfb946d027`
      </td>
    </tr>

    <tr>
      <td>
        card PAR
      </td>

      <td>
        This parameter returns the PAR (Payment Account Reference). This is a unique identity for the card across all the tokens. Typically, this will be used for offers and risk checks.
      </td>

      <td>
        RCKGgxEEFX1un19I
      </td>
    </tr>

    <tr>
      <td>
        card\_no
      </td>

      <td>
        This parameter returns a masked card number with only the last four digits.
      </td>

      <td>
        xxxxxxxxxxxx858
      </td>
    </tr>

    <tr>
      <td>
        card\_token
      </td>

      <td>
        This parameter returns the card token of the card.
      </td>

      <td>
        745d72e2fd9b7e88824fef4e7ed7dac1fe624b7
      </td>
    </tr>

    <tr>
      <td>
        issuer\_token
      </td>

      <td>
        This parameter returns the details of the issuer token in a JSON format.
      </td>

      <td>
        \{  

        "token\_value": "512\*\*\*6789012346",  

        "is\_expired": 0,  

        "token\_exp\_mon": "11",  

        "token\_exp\_yr": "2021",  

        "token\_bin": "512345"  

        }
      </td>
    </tr>

    <tr>
      <td>
        network\_token
      </td>

      <td>
        This parameter returns the details of the network token in a JSON format.
      </td>

      <td>
        \{  

        "token\_value": "512\*\*\*6789012346",  

        "is\_expired": 0,  

        "token\_exp\_mon": "11",  

        "token\_exp\_yr": "2021",  

        "token\_bin": "512345"  

        }
      </td>
    </tr>
  </tbody>
</Table>

## Sample response

### Successful scenario

```plaintext
{
    "status": "1",
    "msg": "Instrument details",
    "details": {
        "one_click_status": "",
        "one_click_flow": "",
        "card_type": "VISA",
        "network_token": {
            "token_exp_yr": "2025",
            "token_value": "464***7450050615",
            "token_exp_mon": "01"
        },
        "trid": "400600",
        "card_mode": "",
        "token_refernce_id": "477***84a5079512934417214171fd01",
        "card_no": "XXXXXXXXXXXX0615",
        "card_PAR": "V0010013021031409361532",
        "one_click_card_alias": "",
        "card_token": "60ac1025f09d1965b7dae2",
        "card_name": "",
        "cryptogram": "/wAAAAoAtd1XnhwAmbHTgkUAAAA="
    }
}
```

### Failure scenario

```plaintext
{
"status": 0,
"msg": card not found
}
```
