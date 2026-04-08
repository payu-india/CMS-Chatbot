---
title: CB -UPI
api:
  file: cb_merchant_hosted_upi.json
  operationId: MerchantHostedCheckout-UPI
hidden: false
link:
  new_tab: false
metadata:
  title: 'Collect Payment API using UPI - Merchant Hosted with Cross-Border Payments '
---
PayU allows you to collect payments using UPI handles. For the list of UPI providers supported, refer to [UPI Handles](doc:upi-handles). The **buyer_type_business** parameter is used for Cross Border payment transactions to indicate the type of business of the buyer.

After the payment is complete, you must use the [Invoice Upload API](ref:invoice_upload_api) to upload invoices / AWBs (Air-way bill number). AWB details are mandatory for Goods transactions.

<Callout icon="📘" theme="info">
  **Reference**: For steps to integrate UPI for Cross-Border Payments, refer to [[S2S] UPI Consent Transaction - Cross Border](doc:upi-consent-transaction-cb)
</Callout>

## Recommended prerequisite before initiating payment

When your customer makes payment through UPI, you can validate the customer's Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle.

Validate the VPA (UPI handle) using the **validateVpa** API. For more information, refer to [Validate VPA Handle API](ref:validate_vpa_api).

## Environment

| Environment                | URL                                                                |
| :------------------------- | :----------------------------------------------------------------- |
| **Test Environment**       | [https://test.payu.in/_payment](https://test.payu.in/_payment)     |
| **Production Environment** | [https://secure.payu.in/_payment](https://secure.payu.in/_payment) |

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location --request POST 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JPM7Fg' \
  --data-urlencode 'txnid=payuTestTransaction12345' \
  --data-urlencode 'amount=100.00' \
  --data-urlencode 'firstname=Ashish' \
  --data-urlencode 'email=test@payu.in' \
  --data-urlencode 'phone=9988776655' \
  --data-urlencode 'productinfo=Product Info' \
  --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'pg=UPI' \
  --data-urlencode 'bankcode=INTENT' \
  --data-urlencode 'txn_s2s_flow=4' \
  --data-urlencode 's2s_client_ip=10.200.12.12' \
  --data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0' \
  --data-urlencode 'udf1=AELPR1234E' \
  --data-urlencode 'udf3=02-02-1980' \
  --data-urlencode 'udf4=XYZ Pvt. Ltd.' \
  --data-urlencode 'udf5=INV123456' \
  --data-urlencode 'buyer_type_business=1' \
  --data-urlencode 'udf_params={"udf7":"0100000029","udf8":"99953729071"}' \
  --data-urlencode 'hash=YOUR_CALCULATED_HASH'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  Collect the response in the  [UPI Collection - S2S](ref:_payment_s2s_upi_collection). under API Reference.  For description of response parameters, refer to [Additional Info for Payment APIs.](ref:addl_info-payment-apis#response-for-initial-server-to-server-request)

  <Accordion title="Using the IntentURIData value in response" icon="fa-code">
    The **IntentURIData** parameter returns the URI in the response. For example, it contains the first debit amount .

    > 📘 Notes:
    >
    > * Every time there is a change, you need to incorporate the changes to avoid breaking the transactions.
    > * The **tid** value which is passed in the intent URI acts as a validation check at NPCI's end which do not allow duplicate transaction.
    > * The tr value not necessary and it is a payU\_id. It can be any reference id for PayU's internal reconciliation.
  </Accordion>

  **Parsed response**

  ```json
  { 
    "rawBankData" : ""  
    "referenceId":  "00c44a4c8306f9cbe5ecf6133afe08a7" 
    "bankData" : { 
    "referenceId": "00c44a4c8306f9cbe5ecf6133afe08a7", 
    "messageDigest": "c2e9e456037f033e5cc3d7b6e556189adf41eeabf706844dff70aac91f6b8e73bb1846286c8f99ea768cf38f7c12369c|523727493647950f32684bd6f1ab07aa6474016f", 
    "pares": "eNrVmdeS47i2pl+lo8+loje968jOCHojGtGLvKM3opHoyacfZmZVde06PWfOzMXEjCIUgkBiYRHAWv8H4s0phyzj7CyZh+z9TcvGMSqy36r0r99jFAfhGIT/gLE8/QNNM/IPEiGoP5CUgGEwAjGCSH9/f7vRVjZ+NvgsnTVLNoxV371D/wL/Bb8B3/+exoekjLrp/S1KXoysv6MkQhHYG/Dt71ubDTL3DkMwhZIgRoIIAoL4G/BV/Qb83f42f5TG0+GtSt9Dp5gMTkMMGzxCLtm1mik1zkV02PzrDfi44y2NpuwdBuHTNgj9BiF/IsSfyOnbZ/3b88Mc3fbzaRuCwDfg54q3c2SGrEv2dwQ7nfnx7y3bnn2XnXecdn6U34C/fXtG3Tv40wcFQeK0fda+Off3t6lqf/YJ/RMi/4ShN+Cz/m2comme34M34FvpLYmW5Z2maYYVTJqWzadhJqu+0t8/57N+3vKWJdU7eA7rx+9nK7op+qGayvbD1X+veAM+XAE+p+79za6K7uxsyH7b2qYb//q9nKbnnwCwruu/VuRf/VAA8PkgAEgB5w3pWBX/8ftXqyyVu7z/32rGRl3fVUnUVEc0nQtEy6ayT3/74ds/mXGsD0sQYPHsH6epPxII7f74qAERCDttAv9s9Kcn++/08quzwxj9MZYR9NHBL4be36wszz5WRPaba8l//f4f36OAq4psnP5Puvve1c8WvtvzombO3mc3DXRwZEp92R+80+1LH1P8RNQ4/9f3dl93vgE//Pvm/NdM/TQiXzc6RMf6GG04qXdxrxgV1PAQ4FJa38tkuNT", 
    "additionalInfo": 
    { 
        "authUdf1": "", 
        "authUdf2": "", 
        "authUdf3": "", 
        "authUdf4": "", 
        "authUdf5": "", 
        "authUdf6": "", 
        "authUdf7": "", 
        "authUdf8": "", 
        "authUdf9": "", 
        "authUdf10": "" 
    } 
  }, 
    "authenticationStatus"  :  "success", 
    "hash" : "664b8ddd1b5b2d1b68abb7eee5ea6e001a02773499ddcd86956ba0833315e7d4e69c641d7b0b3e7590532e21e71936da173f4eda716fc09f83cd1117f0d0c37c"} 
  ```
</Accordion>

## Request parameters

<details>
  <summary>Additional info for request parameters</summary>

  ### Payment Request Parameters

  The payment request parameters include standard fields like key, txnid, amount, firstname, email, phone, and productinfo. For UPI payments, the following specific parameters are important:

  * **pg**: Set to "UPI" to indicate UPI payment method
  * **bankcode**: Set to "UPI" for UPI transactions
  * **vpa**: The Virtual Payment Address (UPI ID) of the customer

  For a comprehensive list of all parameters and their descriptions,  refer to the following:
</details>

<Callout icon="📘" theme="info">
  **Reference:** For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Callout>

<Callout icon="🚧" theme="warn">
  **Testing UPI:** You can test UPI only with the anything@payu or [9999999999@payu.in](mailto:9999999999@payu.in) as VPA.
</Callout>

<Callout icon="❗️" theme="error">
  **Error handling:** If any error message is displayed with an error code, refer to the [Error Codes](ref:error-codes) section to understand the reason for these error codes.
</Callout>