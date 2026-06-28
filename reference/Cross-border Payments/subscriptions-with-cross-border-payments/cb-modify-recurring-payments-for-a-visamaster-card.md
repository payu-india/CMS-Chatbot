---
title: Modify Recurring Payments for a VISA/MASTER Card - Cross-Border Payments
excerpt: 'Resource: **_payment**'
deprecated: false
hidden: true
metadata:
  title: Modify the Recurring Payments for a VISA/MASTER Card
  description: >-
    Learn how to modify existing recurring payment details for a card using
    PayU's API. This documentation provides detailed instructions for updating
    recurring payment information, ensuring compliance with RBI guidelines and
    enabling seamless management of subscription payments.
  keywords:
    - PayU Modify Recurring Payments API
    - Update Recurring Payment for Cards
    - PayU recurring billing updation
    - Update PayU subscription payments for cards
    - Update PayU subscription payments for UPI
    - Modify recurring transactions for Cards
    - _payment modify card recurring
  robots: index
next:
  pages:
    - slug: using-api-integration-recurring-payments
      title: Using API Integration
      type: basic
    - slug: cancel-the-recurring-payment-for-cards
      title: Cancel the Recurring Payment for a Card
      type: endpoint
---
This section describes how to use the **\_payment** API to update an existing recurring payment for a card in case the card belongs to VISA or Mastercard

<Callout icon="📘" theme="info">
  ###

  **Note**: As per RBI guidelines while modifying the recurring payment, taking consent from the customer and doing an additional factor of authentication is mandatory. You must ensure this is done before using this API. You need to pass **authPayuId** and **action** fields to modify the billing details as part of JSON using this API as described in this section.
</Callout>

### Environment

<PaymentAPIEnvironment />

HTTP Method: **POST**

## Request parameters

The following table describes the parameters for modifying the recurring payment details for a card.

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
        key
        `mandatory`
      </td>

      <td>
        `varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        txnid
        `mandatory`
      </td>

      <td>
        `varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction.
        `Character limit`: 25

        **Note**: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.'
      </td>

      <td>
        fd3e847h2
      </td>
    </tr>

    <tr>
      <td>
        amount
        `mandatory`
      </td>

      <td>
        `float` This parameter should contain the payment amount of the particular transaction.

        **Note**: Type-cast the amount to float type
        Depending upon the merchant use case, this value will vary.

        - It can be either 0 INR (for Net Banking) or min 1 INR (for Cards & UPI) in penny transaction use case.

        - In the case of first instalment use cases, this amount can be equal to initiate setup amount, but this use case will be supported only against selected Net Banking (ICICI and HDFC), all Credit / Debit Cards, and UPI
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        productinfo
        `mandatory`
      </td>

      <td>
        `varchar` This parameter should contain a brief product description. It should be a string describing the product.
        `Character limit`: 100
      </td>

      <td>
        Time Magazine Subscription
      </td>
    </tr>

    <tr>
      <td>
        firstname
        `mandatory`
      </td>

      <td>
        `varchar` Must contain the first name of the customer.
        `Character limit`: 60
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        email
        mandatory
      </td>

      <td>
        `varchar` Must contain the email of the customer.
        This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.
        Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.
        Character limit: 50
      </td>

      <td>
        [Ashish@test.com](mailto:Ashish@test.com)
      </td>
    </tr>

    <tr>
      <td>
        phone
        `mandatory`
      </td>

      <td>
        `varchar` Must contain the phone number of the customer.

        This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is required to provide the correct information .Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.<br />Character limit: 50
      </td>

      <td>
        9843176540
      </td>
    </tr>

    <tr>
      <td>
        api\_version
        `mandatory`
      </td>

      <td>
        This parameter must always needs to be passed as 7.
      </td>

      <td>
        7
      </td>
    </tr>

    <tr>
      <td>
        si
        `mandatory`
      </td>

      <td>
        This parameter must be passed with the value as 2 to modify an already existing subscription/consent.
      </td>

      <td>
        3
      </td>
    </tr>

    <tr>
      <td>
        pg
        `mandatory`
      </td>

      <td>
        `String` This parameter defines the payment category that the merchant wants the customer to see by default on the PayU's payment page. In this example, "CC" must be specified. For more information, refer to Payment Mode Codes.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        bankcode
        `mandatory`
      </td>

      <td>
        Each payment option is identified with a String unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For more information, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards)
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        user\_credentials
        `mandatory`
      </td>

      <td>
        `String` This parameter must contain the user credentials.
      </td>

      <td>
        a:b
      </td>
    </tr>

    <tr>
      <td>
        store\_card\_token
        **mandatory**
      </td>

      <td>
        `String` This must include the Network token generated at your end.
      </td>

      <td>
        1234 4567 2456 3566
      </td>
    </tr>

    <tr>
      <td>
        free\_trial
        `optional`
      </td>

      <td>
        This is mandatory only if the merchant wants to support free trial use case with card and net banking together that too on PayU Hosted Checkout integration.

        In this case, PayU adjusts the transaction amount as INR 2.00 for cards. INR 0.00 for Net Banking and UPI registration irrespective of what amount is passed against the amount field in the request.
        This parameter has no significance in the case of seamless flow.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        si\_details
        `mandatory`
      </td>

      <td>
        This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.

        **Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer – [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0) )

        This is a JSON object and it includes a set of parameters are described in the the si\_details Parameter Description table.
      </td>

      <td>
        Refer the example below the si\_details Parameter Description table.
      </td>
    </tr>

    <tr>
      <td>
        hash
        `mandatory`
      </td>

      <td>
        Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions.

        It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si\_details by merchant salt.

        In the case of registration transaction, the formula is used to calculate this hash is similar to the following:
        HASH = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si\_details|SALT)
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

### For network tokens

This is applicable for the following scenarios:

- Merchant has the card token, TAVV(Cryptogram), and the last four digits of the card
- The token could be created by the merchant or through another partner

<Callout icon="📘" theme="info">
  ### Note:

  This scenario is applicable if you are PCI compliant and got the network token and TAVV from any other aggregator or schemes and then sent the card transaction request in the form of authentication.
</Callout>

{/* Properly formatted JSX Table */}

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
        **Value**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        store\_card\_token
        `mandatory`
      </td>

      <td>
        `String` This must include the Network token generated at your end.
      </td>

      <td>
        1234 4567 2456 3566
      </td>
    </tr>

    <tr>
      <td>
        storecard\_token\_type
        `mandatory`
      </td>

      <td>
        `integer` This parameter is used to specify the store card token type. For this scenario, you must include **1**.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        additional\_info
        `mandatory`
      </td>

      <td>
        `String` This parameter will contain the additional information in the following JSON format:
        `{"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}`
      </td>

      <td>
        `{"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}`
      </td>
    </tr>
  </tbody>
</Table>

<Callout icon="📘" theme="info">
  ### Notes for **additional\_info** parameter:

  The JSON format contains the following fields:

  - **trid** (Token Requestor ID) is the identity given by the networks for creating the tokens. You should be able to get the same from your token provider.
  - **tokenRefNo** (Token Reference Number) is generated along with the network token. . You should be able to get the same from your token provider.
  - **TAVV** is a token authentication verification value given by schemes or interchange. Also, known as cryptogram.

  Additional notes:

  - The last 4 digits of cards is mandatory for all transactions.
  - Some payment gateways require the Token Requester ID (trid) and Token Reference Number (tokenRefNo) to be passed for processing the transaction. Not passing these values will restrict the number of payment gateways available for processing the transaction.
  - Token Requester ID (trid) and Token Reference Number (tokenRefNo) are mandatory for Diners token transactions.
</Callout>

#### si\_details Parameter – JSON Details

The description for the **si\_details** parameter (JSON format):

<Callout icon="📘" theme="info">
  ### **Note**:

  If the request was to modify a subscription,  **si\_consent\_action** parameter needs to be validated in the response. The field must return values modify based on the action sent in billing details JSON. Also, the payment source returned in such cases will be payu.
</Callout>

{/* Properly formatted JSX Table */}

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **JSON Field**
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
        billingCycle
        `mandatory`
      </td>

      <td>
        Billing Cycle defines whether the customer needs to be charged over Daily, Weekly basis, Monthly or Yearly basis or one time.
      </td>

      <td>
        ONCE
      </td>
    </tr>

    <tr>
      <td>
        billingInterval
        `mandatory`
      </td>

      <td>
        Billing Interval is closely coupled with the **billingCycle** field and denotes at what frequency, the subscription plan needs to be executed. For monthly subscriptions, parameter values need to be sent in the request are:

        - billingCycle = MONTHLY
        - billingInterval = 1

        Similarly, by keeping the following values, customer will be charged once in every 3 days:

        - billingCycle = DAILY
        - billingInterval = 3
      </td>

      <td>
        - billingCycle = MONTHLY
        - billingInterval = 1
      </td>
    </tr>

    <tr>
      <td>
        billingAmount
        `mandatory`
      </td>

      <td>
        The billing amount is passed in XX. XX format.
        In use cases where **billingCycle = ADHOC**, amount passed is treated as maximum amount since billing amount and billing cycle varies as per the usage of the subscription service.  In this case, the merchant is free to charge any amount for customer up to the amount specified in the defined subscription call.  For UPI, **billingAmount** should not be more than INR 15000 as it is the maximum limit allowed for UPI currently.
      </td>

      <td>
        INR 2000
      </td>
    </tr>

    <tr>
      <td>
        billingCurrency
        `mandatory`
      </td>

      <td>
        This field must be passed as "INR" .
      </td>

      <td>
        INR
      </td>
    </tr>

    <tr>
      <td>
        paymentStartDate
        `mandatory`
      </td>

      <td>
        The start date of the billing plan is specified in this field with the YYYY-MM-DD format.

        **Note**: All the subsequent recurring transactions will be processed from this date onwards as per **billingCycle** and **billingInterval** fields combination. This date acts as reference point for recurring payments. **Note**: In case of UPI, send the current date here and any other value will be ignored.
      </td>

      <td>
        2022-02-14
      </td>
    </tr>

    <tr>
      <td>
        paymentEndDate
        `mandatory`
      </td>

      <td>
        The end date of the billing plan is specified in this field with the YYYY-MM-DD format.

        **Note**: Pass the correct end date to PayU. Depending upon start date and end date, number of payment iterations are internally calculated and same information is passed to acquirers or banks.
      </td>

      <td>
        2023-01-14
      </td>
    </tr>

    <tr>
      <td>
        siTokenRequestor
        `mandatory for saved cards`
      </td>

      <td>
        This is optional and is only needed before 30th September, 2022 to activate new mandate setups in a controlled manner than activating it completely on all users. This involves creating token at the time of subscription set. You can include any of the following values::

        - **1** : PayU will tokenise the card and share it in same subscription setup call with issuers for subscription setup.
        - **2**: PayU will do the authorization on plain card. Later, the same response will be shared to merchant.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        remarks
        `optional`
      </td>

      <td>
        This field is used to provide remarks on PSP applications during the registration transaction of UPI.  For cards and Net Banking, this parameter has no significance.  Character limit = 50.

        **Note**: This field is applicable only for UPI.
      </td>

      <td>
        Subscription for a year
      </td>
    </tr>

    <tr>
      <td>
        billingLimit
        `optional`
      </td>

      <td>
        For UPI, this field is used to decide the period corresponding which the debit from the mandate recurring date can happen and this mandate registration date is confirmed during registration transaction of UPI.

        **Note**: This field is applicable only for UPI.
        The possible values are:

        - **ON** = Use this parameter to deduct on a specific date
        - **BEFORE** = Use this parameter to deduct before and on a specific date
        - **AFTER** = Use this parameter to After and on the specific date

        **Note**: If no value is passed, 'AFTER' is considered by default.
      </td>

      <td>
        ON = 2022-02-20
      </td>
    </tr>

    <tr>
      <td>
        billingRule
        `optional`
      </td>

      <td>
        For UPI, this field is used to decide the limitation on the amount of recurring debit against the mandate amount which is set during registration transaction of UPI.

        **Note**: This field is applicable only for UPI.
        The possible values are:

        - **MAX** = This is the maximum amount that a merchant can debit, that is, merchant can debit lesser or equal to this amount for a recurring transaction.
        - **EXACT**= This the exact amount that a merchant can debit in recurring debits.

        Note: If no value is passed, 'MAX' is considered by default.
      </td>

      <td>
        MAX = 5000
      </td>
    </tr>

    <tr>
      <td>
        billingDate
        `optional`
      </td>

      <td>
        **Applicable for UPI only**: This field is used to decide the date/day, basis which the recurring debit should happen. This can be ignored and the debit will happen as per the start date in every cycle.
      </td>

      <td>
        FORTNIGHTLY = 7
      </td>
    </tr>

    <tr>
      <td>
        authpayuid

        `mandatory for modifying subscription with cards`
      </td>

      <td>
        This field is used only to modify an existing subscription/consent. Modification means modifying billing details like startDate, endDate, billing cycle, billing interval, billing amount.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        action
        `mandatory for cards`
      </td>

      <td>
        This field is used to modify or cancel an existing subscription. Include **modify** to modify a subscription.
      </td>

      <td>
        modify
      </td>
    </tr>
  </tbody>
</Table>

### **si\_details JSON example**

For a yearly plan starting from 1st January 2019, having a monthly billing amount of INR 100, the plan details:

```plaintext
{
  "billingAmount": "10.00",
  "billingCurrency": "INR",
  "billingCycle": "MONTHLY",
  "billingInterval": 1,
  "paymentStartDate": "2022-02-04",
  "paymentEndDate": "2022-12-12",
  "action": "modify",
  "authPayuId": "123"
}
```

## Sample request

```curl
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP**g&txnid=56bb2e3fcb510f1c1521&amount=10000&firstname=Payu-Admin&email=test@example.com&phone=1234567890&productinfo=iPhone&api_version=7&si=3&pg=CC&bankcode=UTIBENCC&surl=https://test.payu.in/admin/test_response&furl=https://test.payu.in/admin/test_response&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=Test User&si_details={"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2022-09-01","paymentEndDate": "2022-12-01","authpayuid" : "403993715525316543","action":"modify"}&hash=e36568b2dfc460eab0eb3387fb7d90543ed861154f273b9593d6fcc152ed93a91e529c2f4be0965eeb57104e82d58889fa5efb52811ec78cbd1ad646e39c29a0"
```

## Sample response

```json
Array
(
    [mihpayid] => 25603951365
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => BmTY3G
    [txnid] => 5527fc7d02f2bfc00eb4
    [amount] => 1.00
    [cardCategory] => signature_premium
    [discount] => 0.00
    [net_amount_debit] => 1
    [addedon] => 2025-10-14 15:44:41
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
    [hash] => 13f0cc034ec407db13a666f5ef4598798efab154791464537008c9e02e05a232b6fa3bd575b016e7631246dfb8d4911613150d677106c2fd14494da9b7a21122
    [field1] => CBC10141015051509EGR573
    [field2] => 185869
    [field3] =>
    [field4] =>
    [field5] =>
    [field6] => 05
    [field7] => AUTHPOSITIVE
    [field8] => 0 | Transaction Completed
    [field9] => Transaction Completed
    [payment_source] => payu
    [meCode] => {"wibmo_merchant_id":"16329672","hash_key":"b5b013c18d762b6ccbe8d2e8b1e9ec02fe642013524ed02b91846978f8eafa70","acquirer_merchant_id":"175645866049780","mcc":"5499"}
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 528710004895
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [cardnum] => XXXXXXXXXXXX4879
)

```

<br />
