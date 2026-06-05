---
title: '[Internal Review] UPI Consent Transaction - Plans'
deprecated: false
hidden: true
metadata:
  title: UPI Recurring Payment Consent Transaction
  description: >-
    Explore how to set up a UPI Recurring Payment Consent Transaction using
    Merchant Hosted Checkout. This API documentation for integrating PayU's
    Netbanking or Net Banking consent feature, enabling secure and efficient
    recurring payments for your customers.
  keywords:
    - PayU UPI Recurring Payment for Custom Checkout
    - UPI Consent Transaction for Custom Checkout
    - PayU UPI Recurring Payment for Merchant Hosted Checkout
    - UPI Consent Transaction for Merchant Hosted Checkout
    - PayU recurring payments for UPI
    - UPI Autopay
    - Autopay for UPI non-PACB flow
    - UPI Autopay Consent Transaction
  robots: index
next:
  pages:
    - slug: using-api-integration-recurring-payments
      title: Using API Integration
      type: basic
    - slug: customer-experience-and-workflow-recurring-payments
      title: Customer Experience and Workflow
      type: basic
---
> ✅
>
> <FreshTag heading="What's New!" asHeading={false} />
>
> - Introducing <Anchor target="_blank" href="https://docs.payu.in/docs/plans">plans</Anchor> for subscriptions

This section provides the request parameters, sample request and response for a UPI Recurring Payment Consent transaction.

> 📘
>
> **Note**: During integration with PayU, first integrate with the Test Server environment. PayU will provide you the necessary Merchant Key for the test serve. After testing is done, you are ready to move to the Production server.

<br />

> 👍
>
> Experience the end-to-end **Merchant Hosted Checkout** > **UPI** flow and instantly generate the complete code for seamless, zero-coding integration into your website.
>
> <HTMLBlock>{`
>                           <style>
>                           .tooltip-btn {
>                               position: relative;
>                               background-color: #4CAF50;
>                               color: white;
>                               padding: 10px 20px;
>                               border: none;
>                               border-radius: 5px;
>                               cursor: pointer;
>                               font-weight: bold; /* Added this line */
>                           }
>                           .tooltip-btn:hover::after {
>                               content: attr(data-tooltip);
>                               position: absolute;
>                               bottom: 125%;
>                               left: 50%;
>                               transform: translateX(-50%);
>                               background-color: #333;
>                               color: white;
>                               padding: 5px 10px;
>                               border-radius: 4px;
>                               white-space: nowrap;
>                               font-size: 12px;
>                               z-index: 1;
>                           }
>                           </style>
>
>                           <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-mandate', '_blank')" 
>                                   class="tooltip-btn" 
>                                   data-tooltip="Click here to see the Merchant Hosted Checkout >  UPI end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
>                               Experience the flow and get the code
>                           </button>
> `}</HTMLBlock>

HTTP Method: **POST**

<PaymentAPIEnvironment />

## Request parameters

In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

| Parameter                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Value                                                                                                                              |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| key<br />`mandatory`                           | `String` The merchant key is a unique identifier for a merchant account in PayU's database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Your Test Key                                                                                                                      |
| api\_version<br />`optional`                   | `String` The API version for this API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 7                                                                                                                                  |
| txnid<br />`mandatory`                         | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. It is used to track the order and must be unique. PayU's system will not accept duplicate transaction IDs.                                                                                                                                                                                                                                                                                                                                                                                                                                         | s7hhDQVWvbhBdN                                                                                                                     |
| amount<br />`mandatory`                        | `String` This field should contain the payment amount for the transaction.<br />The limit for recurring payments using UPI payment mode:<br />- **Auto-debit** is Rs.15000 (the auto-debit limit is higher for below listed purpose)<br />- **With PIN** is Rs.1,00,000<br />**Note**: The auto-debit limit for the following UPI recurring payments is one lakh rupees (Rs.1,00,000):<br />- Insurance premiums<br />- Credit card bill payments<br />- Insurance premium                                                                                                                                                                                   | 10.00                                                                                                                              |
| productinfo<br />`mandatory`                   | `String` It should be a string containing a brief description of the product. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | iPhone                                                                                                                             |
| firstname<br />`mandatory`                     | `String` The first name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Ashish                                                                                                                             |
| email<br />`mandatory`                         | `String` The email of the customer. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [test@gmail.com](mailto:test@gmail.com)                                                                                            |
| phone<br />`mandatory`                         | `String` The phone number of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 9876543210                                                                                                                         |
| lastname<br />`mandatory`                      | `String` The last name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Verma                                                                                                                              |
| address1<br />`optional`                       | `String` The first line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai                                                                            |
| address2<br />`optional`                       | `String` The second line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 34 Saikripa-Estate, Tilak Nagar                                                                                                    |
| city<br />`optional`                           | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Mumbai                                                                                                                             |
| state<br />`optional`                          | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Maharashtra                                                                                                                        |
| country<br />`optional`                        | `String` The country where your customer resides. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | India                                                                                                                              |
| zipcode<br />`optional`                        | `String` Billing address zip code is mandatory for the cardless EMI option. `Character Limit-20`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 400004                                                                                                                             |
| surl<br />`mandatory`                          | `String` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                                             | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                     |
| furl<br />`mandatory`                          | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                     |
| hash<br />`mandatory`                          | `String` It is used to avoid the possibility of transaction tampering. For more information on hash generation process, refer to [Generate Hash](http://docs.payu.in/docs/hashing-request-and-response).<br />In the case of registration transaction, the formula is used to calculate this hash is similar to the following:<br />`HASH = SHA512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|si_details\|SALT)`                                                                                                                                                                                                 | `eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972` |
| pg<br />`mandatory`                            | `varchar` The **pg** parameter for UPI must be UPI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | UPI                                                                                                                                |
| bankcode<br />`mandatory`                      | `varchar` This parameter contains UPI or INTENT for UPI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | UPI                                                                                                                                |
| si<br />`mandatory`                            | This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.<br />**Notes**: You can modify or cancel existing recurring payment registration as described in the following sections:<br />- [Manage Recurring Payment for Cards](http://docs.payu.in/reference/manage-recurring-payment-for-cards)<br />- [Manage UPI Recurring Transaction](http://docs.payu.in/reference/api-commands-to-manage-upi-recurring-transaction)                                                                                 |                                                                                                                                    |
| si\_details<br />`mandatory`                   | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.<br />**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers (for more details refer – [RBI Notification](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0)).<br />This is a JSON object and it includes a set of fields. For more information, refer to [si\_details Object Parameters](https://docs.payu.in/reference/copy-of-upi-consent-transaction#si_details-object-parameters). |                                                                                                                                    |
| vpa<br />`mandatory for UPI Collect`           | `varchar` This parameter contains the customer's VPA handle. For the list UPI handles supported, refer to [UPI Handles](http://docs.payu.in/docs/upi-handles).<br />The merchant is advised to check the validity of the VPA through using the VPA Validation API. PayU extends support for the same if required. For more information on using VPA Validation API, refer to [Validate VPA Handle API](http://docs.payu.in/reference/validate_vpa_api).                                                                                                                                                                                                      | abc\@upi                                                                                                                           |
| txn\_s2s\_flow<br />`mandatory for UPI Intent` | `integer` This parameter must be passed with the values as 4 for UPI Intent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 4                                                                                                                                  |
| free\_trial<br />`optional`                    | This is mandatory only if the merchant wants to support free trial use cases.<br />In this case, PayU adjusts the transaction amount as INR 2.00 for cards and UPI and INR 0.00 for Net Banking irrespective of what amount is passed against the amount field in the request.                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                    |

> 📘 Notes
>
> The **bankcode** parameter value can be any of the following:
>
> - UPI: Pass this value for UPI transactions.
> - INTENT: Pass this value for Intent.

For more information on bank codes used for recurring payments registration, refer to [Bank Codes - Recurring Payments](doc:bank-codes-recurring-payments)

Characters allowed for parameters

For parameters address1, address2, city, state, country, product info, email, and phone following characters are allowed:

- Characters: A to Z, a to z, 0 to 9
- – (Minus)
- \_ (Underscore)
- @ ()
- / (Slash)
- (Space)
- . (Dot)

### `si_details` Object Parameters

You can pass either standing instructions, or plan details or both in the request. Refer to the [Standing Instructions vs Plan](https://docs.payu.in/reference/copy-of-upi-consent-transaction#standing-instructions-vs-plan) section for more information.

| **Parameters**                 | **Description**                                                                                                                                                                                                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `billingAmount` _mandatory_    | `float` The subscription billing amount.                                                                                                                                                                                                            |
| `billingCurrency` _mandatory_  | `string` The billing currency. Here it is `INR`.                                                                                                                                                                                                    |
| `billingCycle` _mandatory_     | `string` The billing cycle at which the amount should be debited.                                                                                                                                                                                   |
| `billingInterval` _mandatory_  | `integer` The billing interval at which the amount should be debited.                                                                                                                                                                               |
| `paymentStartDate` _mandatory_ | `string` The date on which the subscription payment should start.                                                                                                                                                                                   |
| `paymentEndDate` _mandatory_   | `string` The date on which the subscription payment should end.                                                                                                                                                                                     |
| `planId`_&#x20;optional_       | `string` The unique plan ID obtained after creating from the dashboard. Know more about <Anchor target="_blank" href="https://docs.payu.in/docs/internal-review-create-and-manage-plans#create-a-plan">creating a plan</Anchor> from the dashboard. |
| `qty` _optional_               | `string` The quantity of the billing amount. The **total subscription amount** = `billingAmount` × `qty`.<br /><br />**Note:** The `qty` will not create multiple subscriptions. It only multiplies the billing amount.                             |

## Sample request

The sample code block for UPI Seamless integration (Merchant-Hosted Checkout) is similar to the following code block:

> 📘 Note:
>
> Before you make payment request to PayU, it is recommended to validate the UPI handle provided by your customer is eligible for recurring payment using the validateVPA API to avoid transaction failure. For more information, refer to [Validate VPA API](ref:validate_vpa_api).

### UPI Consent Transaction

```curl
curl --location 'https://secure.payu.in/_payment' \
--header 'accept: application/json' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642; PHPSESSID=68ed52caaaf5e' \
--data-urlencode 'key=BmTY3G' \
--data-urlencode 'txnid=my_order_29327' \
--data-urlencode 'amount=1.00' \
--data-urlencode 'firstname=Payu-Admin' \
--data-urlencode 'email=test@example.com' \
--data-urlencode 'phone=1234567890' \
--data-urlencode 'productinfo=my_order_29327' \
--data-urlencode 'api_version=7' \
--data-urlencode 'si=1' \
--data-urlencode 'pg=UPI' \
--data-urlencode 'bankcode=UPI' \
--data-urlencode 'vpa=anything@payu' \
--data-urlencode 'surl=https://test.payu.in/admin/test_response/' \
--data-urlencode 'furl=https://test.payu.in/admin/test_response' \
--data-urlencode 'si_details={"billingAmount": "1.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2025-10-14","paymentEndDate": "2027-12-01", "planId": "83","qty": "20"}' \
--data-urlencode 'hash=67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb'
```

### UPI Intent

```curl
curl --location 'https://secure.payu.in/_payment' \
--header 'accept: application/json' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642; PHPSESSID=68edd726c95b4' \
--data-urlencode 'key=BmTY3G' \
--data-urlencode 'txnid=my_order_95314' \
--data-urlencode 'amount=1.00' \
--data-urlencode 'firstname=Payu-Admin' \
--data-urlencode 'email=test@example.com' \
--data-urlencode 'phone=1234567890' \
--data-urlencode 'productinfo=my_order_95314' \
--data-urlencode 'api_version=7' \
--data-urlencode 'si=1' \
--data-urlencode 'pg=UPI' \
--data-urlencode 'bankcode=INTENT' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'surl=https://test.payu.in/admin/test_response/' \
--data-urlencode 'furl=https://test.payu.in/admin/test_response' \
--data-urlencode 'si_details={"billingAmount": "1.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2025-10-14","paymentEndDate": "2027-12-01", "planId": "83","qty": "20"}' \
--data-urlencode 'hash=67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb'
```

## Understanding Response

For also UPI registration transaction, you must ensure that the payment response from PayU has the expected values as described in the following table so that the UPI registration is successful or initiated successfully with the customer’s bank or UPI provider.

| **Response Parameter** | **Expected Value**               | **Description**                                                                |
| ---------------------- | -------------------------------- | ------------------------------------------------------------------------------ |
| status                 | success                          | Indicates that the transaction is successful with the UPI provider             |
| payment\_source        | SIST                             | Indicates that UPI details have been marked correctly for Standing Instruction |
| mihpayid               | \<mihpayid number> sent. by PayU | Indicates PayU’s transaction acknowledgment for a Consent transaction          |

The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded).

### Sample response

#### UPI Consent Transaction

- The formatted response for UPI Consent Transaction is similar to the following:

```json
Array
(
    [mihpayid] => 25600438037
    [mode] => UPI
    [status] => success
    [unmappedstatus] => captured
    [key] => smsplus
    [txnid] => 1
    [amount] => 1.00
    [discount] => 0.00
    [net_amount_debit] => 1
    [addedon] => 2025-10-14 11:14:34
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
    [udf4] => Executed Callback
    [udf5] => 
    [udf6] => 
    [udf7] => 
    [udf8] => 
    [udf9] => 
    [udf10] => 
    [hash] => 175508d5e19f64280f34d81b90afc010f9ffcd62a12ea286e72135a93220727654f9d87c778c828adfede3aaf2d1b0b71696906d04a589460ecef0a1172e5804
    [field1] => badshahgv-1@okaxis
    [field2] => ICIe68d1f01f2d34fc99ba3077af44f1e4c
    [field3] => badshahgv-1@okaxis
    [field4] => GAURAV  VERMA
    [field5] => 701874bccb514b108c3609e002478fbd@okaxis
    [field6] => 
    [field7] => 00|APPROVED OR COMPLETED SUCCESSFULLY
    [field8] => 
    [field9] => APPROVED OR COMPLETED SUCCESSFULLY|Completed Using Callback
    [payment_source] => sist
    [meCode] => {"pgMid":"9373547","merchantVpa":"bitspingtest.payu@icici"}
    [PG_TYPE] => UPI-PG
    [bank_ref_num] => 528788687631
    [bankcode] => UPI
    [error] => E000
    [error_Message] => No Error
    [rrn] => 528788687631
)
```

#### UPI Intent

- The formatted response for UPI Intent:

```json
{
  "metaData": {
    "message": "Merchant Integration Exception occurred",
    "referenceId": "d8a5cc66c66004df34788f651f19999a",
    "statusCode": "EX158",
    "txnId": "40d73a7d238e3cd98fef",
    "txnStatus": "failed",
    "unmappedStatus": "failure"
  },
  "result": {}
}
```

## Webhook for Getting Transaction Details

You can expose a webhook by requesting the PayU Integration team to configure the same against the **ws\_online\_response** parameter. If this webhook is configured, you will receive the above response object over HTTP form post method similar to the following:

```plaintext
unmappedstatus=success&phone=9999999999&txnid=FCDA1R100870163781&hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d0b6f3c7935e28194ca92f380be7c84c3695415b106dcf52cb016a15fcf6adc98d724&status=success&curl=https://www.abc.in/payment/handlepayuresposne&firstname=NA&card_no=519619XXXXXX5049&furl=https://www.abc.in/payment/handlepayuresposne&productinfo=2&mode=DC&amount=800.00&field4=6807112311042810&field3=6807112311042810&field2=838264&field9=SUCCESS&email=NA&mihpayid=175477248&surl=https://www.ABC.in/payment/handlepayuresposne&card_hash=9e88cb0573d4a826b61d808c0a870ed4a990682459b0ec9e95ea421e8e47be8c&field1=42812&payment_source=sist
```

If the mandate is not confirmed by the customer or the mandate is confirmed by the customer, but the mandate registration is rejected from the banks, the status is communicated as a “failure” over webhook. For more information, refer to [Set up WebHook to Receive Cancellation or Modification Update from the Issuer Bank.](ref:set-up-webhook-to-receive-cancellation-or-modification-update-from-the-issuer-bank)

## Standing Instructions Vs Plan

The following are the points to consider:

- If plan is enabled for a subscription, only plan details are accepted in requests and the standing instructions (if passed) are ignored.
- The transaction moves to the `bounced` state if a invalid `planId` is passed in the request.
- The plan details are automatically used to fetch billing amount, currency, cycle, and other details.
- The checkout will display plan-based subscription information.

<br />
