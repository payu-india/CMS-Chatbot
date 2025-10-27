---
title: UDF Update API
api:
  file: opgsp-invoice-4.json
  operationId: udf_update-OPGSP
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: ''
  description: ''
  robots: index
---
The **UDF Update** API is used to update the UDF1-UDF5 values of a transaction. UDFs are the user-defined fields which are posted from the merchant to PayU. This API is specifically used to update the values in these fields in the PayU database. The return parameters are the updated UDF values of the transaction.

<GENERALAPIsEnvironment />

<Accordion title="Sample request other then UPI AutoPay" icon="fa-code">
  ```
    curl --location --globoff 'https://test.payu.in/merchant/postservice.php?form=2' \
    --form 'key="PRiQvJ"' \
    --form 'command="udf_update"' \
    --form 'var1="my_order_642"' \
    --form 'var2="AAAPZ1234C"' \
    --form 'var4="22/08/1972"' \
    --form 'var5="SellerName"' \
    --form 'var6="INV000000005"' \
    --form 'hash="{{hash}}"'
  ```
</Accordion>

<Accordion title="Sample request for UPI autopay" icon="fa-code">
  ```
    curl --location --globoff 'https://test.payu.in/merchant/postservice.php?form=2' \
    --form 'key="PRiQvJ"' \
    --form 'command="udf_update"' \
    --form 'var1="my_order_64240"' \
    --form 'var2="AAAPZ1234C||22/08/1972"' \
    --form 'var4="INV-123_1231||MerchantName"' \
    --form 'hash="{{hash}}"'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ### Success Scenario

  * If successfully updated for cards

  ```JSON
  {
      "status": "UDF values updated",
      "transaction_id": "my_order_64240",
      "udf1": "AAAPZ1234C",
      "udf2": "",
      "udf3": "22/08/1972",
      "udf4": "SellerName",
      "udf5": "INV000000005"
  }
  ```

  * If successfully updated for UPI autopay:

  ```JSON
  {
      "status": "UDF values updated",
      "transaction_id": "my_order_64240",
      "udf1": "AAAPZ1234C",
      "udf2": "",
      "udf3": "22/08/1972",
      "udf4": "SellerName",
      "udf5": "INV000000005"
  }
  ```

  ### Failure Scenarios

  * If the transaction ID is empty

  ```JSON
  ( 
  [status] => 0 
  [msg] => Parameter missing 
  ) 
  ```

  * If the transaction ID is invalid

  ```JSON
  ( 
  [status] => 0 
  [msg] => Invalid TXN ID 
  ) 
  ```

  * If Hash is invalid:

  ```JSON
  {
      "status": 0,
      "msg": "Invalid Hash."
  }
  ```
  * If the merchant is not enabled for UDF updates:

  ```JSON
{
    "status": "0",
    "msg": "Update not allowed on provided Field"
}
  ```
  * If no data found in the transaction ID:

  ```JSON
{
    "status": "0",
    "msg": "No Data Found for txnid: 3424"
}
  ```
  * If the merchant is inactive:

  ```JSON
{
    "msg": "Merchant is not authorized to use PayU API",
    "status": 0
}
  ```
</Accordion>

## Request parameters

<Accordion title="Reference info for request parameters" icon="fa-flask">
  <HTMLBlock>{`
                              <table>
                                <thead>
                                  <tr>
                                    <th><strong>Parameter</strong></th>
                                    <th><strong>Reference</strong></th>
                                  </tr>
                                </thead>
                                <tbody>
                                  <tr>
                                    <td>key</td>
                                    <td>
                                      The merchant key provided by PayU while onboarding.<br>
                                      For more information on how to generate the Key and Salt, refer to any of the following:<br>
                                      - <strong>Production</strong>: <a href="https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard">Generate Merchant Key and Salt</a><br>
                                      - <strong>Test</strong>: <a href="docs.payu.in/docs/generate-test-merchant-key-and-salt">Generate Test Merchant Key and Salt</a>
                                    </td>
                                  </tr>
                                  <tr>
                                    <td>hash</td>
                                    <td>
                                      Hash logic for payment API is:<br>
                                      <code>sha512(key|command|var1|salt)</code>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
  `}</HTMLBlock>
</Accordion>