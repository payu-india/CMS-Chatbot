---
title: Get BIN Info API
excerpt: ''
api:
  file: bin-info-8.json
  operationId: GetBinInfoAPI
deprecated: false
hidden: false
metadata:
  title: Get BIN Info API
  description: >-
    The Get BIN Info API allows users to retrieve detailed information about a
    card or multiple cards, including the issuing bank, card type, category, and
    support for features like ATM PIN and OTP-on-the-fly, with options to limit
    the response using start index and offset.
  keywords:
    - get_bin_info API Command
    - ' Get BIN Info API'
    - ' BIN Info'
    - ' Card BIN Information'
  robots: index
next:
  description: ''
---
Here's the fixed version of the content with all MDX issues resolved:

```markdown
# Get BIN Info API

The **Get BIN Info** API or **getBinInfo** API is used to determine the following for a single card or multiple cards: 

* Card's issuing bank
* Card type such as, Visa, Master, etc.
* Card category such as Credit/Debit, etc.
* Cards with zero redirect support
* Cards with SI support

You can fetch cards details with the following specific feature-level information:

* Complete BIN list having ATM PIN support is required
* Complete BIN list with OTP-on-the-fly support (IVR) is required

When fetching multiple card details, you can limit the number of card details in the response using the start index and offset.

## Environment

| Environment | URL |
|:------------|:----|
| Test Environment | https://test.payu.in/merchant/postservice?form=2 |
| Production Environment | https://info.payu.in/merchant/postservice?form=2 |

## Sample request

**For single card**

The following values are specified in the var1, var2, and var5 for this scenario:

* var1 = 1
* var2 = 512345
* var5 = 1

```bash
curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g&command=getBinInfo&var1=2&var2=512345&var3=&var4=&var5=1&hash=df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
```

**For multiple cards**

```bash
curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g&command=getBinInfo&var1=3&var2=&var3=1&var4=5&var5=&hash=df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
```

> 📘 **Note**
> 
> When querying multiple cards, make sure to set the appropriate values for var3 (start index) and var4 (offset).


## Sample response

**Success Scenario**

For single card:

```plaintext
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

> 📘 **Note**
>
> Ensure that the value of the **is_otp_on_the_fly** parameter is 1. Only if the value is 1, you can fetch the card details with the Native OTP support.

For multiple cards:

```plaintext
Array
(
    [status] => 1
    [data] => Array
        (
            [total_count] => 2580
            [last] => 0
            [bins_data] => Array
                (
                    [37100] => Array
                        (
                            [issuing_bank] => AMEX
                            [bin] => 37100
                            [category] => UNKNOWN
                            [card_type] => AMEX
                            [is_domestic] => 1
                            [is_atmpin_card] => 1
                            [is_otp_on_the_fly] => 1
                        )

                    [37200] => Array
                        (
                            [issuing_bank] => AMEX
                            [bin] => 37200
                            [category] => UNKNOWN
                            [card_type] => AMEX
                            [is_domestic] => 1
                            [is_atmpin_card] => 1
                            [is_otp_on_the_fly] => 1
                        )

                    [37443] => Array
                        (
                            [issuing_bank] => AMEX
                            [bin] => 37443
                            [category] => UNKNOWN
                            [card_type] => AMEX
                            [is_domestic] => 1
                            [is_atmpin_card] => 1
                            [is_otp_on_the_fly] => 1
                        )

                    [37653] => Array
                        (
                            [issuing_bank] => AMEX
                            [bin] => 37653
                            [category] => UNKNOWN
                            [card_type] => AMEX
                            [is_domestic] => 1
                            [is_atmpin_card] => 1
                            [is_otp_on_the_fly] => 1
                        )

                    [37700] => Array
                        (
                            [issuing_bank] => AMEX
                            [bin] => 37700
                            [category] => UNKNOWN
                            [card_type] => AMEX
                            [is_domestic] => 1
                            [is_atmpin_card] => 1
                            [is_otp_on_the_fly] => 1
                        )

                )

            [nextStart] => 6
        )

)
```

**Failure scenario**

If BIN is not passed with var2 when requesting for single BIN details (var1=1):

```plaintext
Array
(
    [status] => 0
    [data] => Invalid bin passed in var2
)
```

If BIN is passed with var2 when multiple card details are request (var1=2):

```plaintext
Array
(
    [status] => 0
    [data] => Invalid var2, it should be either 1 or 2 according to feature
)
```

If BIN is passed with var2 and multiple card details are requested (var1=3):

```plaintext
Array
(
    [status] => 0
    [data] => Invalid var2, it should be empty as var1 is 3
)
```
## Response parameters description

| **Parameter** | **Description** |
|:--------------|:----------------|
| status | This parameters provides the response whether the API was successful or not. This response value can contain any of the following:* **0** signifies that the API was not successful or invalid details. * **1** signifies that the API was successful in fetching the details. |
| data | The card details are displayed in a JSON format. For more information, refer to the next table. |

When multiple cards are queried using this API, the fields in the following table are displayed in the JSON format:

| **Field** | **Description** |
|:----------|:----------------|
| total_count | The total number of card details fetched and displayed in JSON format. |
| last | This parameter returns any of the following values based on the last page of BIN information displayed: * **0**: The value 0 (zero) is returned if this the not last set of bin information returned. * **1**: The value 1 is returned if this the last set of bin information returned. For example, if the total_count=2308 of bins are returned for a query, if you are posting var3=2300 (index) and var4=10 (offset), the last eight bins information are displayed and this parameter value is 1 |
| bins_data | The BIN information of the cards are displayed in a JSON array format and details of fields in each JSON are described in the next table. |
| next_start | The index of the card next start is returned in the response. |

For multiple cards, the card details in the **bins_data** field are in a JSON array format, and fields in each JSON are described in the following table. For a single card, only the fields are displayed in JSON format.

> 📘 **Enable additionalCardType parameter:**
>
> To receive the response for the **additionalCardType** parameter or enable this parameter, you need to contact your PayU Key Account Manager (KAM) or [PayU Support](https://help.payu.in).

| **Field** | **Description** |
|:----------|:----------------|
| issuingBank | The issuing bank of the card used for the transaction |
| bin | The BIN number of the card is displayed in the response. |
| category | Response value can contain any of the following: * **creditcard** signifies that the particular bin is a credit card BIN * **debitcard** signifies that the particular bin is a debit card BIN |
| card_type | Response value can contain any of the following: * MAST* VISA * MAES* AMEX* DINR * Unknown |
| isDomestic | Response value can contain any of the following: * **1** signifies that the particular BIN is Domestic. * **0** signifies that the particular BIN is International. |
| additonalCardType | The response contains any of the following values to show if it is corporate or prepaid card: * **CE** - Corporate card* **PE** - Prepaid card**Note**: To receive the response for this parameter or enable this parameter, you need to contact your PayU Key Account Manager (KAM) or [PayU Support](https://help.payu.in). |
| is_atmpin_card | Response value can contain any of the following:* **0** signifies that the card is not an ATM card.* **1** signifies that the card is an ATM card. |
| is_otp_on_the_fly | Response value can contain any of the following:* **0** signifies that the card does not have OTP on the fly facility.* **1** signifies that the card have OTP on the fly facility. |
| messageVersion | Response value will contain the 3DS version supported by the CardBin/CardNumber. For example, it can be any of the following: * 1.0.2* 2.1.0* 2.2.0 **Note**: This response parameter value is shown only if **var7** parameter value is posted in the request. |

To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).

## Request parameters

### Reference information for request parameters

| Parameter | Reference |
|:----------|:----------|
| **key** | For more information on how to generate the Key and Salt, refer to any of the following:* **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)* **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt) |
| **hash** | Hash logic for this API is: ```sha512(key|command|var1|salt) sha512``` |
| var1 | Specify any of the following values in this field based on the output you required: * **1**: Specify this value if a single bin-level information is required. Output contains the information on a single bin only. * **2**: Specify this value if a specific feature-level information is required. Output would give the bin list. * **3**: Specify this value if all the bins and their information are required |
| var2 | The value specified in this parameter is based on any of the following var1 parameter value. If var1 = 1, specify the bin number in the var2 parameter. If var1 = 2, specify any of the following values: * **1**: Specify this value to get complete bin list having ATM PIN support is required * **2**: Specify this value to get complete bin list with OTP-on-the-fly support (IVR) is required |
| var3 | Specify the start index in this parameter. By default, the value will be set as 0. |
| var4 | The offset is specified in this field. This is useful when several card bins are returned and you can display number of bins per page based on the offset. By default, it is set as 100. |
| var5 | The parameter is used to check whether the Native OTP or SI is supported by the card. The is_zero_redirect_supported and is_si_supported parameters return the response for the following cases:* If var1=1 and var5=1, two extra parameters will be sent in response   - is_zero_redirect_supported  - is_si_supported * If var1 is specified with the value as 2 or 3 and var5 is specified as 0 or 1, and the is_zero_redirect_supported and is_si_supported parameters will not return a response **Note**: The var2 parameter value needs to be posted according to the var1 parameter value. |


## Example values

Use the following sample values while trying out the API:

* `var1`: 1/2/3, refer to [reference information](https://docs.payu.in/reference/get_bin_info_api#reference-information-for-request-parameters) for the description of this parameter. 
* `var2` (BIN number): 512345, refer to [reference information](https://docs.payu.in/reference/get_bin_info_api#reference-information-for-request-parameters) for the description of this parameter.
