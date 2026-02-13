---
title: Get Aggregator/Parent Transaction Info API
excerpt: ''
api:
  file: get-aggregatorparent-transaction-info-2.json
  operationId: GetAggregator/ParentTransactionInfo
deprecated: false
hidden: false
metadata:
  title: Get Aggregator/Parent Transaction Info API
  description: ''
  keywords:
    - Get Aggregator/Parent Transaction Info API
    - Aggregator/Parent Transaction Info API
    - get_aggregator_transactions API Command
    - API Command get_aggregator_transactions
  robots: index
next:
  description: ''
---
The **Get Aggregator Transactions** API is for getting the transaction info of parent merchants in the Aggregator flow.

<Callout icon="📮" theme="default">
  **Postman Collection**: Download the **Get Aggregator/Parent Transaction Info API  Postman Collection** from the following location:

  https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/s2ppj9w/get-aggregator-parent-transaction-info-api
</Callout>

### Environment

|                            |                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://uat-onepayuonboarding.payu.in>](https://uat-onepayuonboarding.payu.in>) |
| **Production Environment** | \<[https://onboarding.payu.in>](https://onboarding.payu.in>)                       |

<details>
  <summary>Response parameters and sample response</summary>

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
</details>

<details>
  <summary>Response parameters and sample response</summary>

  <HTMLBlock>{`
          <table style="width: 100%; border-collapse: collapse;">
            <thead>
              <tr>
                <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
                <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">status</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This parameter contains the status of response. It can be any of the following:</p>
                  <ul>
                    <li><strong>0:</strong> Failed</li>
                    <li><strong>1:</strong> Success</li>
                  </ul>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">msg</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This parameter contains the response or error message.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">Transaction_details</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This parameter contains the transaction details in an array format and it is displayed only when the <strong>status</strong> field returns the value as <strong>1</strong>. For more information on each field in the array and sample, refer to the next table.</p>
                </td>
              </tr>
            </tbody>
          </table>

          <h3>Fields in the Transaction_details array</h3>

          <table style="width: 100%; border-collapse: collapse;">
            <thead>
              <tr>
                <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
                <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">id</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the PayU transaction ID.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">status</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the transaction status.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">key</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the parent merchant key.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">merchantname</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the parent merchant name.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">txnid</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the transaction ID.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">base_id</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the base PayU Transaction ID. It will be null for a parent transaction.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">firstname</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the first name of the customer who did the transaction.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">lastname</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the last name of the customer who did the transaction.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">addedon</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the transaction created date and time. Format: yyyy-mm-dd hh:ii:ss</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">bank_name</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the bank name of payment transaction.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">payment_gateway</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the payment gateway used in the transaction.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">phone</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the contact number of the customer who did the transaction.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">email</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the email ID of the customer who did the transaction.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">transaction_fee</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the transaction fee without discount and additional charges.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">amount</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the total amount paid by customer.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">discount</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the discount or Subvention charges on the transaction.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">additional_charges</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the additional charges on transaction.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">productinfo</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the product information provided by merchant.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">error_code</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the transaction error code. For more information on errors, refer to <a href="https://docs.payu.in/docs/error-handling">Error Handling</a></p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">bank_ref_no</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the bank reference number.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">ibibo_code</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the IBIBO Code or bank_code that was submitted in transaction by the merchant to PayU.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">mode</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the Mode of transaction, such as, CC, DC, NB, EMI.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">address2</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the address of the customer.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">city</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the city of the customer.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">zipcode</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the PIN code of the customer.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">pg_mid</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the PG ID.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">offer_type</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains the offer type if any offers were used.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">splitCreated</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains no value or null.</p>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">is_parent_transaction</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains any of the the flag to indicate whether it is a Parent Transaction:</p>
                  <ul>
                    <li><strong>true</strong>: When the transaction is a parent transaction</li>
                    <li><strong>false</strong>: When the transaction is not a parent transaction</li>
                  </ul>
                </td>
              </tr>
              <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">splitInfo</td>
                <td style="border: 1px solid #ddd; padding: 8px;">
                  <p>This field contains no value or null for child transactions.</p>
                </td>
              </tr>
            </tbody>
          </table>
  `}</HTMLBlock>
</details>

<details>
  <summary>Sample response</summary>

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
</details>

## Request parameters
