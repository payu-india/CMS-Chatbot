---
excerpt: ''
api:
  file: merchant-hosted-36.json
  operationId: S2S-UPICollection
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: upi-collection-s2s
      title: UPI Collection S2S Integration
---
This section provides the request and response parameters used in Step 1 of [UPI Collection S2S Integration](doc:upi-collection-s2s). You can get the sample request and response when use the "Try It" experience. For the complete integration steps, refer to [UPI Collection S2S Integration](doc:upi-collection-s2s).

<Callout icon="📘" theme="info">
  **Reference**: For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Callout>

<br />

<Cards_PayU_Labs />

<br />

<Additional_paymentRequestParams />

<Accordion_Collect_Fraud_Detection />

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
  --data-urlencode 'hash=YOUR_CALCULATED_HASH'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
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

## Response parameters

For the response parameters, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

## Request parameters

<Callout icon="❗️" theme="error">
  **Error handling**: If any error message is displayed with an error code, refer to the <a href="error-codes" target="_blank">Error Codes</a> section to understand the reason for these error codes.
</Callout>

<Callout icon="🚧" theme="warn">
  **Values to be used in Test environment**: For values to be used in Test environment, refer to <a href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets#web-checkout" target="_blank">Test Cards</a>.
</Callout>
