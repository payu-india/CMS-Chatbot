---
title: Net Banking
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payment using Net Banking with Merchant Checkout API Reference
  description: >-
    Discover the PayU API Reference for integrating NetBanking payments with
    Merchant Hosted Checkout. Access detailed guides on secure authentication
    and transaction processing NetBanking payments or Net Banking.  Ideal for
    developers looking to incorporate efficient NetBanking, internet banking,
    virtual banking or web banking solutions into their custom checkout systems.
  keywords:
    - Net Banking Merchant Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - Net Banking Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for Net Banking Merchant Hosted Checkout
    - _payment API for Net Banking Merchant Hosted Checkout
    - _payment API simulation for Net Banking Custom Checkout
    - _payment API simulation for Net Banking Merchant Hosted Checkout
    - NetBanking Custom Checkout API Reference
    - NetBanking Merchant Hosted Checkout API Reference
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: collect-payments-with-net-banking-seamless
      title: Net Banking Integration
---
Collect payments using Net Banking with Merchant Hosted Checkout integration as described in this section. After collecting the details from the customer, make the transaction request with the payment details to PayU.

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout** > **Net Banking** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

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

                          <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-nb-status', '_blank')" 
                                  class="tooltip-btn" 
                                  data-tooltip="Click here to see the Merchant Hosted Checkout > Net Banking end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                              Experience the flow and get the code
                          </button>
  `}</HTMLBlock>
</Callout>

## Postman Collection

<Postman_collection />

<br />

## Check Net Banking health

You can check whether the Net Banking server is up and running using the **getNetBankingStatus** API. If the Net Banking server is down for a bank, you can inform your customers that the Net Banking server is down. For more information on the **getNetBankingStatus** API, refer to [Get Net Banking Status API](ref:get_net_banking_status_api).

## Recommended integrations for Net Banking

* **Recurring Payments**: Enable recurring payments or subscriptions for wallets. For more information, refer to [Recurring Payments Integration](doc:introduction-recurring-payments-integration).
* **Offers**: Configure offers for cards on Dashboard and then collect payments with offers. For more information, refer to [Create a No-Cost EMI Offer](doc:create-a-no-cost-emi-offer) and [Create a SKU-Based Offer](doc:create-a-sku-based-offer).

<PaymentAPIEnvironment />

## Request parameters

> 📘 Reference:
>
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

<br />

| Parameter                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                        |
| :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| key<br />`mandatory`                            | `String` This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).                                                                                                                                                                                                                                                                                                                                                                                                                        | 8488225                                                                                        |
| txnid<br />`mandatory`                          | `varchar` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant's) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn't been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID'). | fd3e847h2                                                                                      |
| amount<br />`mandatory`                         | `float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 10                                                                                             |
| productinfo<br />`mandatory`                    | `varchar` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice).                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | T-shirt                                                                                        |
| firstname<br />`mandatory`                      | `varchar` This parameter must contain the first name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Ankit                                                                                          |
| email<br />`mandatory`                          | `varchar` This parameter must contain the email of the customer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [test@gmail.com](mailto:test@gmail.com)                                                        |
| phone<br />`mandatory`                          | `integer` Merchant needs to take the customer's GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.                                                                                                                                                                                                                                                                                                                                                                                                                                            | 9876543210                                                                                     |
| pg<br />`mandatory`                             | `string` This parameter contains the payment method to be enabled to collect payment from your customer. For the list of payment methods and their codes, refer to [Payment Mode Codes](doc:payment-mode-codes). For Net Banking, use NB.                                                                                                                                                                                                                                                                                                                                                                                                    | NB                                                                                             |
| bankcode<br />`mandatory`                       | `string` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For the list of bankcodes for Net Banking, refer to [Net Banking Codes](doc:net-banking-codes).                                                                                                                                                                                                                                                                                                                                                             | AXIB                                                                                           |
| surl<br />`mandatory`                           | `string` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                             | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/) |
| furl<br />`mandatory`                           | `string` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                                 | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/) |
| hash<br />`mandatory`                           | `string` The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT) For more information, refer to [Generate Hash](doc:hashing-request-and-response).                                                                                                                                                                                                                                                                                                                         | a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0                                                       |
| lastname<br />`optional`                        | `string` The last name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Sharma                                                                                         |
| address1<br />`optional`                        | `string` The first line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 123 Main Street                                                                                |
| address2<br />`optional`                        | `string` The second line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Apartment 4B                                                                                   |
| city<br />`optional`                            | `string` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Mumbai                                                                                         |
| state<br />`optional`                           | `string` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Maharashtra                                                                                    |
| country<br />`optional`                         | `string` The country where your customer resides.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | India                                                                                          |
| zipcode<br />`optional`                         | `string` Billing address zip code is mandatory for the cardless EMI option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 400001                                                                                         |
| udf1<br />`mandatory for Cross-Border Payments` | `string` This parameter has been made for you to keep any information corresponding to the transaction. **Note**: This parameter must contain buyer's PAN number for Cross-Border Payments.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | ABCDE1234F                                                                                     |
| udf2<br />`optional`                            | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 1                                                                              |
| udf3<br />`mandatory for Cross-Border Payments` | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | GSTIN123456                                                                                    |
| udf4<br />`optional`                            | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 2                                                                              |
| udf5<br />`optional`                            | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 3                                                                              |

Perfect! ✨ Now each parameter name is on its own line, followed by the mandatory/optional status on the next line, making the table much more readable and organized.

> 🚧 Values to be used in Test environment
>
> You can test NetBanking only with pg=TESTPG and bankcode=TESTPGNB only.

## Sample request

```curl
curl -X \
 POST "https://test.payu.in/_payment-H "accept: application/json" -H \
 "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&txnid=bvRCCBO4YiGGHE&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=TESTPG&bankcode=TESTPGNB&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64"
```

## Response parameters

> 📘 Reference
>
> For the response parameters description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis#response-parameters).

## Sample response

The following is a sample response URL when the transaction is successful:

Sample Response URL

```plaintext
mihpayid=403993715524046125&mode=NB&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=bvRCCBO4YiGGHE&amount=10.00&discount=0.00&net_amount_debit=10&addedon=2021-09-06+13%3A59%3A39&productinfo=iPhone&firstname=Ashish&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=fa7bb889d25b2a60bcf32316d1c9346589ff3de012dd0c66aa47ec12f1349837163ef8a603bd8b357de610b768f08dc4fb3bb4702d1ca6d9751300667fd763a6&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=NB-PG&bank_ref_num=ae67e632-f4eb-4121-b47b-2d35dce5ec2e&bankcode=TESTPGNB&error=E000&error_Message=No+Error
```

The following is the parsed sample response body (of the above response):

Parsed Sample Response Body

```plaintext
Array
(
    [mihpayid] => 403993715524046125
    [mode] => NB
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => bvRCCBO4YiGGHE
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-06 13:59:39
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
    [hash] => fa7bb889d25b2a60bcf32316d1c9346589ff3de012dd0c66aa47ec12f1349837163ef8a603bd8b357de610b768f08dc4fb3bb4702d1ca6d9751300667fd763a6
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
    [PG_TYPE] => NB-PG
    [bank_ref_num] => ae67e632-f4eb-4121-b47b-2d35dce5ec2e
    [bankcode] => TESTPGNB
    [error] => E000
    [error_Message] => No Error
)
```
