---
title: Payment Consent Transaction using PayU Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Payment Consent Transaction using PayU Hosted Checkout
  description: >-
    Learn how to set up a Payment Consent or Registration transaction using PayU
    Hosted Checkout. This API documentation provides detailed instructions for
    integrating PayU's payment consent feature, enabling seamless recurring and
    subscription payments.
  keywords:
    - PayU Payment Consent API
    - ' PayU Hosted Checkout Subscription Registration Transaction'
    - ' Payment Consent Transaction for PayU Hosted Checkout'
    - ' PayU recurring payments registration transaction'
    - ' PayU hosted checkout subscription payments registration'
    - ' PayU hosted checkout subscription transaction consent'
    - ' Prebuilt Autopay integration'
    - ' Autopay for UPI non-PACB flow'
    - ' Pre-built Autopay Consent Transaction'
    - ' PayU Hosted Autopay'
    - ' Autopay for PayU Hosted non-PACB flow'
    - ' PayU Hosted Autopay Consent Transaction'
  robots: index
next:
  description: ''
  pages:
    - slug: customer-experience-and-workflow-recurring-payments
      title: Customer Experience and Workflow
      type: basic
    - slug: introduction-recurring-payments-integration
      title: Introduction
      type: basic
---
This section describes how to set up a Payment Consent or Registration transaction using PayU Hosted Checkout integration with **_payment** API.

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Subscriptions** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

  <HTMLBlock>{`
                      <style>
                      .tooltip-btn {
                          position: relative;
                          background-color: #4CAF50;
                          color: white;
                          padding: 10px 20px;
                          border: none;
                          border-radius: 5px;
                          cursor: pointer;
                          font-weight: bold; /* Added this line */
                      }
                      .tooltip-btn:hover::after {
                          content: attr(data-tooltip);
                          position: absolute;
                          bottom: 125%;
                          left: 50%;
                          transform: translateX(-50%);
                          background-color: #333;
                          color: white;
                          padding: 5px 10px;
                          border-radius: 4px;
                          white-space: nowrap;
                          font-size: 12px;
                          z-index: 1;
                      }
                      </style>

                      <button onclick="window.open('https://payu.in/integrationlab/subscription', '_blank')" 
                              class="tooltip-btn" 
                              data-tooltip="Automatically generate code including hashing for your eCommerce website to integrate Subscriptions - PayU Hosted Checkout with zero coding knowledge.">
                          Experience the flow and get the code
                      </button>
  `}</HTMLBlock>
</Callout>

HTTP Method: **POST**

**Environment**

|                            |                                                                    |
| :------------------------- | :----------------------------------------------------------------- |
| **Production Environment** | [https://secure.payu.in/_payment](https://secure.payu.in/_payment) |
| **Test Environment**       | [https://test.payu.in/_payment](https://test.payu.in/_payment)     |

## Request parameters

In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

<HTMLBlock>{`
<style>
/* Target only the second column in the table */
.markdown-body table td:nth-child(2) {
  word-break: break-word !important;
}

/* Keep the first column from breaking unnecessarily */
.markdown-body table td:nth-child(1) {
  word-break: normal;
  white-space: nowrap;
}
</style>
<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Parameter
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        key <br/>
        <code>mandatory</code>
      </td>

      <td style={{ textAlign: "left" }}>
        <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account.
      </td>

      <td style={{ textAlign: "left" }}>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        txnid <br/>
        <code>mandatory</code>
      </td>

      <td style={{ textAlign: "left" }}>
        <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction. <code>Character limit</code>: 25 <br/><strong>Note</strong>: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.'
      </td>

      <td style={{ textAlign: "left" }}>
        fd3e847h2
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        amount <br/>
        <code>mandatory</code>
      </td>

      <td style={{ textAlign: "left" }}>
        <code>float</code> This parameter should contain the payment amount of the particular transaction.
        <br/><strong>Note</strong>: Type-cast the amount to float type Depending upon the merchant use case, this value will vary. <br/>- It can be either 0 INR (for Net Banking) or min 1 INR (for Cards & UPI) in penny transaction use case. <br/>- In the case of first instalment use cases, this amount can be equal to initiate setup amount, but this use case will be supported only against selected Net Banking (ICICI and HDFC), all Credit / Debit Cards, and UPI
      </td>

      <td style={{ textAlign: "left" }}>
        1000
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        productinfo <br/>
        <code>mandatory</code>
      </td>

      <td style={{ textAlign: "left" }}>
        <code>varchar</code> This parameter should contain a brief product description. It should be a string describing the product. <code>Character limit</code>: 100
      </td>

      <td style={{ textAlign: "left" }}>
        Time Magazine Subscription
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        firstname <br/>
        <code>mandatory</code>
      </td>

      <td style={{ textAlign: "left" }}>
        <code>varchar</code> Must contain the first name of the customer. <code>Character limit</code>: 60
      </td>

      <td style={{ textAlign: "left" }}>
        Ashish
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        email <br/>
        <code>mandatory</code>
      </td>

      <td style={{ textAlign: "left" }}>
        <code>varchar</code> Must contain the email of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information. Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. <code>Character limit</code>: 50
      </td>

      <td style={{ textAlign: "left" }}>
        <a href="mailto:Ashish@test.com">Ashish@test.com</a>
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        phone <br/>
        <code>mandatory</code>
      </td>

      <td style={{ textAlign: "left" }}>
        <code>varchar</code> Must contain the phone number of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. <code>Character limit</code>: 50
      </td>

      <td style={{ textAlign: "left" }}>
        9843176540
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        surl <br/>
        <code>mandatory</code>
      </td>

      <td style={{ textAlign: "left" }}>
        surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        furl <br/>
        <code>mandatory</code>
      </td>

      <td style={{ textAlign: "left" }}>
        furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        api_version <br/>
        <code>mandatory</code>
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter must always needs to be passed as 7.
      </td>

      <td style={{ textAlign: "left" }}>
        7
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        si <br/>
        <code>mandatory</code>
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.
        <br/><strong>Notes</strong>: You can modify or cancel existing recurring payment registration as described in the following sections: <br/>- <a href="https://docs.payu.in/docs/manage-recurring-payment-for-cards">Manage Recurring Payment for Cards</a> <br/>- <href="https://docs.payu.in/docs/api-commands-to-manage-upi-recurring-transaction">Manage UPI Recurring Transaction</a>
      </td>

      <td style={{ textAlign: "left" }}>
        1
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        free_trial <br/>
        <code>optional</code>
      </td>

      <td style={{ textAlign: "left" }}>
        This is mandatory only if the merchant wants to support free trial use cases.
        In this case, PayU adjusts the transaction amount as INR 2.00 for cards and UPI and INR 0.00 for Net Banking irrespective of what amount is passed against the amount field in the request.
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        si_details <br/>
        <code>mandatory</code>
      </td>

      <td style={{ textAlign: "left" }}>
        This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.
        <br/><strong>Note</strong>: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer <a href="https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0">https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0</a> ) This is a JSON object and it includes a set of fields. For more information, refer to <a href="ref:https://docs.payu.in/reference/si-parameter-json-details/">SI Parameter JSON Details</a>
      </td>

      <td style={{ textAlign: "left" }}>
        {"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        hash <br/>
        <code>mandatory</code>
      </td>

      <td style={{ textAlign: "left" }}>
        Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions. It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt. In the case of registration transaction. The formula is used to calculate this hash is similar to the following:<br/>
        <code>HASH = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)</code>
      </td>

      <td style={{ textAlign: "left" }}>
        txnid
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>

## Sample request

```curl
curl --location 'https://secure.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642; PHPSESSID=68ed52caaaf5e' \
--data-urlencode 'key=BmTY3G' \
--data-urlencode 'txnid=my_order_49428' \
--data-urlencode 'amount=1' \
--data-urlencode 'firstname=PayU User' \
--data-urlencode 'email=test@gmail.com' \
--data-urlencode 'phone=9876543210' \
--data-urlencode 'productinfo=my_order_49428' \
--data-urlencode 'pg=cc#bankcode=AIRPENCC' \
--data-urlencode 'si=1' \
--data-urlencode 'surl=https://apiplayground-response.herokuapp.com/' \
--data-urlencode 'furl=https://apiplayground-response.herokuapp.com/' \
--data-urlencode 'si_details={"billingAmount": "1.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2025-10-14","paymentEndDate": "2027-12-01"}' \
--data-urlencode 'hash=67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb'
```

Characters allowed for parameters

For parameters address1, address2, city, state, country, product info, email, and phone following characters are allowed:

* Characters: A to Z, a to z, 0 to 9
* – (Minus)
* _ (Underscore)
* @ ()
* / (Slash)
* (Space)
* . (Dot)

## Sample response

The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded).

### Parsed response

```
Array
(
    [mihpayid] => 25599222315
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => BmTY3G
    [txnid] => 181bfc5ac3d7ed7f79a3
    [amount] => 1.00
    [cardCategory] => signature_premium
    [discount] => 0.00
    [net_amount_debit] => 1
    [addedon] => 2025-10-14 09:33:15
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
    [hash] => 0c70aea98b41c79bace6a959c8ad674915a98fbb457c0d13ce42a5636ebb5db861e3244761257261dcb4fd336653342a18592993e53f67a00b9509b1c37940ab
    [field1] => 7604146351426907605915
    [field2] => 180034
    [field3] => 1.00
    [field4] => 
    [field5] => 00
    [field6] => 05
    [field7] => AUTHPOSITIVE
    [field8] => AUTHORIZED
    [field9] => Transaction is Successful
    [payment_source] => sist
    [meCode] => {"MID":"hdfc_89051842","TKey":"0wMbyodmbgzwIOejqyUOpAkCJdBC01zQGwHS+Pm1rGGxBki5xPR60G948KUmnPR5l7xDpxYOWIOLfE1q0z5ezIA7dG/yVAkp4nZmbddhWyNpdLusIKmiJzXH6ASAMJKZJ0dH3NyQypy9w51PfUKAz80I4y4Udq8zCKB+yiDP3JqkOfz366Y5SjKI/BWNMXCMXOXIvzVNSinDVi4bVW+WtimdJ1BS9WACx8zkYjPjTkuGB6TMYeJGYt0JJ6oSQce4xk4yW3al+fFABVC26S+2wNuHYMMFvhd09AK4nUvFMh9SHjhWWw6T81miW2kqxi0o+rdvCCYEO3Aa3R5kH8kmIw=="}
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 7604146351426907605915
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [cardToken] => 69e986cc8579946a92262
    [card_token] => 69e986cc8579946a92262
    [cardnum] => XXXXXXXXXXXX4879
)
```

<br />
