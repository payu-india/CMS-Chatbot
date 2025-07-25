---
title: Split by Percentage During Transaction - v2 Payment API
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can split during a transaction made using **\_payment** API by percentage, where you must ensure that the sum of percentage of all splits is equal to 100.

> 📘 Note:
>
> You must specify two decimal places for each split, but ensure the sum of percentage of all splits is equal to 100.

**Environment**

<V2_payment_envrionment />

## Request header

<V2_payment_header_params />

## Request body

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>accountId</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Represents the merchant key provided by PayU during onboarding. For more information, refer to <a href="https://docs.payu.in/v2/reference/absolute-split-during-transaction-v2_payment/#request-body">Request Body Parameters</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">MERCHANT123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnId</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Transaction ID for transaction tracking. Must be unique for every transaction. For more information, refer to <a href="https://docs.payu.in/v2/reference/absolute-split-during-transaction-v2_payment/#request-body">Request Body Parameters</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">TXN123456</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentMethod</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains details of the payment method. For more information, refer to <a href="https://docs.payu.in/v2/reference/absolute-split-during-transaction-v2_payment/#paymentmethod-object-fields-description">paymentMethod Object Fields Description</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>order</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains transaction order details such as product info, ordered items, user-defined fields, and payment charge details. For more information, refer to <a href="https://docs.payu.in/v2/reference/absolute-split-during-transaction-v2_payment/#order-object-fields-description">order Object Fields Description</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Additional metadata for the transaction. For more information, refer to <a href="https://docs.payu.in/v2/reference/absolute-split-during-transaction-v2_payment/#additionalinfo-object-fields-description">additionalInfo Object Fields Description</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>callBackActions</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL actions for payments (e.g., success, failure, cancel). For more information, refer to <a href="https://docs.payu.in/v2/reference/absolute-split-during-transaction-v2_payment/#callbackactions-object-fields-description">callBackActions Object Fields Description</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>billingDetails</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Customer billing details including name, phone, and address. For more information, refer to <a href="https://docs.payu.in/v2/reference/absolute-split-during-transaction-v2_payment/#billingdetails-object-fields-description">billingDetails Object Fields Description</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>authorization</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Authorization details for the payment process, including 3DS metadata. For more information, refer to <a href="https://docs.payu.in/v2/reference/absolute-split-during-transaction-v2_payment/#authorization-object-fields-description">authorization Object Fields Description</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>splitRequest </br> <code>mandatory for Split Settlement</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the split payment. For more information, refer to <a href="https://docs.payu.in/v2/reference/absolute-split-during-transaction-v2_payment/#splitrequest-object-fields-description">splitRequest Object Fields Description</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {<br>                  &quot;type&quot;: &quot;absolute&quot;,<br>                  &quot;splitInfo&quot;: {<br>                    &quot;123412&quot;: {<br>                      &quot;aggregatorSubTxnId&quot;: &quot;12312941&quot;,<br>                      &quot;aggregatorSubAmt&quot;: &quot;2000.55&quot;<br>                    },<br>                    &quot;2300019&quot;: {<br>                      &quot;aggregatorSubTxnId&quot;: &quot;12312941&quot;,<br>                      &quot;aggregatorSubAmt&quot;: &quot;134.23&quot;<br>                    }<br>                  }</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentMethod object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">name<br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Represents the payment method used. For credit card, include CreditCard.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CreditCard</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">bankCode<br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains the bank code. Valid values: CC, MAST, VISA.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CC</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">paymentCard<br/><code>mandatory for cards</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains physical card or saved card details. For more information, refer to </td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentCard object fields description

<V2_paymentCard />

### order object fields description

<V2_order_object />

### additionalInfo object fields description

<AdditionalI_Info_object />

### callBackActions object fields description

<CallbackActions_object />

### billingDetails object fields description

<BillingDetails_object />

### authorization object fields description

<V2_authorization_cards />

### threeDS2RequestData

<ThreeDSRequestData_object />

### splitRequest object fields description

The following fields are included in the **splitRequest** parameter in a JSON format to specify the absolute split details. The fields in the JSON format are described in the following table:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Field**
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
        type
        **mandatory**
      </td>

      <td>
        `string` Specify the **percentage** type of split in this field. The absolute amount is specified in the **aggregatorSubAmt** field of the JSON for each child or aggregator.
      </td>

      <td>
        percentage
      </td>
    </tr>

    <tr>
      <td>
        splitInfo
        **mandatory**
      </td>

      <td>
        `JSON` This parameter must include the list of aggregator sub transaction IDs and sub amounts as follows:

        * **aggregatorSubTxnId**: The transaction ID of the aggregator is posted in this parameter. This field is mandatory and applicable only for child merchants.
        * **aggregatorSubAmt**: The transaction amount or percentage split for the aggregator is posted in this parameter. This field is mandatory.
        * **aggregatorCharges** (optional): The transaction amount or percentage split for aggregator charges is posted in this parameter. This field is optional.
          * *Note*\*: Only the parent aggregators can have the aggregatorCharges field as part of their JSON to collect charges.
      </td>

      <td>
        \{\
        "merchantKey1": \{
        "aggregatorSubTxnId": "30nknyhkhib",
        "aggregatorSubAmt": "8"
        } 
      </td>
    </tr>
  </tbody>
</Table>

#### JSON request structure of splitInfo

The sample JSON structure for the **splitInfo** field:

> 📘 Notes:
>
> Before peruse the following sample code, remove the white spaces as some editors may introduce junk characters.

```plaintext
{
  "type": "percentage",
  "splitInfo": {
    "merchantKey1": {
      "aggregatorSubTxnId": "30nknyhkhib",
      "aggregatorSubAmt": "53.33", // %age wrt to total payable amount
      "aggregatorCharges": "13.33" // parent merchant commission (Optional) | %age wrt to total payable amount
    },
    "merchantKey2": {
      "aggregatorSubTxnId": "13u0nknou0", //%age wrt to total payable amount
      "aggregatorSubAmt": "13.33" // %age wrt to total payable amount
    },
    "merchantKey3": {
      "aggregatorSubTxnId": "13u0nknou0",
      "aggregatorSubAmt": "13.33", // %age wrt to total payable amount
      "aggregatorCharges": "6.68" // parent merchant commission (Optional) | %age wrt to total payable amount
    }
  }
}
```

## Sample request

```
curl --location 'https://apitest.payu.in/v2/payments/v2/payments' \
--header 'date: Tue, 05 Nov 2024 06:12:57 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="d583ff8069c7dfa8340464a24bdd01cbebf4432b4dfe4de862065cc9c9dc622c24c77cb1ac1142bf581ec07eca8d0ec78a66db93f6cd557d0da552f05c0825e3"' \
--header 'Content-Type: application/json' \
--header 'mid: 8390470' \
--header 'X-CREDENTIAL-USERNAME: UMXDPA' \
--data-raw '{
                "accountId": "smsplus",
                "referenceId": "b5f2d8785768087678fn4",
                "amount": 10,
                "currency": "INR",
                "paymentSource": "WEB",
                "paymentMethod": {
                  "name": "CC",
                  "bankCode": "CC",
                  "paymentCard": {
                    "cardNumber": 5123456789012346,
                    "validThrough": "04/2022",
                    "ownerName": "Sartaj",
                    "alternateName": "doe,John",
                    "cvv": 987
                  }
                },
                "order": {
                  "productInfo": "qwertyuiopasdfghjkl",
                  "userDefinedFields": {
                    "udf1": "",
                    "udf2": "",
                    "udf3": "",
                    "udf4": "",
                    "udf5": "",
                    "udf6": "",
                    "udf7": "",
                    "udf8": "",
                    "udf9": "",
                    "udf10": ""
                  },
                  "paymentChargeSpecification": {
                    "price": 10 
                  }
                },
                "additionalInfo": {
                  "createOrder": "false"
                },
                "callBackActions": {
                  "successAction": "https://pp78admin.payu.in/test_response",
                  "failureAction": "https://pp78admin.payu.in/test_response",
                  "cancelAction": "https://pp78admin.payu.in/test_response"
                },
                "billingDetails": {
                  "firstName": "sartaj",
                  "lastName": "",
                  "phone": "9876543210",
                  "email": "testv2@example.in",
                  "city": "Bharatpur",
                  "state": "Rajasthan",
                  "country": "India",
                  "zipCode": "321028"
                },
                "splitRequest": {
                  "type": "absolute",
                  "splitInfo": {
                    "123412": {
                      "aggregatorSubTxnId": "12312941",
                      "aggregatorSubAmt": "2000.55"
                    },
                    "2300019": {
                      "aggregatorSubTxnId": "12312941",
                      "aggregatorSubAmt": "134.23"
                    }
                  }
                }
              }
            }
          }'
```

## Check the response from PayU

```
Array
(
    [referenceId] => b5f2d8785768087678fm9
    [paymentId] => 1999110000001769
    [message] => Please call verify api to get the transaction status
)
```

> 📘 Reference:
>
> To check the transaction status, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api).

<br />

#### **TDR model**

The formatted response for the above sample request is similar to the following:

```plaintext
Array
(
    [mihpayid] => 41**45678912383977
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => Ax4j7J
    [txnid] => 9a70ea0155268101001b
    [amount] => 100.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 100
    [addedon] => 2021-12-22 19:02:15
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
    [hash] => 6e700275583072c0361bac771a4166a4be5334112d59e40181c5668895c477a047c7be250068186fd26ca72928d7e168f92bb96003a7fffbf4933bb818f4c48a
    [field1] => 5582299554914671900181
    [field2] => 113476
    [field3] => 100.00
    [field4] => 41**45678912383977
    [field5] => 100
    [field6] => 02
    [field7] => AUTHPOSITIVE
    [field8] => 
    [field9] => Transaction is Successful
    [payment_source] => payu
    [PG_TYPE] => AxisCYBER
    [bank_ref_num] => 5582299554914671900181
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => Test User
    [cardnum] => 512345XXXXXX2346
    [cardhash] => This field is no longer supported in postback params.
    [splitInfo] => {"splitStatus":"success","splitSegments":[{"merchantKey":"P41sCY","amount":50,"subvention_amount":0,"txnId":"9a70ea0155268101001ba"},{"merchantKey":"P41sCK","amount":30,"subvention_amount":0,"txnId":"9a70ea0155268101001bb"},{"merchantKey":"sd3fsmr","amount":20,"subvention_amount":0,"txnId":"9a70ea0155268101001b"}]}
)
```

#### **Convenience fee model**

The formatted response for the above sample request is similar to the following:

```plaintext
Array
(
    [mihpayid] => 41**45678912383977
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => Ax4j7J
    [txnid] => 9a70ea0155268101001b
    [amount] => 110.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 110
    [addedon] => 2021-12-22 19:02:15
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
    [hash] => 6e700275583072c0361bac771a4166a4be5334112d59e40181c5668895c477a047c7be250068186fd26ca72928d7e168f92bb96003a7fffbf4933bb818f4c48a
    [field1] => 5582299554914671900181
    [field2] => 113476
    [field3] => 110.00
    [field4] => 41**45678912383977
    [field5] => 100
    [field6] => 02
    [field7] => AUTHPOSITIVE
    [field8] => 
    [field9] => Transaction is Successful
    [payment_source] => payu
    [PG_TYPE] => AxisCYBER
    [bank_ref_num] => 5582299554914671900181
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => Test User
    [cardnum] => 512345XXXXXX2346
    [cardhash] => This field is no longer supported in postback params.
    [splitInfo] => {"splitStatus":"success","splitSegments":[
				{"merchantKey":"P41sCY","amount":50,"subvention_amount":0,"txnId":"9a70ea0155268101001ba, “discount":0,"additionalCharges":0,”transaction_fee":0”},
				{"merchantKey":"P41sCK","amount":30,"subvention_amount":0,"txnId":"9a70ea0155268101001bb, “discount”:0,"additionalCharges":0,"transaction_fee":0"}
				,{"merchantKey":"sd3fsmr","amount":20,"subvention_amount":0,"txnId":"9a70ea0155268101001b, “discount”:0,"additionalCharges":10,"transaction_fee":0"}
				]
   			}
)
```