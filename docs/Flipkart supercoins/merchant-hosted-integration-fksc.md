---
title: Merchant Hosted Integration
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: understanding-refunds-fksc
      title: Understanding Refunds
    - type: basic
      slug: customer-journey-for-fksc
      title: Customer Journey for FKSC
---
You can collect payments from customers by redeeming their Flipkart Supercoins (FKSC) using the Merchant Hosted Checkout integration.

When your customer makes a payment by redeeming their SuperCoins, you can check the SuperCoins balance using the **Supercoins Balance** API and then initiate payment. You need to ensure that **LR** for the **pg** parameter and **FKSC** for the **bankcode** parameter is posted as mentioned in  [Collect Payment API - Merchant Hosted](ref:_payment_merchant_hosted).

***

## Step 1: Check the SuperCoins Balance

Use the following APIs under API Reference to check the SuperCoins balance:

- [Send OTP API](ref:send-otp-api-fksc)
- [Verify Token API](ref:verify-token-api-fksc)
- [Get SuperCoins Balance API](ref:get-supercoins-balance-api)

> 📘 **Notes:**
> 
> - The **Send OTP** and **Verify OTP** APIs for Flipkart Supercoins will be used only for the first time when the customer logs in using the mobile number associated with  Flipkart. After the OTP validation is successful, PayU responds to the merchant with a token. The merchant must save this token and must be used in repeat flows when the same customer uses Flipkart Supercoins for payments.
> - Merchant has to create screens to accept their customer’s mobile number to send the OTP using the **Send OTP** API and authenticate the OTP using the **Verify OTP** API.

***

## Step 2: Initiate the Payment

### Post Request Syntax & Composition

Markup

\<body>

\<form _action_\='<https://test.payu.in/_payment'> _method_\='post'>

\<input _type_\="hidden" _name_\="key" _value_\="JP\*\*\*g" />

\<input _type_\="hidden" _name_\="txnid" _value_\="t6svtqtjRdl34W" />

\<input _type_\="hidden" _name_\="productinfo" _value_\="iPhone" />

\<input _type_\="hidden" _name_\="amount" _value_\="1000" />

\<input _type_\="hidden" _name_\="email" _value_\="[test@gmail.com](mailto:test@gmail.com)" />

\<input _type_\="hidden" _name_\="firstname" _value_\="Ashish" />

\<input _type_\="hidden" _name_\="lastname" _value_\="Kumar" />

\<input _type_\="hidden" _name_\="pg" _value_\="LR" />

\<input _type_\="hidden" _name_\="bankcode" _value_\="FKSC" />

\<input _type_\="hidden" _name_\="surl" _value_\="your own success url" />

\<input _type_\="hidden" _name_\="furl" _value_\="your own failure url" />

\<input _type_\="hidden" _name_\="phone" _value_\="9988776655” />

\<input type="_hidden"_ _name_\="hash" _value_\="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />

\<input _type_\="submit" _value_\="submit"> \</form>

\</body>

\</html>

**Note:** The above HTML code block is for Merchant Checkout integration on the SuperCoins call for the test environment.

### Request Parameters for Transaction Request

Along with the mandatory parameters mentioned in [Collect Payment API - Merchant Hosted](ref:_payment_merchant_hosted), you must post the following parameters for the Flipkart Supercoins:

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "pg  \n**mandatory**",
    "0-1": "`String` It defines the payment category using the Merchant Hosted Checkout integration. For a FKSC redemption, \"LR\" must be specified in the **pg** parameter.",
    "0-2": "LR",
    "1-0": "bankcode  \n**mandatory**",
    "1-1": "`String` Pass the values as **FKSC** for Flipkart Supercoins redemption.",
    "1-2": "FKSC"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### Sample Request

```curl
curl -XPOST -H 'content-type: application/x-www-form-urlencoded' -d 'hash=015c45945db5cf29d4253e148d0cecbd136eabe40aea64b38afc8704b5ffb0daae07e3cc95c21e77d843dac6400ec40a42a417efd84cd15eaa896bcd5324f7e2&key=J*****g&txnid=c4af13d516044e22e251&version=&api_version=1&pre_init_mode=0&amount=10&additional_charges=&firstname=Payu-Admin&salt_version=1&email=test%40example.com&phone=1234567890&productinfo=Product+Info&user_credentials=&surl=https%3A%2F%2Fpp225admin.payu.in%2Ftest_response&txtid=afb82b0dc86628a66f7fc4eb5b166786&furl=https%3A%2F%2Fpp225admin.payu.in%2Ftest_response&panNumber=&notifyurl=https%3A%2F%2Fpp225admin.payu.in%2Ftest_notification.php&percentage_additional_charges=&codurl=https%3A%2F%2Fpp225admin.payu.in%2Ftest_response&ipurl=https%3A%2F%2Fpp225admin.payu.in%2Ftest_response&miles=&pubkey=&lastname=&curl=&address1=&address2=&shipping_firstname=&shipping_lastname=&shipping_address1=&shipping_address2=&shipping_city=&shipping_state=&shipping_country=&shipping_zipcode=&shipping_phone=&city=&state=&country=&zipcode=&nsc=&enforce_paymethod=&drop_category=&offer_key=&service_provider=&user_token=&cart_details=&offer_auto_apply=&note_category=&custom_note=&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&base_payuid=&base_merchantid=&vendor_id=&service_provider=&one_click=&si=&subscriptionId=&free_trial=&twid_customer_hash=&visaabpdetails=&force_pgid=&app_id=&beneficiarydetail=&gstParams=&paisa_mecode=&device_type=&instrument_type=&instrument_id=&ismobileview=&card_merchant_param=&retry_payuids=&boltEnabled=&s2s_client_ip=&s2s_device_info=&html=&sdktoken=&snooze=0&transactionContext=&device_context=&sdk_flow_type=&sdk_platform=&sdk_retry=&loan_id=&acquiring_bin=&mcpLookupId=&pg=LR&bankcode=FKSC&subvention_amount=&subvention_eligibility=&ccnum=5123456789012346&ccname=Test+User&ccvv=123&storecard_token_type=&additional_info=&ccexpmon=05&ccexpyr=2025&otp=123456&store_card_token=&store_card=&card_name=&txn_s2s_flow=&decoded_s2s_response=&authentication_flow=&authentication_info=&tokenService=&pre_authorize=&skip3ds=&auth_only=&termUrl=&is_atm_pin=&vpa=&vpa_phone=&merchant_data=&dm_fp_session=&callId=&skipcvv=&citi_reward=&source_id=&three_DS2_request_data=&save_sodexo_card=&is_check_balance=&si_details=&tools_txn_type=&one_click_details=&splitRequest=&moneyMerchantName=&moneyWebsiteUrl=&offer_product_id=&offer_brand_id=&payoutdetails=&upi_custom_note=&icp_type='
```

### Sample Response

The following is the sample response from PayU for Merchant Hosted Checkout. For the description of the response parameters, refer to [Collect Payment API - Merchant Hosted](ref:_payment_merchant_hosted).

```
Array
(
    [mihpayid] => 403993715523409521
    [mode] => LR
    [status] => success
    [unmappedstatus] => captured
    [key] => JP***g
    [txnid] => 5jJ9xYceXX1ydT
    [amount] => 1000.00
    [discount] => 0.00
    [net_amount_debit] => 1000
    [addedon] => 2021-07-02 15:03:50
    [productinfo] => iPhone
    [firstname] => PayU User
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
    [hash] => 716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
    [field1] => 9876543210
    [field2] => 5jJ9xRceXX1ydT
    [field3] => 
    [field4] => PayU User
    [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
    [field6] => 
    [field7] => Transaction completed successfully
    [field8] => 
    [field9] => Transaction completed successfully
    [payment_source] => payu
    [PG_TYPE] => LR-PG
    [bank_ref_num] => 5jJ9xRceXX1ydT
    [bankcode] => FKSC
    [error] => E000
    [error_Message] => No Error
)

```