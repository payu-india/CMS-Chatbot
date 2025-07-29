---
title: v2 Get BIN Info API
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

| Environment            | URL                                                                                  |
| :--------------------- | :----------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/issuing-bank/v1/bin](https://test.payu.in/issuing-bank/v1/bin) |
| Production Environment | [https://info.payu.in/issuing-bank/v1/bin](https://info.payu.in/issuing-bank/v1/bin) |

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

  | Parameter | Description                                                                                                                                                                                                                                                                 |
  | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | status        | This parameters provides the response whether the API was successful or not. This response value can contain any of the following: • **0** signifies that the API was not successful or invalid details. • **1** signifies that the API was successful in fetching the details. |
  | data          | The card details are displayed in a JSON format. For more information, refer to the next table.                                                                                                                                                                                 |

  ## Card Details in bins\_data Field

  For multiple cards, the card details in the **bins\_data** field are in a JSON array format, and fields in each JSON are described in the following table. For a single card, only the fields are displayed in JSON format.

  > 📘 **Enable additionalCardType parameter:**
  >
  > To receive the response for the **additionalCardType** parameter or enable this parameter, you need to contact your PayU Key Account Manager (KAM) or [PayU Support](https://help.payu.in).

  | **Field**             | **Description**                                                                                                                                                                                                                                                                                                                 |
  | :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | issuingBank           | The issuing bank of the card used for the transaction                                                                                                                                                                                                                                                                           |
  | bin                   | The BIN number of the card is displayed in the response.                                                                                                                                                                                                                                                                        |
  | category              | Response value can contain any of the following: • **creditcard** signifies that the particular bin is a credit card BIN • **debitcard** signifies that the particular bin is a debit card BIN                                                                                                                                  |
  | card\_type            | Response value can contain any of the following: • MAST • VISA • MAES • AMEX • DINR • Unknown                                                                                                                                                                                                                                   |
  | isDomestic            | Response value can contain any of the following: • **1** signifies that the particular BIN is Domestic. • **0** signifies that the particular BIN is International.                                                                                                                                                             |
  | additonalCardType     | The response contains any of the following values to show if it is corporate or prepaid card: • **CE** - Corporate card • **PE** - Prepaid card **Note**: To receive the response for this parameter or enable this parameter, you need to contact your PayU Key Account Manager (KAM) or [PayU Support](https://help.payu.in). |
  | is\_atmpin\_card      | Response value can contain any of the following: • **0** signifies that the card is not an ATM card. • **1** signifies that the card is an ATM card.                                                                                                                                                                            |
  | is\_otp\_on\_the\_fly | Response value can contain any of the following: • **0** signifies that the card does not have OTP on the fly facility. • **1** signifies that the card have OTP on the fly facility.                                                                                                                                           |
  | messageVersion        | Response value will contain the 3DS version supported by the CardBin/CardNumber. For example, it can be any of the following: • 1.0.2 • 2.1.0 • 2.2.0 **Note**: This response parameter value is shown only if **var7** parameter value is posted in the request.                                                               |

  To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).

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