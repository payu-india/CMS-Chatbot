---
title: Get Child/Parent Split Transaction Info API
excerpt: ''
api:
  file: get-aggregatorparent-transaction-info-4.json
  operationId: GetChildParentSplitTransactionInfo
deprecated: false
hidden: false
metadata:
  title: Get Child/Parent Split Transaction Info API
  description: ''
  keywords:
    - get_split_transactions API Command
    - Get Child Split Transaction Info
    - API Command get_split_transactions
    - Get Parent Split Transaction Info API
  robots: index
next:
  description: ''
---
The **Get Child/Parent Split Transactions** API is for getting the transaction info of a child or parent split in Aggregator Flow.

<Callout icon="📘" theme="info">
  **Note**: You can check the transaction info only for a single child or parent split. You need to submit separate requests for multiple splits to get the corresponding split information.
</Callout>

<Callout icon="📮" theme="default">
  **Postman Collection**: Download the **Get Child/Parent Split Transaction Info API Postman Collection** from the following location:

  https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/04tmd4c/get-child-parent-split-transaction-info-api
</Callout>

### Environment

|                        |                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------- |
| Test Environment       | \<[https://uat-onepayuonboarding.payu.in>](https://uat-onepayuonboarding.payu.in>) |
| Production Environment | \<[https://onboarding.payu.in>](https://onboarding.payu.in>)                       |

<details>
  <summary>Sample request</summary>

  ```curl
  curl --location --request POST 'https://info.payu.in/merchant/postservice?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=A***J' \
  --data-urlencode 'command=get_split_transactions' \
  --data-urlencode 'var1=2021-12-30 00:00' \
  --data-urlencode 'hash=586e3379b3d9f90682329cf7efd27273aeb290936d9edf98686370bc59fdc67b06c57a5201b9bd193dc0f00fe6ecd821f60d81d5789ca2ee516db309f28025e9' \
  --data-urlencode 'var2=2021-12-30 14:00' \
  --data-urlencode 'var3=1' \
  --data-urlencode 'var4=10' \
  --data-urlencode 'var5=A****J'
  ```
</details>

<details>
  <summary>Response parameters</summary>

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
        <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the status of response. It can be any of the following:  </p>
      <ul>
      <li><strong>0:</strong> Failed</li>
      <li>**1:**Success</li>
      </ul>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>msg</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the response or error message.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>Transaction_details</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the transaction details in an array format and it is displayed only when the <strong>status</strong> field returns the value as <strong>1</strong>. For more information on each field in the array, refer to the next table.</p>
      </td>
      </tr>
      </tbody>
      </table>
  `}</HTMLBlock>

  ### Fields in the  Transaction\_details array

  <HTMLBlock>{`
      <table style="width: 100%; border-collapse: collapse;">
      <thead>
      <tr>
        <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>id</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the PayU transaction ID.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the transaction status.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>key</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the parent merchant key.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantname</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the parent merchant name.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>txnid</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the transaction ID.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>base_id</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the base PayU Transaction ID. It will be null for a parent transaction.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>firstname</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the first name of the customer who did the transaction.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>lastname</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the last name of the customer who did the transaction.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>addedon</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the transaction created date and time. Format: yyyy-mm-dd hh:ii:ss</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>bank_name</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the bank name of payment transaction.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>payment_gateway</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the payment gateway used in the transaction.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>phone</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the contact number of the customer who did the transaction.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>email</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the email ID of the customer who did the transaction.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>transaction_fee</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the transaction fee without discount and additional charges.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>amount</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the total amount paid by customer.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>discount</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the discount or Subvention charges on the transaction.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>additional_charges</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the additional charges on transaction.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>productinfo</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the product information provided by merchant.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>error_code</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the transaction error code. For more information on errors, refer to <a href="https://docs.payu.in/docs/error-handling">Error Handling</a></p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>bank_ref_no</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the bank reference number.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>ibibo_code</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the IBIBO Code or bank_code that was submitted in transaction by the merchant to PayU.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>mode</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the Mode of transaction, such as, CC, DC, NB, EMI.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>address2</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the address of the customer.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>city</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the city of the customer.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>zipcode</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the PIN code of the customer.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>pg_mid</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the PG ID.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>offer_type</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the offer type if any offers were used.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>splitCreated</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains no value or null.</p>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>is_parent_transaction</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains any of the the flag to indicate whether it is a Parent Transaction:  </p>
      <ul>
      <li><strong>true</strong>; When the transaction is a parent transaction</li>
      <li>**false **; When the transaction is not a parent transaction</li>
      </ul>
      </td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>splitInfo</p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains no value or null for child transactions.</p>
      </td>
      </tr>
      </tbody>
      </table>
  `}</HTMLBlock>
</details>

<details>
  <summary>Sample response</summary>

  **Success scenario**

  ```
  {
      "status": 1,
      "msg": "Transaction Fetched Successfully",
      "Transaction_details": [
          {
              "id": "412345678912384187",
              "status": "captured",
              "key": "A****J",
              "merchantname": "Aggregator-OwnChild",
              "txnid": "6de4dc8abc38473122cb",
              "base_id": "412345678912384184",
              "firstname": "Payu-Admin",
              "lastname": "",
              "addedon": "2021-12-30 13:59:01",
              "bank_name": "Credit Cards",
              "payment_gateway": "AxisCYBER",
              "phone": "1234567890",
              "email": "test@example.com",
              "transaction_fee": "2.00",
              "amount": "2.00",
              "discount": "0.00",
              "additional_charges": "0.00",
              "productinfo": "Product Info",
              "error_code": "E000",
              "bank_ref_no": "2516463285587866763243",
              "ibibo_code": "CC",
              "mode": "CC",
              "address2": "",
              "city": "",
              "zipcode": "",
              "pg_mid": null,
              "offer_type": null,
              "splitCreated": null,
              "is_parent_transaction": false,
              "splitInfo": null
          },
          {
              "id": "412345678912384190",
              "status": "captured",
              "key": "A****J",
              "merchantname": "Aggregator-OwnChild",
              "txnid": "6de4dc8abc38473122cb",
              "base_id": "412345678912384184",
              "firstname": "Payu-Admin",
              "lastname": "",
              "addedon": "2021-12-30 13:59:06",
              "bank_name": "Credit Cards",
              "payment_gateway": "AxisCYBER",
              "phone": "1234567890",
              "email": "test@example.com",
              "transaction_fee": "2.00",
              "amount": "2.00",
              "discount": "0.00",
              "additional_charges": "0.00",
              "productinfo": "Product Info",
              "error_code": "E000",
              "bank_ref_no": "2516463285587866763243",
              "ibibo_code": "CC",
              "mode": "CC",
              "address2": "",
              "city": "",
              "zipcode": "",
              "pg_mid": null,
              "offer_type": null,
              "splitCreated": null,
              "is_parent_transaction": false,
              "splitInfo": null
          }
      ]
  }
  ```

  > 📘 Note:
  >
  > If the response has three pages and you submit 4 in the var3 parameter of the request, you will get the Transaction\_Details parameter value in the response as blank.

  **Failure scenario**

  ```
  {
      "status": 0,
      "msg": "Invalid Hash."
  }
  ```
</details>

## Request parameters
