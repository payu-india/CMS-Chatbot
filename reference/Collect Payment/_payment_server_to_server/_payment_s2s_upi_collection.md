---
excerpt: ''
api:
  file: merchant-hosted-36.json
  operationId: S2S-UPICollection
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - slug: upi-collection-s2s
      title: UPI Collection S2S Integration
      type: basic
---
This section provides the request and response parameters used in Step 1 of [UPI Collection S2S Integration](doc:upi-collection-s2s). You can get the sample request and response when use the "Try It" experience. For the complete integration steps, refer to [UPI Collection S2S Integration](doc:upi-collection-s2s).

> 📘 **Reference**:&#x20;
>
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

<br />

> 👍 Zero-coding integration into your website:
>
> Experience the end-to-end **Merchant Hosted Checkout** > **UPI** flow and instantly generate the complete code for seamless, zero-coding integration into your website.
>

<HTMLBlock>{`
                                      <style>
                                      .tooltip-btn {
                                          position: relative;
                                          background-color: #4CAF50;
                                          color: white;
                                          padding: 10px 20px;
                                          border: none;
                                          border-radius: 5px;
                                          cursor: pointer;
                                          font-weight: bold; /* Added this line */
                                      }
                                      .tooltip-btn:hover::after {
                                          content: attr(data-tooltip);
                                          position: absolute;
                                          bottom: 125%;
                                          left: 50%;
                                          transform: translateX(-50%);
                                          background-color: #333;
                                          color: white;
                                          padding: 5px 10px;
                                          border-radius: 4px;
                                          white-space: nowrap;
                                          font-size: 12px;
                                          z-index: 1;
                                      }
                                      </style>

                                      <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-upiflow', '_blank')" 
                                              class="tooltip-btn" 
                                              data-tooltip="Click here to see the Merchant Hosted Checkout > UPI end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                                          Experience the flow and get the code
                                      </button>
`}</HTMLBlock>

<br />

<Additional_paymentRequestParams />

<Accordion_Collect_Fraud_Detection />

<Accordion title="Sample request" icon="fa-code">
  ```curl
    curl --location 'https://test.payu.in/_payment' \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'key=PRiQvJ' \
   --data-urlencode 'txnid=my_order_991' \
   --data-urlencode 'amount=1' \
   --data-urlencode 'productinfo=my_order_991' \
   --data-urlencode 'email=' \
   --data-urlencode 'phone=9368252248' \
   --data-urlencode 'txn_s2s_flow=4' \
   --data-urlencode 'hash=||||||ABCDE1234F||1990-01-01||INV123456||||||' \
   --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
   --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
   --data-urlencode 'udf1=buyer'\''s DOB' \
   --data-urlencode 'udf2=' \
   --data-urlencode 'udf3=buyer'\''s PAN' \
   --data-urlencode 'udf4=' \
   --data-urlencode 'udf5=invoice number' \
   --data-urlencode 's2s_client_ip=10.200.12.12' \
   --data-urlencode 's2s_device_info=1_|_4' \
   --data-urlencode 'firstname=' \
   --data-urlencode 'lastname=kr' \
   --data-urlencode 'address1=308,third floor' \
   --data-urlencode 'address2=testing' \
   --data-urlencode 'city=Gurugram' \
   --data-urlencode 'state=UP' \
   --data-urlencode 'country=India' \
   --data-urlencode 'zipcode=122018' \
   --data-urlencode 'pg=UPI' \
   --data-urlencode 'bankcode=INTENT' \
   --data-urlencode 'upiAppName=gpay' \
   --data-urlencode 'udf_params={"udf7":"asdf","udf8":"12"}' \
   --data-urlencode 'buyer_type_business=1'
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

  <Accordion title="Additional Info for Request Parameters" icon="fa-code">
| `upiAppName`<br/>_mandatory_ | Any of the values listed under the [upiAppName list](#upiAppName-list) | amazonpay |
| `s2s_device_info`<br/>_conditional_ | `String` Customer agent's device information. For the list of accepted values, refer to [s2s\_device\_info Values Description](#s2s_device_info-values-description) table<br/>**Note**: This Required for UPI Intent flow. | 1\_\|\_0 for mobile browser|

###  upiAppName eNum List
  <Accordion title="UPI App Name List" icon="fa-list">
The following are the enum's expected for UPI apps:
- phonepe
- googlepay
- paytm
- bhim
- cred
- amazonpay
- whatsapp
- adityabirla
- bajajfinserv
- bankofindiaomnineo
- bharatpe
- bhimdlbupi
- canaraai1pe
- cheq
- credilio
- curiemoney
- ebixcash
- famappbytrio
- flipkart
- freo
- gomobile
- groww
- herofincorp
- idfcmobilebankingapp
- imobilebyicicibank
- indmoney
- iris
- jar
- jiofinance
- jumpp
- jupiter
- kiwi
- kreditbee
- kreditpe
- lxme
- mobikwik
- moneyview
- mufin
- myairtel
- navi
- omnicard
- onecard
- paynearby
- pinelabsplusplay
- popclub
- pzw
- rediff
- revolut
- rio
- salaryse
- samsungpay
- scapia
- shriramone
- slice
- stashfin
- supermoney
- tataneu
- timepay
- twidpay
- yespaynext
- zet
- genericintent – For any other app apart from
above
</Accordion>
#### s2s_device_info Values Description 
 <Accordion title="s2s_device_info Values" icon="fa-list">
| Value | Description |
|-------|-------------|
| 0\_\|\_0 | web |
| 0\_\|\_1 | web |
| 0\_\|\_4 | web |
| 1\_\|\_0 | mobile browser |
| 1\_\|\_2 | tablet |
| 1\_\|\_3 | iOS App |
| 1\_\|\_4 | Android App |
</Accordion>
  </Accordion>

> ❗️
>
> **Error handling**: If any error message is displayed with an error code, refer to the <a href="error-codes" target="_blank">Error Codes</a> section to understand the reason for these error codes.

> 🚧
>
> **Values to be used in Test environment**: For values to be used in Test environment, refer to <a href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets#web-checkout" target="_blank">Test Cards</a>.

<br />