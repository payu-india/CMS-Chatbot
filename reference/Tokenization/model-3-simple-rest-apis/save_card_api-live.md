---
title: '[OLD]Save a Card API'
excerpt: 'API Command: **save_payment_instrument**'
api:
  file: storecard-1.json
  operationId: save_payment_instrument
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Save Card API is used for saving a card to the vault. After successfully storing a card, it returns the `cardToken`.

> 📘 Note
>
> As per RBI guidelines, taking consent from the customer and doing an additional factor of authentication is mandatory to tokenize the card. You must ensure this is done before using this API.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

## Response parameters

For the response parameter descriptions and sample responses, refer to [Additional Info for Simple REST APIs](/reference/additional-info-for-model-3-parameters#response-parameters-for-save-a-card-api).

## Reference info for request parameters

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>
      <th>
        Reference
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        key
      </td>
      <td>
        The merchant key provided by PayU while onboarding.

        For more information on how to generate the Key and Salt, refer to any of the following:  

        * **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  
        * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>
    <tr>
      <td>
        hash
      </td>
      <td>
        Hash logic for this API is:
        ```
        sha512(key|command|var1|salt)
        sha512
        ```
      </td>
    </tr>
    <tr>
      <td>
        var3
      </td>
      <td>
        For more information on card mode codes, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards).
      </td>
    </tr>
    <tr>
      <td>
        var4
      </td>
      <td>
        For more information on card type codes, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards)
      </td>
    </tr>
    <tr>
      <td>
        var6
      </td>
      <td>
        Use only the following **test cards** for doing mock API calls here:  

        * 4895370077346937 (VISA is the card type)  
        * 5506900480000008 (MAST is the card type)
      </td>
    </tr>
    <tr>
      <td>
        var9
      </td>
      <td>
        * **Note**: This parameter is mandatory for Rupay cards. Authentication reference number will be sent by the PG in the authorization response. Currently, this check is skipped by Rupay.
      </td>
    </tr>
  </tbody>
</Table>

## Request parameters