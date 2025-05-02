---
title: Integration APIs for Maximizer
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
The **\_payment** APIs are used to integrate <Glossary>Maximizer</Glossary>. For more information, refer to the following APIs under API Reference:

* [Collect Payment API - PayU Hosted](ref:_payment_payu_hosted_checkout)
* [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted)
* [Collect Payment API - Server-to-Server](ref:_payment_server_to_server)

> 📘 Notes:
>
> The transaction routed to which aggregator will be identified by the parameter **pa\_name** in the transaction response. Also on dashboard merchant can view the aggregator name in transaction list and view details. For example, transaction routed through PayU, UDF will have PayU. Similarly, UDF contains corresponding aggregator name for Razorpay, BillDesk, Pinelabs and Paytm. For more information, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis#from-other-payment-aggregator-using-maximiser). The sample response is similar to the following:
>
> ```
> (
>     [mihpayid] => 19855444473
>     [mode] => DC
>     [status] => success
>     [unmappedstatus] => captured
>     [key] => mBWD5W
>     [txnid] => fb1329207367842ddfa3d
>     [amount] => 2.00
>     [cardCategory] => domestic
>     [discount] => 0.00
>     [net_amount_debit] => 2
>     [addedon] => 2024-05-10 11:50:19
>     [productinfo] => Product Info
>     [firstname] => Payu-Admin
>     [lastname] => 
>     [address1] => 
>     [address2] => 
>     [city] => 
>     [state] => 
>     [country] => 
>     [zipcode] => 
>     [email] => test@example.com
>     [phone] => 1234567890
>     [udf1] => 
>     [udf2] => 
>     [udf3] => 
>     [udf4] => 
>     [udf5] => 
>     [udf6] => 
>     [udf7] => 
>     [udf8] => 
>     [udf9] => 
>     [udf10] => 
>     [hash] => c82ae4a92f52e8cfa7397d1ec787b830e7115ececbe8aab301df3700e96aae8a4d893ff79a92c676c1fd3bc8c41cdf33231c9670a63e5995bb950d6147b33e2c
>     [field1] => 
>     [field2] => 0
>     [field3] => 
>     [field4] => 
>     [field5] => RazorPay
>     [field6] => pay_O8gqNOgWN5jeJa
>     [field7] => {"acquirer_payment_id":{},"amount":{},"amount_orig":{},"authorization_staus":{},"bank_code":{},"bank_ref_no":{},"cardmasked":{},"currency":{},"customer_email":{},"customer_name":{},"customer_phone":{},"description":{},"error_desc":{},"order_id":{},"payment_channel":{},"payment_datetime":{},"payment_mode":{},"response_code":{},"response_message":{},"tax_on_tdr_amount":{},"tdr_amount":{},"transaction_id":{},"udf1":{},"udf2":{},"udf3":{},"udf4":{},"udf5":{}}
>     [field8] => 
>     [field9] => Transaction Completed Successfully
>     [payment_source] => payu
>     [pa_name] => RazorPay
>     [PG_TYPE] => DC-PG
>     [bank_ref_num] => RPMASDF888D078DF6
>     [bankcode] => MAST
>     [error] => E000
>     [error_Message] => No Error
>     [cardnum] => XXXXXXXXXXXX0231
>     [cardhash] => This field is no longer supported in postback params.
>     [corporate_card] => 0
>     [cobranded_card] =>
> ```