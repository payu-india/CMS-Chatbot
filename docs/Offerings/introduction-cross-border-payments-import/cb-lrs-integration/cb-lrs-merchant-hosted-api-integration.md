---
title: Integrate Merchant Hosted Checkout
deprecated: false
hidden: false
metadata:
  title: Integrate Merchant Hosted Checkout - Cross Border Transaction under LRS
  keywords:
    - Integrate Merchant Hosted Checkout for Cross Border Transaction under LRS
    - Integrate Merchant Hosted Checkout for CB LRS
  robots: index
---
PayU’s **_payment** API supports LRS implementation using the following parameters mandatorily in an S2S transaction:

* lrs_service_type
* lrs_mandatory_limit_declaration
* lrs_tnc
* tcs_amount
* buyer_type_business (optional)

The steps to integrate involves:

1. [Validate the PAN card](#step-1-validate-the-pan-card)
2. [Request Payment with PayU](#step-2-request-payment-with-payu)
3. [Check response from PayU](#step-3-check-response-from-payu)
4. [Verify the Payment](#step-4-verify-the-payment)

## Step 1: Validate the PAN card

The PAN Card Status Check API allows merchants to verify PAN (Permanent Account Number) card details. It validates whether a given PAN number is active, confirms if the provided name and date of birth match the official PAN records, and checks the seeding status of the PAN. This API is essential for KYC (Know Your Customer) processes, identity verification, and regulatory compliance.

**Endpoint**

```
https://test10-onboarding.payu.in/dvs/kyc/check_pan_card_status
```

### Request parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        pan_number
        `mandatory`
      </td>

      <td>
        The PAN (Permanent Account Number) to be verified
      </td>

      <td>
        `"CYCPD2784G"`
      </td>
    </tr>

    <tr>
      <td>
        name
        `mandatory`
      </td>

      <td>
        The name of the PAN card holder as it appears on the PAN card
      </td>

      <td>
        `"AKASH DEEP"`
      </td>
    </tr>

    <tr>
      <td>
        dob
        `mandatory`
      </td>

      <td>
        Date of Birth of the PAN holder in DD/MM/YYYY format
      </td>

      <td>
        `"15/09/1993"`
      </td>
    </tr>
  </tbody>
</Table>

### Sample request

```bash
curl --location 'https://test10-onboarding.payu.in/dvs/kyc/check_pan_card_status' \
--header 'Content-Type: application/json' \
--header 'Date: Thu, 17 Jun 2025 08:17:59 GMT' \
--header 'Digest: DFXmqI0rFnXlmHLlsRwdDMw9vUSVzyYQzGP+MKLo8f8=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="7qjgpH9B4QALxDR0nVlHdEKEYMZ0XeJ0QpnvveSyqMo="' \
--header 'platformId: 1' \
--data '{
    "pan_number": "CYCPD2784G",
    "name": "AKASH DEEP",
    "dob": "15/09/1993"
}'
```

### Sample response

```json
{
    "id": 86235,
    "api_name": "pan_status_check",
    "identifier": "79c0d918a4f4661cb9cb17d96d24ac1cf04b6013d504cc766ac5235380bfc0d5",
    "response": {
        "result": {
            "status": "Active",
            "nameMatch": "Y",
            "dobMatch": "Y",
            "seedingStatus": "Y"
        }
    },
    "status": "success",
    "http_status": 200,
    "client_id": "195ab95fa4700eeaaf38b7f5b538d2979f0f281e0a4eaedca1aa675b79b331a2",
    "created_at": "2025-04-30T05:51:40.000Z",
    "updated_at": "2025-04-30T05:51:40.000Z",
    "client_name": "SignzyClient"
}
```

### Response parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        id
      </td>

      <td>
        Unique identifier for the verification request
      </td>

      <td>
        `86235`
      </td>
    </tr>

    <tr>
      <td>
        api_name
      </td>

      <td>
        Identifier of the API that was called
      </td>

      <td>
        `"pan_status_check"`
      </td>
    </tr>

    <tr>
      <td>
        identifier
      </td>

      <td>
        A unique hash identifier for the verification request
      </td>

      <td>
        `"79c0d918a  
                                                                                                                                                                4f4661cb9cb  
                                                                                                                                                                17d96d24ac1  
                                                                                                                                                                cf04b6013d50  
                                                                                                                                                                4cc766ac5235  
                                                                                                                                                                380bfc0d5"`
      </td>
    </tr>

    <tr>
      <td>
        response
      </td>

      <td>
        Contains the verification results
      </td>

      <td>
        See result table below
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        Overall status of the API call
      </td>

      <td>
        `"success"`
      </td>
    </tr>

    <tr>
      <td>
        http_status
      </td>

      <td>
        HTTP status code of the response
      </td>

      <td>
        `200`
      </td>
    </tr>

    <tr>
      <td>
        client_id
      </td>

      <td>
        Unique identifier of the client making the request
      </td>

      <td>
        `"195ab95fa  
                                                                                                                                                                4700eeaaf38  
                                                                                                                                                                b7f5b538d29  
                                                                                                                                                                79f0f281e0  
                                                                                                                                                                a4eaedca1a  
                                                                                                                                                                a675b79b3  
                                                                                                                                                                31a2"`
      </td>
    </tr>

    <tr>
      <td>
        created_at
      </td>

      <td>
        Timestamp when the verification record was created
      </td>

      <td>
        `"2025-04-30T05:51:40.000Z"`
      </td>
    </tr>

    <tr>
      <td>
        updated_at
      </td>

      <td>
        Timestamp when the verification record was last updated
      </td>

      <td>
        `"2025-04-30T05:51:40.000Z"`
      </td>
    </tr>

    <tr>
      <td>
        client_name
      </td>

      <td>
        Name of the client account
      </td>

      <td>
        `"SignzyClient"`
      </td>
    </tr>
  </tbody>
</Table>

#### Response Result Object

| Parameter     | Description                                                        | Example    |
| ------------- | ------------------------------------------------------------------ | ---------- |
| status        | Status of the PAN card                                             | `"Active"` |
| nameMatch     | Indicates if the provided name matches with PAN records (Y/N)      | `"Y"`      |
| dobMatch      | Indicates if the provided DOB matches with PAN records (Y/N)       | `"Y"`      |
| seedingStatus | Indicates if the PAN is seeded with additional verifications (Y/N) | `"Y"`      |

## Step 2: Request Payment with PayU

The following parameters (mandatory) must be posted using any of the following seamless integration and refer to the corresponding section of [Web Checkout Integration](doc:introduction-web) documentation for the complete list of parameters to be posted:

* [Merchant Hosted Checkout > Cards](doc:collect-payments-with-cards-seamless)
* [Server-to-Server > General Integration](doc:integration-with-s2s)

### Request parameters

**Environment**

|                            |                                                                        |
| :------------------------- | :--------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/_payment>](https://secure.payu.in/_payment>) |

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
        `String`Merchant key provided by PayU during onboarding.
      </td>

      <td>
         JPg****f
      </td>
    </tr>

    <tr>
      <td>
        txnid
        `mandatory`
      </td>

      <td>
        `String`The transaction ID is a reference number for a specific order that is generated by the merchant.
      </td>

      <td>
        ypl938459435
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        `String`The transaction amount.
      </td>

      <td>
        100.00
      </td>
    </tr>

    <tr>
      <td>
        productinfo
        `mandatory`
      </td>

      <td>
        `String`A brief description of the product.
      </td>

      <td>
         iPhone
      </td>
    </tr>

    <tr>
      <td>
        firstname
        `mandatory`
      </td>

      <td>
        `String` The first name of the customer as on their Permanent Account Number (PAN)

        _Note: This should be validated by PAN Status Check API_
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        lastname
        `mandatory`
      </td>

      <td>
        `String` The last name of the customer as on their Permanent Account Number (PAN)

        _Note: This should be validated by PAN Status Check API_
      </td>

      <td>
        Kumar
      </td>
    </tr>

    <tr>
      <td>
        email
        `mandatory`
      </td>

      <td>
        `String`The email address of the customer.
      </td>

      <td>
         [abc@payu.in](mailto:abc@payu.in)
      </td>
    </tr>

    <tr>
      <td>
        phone
        `mandatory`
      </td>

      <td>
        `String`The phone number of the customer.
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        address1
        `optional`
      </td>

      <td>
        `String` The first line of the billing address.
        H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai

        * _Note_*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.
      </td>

      <td>
        34 Saikripa-Estate, Tilak Nagar
      </td>
    </tr>

    <tr>
      <td>
        address2
        `optional`
      </td>

      <td>
        `String` The second line of the billing address.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        city
        `optional`
      </td>

      <td>
        `String` The city where your customer resides as part of the billing address.
      </td>

      <td>
        Mumbai
      </td>
    </tr>

    <tr>
      <td>
        state
        `optional`
      </td>

      <td>
        `String` The state where your customer resides as part of the billing address,
      </td>

      <td>
        Maharashtra
      </td>
    </tr>

    <tr>
      <td>
        country
        `optional`
      </td>

      <td>
        `String` The country where your customer resides.
      </td>

      <td>
        India
      </td>
    </tr>

    <tr>
      <td>
        zipcode
        `mandatory`
      </td>

      <td>
        `String` Billing address zip code is mandatory for the cardless EMI option.
        `Character Limit-20
      </td>

      <td>
        400004
      </td>
    </tr>

    <tr>
      <td>
        pg
        `mandatory for seamless/s2s flow`
      </td>

      <td>
        `String` It defines the payment category that the merchant wants the customer to see by default on the PayU’s payment page. If this field is empty, the system assumes the credit card payment option by default.
      </td>

      <td>
        CC, NB or UPI
      </td>
    </tr>

    <tr>
      <td>
        bankcode
        `mandatory for seamless/s2s flow`
      </td>

      <td>
        `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option’s bank code value in it.
      </td>

      <td>
        AMEX
      </td>
    </tr>

    <tr>
      <td>
        ccnum
        `mandatory for cards`
      </td>

      <td>
        `String` Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to Card Number Formats and display error message on invalid input.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ccname
        `mandatory for cards`
      </td>

      <td>
        `String` This parameter must contain the name on card – as entered by the customer for the transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ccvv
        `mandatory for cards`
      </td>

      <td>
        `String` Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ccexpmon
        `mandatory for cards`
      </td>

      <td>
        `String` This parameter must contain the card’s expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ccexpyr
        `mandatory for cards`
      </td>

      <td>
        `String` This parameter must contain the card’s expiry year – as entered by the customer for the transaction. It must be of four digits.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        surl
        `mandatory`
      </td>

      <td>
        `String` The success URL, which is the page PayU will redirect to if the transaction is successful.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        furl
        `mandatory`
      </td>

      <td>
        `String`The Failure URL, which is the page PayU will redirect to if the transaction is failed.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf1
        `mandatory for LRS S2S transaction`
      </td>

      <td>
        `String` The Permanent Account Number (PAN) of the buyer must be collected in this field.
      </td>

      <td>
        AELPR****E
      </td>
    </tr>

    <tr>
      <td>
        udf3
        `mandatory for LRS S2S transaction`
      </td>

      <td>
        `String` The date of birth of the buyer must be collected using this field in the DD-MM-YYYY format as on their Permanent Account Number (PAN).

        _Note: This should be validated by PAN Status Check API_
      </td>

      <td>
        02-02-1980
      </td>
    </tr>

    <tr>
      <td>
        udf4
        `mandatory for payment aggregators`
      </td>

      <td>
        `String` This parameter must include end merchant legal entity name.
      </td>

      <td>
        XYZ Pvt. Ltd.
      </td>
    </tr>

    <tr>
      <td>
        udf5
        `mandatory`
      </td>

      <td>
        `String`The invoice ID or invoice number must be collected using this field.
      </td>

      <td>
        INV123456
      </td>
    </tr>

    <tr>
      <td>
        buyer_type_business
        `conditional for cross-border transactions`
      </td>

      <td>
        This parameter is used to identify whether it is a business-to-business transaction.  If 1 is posted, it is a B2B transaction.

        In case of B2B, no other LRS specific parameters (listed below) need to be sent, as B2B transactions are outside the scope of the regulation.
      </td>

      <td>
        0
      </td>
    </tr>

    <tr>
      <td>
        lrs_mandatory_limit_declaration

        `mandatory for LRS S3S transactions`
      </td>

      <td>
        `String`Mandatory declaration from buyer that they have remitted less than $250,000 USD under Liberalised Remittance Scheme.

        <br />

        **Note**: The limit is as per RBI regulation and needs to be mandatorily collected on the checkout page.

        <br />
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        lrs_tnc
        `mandatory for LRS S2S transactions`
      </td>

      <td>
        `String`Mandatory declaration from buyer that they agree to PayU's terms & conditions.

        <br />

        **Note**: The declaration needs to be taken mandatorily from the buyer on the checkout page.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        lrs_service_type
        `mandatory for LRS S2S transactions`
      </td>

      <td>
        `String` The LRS service type describes the nature of service & decides the tax amount based on it. For more information, refer to the [lrs_service_type parameter values](#lrs_service_type-parameter-values)  table.
      </td>

      <td>
        travel
      </td>
    </tr>

    <tr>
      <td>
        tcs_amount
        `mandatory for LRS S2S transactions`
      </td>

      <td>
        `String` Amount of TCS (Tax Collected at Source) to be charged.  

        **Note**: The amount needs to be captured as per guidance in the [lrs_service_type parameter values](#lrs_service_type-parameter-values)   table.
      </td>

      <td>
        2.00
      </td>
    </tr>

    <tr>
      <td>
        lrs_tcs_declaration_under_limit  

        `mandatory for LRS S2S transactions`
      </td>

      <td>
        `String`Declaration from buyer that they are either under or over INR 1,00,000 based on which TCS will be collected.  

        Values expected:

        **0** (in case of under the limit)  
        **1**   (in case of over the limit  

        **Note**: The declaration needs to be taken mandatorily from the buyer on the checkout page. Also, when user declares they are over the limit (i.e. when this param is sent as "1", the "tcs_amount" field to contain amount calculated as per the the [lrs_service_type parameter values](#lrs_service_type-parameter-values)    table.
      </td>

      <td>
        0 / 1
      </td>
    </tr>
  </tbody>
</Table>

#### lrs_service_type parameter values

<HTMLBlock>{`
<HTMLBlock>{\`
<table>
    <tbody>
        <tr>
            <td>
                <strong>lrs_service_type</strong>&nbsp;
            </td>
            <td>
                <strong>Txn Amount &lt;= INR 10 lacs</strong>&nbsp;
            </td>
            <td>
                <strong>Txn Amount &gt; INR 10 lacs</strong>&nbsp;
            </td>
        </tr>
        <tr>
            <td>
                education_loan&nbsp;
            </td>
            <td>
                0&nbsp;
            </td>
            <td>
                0&nbsp;
            </td>
        </tr>
        <tr>
            <td>
                education_non_loan&nbsp;
            </td>
            <td>
                0&nbsp;
            </td>
            <td>
                5%&nbsp;
            </td>
        </tr>
        <tr>
            <td>
                medical&nbsp;
            </td>
            <td>
                0&nbsp;
            </td>
            <td>
                5%&nbsp;
            </td>
        </tr>
        <tr>
            <td>
                travel&nbsp;
            </td>
            <td>
                0&nbsp;
            </td>
            <td>
                20%&nbsp;
            </td>
        </tr>
        <tr>
            <td>
                others&nbsp;
            </td>
            <td>
                0&nbsp;
            </td>
            <td>
                20%&nbsp;
            </td>
        </tr>
    </tbody>
</table>
\`}</HTMLBlock>
`}</HTMLBlock>

<br />

### Sample request

```curl
curl --location 'https://test.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=PRiQvJ' \
--data-urlencode 'txnid=my_order_64240' \
--data-urlencode 'amount=5' \
--data-urlencode 'productinfo=asfas' \
--data-urlencode 'email=test@test.com' \
--data-urlencode 'phone=8688359250' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'hash={{hash}}' \
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=CC' \
--data-urlencode 'surl=https://test.payu.in/admin/test_response' \
--data-urlencode 'furl=https://test.payu.in/admin/test_response' \
--data-urlencode 'udf1=CYCPD2784G' \
--data-urlencode 'udf2=' \
--data-urlencode 'udf3=02-02-1980' \
--data-urlencode 'udf4=XYZ Pvt. Ltd' \
--data-urlencode 'udf5=INV123456' \
--data-urlencode 'ccnum=5506900480000008' \
--data-urlencode 'ccexpyr=2025' \
--data-urlencode 'ccexpmon=09' \
--data-urlencode 'ccvv=123' \
--data-urlencode 'ccname=test' \
--data-urlencode 'si_details={"billingAmount":"10.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval": 1,"paymentStartDate":"2024-11-19","paymentEndDate":"2025-12-01"}' \
--data-urlencode 'api_version=7' \
--data-urlencode 'si=1' \
--data-urlencode 'firstname=sudhanshu' \
--data-urlencode 'user_credentials=T58CQx:sudhanshu' \
--data-urlencode 'address1=308,third floor' \
--data-urlencode 'address2=testing' \
--data-urlencode 'city=ggn' \
--data-urlencode 'state=UP' \
--data-urlencode 'country=IND' \
--data-urlencode 'zipcode=122018' \
--data-urlencode 'buyer_type_business=0' \
--data-urlencode 'lrs_mandatory_limit_declaration=1' \
--data-urlencode 'lrs_tnc=1' \
--data-urlencode 'lrs_service_type=travel' \
--data-urlencode 'lrs_tcs_declaration_under_limit=0'  

```

## Step 3: Check response from PayU

<ReverseHashing />

### Sample response (parsed)

* Success scenario

```
Array
(
    [mihpayid] => 403993715524069222
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => JF***g
    [txnid] => EaE4ZO3vU4iPsp
    [amount] => 10.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 12
    [addedon] => 2021-09-08 19:37:19
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => test@gmail.com
    [phone] => 9876543210
    [udf1] => 
    [udf2] => 
    [udf3] => 
    [udf4] => 
    [udf5] => 
    [udf6] => 
    [udf7] => 
    [udf8] => 
    [udf9] => 
    [udf10] => 
    [hash] => ed99957adb08fea56c907b88e8d158a79c3562c67f96c298461509826f77a7ae9e88b2a176b3234c25f50bcd451271728719656f3bb59c13a52bebabc468615a
    [field1] => 0608273386032718000015
    [field2] => 986987
    [field3] => 10.00
    [field4] => 403993715524069222
    [field5] => 100
    [field6] => 02
    [field7] => AUTHPOSITIVE
    [field8] => 
    [field9] => Transaction is Successful
    [payment_source] => payu
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 0608273386032718000015
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => payu
    [cardnum] => 512345XXXXXX2346
		[tcs_amount] => 2
)
```

* Failure scenario

```
Array
(
    [mihpayid] => 20869277619
    [mode] => CC
    [status] => failure
    [unmappedstatus] => failed
    [key] => L43t1c
    [txnid] => 26ba7cd6a67b0a010542
    [amount] => 10.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 0.00
    [addedon] => 2024-09-05 17:46:10
    [productinfo] => Product Info
    [firstname] => Payu-Admin
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => test@example.com
    [phone] => 1234567890
    [udf1] => 
    [udf2] => 
    [udf3] => 
    [udf4] => 
    [udf5] => 
    [udf6] => 
    [udf7] => 
    [udf8] => 
    [udf9] => 
    [udf10] => 
    [hash] => ac7720e4bc33e5494bec6d37302e522171175a987f9d47286bfd29e8a7fc794f56433fcacf0bc120db781c4dc1d05a4857d71e83f00f6ed6aa9c97a1938b9467
    [field1] => 
    [field2] => 
    [field3] => 
    [field4] => 
    [field5] => 05
    [field6] => 
    [field7] => AUTHNEGATIVE
    [field8] => 
    [field9] => Authorization failed at Bank
    [payment_source] => payu
    [pa_name] => PayU
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 2409052690
    [bankcode] => AMEX
    [error] => E1903
    [error_Message] => Authorization failed at Bank
    [cardnum] => XXXXXXXXXXXX2003
    [cardhash] => This field is no longer supported in postback params.
		[tcs_amount] => 2
)
```

## Step 4: Verify the Payment

Verify the transaction details using the Verification APIs. For API reference, refer to [Verify Payment API](doc:verify_payment_api) under API Reference.
