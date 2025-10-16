---
title: Get BIN Info API
api:
  file: bin-info-8.json
  operationId: GetBinInfoAPI
deprecated: false
hidden: false
link:
  new_tab: false
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
---
The **Get BIN Info** API or **getBinInfo** API is used to determine the following for a single card or multiple cards:

* Card's issuing bank
* Card type such as, Visa, Master, etc.
* Card category such as Credit/Debit, etc.
* Cards with zero redirect support
* Cards with SI support

You can fetch cards details with the following specific feature-level information:

* Complete BIN list having ATM PIN support is required
* Complete BIN list with OTP-on-the-fly support (IVR) is required

<Callout icon="📘" theme="info">
  **Use 9-digit BIN for more accuracy**: It is highly recommended to utilize a 9-digit BIN for more accuracy, as banks are transitioning from 6-digit BINs to an 8-9 digit BIN range. PayU will provide the corresponding available BIN within the response.
</Callout>

<GENERALAPIsEnvironment />

<Accordion title="BIN API Use Cases" icon="fa-info-circle">
  The following table shows different use cases for BIN (Bank Identification Number) lookup system, with various parameters (var1-var5) and their corresponding descriptions. The empty backticks (\`\`) in var2 for some rows likely represent empty or null values for that parameter.

  | Use Case              | var1 | var2   | var3 | var4 | var5 | Description                                |
  | --------------------- | ---- | ------ | ---- | ---- | ---- | ------------------------------------------ |
  | Single BIN Query      | 1    | 512345 | 0    | 0    | 0    | Get info for specific BIN                  |
  | Single BIN + Enhanced | 1    | 512345 | 0    | 0    | 1    | Single BIN with zero redirect & SI support |
  | ATM PIN Support Cards | 2    | 1      | 1    | 20   | 0    | Get BINs with ATM PIN support              |
  | OTP Support Cards     | 2    | 2      | 1    | 20   | 0    | Get BINs with OTP-on-the-fly support       |
  | All Cards - Page 1    | 3    | \`\`   | 1    | 20   | 0    | First 20 cards (records 1-20)              |
  | All Cards - Page 2    | 3    | \`\`   | 21   | 20   | 0    | Next 20 cards (records 21-40)              |
  | All Cards - Page 3    | 3    | \`\`   | 41   | 20   | 0    | Next 20 cards (records 41-60)              |
  | Large Batch Query     | 3    | \`\`   | 1    | 100  | 0    | Get 100 cards at once                      |
  | Custom Range          | 3    | \`\`   | 501  | 50   | 0    | Cards 501-550                              |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ## For Single Card

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

  ## For Multiple Cards

  ```bash
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=getBinInfo&var1=3&var2=&var3=1&var4=5&var5=&hash=df4ff56008defd9d7f9bf09506061f5c790dbe1d011659d85b88d34323ff49a65181e522eddf3075285c17708566709c803d3b0b0979120804b00f62236062a2"
  ```

  > 📘 **Note**
  >
  > When querying multiple cards, make sure to set the appropriate values for var3 (start index) and var4 (offset).
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ## Success Scenario

  **For single card:**

  ```php
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
  > Ensure that the value of the **is\_otp\_on\_the\_fly** parameter is 1. Only if the value is 1, you can fetch the card details with the Native OTP support.

  **For multiple cards:**

  ```php
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

  ## Failure Scenarios

  **If BIN is not passed with var2 when requesting for single BIN details (var1=1):**

  ```php
  Array
  (
      [status] => 0
      [data] => Invalid bin passed in var2
  )
  ```

  **If BIN is passed with var2 when multiple card details are request (var1=2):**

  ```php
  Array
  (
      [status] => 0
      [data] => Invalid var2, it should be either 1 or 2 according to feature
  )
  ```

  **If BIN is passed with var2 and multiple card details are requested (var1=3):**

  ```php
  Array
  (
      [status] => 0
      [data] => Invalid var2, it should be empty as var1 is 3
  )
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  ## Main Response Parameters

  | **Parameter** | **Description**                                                                                                                                                                                                                                                                 |
  | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | status        | This parameters provides the response whether the API was successful or not. This response value can contain any of the following: • **0** signifies that the API was not successful or invalid details. • **1** signifies that the API was successful in fetching the details. |
  | data          | The card details are displayed in a JSON format. For more information, refer to the next table.                                                                                                                                                                                 |

  ## Multiple Cards Response Fields

  When multiple cards are queried using this API, the fields in the following table are displayed in the JSON format:

  | **Field**    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  | :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | total\_count | The total number of card details fetched and displayed in JSON format.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
  | last         | This parameter returns any of the following values based on the last page of BIN information displayed: • **0**: The value 0 (zero) is returned if this the not last set of bin information returned. • **1**: The value 1 is returned if this the last set of bin information returned. For example, if the total\_count=2308 of bins are returned for a query, if you are posting var3=2300 (index) and var4=10 (offset), the last eight bins information are displayed and this parameter value is 1 |
  | bins\_data   | The BIN information of the cards are displayed in a JSON array format and details of fields in each JSON are described in the next table.                                                                                                                                                                                                                                                                                                                                                               |
  | next\_start  | The index of the card next start is returned in the response.                                                                                                                                                                                                                                                                                                                                                                                                                                           |

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
</Accordion>

## Request Parameters

<Accordion title="Additional information for request parameters" icon="fa-book">
  ## Reference Information for Request Parameters

  | Parameter | Reference                                                                                                                                                                                                                                                                                    |
  | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **key**   | For more information on how to generate the Key and Salt, refer to any of the following: • **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard) • **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt) |
  | **hash**  | Hash logic for this API is: sha512(key\\\|command\\\|var1\\\|salt) sha512                                                                                                                                                                                                                    |

  ## Request Parameters Description

  | Parameter | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  | :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | var1      | Specify any of the following values in this field based on the output you required: • **1**: Specify this value if a single bin-level information is required. Output contains the information on a single bin only. • **2**: Specify this value if a specific feature-level information is required. Output would give the bin list. • **3**: Specify this value if all the bins and their information are required                                                                                                                                                                                            |
  | var2      | The value specified in this parameter is based on any of the following var1 parameter value. If var1 = 1, specify the bin number in the var2 parameter. If var1 = 2, specify any of the following values: • **1**: Specify this value to get complete bin list having ATM PIN support is required • **2**: Specify this value to get complete bin list with OTP-on-the-fly support (IVR) is required                                                                                                                                                                                                            |
  | var3      | Specify the start index in this parameter. By default, the value will be set as 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | var4      | The offset is specified in this field. This is useful when several card bins are returned and you can display number of bins per page based on the offset. By default, it is set as 100.                                                                                                                                                                                                                                                                                                                                                                                                                        |
  | var5      | The parameter is used to check whether the Native OTP or SI is supported by the card. The is\_zero\_redirect\_supported and is\_si\_supported parameters return the response for the following cases: • If var1=1 and var5=1, two extra parameters will be sent in response - is\_zero\_redirect\_supported - is\_si\_supported • If var1 is specified with the value as 2 or 3 and var5 is specified as 0 or 1, and the is\_zero\_redirect\_supported and is\_si\_supported parameters will not return a response **Note**: The var2 parameter value needs to be posted according to the var1 parameter value. |

  ## Example Values

  Use the following sample values while trying out the API:

  * `var1`: 1/2/3, refer to [reference information](#reference-information-for-request-parameters) for the description of this parameter.
  * `var2` (BIN number): 512345, refer to [reference information](#reference-information-for-request-parameters) for the description of this parameter.

  **Important Notes:**

  1. **Single Card Query**: Use var1=1 and specify the BIN number in var2
  2. **Feature-based Query**: Use var1=2 to get specific feature lists (ATM PIN or OTP support)
  3. **All Cards Query**: Use var1=3 to get all BIN information with pagination
  4. **Pagination**: Use var3 (start index) and var4 (offset) for managing large result sets
  5. **Enhanced Features**: Use var5=1 to get zero redirect and SI support information
  6. **3DS Version**: Include var7 parameter to get messageVersion in response
</Accordion>
