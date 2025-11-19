---
title: Create the Split
excerpt: >-
  Before diving into the specifics of using the Marketplace solution, you need
  to understand a few terms used throughout this document and in the API.  1.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Creating a split involves the following:

* The marketplace owners are referred to as the “aggregator merchant”
* The individual providers or sub-sellers of that marketplace are referred to as “child merchants”
* The fee that the parent Merchant can optionally apply per Sub Merchant transaction is called the “aggregatorCharges”.
* The amount that will be settled to given child merchants is referred to as the “amountToBeSettled”.

To perform a basic API setup for adding a payment, adding splits (sub-payment) for payment, and releasing a sub-payment:

<br />

<Cards columns={3}>
  <Card title="1. Implement Split" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-1-implement-split">
    Implement payment splitting functionality to distribute funds among multiple parties

    <br />
  </Card>

  <Card title="2. Get Aggregator/Parent Transaction Info" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-2-get-aggregatorparent-transaction-info">
    Retrieve information about the aggregator or parent transaction for split payments

    <br />
  </Card>

  <Card title="3. Release Settlement API" href="https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers#step-3-release-settlement-api">
    Use the Release Settlement API to manage fund disbursement for split transactions
  </Card>
</Cards>

## Step 1: Implement split

<Tabs>
  <Tab title="Split After Transaction">
    You must specify two decimal places for each split, but ensure the sum split amounts are equal to the transaction amount.

    <Callout icon="📘" theme="info">
      **Note**: You must specify two decimal places for each split, but ensure the sum of the percentage of all splits is equal to 100.
    </Callout>

    HTTP Method: **POST**

    <GENERALAPIsEnvironment />

    <Accordion title="Request parameters" icon="fa-table">
      <HTMLBlock>{`
                                                                      <table style="width: 100%; border-collapse: collapse;">
                                                                      <thead>
                                                                      <tr>
                                                                        <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
                                                                        <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
                                                                        <th style="border: 1px solid #ddd; padding: 8px;"><strong>Sample Value</strong></th>
                                                                      </tr>
                                                                      </thead>
                                                                      <tbody>
                                                                      <tr>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p>key</p>
                                                                      </td>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> This parameter must include the Merchant key that was provided by PayU.</p>
                                                                      </td>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p>vDy3i7</p>
                                                                      </td>
                                                                      </tr>
                                                                      <tr>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p>api_version</p>
                                                                      </td>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Version of the API must be 7 for Split Settlements.</p>
                                                                      </td>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p>7</p>
                                                                      </td>
                                                                      </tr>
                                                                      <tr>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p>command</p>
                                                                      </td>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The parameter must contain the name of the web service.</p>
                                                                      </td>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p>payment_split</p>
                                                                      </td>
                                                                      </tr>
                                                                      <tr>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p>hash</p>
                                                                      </td>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The hash string encryption is specified in this parameter. The format of the hash is:<br>|sha512(key|command|var1|salt)<br>Where, var1 contains the fields as described in the var1 description.</p>
                                                                      </td>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
                                                                      </td>
                                                                      </tr>
                                                                      <tr>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p>var1</p>
                                                                      </td>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string (JSON)</code> This parameter is in a JSON format and fields included in the JSON format are explained the <a href="#json-request-structure">JSON request structure table</a>.</p>
                                                                      </td>
                                                                        <td style="border: 1px solid #ddd; padding: 8px;"><p>For an example, refer the <a href="#request-structure-for-var1-to-be-included-in--payment_split-api">Request Structure</a> subsection.</p>
                                                                      </td>
                                                                      </tr>
                                                                      </tbody>
                                                                      </table>
      `}</HTMLBlock>

      <Accordion title="Request structure for var1 to be included in  payment_split API" icon="fa-code">
        ```plaintext
        {  "type": "absolute",  
            "payuId": "<PayuID of parent transaction which needs to be split>",  
           "splitInfo": 
             {    
                "<Child Merchant 1 key>":{
                 "aggregatorSubTxnId":"<unique transaction ID for this specific sub-transaction>",
                 "aggregatorSubAmt":"<amount to be transferred to this child merchant>",
                 "aggregatorCharges":"<charges associated with this entity's part of the transaction to be transferred to parent (optional)>"
              },
              "<Child merchant 2 key>":{
                 "aggregatorSubTxnId":"<unique transaction ID for this specific sub-transaction>",
                 "aggregatorSubAmt":"<amount to be transferred to this child merchant>"
              },
               "Child merchant 3 key":
               {
                "aggregatorSubTxnId": "<unique transaction ID for this specific sub-transaction>",
                "aggregatorSubAmt": "<amount to be transferred to this child merchant>",
                "aggregatorCharges": "<charges associated with this entity's part of the transaction to be transferred to parent (optional)>"
               }
            }
        }
        ```

        <Accordion title="JSON request structure" icon="fa-table">
          The **var1** parameter is in JSON format. The fields in the JSON format are described in the following table:

          <HTMLBlock>{`
                                                                                                        <table style="width: 100%; border-collapse: collapse;">
                                                                                                        <thead>
                                                                                                        <tr>
                                                                                                          <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
                                                                                                          <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
                                                                                                          <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
                                                                                                        </tr>
                                                                                                        </thead>
                                                                                                        <tbody>
                                                                                                        <tr>
                                                                                                          <td style="border: 1px solid #ddd; padding: 8px;"><p>type</p>
                                                                                                        </td>
                                                                                                          <td style="border: 1px solid #ddd; padding: 8px;"><p>The type of split is specified in this field. Use <strong>absolute</strong> in this field. The absolute amount is specified for each part of the split. The absolute amount is specified in the aggregatorSubAmt field of the JSON for each child or aggregator.</p>
                                                                                                        </td>
                                                                                                          <td style="border: 1px solid #ddd; padding: 8px;"><p>absolute</p>
                                                                                                        </td>
                                                                                                        </tr>
                                                                                                        <tr>
                                                                                                          <td style="border: 1px solid #ddd; padding: 8px;"><p>payuid</p>
                                                                                                        </td>
                                                                                                          <td style="border: 1px solid #ddd; padding: 8px;"><p>The payment identifier provided by PayU for the transaction.</p>
                                                                                                        </td>
                                                                                                          <td style="border: 1px solid #ddd; padding: 8px;"><p>403993715525003544</p>
                                                                                                        </td>
                                                                                                        </tr>
                                                                                                        <tr>
                                                                                                          <td style="border: 1px solid #ddd; padding: 8px;"><p>splitInfo</p>
                                                                                                        </td>
                                                                                                          <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must include the list of aggregator sub transaction IDs and sub amounts as specified in the <a href="#request-structure-for-var1-to-be-included-in--payment_split-api">Request Structure for var1</a> subsection:  </p>
                                                                                                        <ul>
                                                                                                        <li><strong>aggregatorSubTxnId</strong>: The aggregator sub transaction ID is specified in this field.</li>
                                                                                                        <li><strong>aggregatorSubAmt</strong>: The aggregator sub amount is specified in this field.</li>
                                                                                                        <li><strong>aggregatorCharges</strong>: The aggregator charges is specified in this field.<strong>Note</strong>: The aggregatorCharges field can only be used by parent merchant to get the aggregator commission.</li>
                                                                                                        </ul>
                                                                                                        </td>
                                                                                                          <td style="border: 1px solid #ddd; padding: 8px;"><p>Refer to <a href="#request-structure-for-var1-to-be-included-in--payment_split-api">Request Structure for var1</a> subsection.</p>
                                                                                                        </td>
                                                                                                        </tr>
                                                                                                        </tbody>
                                                                                                        </table>
          `}</HTMLBlock>
        </Accordion>
      </Accordion>
    </Accordion>

    <Accordion title="Sample request" icon="fa-code">
      ```curl
      curl -X POST "https://info.payu.in/merchant/postservice?form=2"
      -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
      “key=A6lB8r&command=payment_splity&var1="type":"absolute","payuId":"403993715525003544","splitInfo":{"imAJ7I":{"aggregatorSubTxnId":"CHild101","aggregatorSubAmt":"50"},"qOoYIv":{"aggregatorSubTxnId":"Child202","aggregatorSubAmt":"50"}}}&hash=6692a8b560c51e8a4bb830206d3b8fac3678fb5b08443c7590047545beba66ec97257fec11775abbc339eabbaf1b1bf5e1c50d2c6bbf67e1a69ad597480d3691"
      ```
    </Accordion>

    <Accordion title="Sample response" icon="fa-code">
      <Accordion title="Sample response for a successful split" icon="fa-code">
        When split get saved & created

        ```plaintext
        {
          "status": 1,
          "message": "Splits creation successful.",
          "splitStatus": "success",
          "splitSegments": [
            {
              "merchantKey": "imAJ7I",
              "amount": 50,
              "subvention_amount": 0,
              "txnId": "CHild101",
              "additional_charges": 0,
              "transaction_fee": 50    },
            {
              "merchantKey": "qOoYIv",
              "amount": 50,
              "subvention_amount": 0,
              "txnId": "Child202",
              "additional_charges": 0,
              "transaction_fee": 50    }
          ]
        }
        ```
      </Accordion>

      <Accordion title="Sample response when split gets saved but are not yet created" icon="fa-code">
        When split get saved but aren’t yet created)

        ```plaintext
        {
          "status": 2,
          "message": "Splits saved, but not created yet",
          "splitStatus": "PENDING"
        }
        ```
      </Accordion>

      <Accordion title="Split creation is failed" icon="fa-code">
        In this sample response, the **error\_code** and **error\_desc** parameters display based on the failure. For the list of error\_codes, refer to [Error Codes & Error Messages](https://devguide.payu.in/split-apis/steps-to-create-the-split/payment_split-api/#Error).

        ```plaintext
        {
          "status": 0,
          "error_code": "AGG-107",
          "error_desc": "Invalid split payload in payment request"
        }
        ```

        ```plaintext
        {
           "P41sCY":{
              "aggregatorSubTxnId":"0e7411799c9f0e96620c1",
              "aggregatorSubAmt":"3",
              "aggregatorCharges":"2"
           },
           "P41sCK":{
              "aggregatorSubTxnId":"0e7411799c9f0e96620c2",
              "aggregatorSubAmt":"5"
           }
        }
        ```
      </Accordion>
    </Accordion>

    > 📘 Refunds for Split Transactions:
    >
    > You must include the var8 parameter similar to the following JSON array format with the refund details of split where **child\_merchant\_key\_x** must be substituted with the child merchant key. For more information, refer to  [Refund Transaction API > Other request parameters](ref:refund_transaction_api#other-request-parameters)
    >
    > ```plaintext
    > {
    >    "child_merchant_key_1":{
    >       "amount":100,
    >       "aggregatorRefundAmount":40
    >    },
    >    "child_merchant_key_2":{
    >       "amount":20,
    >       "aggregatorRefundAmount":0
    >    }
    > }
    > ```
  </Tab>

  <Tab title="Split During Transaction">
    This section describes the **\_payment** API contract for getting split info of the parent transaction in the Aggregator flow.

    <PaymentAPIEnvironment />

    New parameter (**splitRequest**) merchant needs to post in the payment request.

    > 📘 Notes:
    >
    > * Total **aggregatorSubAmt** must be equal to transaction amount posted by merchant.
    > * Merchant key posted in split request must belong to parent key.
    > * Transactions are not allowed on child merchant accounts or child merchant keys.
    > * You must specify two decimal places for each split, but ensure the sum of percentage of all splits is equal to 100 or sum of split amount is equal to transaction amount.

    <Accordion title="Request parameters" icon="fa-table">
      The **splitRequest** parameter  must be included in the **\_payment** API along with the regular parameters.  The following are the request parameters used for split settlements:

      <HTMLBlock>{`
                                                                <table style="width: 100%; border-collapse: collapse;">
                                                                <thead>
                                                                <tr>
                                                                  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
                                                                  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
                                                                </tr>
                                                                </thead>
                                                                <tbody>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>&lt;<a href="glossary:key">glossary:key</a>&gt;<br><code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Merchant key provided by PayU during onboarding.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>&lt;<a href="glossary:txnid">glossary:txnid</a>&gt;<br> <code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The transaction ID is a reference number for a specific order that is generated by the merchant.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount  <code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The payment amount for the transaction.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>productinfo  <code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>A brief description of the product.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>firstname  <code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The first name of the customer.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>email<br><code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The email address of the customer.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>phone<br> <code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The phone number of the customer.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>pg<br><code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The pg parameter determines which payment tabs will be displayed on the PayU page. For cards, &#39;CC&#39; will be the value. </p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankcode <code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option’s bank code value in it. For more information, refer to <a href="card-type-codes-and-supported-banks-for-cards" target="_blank"> Card Type Codes and Supported Banks for Cards</a>. </p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>ccnum<br> <code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Use 13-19 digit card number for credit/debit cards (15 digits for AMEX, 13-19 for Maestro) and validate with LUHN algorithm. Refer to  <a href="card-number-formats" target="_blank"> Card Number Formats</a> and display error message on invalid input.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>ccname  <code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the name on card – as entered by the customer for the transaction.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>ccvv<br><code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Use 3-digit CVV number for credit/debit cards and 4-digit security code (4DBC/CID) for AMEX cards. Validate with BIN API.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>ccexpmon  <code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the card’s expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format. For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>ccexpyr<br><code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the card’s expiry year – as entered by the customer for the transaction. It must be of four digits.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>furl<br><code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The success URL, which is the page PayU will redirect to if the transaction is successful.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>surl<br><code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The Failure URL, which is the page PayU will redirect to if the transaction is failed.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>splitRequest<br><code>mandatory for Split Settlements</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON</code>The JSON includes the split settlement details. For more information, refer to <a href="#json-request-structure-of-splitrequest-parameter">JSON Request Structure for splitRequest parameter</a>.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><code>mandatory</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>It is the hash calculated by the merchant. The hash calculation logic is:<br><code>sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\||\||\||SALT)</code></p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>address1<br><code>optional</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The first line of the billing address.<br><strong>For Fraud Detection</strong>: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>address2<br><code>optional</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The second line of the billing address.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>city<br><code>optional</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The city where your customer resides as part of the billing address.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>state<br><code>optional</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The state where your customer resides as part of the billing address,</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>country<br><code>optional</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The country where your customer resides.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>zipcode<br><code>optional</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Billing address zip code is mandatory for the cardless EMI option.<br><code>Character Limit</code>-20</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf1<br><code>optional</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf2<br><code>optional</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf3<br><code>optional</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf4<br><code>optional</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf5<br><code>optional</code></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> User-defined fields (udf) are used to store any information corresponding to a particular transaction.</p>
                                                                </td>
                                                                </tr>
                                                                </tbody>
                                                                </table>
      `}</HTMLBlock>
    </Accordion>

    <Accordion title="JSON Request structure of splitRequest parameter" icon="fa-code">
      The sample JSON structure for the **splitRequest** field:

      > 📘 **Notes**:
      >
      > * For the **absolute** type split, you must ensure that the sum of the amount of all splits is equal to the parent transaction amount.
      > * For the percentage type split, you must ensure that the sum of the percentage of all splits is equal to 100. You can use any number of decimal places for each split, but ensure the sum of the percentage of all splits is equal to 100.

      ```plaintext
      {
         "type":"<Type of split, absolute or split>",
         "splitInfo":{
            "<Child Merchant 1 key>":{
               "aggregatorSubTxnId":"<unique transaction ID for this specific sub-transaction>",
               "aggregatorSubAmt":"<amount to be transferred to this child merchant>",
               "aggregatorCharges":"<charges associated with this entity's part of the transaction to be transferred to parent (optional)>"
            },
            "<Child merchant 2 key >":{
               "aggregatorSubTxnId":"<unique transaction ID for this specific sub-transaction>",
               "aggregatorSubAmt":"<amount to be transferred to this child merchant>"
            }
         }
      }
      ```

      The following fields are included in the **splitRequest** parameter in a JSON format to specify the split details. The fields in the JSON format are described in the following table:

      <HTMLBlock>{`
                                                                <table style="width: 100%; border-collapse: collapse;">
                                                                <thead>
                                                                <tr>
                                                                  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
                                                                  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
                                                                  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
                                                                </tr>
                                                                </thead>
                                                                <tbody>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>type<br><strong>mandatory</strong></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Any of the following type of split is specified in this field.  </p>
                                                                <ul>
                                                                <li><strong>absolute</strong>: The absolute amount is specified for each part of the split. The absolute amount is specified in the aggregatorSubAmt field of the JSON for each child or aggregator. For a sample request and response, refer to Absolute Split During Payment</li>
                                                                <li><strong>percentage</strong>: The percentage of the amount is specified for each part of the split. The percentage of the amount is specified in the aggregatorSubAmt field of the JSON for each child or aggregator. For a sample request and response, refer to Split by Percentage During Payment</li>
                                                                </ul>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>absolute</p>
                                                                </td>
                                                                </tr>
                                                                <tr>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>splitInfo<br><strong>mandatory</strong></p>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"><p>JSON\` This parameter must include the list of aggregator sub transaction IDs and sub amounts as follows:  </p>
                                                                <ul>
                                                                <li><strong>aggregatorSubTxnId</strong>: The transaction ID of the aggregator is posted in this parameter. This field is mandatory and applicable only for child merchants.</li>
                                                                <li><strong>aggregatorSubAmt</strong>: The transaction amount or percentage split for the aggregator is posted in this parameter. This field is mandatory.</li>
                                                                <li><strong>aggregatorCharges</strong>: The transaction amount or percentage split for aggregator charges is posted in this parameter. This field is optional.<br><strong>Note</strong>: Only the parent aggregators can have the aggregatorCharges field as part of their JSON to collect charges.</li>
                                                                </ul>
                                                                </td>
                                                                  <td style="border: 1px solid #ddd; padding: 8px;"></td>
                                                                </tr>
                                                                </tbody>
                                                                </table>
      `}</HTMLBlock>
    </Accordion>

    <Accordion title="Hashing request" icon="fa-code">
      Added as extra parameter in the calculation of hash in case of providing Split Request at time of payment. This parameter will be at the end of the hash pattern. and required while sending Split Request at time of payment.

      You need to generate a string using certain parameters and apply the SHA-512 algorithm to this string. For more information on hashing, refer to [Generate Hash](doc:generate-hash-merchant-hosted).

      > 📘 Note:
      >
      > Ensure that you use pipe (|) character between these parameters as mentioned in the following code block.

      The parameter order is in the following code block`:`

      ```plaintext
      sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|splitRequest)
      ```

      Where, `splitRequest` will be at the end of the hash pattern string.

      **Example**:

      ```plaintext
      hash('sha512', 'Ax4j7J|payment-txnid-1|10|Product Info|Payu-Admin|test@example.com|||||||||||t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL|{"type":"absolute","splitInfo":{"P41sCY":{"aggregatorSubTxnId":"0e7411799c9f0e96620c11","aggregatorSubAmt":"3","aggregatorCharges":"2"},"P41sCK":{"aggregatorSubTxnId":"0e7411799c9f0e96620c22","aggregatorSubAmt":"5"}}}'));
      ```
    </Accordion>

    <Accordion title="Hash validation logic for payment response (Reverse hashing)" icon="fa-code">
      Use the following algorithm for reverse hashing the response from PayU:

      ```
      sha512(SALT|status|splitInfo||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
      ```
    </Accordion>

    > **Note**: You can implement the convenience fee for any of the above Split APIs. For more information on convenience fee, refer to [Convenience Fee Handling](doc:convenience-fee-handling).

  </Tab>
</Tabs>

## Step 2. Get Aggregator/Parent Transaction Info

The **Get Aggregator Transactions** API is for getting the transaction info of parent merchants in the Aggregator flow.
**Environment**

|                            |                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://uat-onepayuonboarding.payu.in>](https://uat-onepayuonboarding.payu.in>) |
| **Production Environment** | \<[https://onboarding.payu.in>](https://onboarding.payu.in>)                       |

<Accordion title="Sample request" icon="fa-code">
  ```
    curl --location --request POST 'https://info.payu.in/merchant/postservice?form=2' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=A****J' \
    --data-urlencode 'command=get_aggregator_transactions' \
    --data-urlencode 'var1=2021-12-29 22:00' \
    --data-urlencode 'hash=586e3379b3d9f90682329cf7efd27273aeb290936d9edf98686370bc59fdc67b06c57a5201b9bd193dc0f00fe6ecd821f60d81d5789ca2ee516db309f28025e9' \
    --data-urlencode 'var2=2021-12-29 22:30' \
    --data-urlencode 'var3=1' \
    --data-urlencode 'var4=100' \
    --data-urlencode 'var5='
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  ```
    {
        "status": 1,
        "msg": "Transaction Fetched Successfully",
        "Transaction_details": [
            {
                "id": "412345678912384148",
                "status": "captured",
                "key": "A***J",
                "merchantname": "Aggregator-Parent",
                "txnid": "2c1c4431f3fcf5a98a66",
                "base_id": null,
                "firstname": "Payu-Admin",
                "lastname": "",
                "addedon": "2021-12-29 22:11:08",
                "bank_name": "Credit Cards",
                "payment_gateway": "AxisCYBER",
                "phone": "1234567890",
                "email": "test@example.com",
                "transaction_fee": "10.00",
                "amount": "10.00",
                "discount": "0.00",
                "additional_charges": "0.00",
                "productinfo": "Product Info",
                "error_code": "E000",
                "bank_ref_no": "5192296867061049177385",
                "ibibo_code": "CC",
                "mode": "CC",
                "address2": "",
                "city": "",
                "zipcode": "",
                "pg_mid": null,
                "offer_type": null,
                "splitCreated": true,
                "is_parent_transaction": true,
                "splitInfo": [
                    {
                        "id": "412345678912384152",
                        "status": "captured",
                        "merchantId": "39032915",
                        "key": "P****Y",
                        "txnid": "2c1c4431f3fcf5a98a661",
                        "addedon": "2021-12-29 22:11:53",
                        "transaction_fee": "3.00",
                        "amount": "3.00",
                        "discount": "0.00",
                        "additional_charges": "0.00"
                    },
                    {
                        "id": "412345678912384153",
                        "status": "captured",
                        "merchantId": "39032916",
                        "key": "P****K",
                        "txnid": "2c1c4431f3fcf5a98a662",
                        "addedon": "2021-12-29 22:11:53",
                        "transaction_fee": "5.00",
                        "amount": "5.00",
                        "discount": "0.00",
                        "additional_charges": "0.00"
                    },
                    {
                        "id": "412345678912384154",
                        "status": "captured",
                        "merchantId": "39032914",
                        "key": "A****J",
                        "txnid": "2c1c4431f3fcf5a98a66",
                        "addedon": "2021-12-29 22:11:53",
                        "transaction_fee": "2.00",
                        "amount": "2.00",
                        "discount": "0.00",
                        "additional_charges": "0.00"
                    }
                ]
            },
            {
                "id": "412345678912384155",
                "status": "bounced",
                "key": "A****J",
                "merchantname": "Aggregator-Parent",
                "txnid": "02b3e5b6bc97dc3a3418",
                "base_id": null,
                "firstname": "Payu-Admin",
                "lastname": "",
                "addedon": "2021-12-29 22:13:08",
                "bank_name": "Credit Cards",
                "payment_gateway": "AxisCYBER",
                "phone": "1234567890",
                "email": "test@example.com",
                "transaction_fee": "11.00",
                "amount": "11.00",
                "discount": "0.00",
                "additional_charges": "0.00",
                "productinfo": "Product Info",
                "error_code": "E501",
                "bank_ref_no": null,
                "ibibo_code": "CC",
                "mode": "CC",
                "address2": "",
                "city": "",
                "zipcode": "",
                "pg_mid": null,
                "offer_type": null,
                "splitCreated": false,
                "is_parent_transaction": true,
                "splitInfo": null
            },
            {
                "id": "412345678912384156",
                "status": "captured",
                "key": "A****J",
                "merchantname": "Aggregator-Parent",
                "txnid": "61c21439bbd4609e258b",
                "base_id": null,
                "firstname": "Payu-Admin",
                "lastname": "",
                "addedon": "2021-12-29 22:14:23",
                "bank_name": "Credit Cards",
                "payment_gateway": "AxisCYBER",
                "phone": "1234567890",
                "email": "test@example.com",
                "transaction_fee": "11.00",
                "amount": "11.00",
                "discount": "0.00",
                "additional_charges": "0.00",
                "productinfo": "Product Info",
                "error_code": "E000",
                "bank_ref_no": "6333825950714879001604",
                "ibibo_code": "CC",
                "mode": "CC",
                "address2": "",
                "city": "",
                "zipcode": "",
                "pg_mid": null,
                "offer_type": null,
                "splitCreated": true,
                "is_parent_transaction": true,
                "splitInfo": [
                    {
                        "id": "412345678912384160",
                        "status": "captured",
                        "merchantId": "39032915",
                        "key": "P****Y",
                        "txnid": "61c21439bbd4609e258b1",
                        "addedon": "2021-12-29 22:14:40",
                        "transaction_fee": "3.00",
                        "amount": "3.00",
                        "discount": "0.00",
                        "additional_charges": "0.00"
                    },
                    {
                        "id": "412345678912384161",
                        "status": "captured",
                        "merchantId": "39032916",
                        "key": "P****K",
                        "txnid": "61c21439bbd4609e258b2",
                        "addedon": "2021-12-29 22:14:40",
                        "transaction_fee": "6.00",
                        "amount": "6.00",
                        "discount": "0.00",
                        "additional_charges": "0.00"
                    },
                    {
                        "id": "412345678912384162",
                        "status": "captured",
                        "merchantId": "39032914",
                        "key": "A****J",
                        "txnid": "61c21439bbd4609e258b",
                        "addedon": "2021-12-29 22:14:40",
                        "transaction_fee": "2.00",
                        "amount": "2.00",
                        "discount": "0.00",
                        "additional_charges": "0.00"
                    }
                ]
            }
        ]
    }
  ```
</Accordion>

## Step 3. Release Settlement API

The** Release Settlement** API is used to flag the sub-payment you want to settle; after adding splits for a particular payment, the money will not be settled directly into the child merchants account unless you call a release event corresponding to the individual suborder you want to settle.

The Release Settlement API can be used to release the settlement of all the blocked child transactions in the aggregator workflow.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2"
  -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
  "key=A****r&command=release_settlement&var1=8000123&var2=8000123&hash=6692a8b560c51e8a4bb830206d3b8fac3678fb5b0844"
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-code">
  <Accordion title="Success Scenario" icon="fa-code">
    * Successful Transaction

    Sample Success Response for Release Settlement

    ```plaintext
    {"status":1,"msg":"Release request is accepted"}
    ```
  </Accordion>
</Accordion>

<Accordion title="Failure Scenarios" icon="fa-code">
  * Failure Response when PayU ID is empty

  Failure Response when PayUID is empty

  ```plaintext
  {"status":0,"msg":"payuId is empty"}
  ```

  * Failure response when child merchant ID is empty

  Failure response when child merchant ID is empty

  ```plaintext
  {"status":0,"msg":"Mid passed is empty"}
  ```

  * Failure Response when child merchant ID and PayU ID do not match

  Failure Response when child merchant ID and PayU ID do not match

  ```plaintext
  {"status":0,"msg":"Invalid childMid and payuId"}
  ```

  * Failure response when attempting to release an already released sub-payment

  Failure response when attempt to release an already released sub- payment

  ```plaintext
  {"status":0,"msg":"Release request is already accepted"}
  ```
</Accordion>

> 📘 Refunds for Split Transactions:
>
> You must include the var8 parameter similar to the following JSON array format with the refund details of split where **child_merchant_key_x** must be substituted with the child merchant key. For more information, refer to  [Refund Transaction API > Other request parameters](ref:refund_transaction_api#other-request-parameters)
>
> ```plaintext
> {
>    "child_merchant_key_1":{
>       "amount":100,
>       "aggregatorRefundAmount":40
>    },
>    "child_merchant_key_2":{
>       "amount":20,
>       "aggregatorRefundAmount":0
>    }
> }
> ```
