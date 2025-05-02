---
title: Cards
excerpt: ''
api:
  file: merchant-hosted-13.json
  operationId: MerchantHostedCheckout-Cards
deprecated: false
hidden: false
metadata:
  title: Collect Payments using Cards using Merchant Hosted Checkout
  description: >-
    Access the PayU API Reference for collecting card payments with Merchant
    Hosted Checkout. Find detailed documentation on integrating debit or card
    payments and secure authentication. Utilize the interactive simulator to
    test API calls, ensuring smooth and efficient payment processing. Perfect
    for developers aiming to integrate robust card payment solutions into their
    custom checkout systems.
  keywords:
    - Cards Merchant Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - Cards Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for Cards Merchant Hosted Checkout
    - _payment API for Cards Merchant Hosted Checkout
    - _payment API simulation for Cards Custom Checkout
    - _payment API simulation for Cards Merchant Hosted Checkout
    - ' Credit Cards Merchant Hosted Checkout Collect Payment API'
    - Simulator for PayU payment collection
    - Credit Cards Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for Credit Cards Merchant Hosted Checkout
    - _payment API for Credit Cards Merchant Hosted Checkout
    - _payment API simulation for Credit Cards Custom Checkout
    - _payment API simulation for Credit Cards Merchant Hosted Checkout
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: collect-payments-with-cards-seamless
      title: Cards Integration
    - type: endpoint
      slug: process-transaction-with-a-saved-card
      title: Process Transaction with a Saved Card
---
You can collect payments from customers with leading cards using the Merchant Hosted integration. You need to ensure that **CC** or **DC** for the **<Glossary>pg</Glossary>** parameter and  card code based on the desired card provider for the **<Glossary>bankcode</Glossary>** parameter is posted.

> 📘 Note:
>
> PayU accepts domestic and international transactions, but international transactions need to be enabled by writing to PayU Integration Team ([integration@pay.in](mailto:integration@pay.in)).

|                            |                                                                         |
| :------------------------- | :---------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |


##Sample response

### Response for a normal transaction

&#x20; \`\`\`
&#x20; mihpayid=403993715531077182\&mode=CC\&status=success\&unmappedstatus=captured\&key=JPM7Fg\&txnid=ypl938459435dfdfdf\&amount=1000.00\&cardCategory=domestic\&discount=0.00\&net\_amount\_debit=1000\&addedon=2024-02-27+15%3A11%3A37\&productinfo=iPhone\&firstname=Ashish+User\&lastname=\&address1=\&address2=\&city=\&state=\&country=\&zipcode=\&email=ashish%40gmail.com\&phone=9876543210\&udf1=\&udf2=\&udf3=\&udf4=\&udf5=\&udf6=\&udf7=\&udf8=\&udf9=\&udf10=\&hash=afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa\&field1=\&field2=\&field3=\&field4=\&field5=\&field6=\&field7=\&field8=\&field9=Transaction+Completed+Successfully\&payment\_source=payu\&PG\_TYPE=CC-PG\&bank\_ref\_num=7f0d5ada-59bb-41d7-9e41-20a6af2406c9\&bankcode=CC\&error=E000\&error\_Message=No+Error\&name\_on\_card=test\&cardnum=411111XXXXXX1111\&cardhash=This+field+is+no+longer+supported+in+postback+params.
&#x20; \`\`\`

&#x20; \### Parsed response for a normal transaction

&#x20; \`\`\`
&#x20;   \{
&#x20;   "mihpayid": "403993715531077182",
&#x20;   "mode": "CC",
&#x20;   "status": "success",
&#x20;   "unmappedstatus": "captured",
&#x20;   "key": "JPM7Fg",
&#x20;   "txnid": "ypl938459435dfdfdf",
&#x20;   "amount": "1000.00",
&#x20;   "cardCategory": "domestic",
&#x20;   "discount": "0.00",
&#x20;   "net\_amount\_debit": "1000",
&#x20;   "addedon": "2024-02-27 15:00:42",
&#x20;   "productinfo": "iPhone",
&#x20;   "firstname": "Ashish",
&#x20;   "lastname": "",
&#x20;   "address1": "",
&#x20;   "address2": "",
&#x20;   "city": "",
&#x20;   "state": "",
&#x20;   "country": "",
&#x20;   "zipcode": "",
&#x20;   "email": "ashish\@gmail.com",
&#x20;   "phone": "9876543210",
&#x20;   "udf1": "",
&#x20;   "udf2": "",
&#x20;   "udf3": "",
&#x20;   "udf4": "",
&#x20;   "udf5": "",
&#x20;   "udf6": "",
&#x20;   "udf7": "",
&#x20;   "udf8": "",
&#x20;   "udf9": "",
&#x20;   "udf10": "",
&#x20;   "hash": "84bbbf0fa3ba2a39942f6c3deab234c4d00bc5b6aceee5cda3c8200d6e1714e19c224d47e24d0c4a9a0cce40eddbae1dc46455c69e5e7d5dd62f6636bfab337c",
&#x20;   "field1": "896193988312194700",
&#x20;   "field2": "857712",
&#x20;   "field3": "1000.00",
&#x20;   "field4": "",
&#x20;   "field5": "00",
&#x20;   "field6": "02",
&#x20;   "field7": "AUTHPOSITIVE",
&#x20;   "field8": "AUTHORIZED",
&#x20;   "field9": "Transaction is Successful",
&#x20;   "payment\_source": "payu",
&#x20;   "PG\_TYPE": "CC-PG",
&#x20;   "bank\_ref\_num": "896193988312194700",
&#x20;   "bankcode": "CC",
&#x20;   "error": "E000",
&#x20;   "error\_Message": "No Error",
&#x20;   "cardnum": "XXXXXXXXXXXX2346",
&#x20;   "cardhash": "This field is no longer supported in postback params.",
&#x20;   "splitInfo": "\{\\"splitStatus\\":\\"splitNotReceived\\",\\"splitSegments\\":\[]}"
&#x20; }
&#x20; \`\`\`

&#x20; \## Save card transaction

&#x20; \### Response for a save card transaction

&#x20; \`\`\`
&#x20; mihpayid=403993715532392220\&mode=CC\&status=success\&key=gtKFFx\&txnid=05539c1e8d56c0bf4f2e\&amount=10.00\&addedon=2024-09-26+16%3A39%3A03\&productinfo=Product+Info\&firstname=CARDHOLDERXXXXXXXXNAME-Admin\&lastname=\&address1=\&address2=\&city=\&state=\&country=\&zipcode=\&email=test%40example.com&"phone":"##########"\&udf1=\&udf2=\&udf3=\&udf4=\&udf5=\&udf6=\&udf7=\&udf8=\&udf9=\&udf10=\&card\_token=96f5e43b7fa3c78b93656\&card\_no=XXXXXXXXXXXX0008\&field0=\&field1=6MAESTROMAESTRO0\&field2=696292\&field3=10.00\&field4=\&field5=00\&field6=02\&field7=AUTHPOSITIVE\&field8=AUTHORIZED\&field9=Transaction+is+Successful\&payment\_source=sist\&PG\_TYPE=CC-PG\&error=E000\&error\_Message=No+Error\&issuing\_bank=YES\&card\_type=MAST\&cardToken=\&net\_amount\_debit=10\&discount=0.00\&offer\_key=\&offer\_availed=\&unmappedstatus=captured\&hash=14b08bf22072fde0a6a59cac5826d386e107dd8dce058d1a457b102e624aa729b0119d8b7920354ee0d6e6541af2851f7b88e9332eda8fd79c556a5ea6babe4c\&bank\_ref\_no=6MAESTROMAESTRO0\&bank\_ref\_num=6MAESTROMAESTRO0\&bankcode=CC\&surl=https%3A%2F%2Ftest.payu.in%2Fadmin%2Ftest\_response\&curl=https%3A%2F%2Ftest.payu.in%2Fadmin%2Ftest\_response\&furl=https%3A%2F%2Ftest.payu.in%2Fadmin%2Ftest\_response\&card\_hash=46261359f70225c5ed11ef395058f3b2f7d003280bb4feb2f21e41aac113a252\&pa\_name=CARDHOLDERXXXXXXXXNAME
&#x20; \`\`\`

&#x20; \### Parsed response for a save card transaction

&#x20; \`\`\`
&#x20; \[mihpayid] => 403993715532392220
&#x20;     \[mode] => CC
&#x20;     \[status] => success
&#x20;     \[unmappedstatus] => captured
&#x20;     \[key] => gtKFFx
&#x20;     \[txnid] => 05539c1e8d56c0bf4f2e
&#x20;     \[amount] => 10.00
&#x20;     \[cardCategory] => domestic
&#x20;     \[discount] => 0.00
&#x20;     \[net\_amount\_debit] => 10
&#x20;     \[addedon] => 2024-09-26 16:39:03
&#x20;     \[productinfo] => Product Info
&#x20;     \[firstname] => Payu-Admin
&#x20;     \[lastname] =>&#x20;
&#x20;     \[address1] =>&#x20;
&#x20;     \[address2] =>&#x20;
&#x20;     \[city] =>&#x20;
&#x20;     \[state] =>&#x20;
&#x20;     \[country] =>&#x20;
&#x20;     \[zipcode] =>&#x20;
&#x20;     \[email] => test\@example.com
&#x20;     \[phone] => 1234567890
&#x20;     \[udf1] =>&#x20;
&#x20;     \[udf2] =>&#x20;
&#x20;     \[udf3] =>&#x20;
&#x20;     \[udf4] =>&#x20;
&#x20;     \[udf5] =>&#x20;
&#x20;     \[udf6] =>&#x20;
&#x20;     \[udf7] =>&#x20;
&#x20;     \[udf8] =>&#x20;
&#x20;     \[udf9] =>&#x20;
&#x20;     \[udf10] =>&#x20;
&#x20;     \[hash] => 14b08bf22072fde0a6a59cac5826d386e107dd8dce058d1a457b102e624aa729b0119d8b7920354ee0d6e6541af2851f7b88e9332eda8fd79c556a5ea6babe4c
&#x20;     \[field1] => 639639309044936000
&#x20;     \[field2] => 696292
&#x20;     \[field3] => 10.00
&#x20;     \[field4] =>&#x20;
&#x20;     \[field5] => 00
&#x20;     \[field6] => 02
&#x20;     \[field7] => AUTHPOSITIVE
&#x20;     \[field8] => AUTHORIZED
&#x20;     \[field9] => Transaction is Successful
&#x20;     \[payment\_source] => sist
&#x20;     \[pa\_name] => PayU
&#x20;     \[PG\_TYPE] => CC-PG
&#x20;     \[bank\_ref\_num] => 639639309044936000
&#x20;     \[bankcode] => CC
&#x20;     \[error] => E000
&#x20;     \[error\_Message] => No Error
&#x20;     \[cardToken] => 96f5e43b7fa3c78b93656
&#x20;     \[cardnum] => XXXXXXXXXXXX0008
&#x20;     \[cardhash] => This field is no longer supported in postback params.
&#x20;     \[issuing\_bank] => YES
&#x20;     \[card\_type] => MAST
&#x20; \`\`\`

&#x20; \<br />
\</details>

\<details>
&#x20; \<summary>Response parameters\</summary>

&#x20; \<Table>
&#x20;   \<thead>
&#x20;     \<tr>
&#x20;       \<th>
&#x20;         \*\*Parameter\*\*
&#x20;       \</th>

&#x20;       \<th>
&#x20;         \*\*Description\*\*
&#x20;       \</th>
&#x20;     \</tr>
&#x20;   \</thead>

&#x20;   \<tbody>
&#x20;     \<tr>
&#x20;       \<td>
&#x20;         mihpayid
&#x20;       \</td>

&#x20;       \<td>
&#x20;         It is a unique reference number created for each transaction at PayU’s end which is used to identify a transaction in case of a refund.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         mode
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:  
&#x20;         \&#x9;•	Credit Card – CC 
&#x20;         \&#x9;•	Debit Card – DC 
&#x20;         \&#x9;•	Net Banking – NB
&#x20;         \&#x9;•	Cash Card – CASH
&#x20;         \&#x9;•	EMI – EMI 
&#x20;         \&#x9;•	Cardless EMI – CLEMI
&#x20;         \&#x9;•	Buy Now Pay Later - BNPL
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         bankcode
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         status
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter returns the status of the transaction and must be used to map the order status. Possible values are success, failure, or pending. The significance of the values for these values are:  
&#x20;         \&#x9;•	\*\*Success\*\*: If the value of status parameter is ’success’, the transaction is successful. 
&#x20;         \&#x9;•	\*\*Failed\*\*: If the value of status parameter is ‘failure’ or ‘pending’, must only be treated as a failed transaction.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         unmappedstatus
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to  \[Payment State Explanations]\(ref:payment-state-explanations).
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         key
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the merchant key.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         error
&#x20;       \</td>

&#x20;       \<td>
&#x20;         For the failed transactions, this parameter provides the reason for failure.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         error\\\_message
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the error message. For the list of error message, refer to \[Error Codes]\(ref:error-codes).
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         bank\\\_ref\\\_num
&#x20;       \</td>

&#x20;       \<td>
&#x20;         For each successful transaction – this parameter contains the bank reference number generated by the bank.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         txnid
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the transaction ID value posted by the merchant during the transaction request.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         amount
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the original amount which was sent in the transaction request by the merchant.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         cardCategory
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the card category to indicate whether it is domestic or international.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         discount
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the discount amount by the merchant.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         net\\\_amount\\\_debit
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the net amount debited.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         addedon
&#x20;       \</td>

&#x20;       \<td>
&#x20;         The transaction date and time of the transaction.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         productinfo
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of product information which was sent in the transaction request from the merchant’s end to PayU.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         firstname
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of first name which was sent in the transaction request from the merchant’s end to PayU.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         lastname
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of last name which was sent in the transaction request from the merchant’s end to PayU.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         email
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of email which was sent in the transaction request from the merchant’s end to PayU.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         phone
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of phone which was sent in the transaction request from the merchant’s end to PayU.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         hash
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to \[Generate Hash]\(doc:generate-hash-merchant-hosted).
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         PG\\\_TYPE
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter gives information on the payment gateway used for the transaction.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         udf1
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         udf2
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         udf3
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5 which was sent in the transaction request from the merchant’s end to PayU.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         udf4
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         udf5
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         udf6
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         udf7
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.\\\*\\\*\\\*\\\*
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         udf8
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         udf9
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         success\\\_at
&#x20;       \</td>

&#x20;       \<td>
&#x20;         This parameter contains the date and timestamp when the transaction was successful.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         cardnum
&#x20;       \</td>

&#x20;       \<td>
&#x20;         The parameter contains the card number masked and only last 4 digits are returned.
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td>
&#x20;         issuing\\\_bank
&#x20;       \</td>

&#x20;       \<td>
&#x20;         The parameters contains the card issuing bank.
&#x20;       \</td>
&#x20;     \</tr>
&#x20;   \</tbody>
&#x20; \</Table>



## Request parameters


> 🚧 Values to be used in Test environment
>
> For values to be used in Test environment, refer to <a href="test-cards-upi-id-and-wallets#web-checkout" target="_blank">Test Cards</a>.

<TransactionStages />

> 📘 Reference
>
> * For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
> * Card number formats of various card types: [Card Number Formats](doc:card-number-formats).