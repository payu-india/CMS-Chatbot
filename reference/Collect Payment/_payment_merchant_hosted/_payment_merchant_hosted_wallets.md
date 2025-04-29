---
title: Wallets
excerpt: ''
api:
  file: merchant-hosted-16.json
  operationId: MerchantHostedCheckout-Wallets
deprecated: false
hidden: false
metadata:
  title: Collect Payment using Wallets with Merchant Hosted Checkout
  description: >-
    Discover how PayU's Merchant Hosted Wallets streamline online payments for
    merchants and customers. Learn integration steps, API details, and best
    practices for secure, efficient transactions. Enhance your e-commerce
    platform with robust payment solutions.
  keywords:
    - Wallets Merchant Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - Wallets Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for Wallets Merchant Hosted Checkout
    - _payment API for Wallets Merchant Hosted Checkout
    - _payment API simulation for Wallets Custom Checkout
    - _payment API simulation for Wallets Merchant Hosted Checkout
    - ' Digital Wallet Merchant Hosted Checkout Collect Payment API'
    - Digital Wallet Custom Checkout integration with PayU
    - Collect Payment API for Digital Wallet Merchant Hosted Checkout
    - ' Mobile Wallet Merchant Hosted Checkout Collect Payment API'
    - Mobile Wallet Custom Checkout integration with PayU
    - Collect Payment API for Mobile Wallet Merchant Hosted Checkout
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: collect-payments-with-wallets-seamless
      title: Wallets Integration
---
You can collect payments from customers with leading wallets using the Merchant Hosted integration. You need to ensure that **CASH** for the **pg** parameter and wallet code based on the desired wallet for the **bankcode** parameter is posted.

<PaymentAPIEnvironment />

<details>

<summary>Sample request</summary>

```curl
curl -X \
 POST "https://test.payu.in/_payment-H "accept: application/json" -H \
 "Content-Type: application/x-www-form-urlencoded" -d"key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&producinfo=iPhone&firstname=Ashish&email=test@gmail.com&phone=9876543210&pg=cash&bankcode=paytm&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```

</details>

<details>  

<summary>Sample response</summary>

```
Array
(
    [mihpayid] => 403993715527518775
    [mode] => CASH
    [status] => success
    [unmappedstatus] => captured
    [key] => J*****g
    [txnid] => HC13glcAkssIkl
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2022-10-21 17:45:24
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
    [hash] => 007435a716982c7f5eec5cff95701f65eb1bdbff8f852e461224e3b5e17126ad26bb3a3ffdb95cded6a87d3515fe86fc58925cad024595a4a6825adfed2dc436
    [field1] => 
    [field2] => 
    [field3] => 
    [field4] => 
    [field5] => 
    [field6] => 
    [field7] => 
    [field8] => 
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => CASH-PG
    [bank_ref_num] => 540898ed-72e7-40a8-a96e-f17de621cbb4
    [bankcode] => CASH
    [error] => E000
    [error_Message] => No Error
    [splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":[]}
)
```

</details>

<details>
  <summary>Response parameters</summary>

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        mihpayid
      </td>

      <td>
        It is a unique reference number created for each transaction at PayU’s end which is used to identify a transaction in case of a refund.
      </td>
    </tr>

    <tr>
      <td>
        mode
      </td>

      <td>
        This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:  \
        &#x9;•	Credit Card – CC \
        &#x9;•	Debit Card – DC \
        &#x9;•	Net Banking – NB\
        &#x9;•	Cash Card – CASH\
        &#x9;•	EMI – EMI \
        &#x9;•	Cardless EMI – CLEMI\
        &#x9;•	Buy Now Pay Later - BNPL
      </td>
    </tr>

    <tr>
      <td>
        bankcode
      </td>

      <td>
        This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        This parameter returns the status of the transaction and must be used to map the order status. Possible values are success, failure, or pending. The significance of the values for these values are:  \
        &#x9;•	**Success**: If the value of status parameter is ’success’, the transaction is successful. \
        &#x9;•	**Failed**: If the value of status parameter is ‘failure’ or ‘pending’, must only be treated as a failed transaction.
      </td>
    </tr>

    <tr>
      <td>
        unmappedstatus
      </td>

      <td>
        This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to  [Payment State Explanations](ref:payment-state-explanations).
      </td>
    </tr>

    <tr>
      <td>
        key
      </td>

      <td>
        This parameter contains the merchant key.
      </td>
    </tr>

    <tr>
      <td>
        error
      </td>

      <td>
        For the failed transactions, this parameter provides the reason for failure.
      </td>
    </tr>

    <tr>
      <td>
        error\_message
      </td>

      <td>
        This parameter contains the error message. For the list of error message, refer to [Error Codes](ref:error-codes).
      </td>
    </tr>

    <tr>
      <td>
        bank\_ref\_num
      </td>

      <td>
        For each successful transaction – this parameter contains the bank reference number generated by the bank.
      </td>
    </tr>

    <tr>
      <td>
        txnid
      </td>

      <td>
        This parameter contains the transaction ID value posted by the merchant during the transaction request.
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        This parameter contains the original amount which was sent in the transaction request by the merchant.
      </td>
    </tr>

    <tr>
      <td>
        cardCategory
      </td>

      <td>
        This parameter contains the card category to indicate whether it is domestic or international.
      </td>
    </tr>

    <tr>
      <td>
        discount
      </td>

      <td>
        This parameter contains the discount amount by the merchant.
      </td>
    </tr>

    <tr>
      <td>
        net\_amount\_debit
      </td>

      <td>
        This parameter contains the net amount debited.
      </td>
    </tr>

    <tr>
      <td>
        addedon
      </td>

      <td>
        The transaction date and time of the transaction.
      </td>
    </tr>

    <tr>
      <td>
        productinfo
      </td>

      <td>
        This parameter contains the same value of product information which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        firstname
      </td>

      <td>
        This parameter contains the same value of first name which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        lastname
      </td>

      <td>
        This parameter contains the same value of last name which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        email
      </td>

      <td>
        This parameter contains the same value of email which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        phone
      </td>

      <td>
        This parameter contains the same value of phone which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
        This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).
      </td>
    </tr>

    <tr>
      <td>
        PG\_TYPE
      </td>

      <td>
        This parameter gives information on the payment gateway used for the transaction.
      </td>
    </tr>

    <tr>
      <td>
        udf1
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf2
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf3
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5 which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf4
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf5
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf6
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf7
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.\*\*\*\*
      </td>
    </tr>

    <tr>
      <td>
        udf8
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf9
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        success\_at
      </td>

      <td>
        This parameter contains the date and timestamp when the transaction was successful.
      </td>
    </tr>

    <tr>
      <td>
        cardnum
      </td>

      <td>
        The parameter contains the card number masked and only last 4 digits are returned.
      </td>
    </tr>

    <tr>
      <td>
        issuing\_bank
      </td>

      <td>
        The parameters contains the card issuing bank.
      </td>
    </tr>
  </tbody>
</Table>

</details>

## Request parameters

<details>  <summary>Additional info for request parameters</summary>

<Additional_paymentRequestParams />

</details>

> 📘 Reference
>
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

> 🚧 Values to be used in Test environment
>
> Use only **CASH** as the bankcode.

{/*

 

> You can test wallets with the following only:
>
> - **PayTM**: Use bankcode=PAYTM and works only with mobile number 7777777777 or cards listed under <a href="test-cards-upi-id-and-wallets#test-wallets" target="_blank">Test Cards, UPI ID and WalletsI</a>.
> - **Amazon**: You can test using your original Amazon account details.
> - **Airtel**: Use your mobile number. !

*/}

<TransactionStages />
