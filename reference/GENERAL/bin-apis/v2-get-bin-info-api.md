---
title: Get BIN Info API
deprecated: false
hidden: false
metadata:
  robots: index
---
The v2 **Get BIN Info** API is used to determine the following for a single card or multiple cards:

* Card's issuing bank
* Card type such as, Visa, Master, etc.
* Card category such as Credit/Debit, etc.
* Cards with zero redirect support
* Cards with SI support

You can fetch cards details with the following specific feature-level information:

* Complete BIN list having ATM PIN support is required
* Complete BIN list with OTP-on-the-fly support (IVR) is required

When fetching multiple card details, you can limit the number of card details in the response using the start index and offset.

**Environment**

|                        |                                                                                      |
| :--------------------- | :----------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/issuing-bank/v1/bin](https://test.payu.in/issuing-bank/v1/bin) |
| Production Environment | [https://info.payu.in/issuing-bank/v1/bin](https://info.payu.in/issuing-bank/v1/bin) |

## Request header

<V2_payment_header_params />

## Request body

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bin<br/><code>mandatory</code></td>
      <td><code>Integer</code> Specific output request type:<br/>• <strong>1</strong>: Fetch information for a single BIN level.<br/>• <strong>2</strong>: Fetch specific feature-level BIN list.<br/>• <strong>3</strong>: Fetch all BIN and related information.</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

<br />

## Sample request

```bash
curl --location 'https://info.payu.in/issuing-bank/v1/bin' \
--header 'Content-Type: application/json' \
--header 'date: {{date}}' \
--header 'Authorization: {{authorization}}' \
--data '{
    "bin": "512345"
  }'
```

## Response parameters

| Parameter | Description                                                                                                                                                                                                                                                                     |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| status    | This parameters provides the response whether the API was successful or not. This response value can contain any of the following: • **0** signifies that the API was not successful or invalid details. • **1** signifies that the API was successful in fetching the details. |
| data      | The card details are displayed in a JSON format. For more information, refer to the next table.                                                                                                                                                                                 |

## Card Details in bins_data Field

For multiple cards, the card details in the **bins_data** field are in a JSON array format, and fields in each JSON are described in the following table. For a single card, only the fields are displayed in JSON format.

> 📘 **Enable additionalCardType parameter:**
>
> To receive the response for the **additionalCardType** parameter or enable this parameter, you need to contact your PayU Key Account Manager (KAM) or [PayU Support](https://help.payu.in).

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        issuingBank
      </td>

      <td>
        The issuing bank of the card used for the transaction
      </td>
    </tr>

    <tr>
      <td>
        bin
      </td>

      <td>
        The BIN number of the card is displayed in the response.
      </td>
    </tr>

    <tr>
      <td>
        category
      </td>

      <td>
        Response value can contain any of the following: • **creditcard** signifies that the particular bin is a credit card BIN • **debitcard** signifies that the particular bin is a debit card BIN
      </td>
    </tr>

    <tr>
      <td>
        card_type
      </td>

      <td>
        Response value can contain any of the following: • MAST • VISA • MAES • AMEX • DINR • Unknown
      </td>
    </tr>

    <tr>
      <td>
        isDomestic
      </td>

      <td>
        Response value can contain any of the following:
        • **1** signifies that the particular BIN is Domestic.
        • **0** signifies that the particular BIN is International.
      </td>
    </tr>

    <tr>
      <td>
        additonalCardType
      </td>

      <td>
        The response contains any of the following values to show if it is corporate or prepaid card:
        • **CE** - Corporate card
        • **PE** - Prepaid card
        **Note**: To receive the response for this parameter or enable this parameter, you need to contact your PayU Key Account Manager (KAM) or

        [PayU Support](https://help.payu.in)

        .
      </td>
    </tr>

    <tr>
      <td>
        is_atmpin_card
      </td>

      <td>
        Response value can contain any of the following:
        • **0** signifies that the card is not an ATM card.
        • **1** signifies that the card is an ATM card.
      </td>
    </tr>

    <tr>
      <td>
        is_otp_on_the_fly
      </td>

      <td>
        Response value can contain any of the following:
        • **0** signifies that the card does not have OTP on the fly facility.
        • **1** signifies that the card have OTP on the fly facility.
      </td>
    </tr>

    <tr>
      <td>
        messageVersion
      </td>

      <td>
        Response value will contain the 3DS version supported by the CardBin/CardNumber. For example, it can be any of the following: • 1.0.2 • 2.1.0 • 2.2.0
        **Note**: This response parameter value is shown only if **var7** parameter value is posted in the request.
      </td>
    </tr>
  </tbody>
</Table>

To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/v2/reference/error-codes).

## Sample response

```
Array
(
    [status] => 1
    [data] => Array
        (
            [bins_data] => Array
                (
                    [issuing_bank] => HDFC
                    [bin] => 512345
                    [category] => creditcard
                    [card_type] => MAST
                    [is_domestic] => 1
                    [is_atmpin_card] => 1
                    [is_otp_on_the_fly] => 1
                    [is_zero_redirect_supported] => 1
                    [is_si_supported] => 0
                )
        )
)
```
