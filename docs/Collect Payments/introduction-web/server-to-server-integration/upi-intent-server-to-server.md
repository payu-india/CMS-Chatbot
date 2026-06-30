---
title: UPI Intent Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section includes the workflow and steps to integrate UPI Intent with Server-to-Server integration.

<NPCI_Mandate />

> 👍 Note: &#x20;
>
> Experience the end-to-end **Merchant Hosted Checkout** > **UPI** flow and instantly generate the complete code for seamless, zero-coding integration into your website.
>
>
>
> <HTMLBlock>{`
>                             <style>
>                             .tooltip-btn {
>                                 position: relative;
>                                 background-color: #4CAF50;
>                                 color: white;
>                                 padding: 10px 20px;
>                                 border: none;
>                                 border-radius: 5px;
>                                 cursor: pointer;
>                                 font-weight: bold; /* Added this line */
>                             }
>                             .tooltip-btn:hover::after {
>                                 content: attr(data-tooltip);
>                                 position: absolute;
>                                 bottom: 125%;
>                                 left: 50%;
>                                 transform: translateX(-50%);
>                                 background-color: #333;
>                                 color: white;
>                                 padding: 5px 10px;
>                                 border-radius: 4px;
>                                 white-space: nowrap;
>                                 font-size: 12px;
>                                 z-index: 1;
>                             }
>                             </style>
>
>                             <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-upiflow', '_blank')" 
>                                     class="tooltip-btn" 
>                                     data-tooltip="Click here to see the Merchant Hosted Checkout >  UPI end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
>                                 Experience the flow and get the code
>                             </button>
> `}</HTMLBlock>

## Smart Intent Flow

### Workflow


<Image src="https://files.readme.io/991937481c8ab71eeb4f5f1477eb18e5bac248eb65d8ea924ed51705b520bb6f-UPI_One_time_Intent_-_Android_App_Non_SDK_Solution.png" align="center" />


### Steps to integrate

<Accordion title="Update Manifest File [One-Time]" icon="fa-code">
  Add package ids in your apps manifest file to allow your application to access apps installed on the customer's device. This is required for Android 11 and above.

  ```
   <queries>
          <package android:name="in.amazon.mShop.android.shopping"/>
          <package android:name="com.upi.axispay"/>
          <package android:name="com.axis.mobile"/>
          <package android:name="com.fisglobal.bandhanupi.app"/>
          <package android:name="com.bankofbaroda.upi"/>
          <package android:name="in.org.npci.upiapp"/>
          <package android:name="com.canarabank.mobility"/>
          <package android:name="com.citiuat"/>
          <package android:name="com.dbs.in.digitalbank"/>
          <package android:name="com.olive.dcb.upi"/>
          <package android:name="com.finopaytech.bpayfino"/>
          <package android:name="com.freecharge.android"/>
          <package android:name="com.google.android.apps.nbu.paisa.user"/>
          <package android:name="com.snapwork.hdfc"/>
          <package android:name="com.mgs.hsbcupi"/>
          <package android:name="com.csam.icici.bank.imobile"/>
          <package android:name="com.icicibank.pockets"/>
          <package android:name="com.euronet.iobupi"/>
          <package android:name="com.mgs.induspsp"/>
          <package android:name="com.fss.jnkpsp"/>
          <package android:name="com.jio.myjio"/>
          <package android:name="com.mycompany.kvb"/>
          <package android:name="com.kvb.mobilebanking"/>
          <package android:name="com.lcode.smartz"/>
          <package android:name="com.msf.kbank.mobile"/>
          <package android:name="com.upi.federalbank.org.lotza"/>
          <package android:name="com.infrasofttech.mahaupi"/>
          <package android:name="com.mipay.in.wallet"/>
          <package android:name="com.myairtelapp"/>
          <package android:name="com.mobikwik_new"/>
          <package android:name="com.onymy.paybee.prod"/>
          <package android:name="net.one97.paytm"/>
          <package android:name="com.phonepe.app"/>
          <package android:name="com.Version1"/>
          <package android:name="com.samsung.android.spay"/>
          <package android:name="com.sbi.upi"/>
          <package android:name="com.SIBMobile"/>
          <package android:name="com.truecaller"/>
          <package android:name="com.infrasoft.uboi"/>
          <package android:name="com.lcode.ucoupi"/>
          <package android:name="com.YesBank"/>
          <package android:name="com.dreamplug.androidapp"/>
          <package android:name="money.bullet"/>
      </queries>
  ```

  <br />
</Accordion>

<Accordion title="Step 1: Fetch the List of UPI and Smart Intent Supported Apps" icon="fa-code">
  List the specific apps for app/webview/m-web, (In IOS, UPI collect can still be used).
</Accordion>

<Accordion title="Step 2: Get Intent URI" icon="fa-code">
  Use the **\_payment** API to get Intent URI and transaction details for the UPI app selected by the customer. For more information, refer to <Anchor label="Collect Payment API > UPI Collection with S2S Integration" target="_blank" href="https://docs.payu.in/docs/upi-intent-server-to-server">UPI Intent with S2S Integration</Anchor>.

  <Accordion title="Request Parameters" icon="fa-table">
<HTMLBlock>
{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>key<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Merchant key provided by PayU during onboarding.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>JPg****f</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>txnid<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>ypl938459435</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The payment amount for the transaction.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>10.00</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>productinfo<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> A brief description of the product.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>iPhone</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>firstname<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The first name of the customer.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Ashish</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>lastname<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The last name of the customer.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Kumar</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>email<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The email address of the customer.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>abc@payu.in</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>phone<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The phone number of the customer.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p></p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>address1<br/><code>optional but recommended for higher approval rate</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The first line of the billing address. H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai<br/><strong>Note</strong>: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>34 Saikripa-Estate, Tilak Nagar</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>address2<br/><code>optional but recommended for higher approval rate</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The second line of the billing address.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p></p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>city<br/><code>optional but recommended for higher approval rate</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The city where your customer resides as part of the billing address.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Mumbai</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>state<br/><code>optional but recommended for higher approval rate</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The state where your customer resides as part of the billing address.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Maharashtra</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>country<br/><code>optional but recommended for higher approval rate</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The country where your customer resides.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>India</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>zipcode<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Billing address zip code is mandatory for the cardless EMI option. Character Limit-20</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>400004</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>pg<br/><code>mandatory for seamless/s2s flow</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> It defines the payment category and post <strong>UPI</strong>.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>UPI</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>bankcode<br/><code>mandatory for seamless/s2s flow</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Each payment option is identified with a unique bank code at PayU. For UPI Autopay, post <strong>UPI</strong>.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>UPI</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>surl<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p></p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>furl<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The Failure URL, which is the page PayU will redirect to if the transaction is failed.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p></p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>vpa<br/><code>conditional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Customer's VPA handle. Mandatory for UPI Collect flow.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>customer@upi</code></p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>si<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Signifies successful consent taken from the user. Must be <code>1</code> for subscription setup.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>1</code></p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>si_details<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON String</code> JSON object containing mandate details (billingAmount, billingCurrency, billingCycle, etc.). Refer to si_details JSON Object below.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>See si_details accordion</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>upiAppName<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Any of the values listed under the <a href="#upiappname-enum-list">upiAppName list</a></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>amazonpay</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>txn_s2s_flow<br/><code>conditional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Integer</code> Parameter to enable S2S flow. Must be <code>4</code> for Legacy Decoupled flow (UPI Intent).</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>4</code></p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>s2s_client_ip<br/><code>conditional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Source IP of the customer. Required for UPI Intent flow.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>10.200.12.12</code></p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>s2s_device_info<br/><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Real customer User-Agent on payment for every S2S 4 txn initiated from backend. For more information, refer to <a href="#s2s_device_info-values-description">s2s_device_info Values Description</a> table.<br/><strong>Note</strong>: This is required for UPI Intent flow.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build, etc.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>udf1<br/><code>mandatory if AD bank request this detail</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the Buyer's PAN and date of birth in the following format (separated by two pipe characters): Buyer's PAN||Buyer's DOB</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>AAAPZ1234C||22/08/1972</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>udf3<br/><code>mandatory if AD bank request this detail</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the invoice ID of the transaction (generated by the merchant) and merchant name in the following format (separated by two pipe characters): Invoice ID||MerchantName</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>INV-123_1231||MerchantName</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>buyer_type_business<br/><code>optional in case of B2B transaction for cross-border payments</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Binary</code> To be sent as "1" in case the buyer is a business. In case of individual buyers, it can be skipped. Default is "0".<br/><strong>Note</strong>: This will be included in hash if posted (covered in next section)</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

####  upiAppName eNum List
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
| Customer environment | Example value (illustrative)                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------- |
| Android native app   | `Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/...)`                                                        |
| Android Chrome       | `Mozilla/5.0 (Linux; Android 13; ...) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/... Mobile Safari/537.36`   |
| iOS in-app / WebView | `Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148` |
| iOS Safari           | `Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) ... Version/17.4 Mobile/15E148 Safari/604.1`            |

  </Accordion>

  <Accordion title="Sample Request" icon="fa-code">
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
   --data-urlencode 's2s_device_info=s2s_device_info=Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/...)' \
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
</Accordion>

<Accordion title="Step 3: Retrieve Deeplink(uriIntentData) from the response," icon="fa-code">
  If metaData.unmappedStatus = pending, then get the result.intentURIData and add the prefix upi://pay?to make it to create a fully qualified deeplink to trigger the UPI App.
<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout** flow and instantly generate the complete code for seamless, zero-coding integration into your website. Navigate to **ACS Template Decoder** under **Tools & Utilities** to generate code for decoding the ACS template in the response:

  <HTMLBlock>{/*RDMX_HTMLBLOCK:CiAgICAgICAgICAgICAgICAgICAgICAgIDxzdHlsZT4KICAgICAgICAgICAgICAgICAgICAgICAgLnRvb2x0aXAtYnRuIHsKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBvc2l0aW9uOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJhY2tncm91bmQtY29sb3I6ICM0Q0FGNTA7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjb2xvcjogd2hpdGU7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwYWRkaW5nOiAxMHB4IDIwcHg7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBib3JkZXI6IG5vbmU7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBib3JkZXItcmFkaXVzOiA1cHg7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjdXJzb3I6IHBvaW50ZXI7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmb250LXdlaWdodDogYm9sZDsgLyogQWRkZWQgdGhpcyBsaW5lICovCiAgICAgICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICAgICAgICAgLnRvb2x0aXAtYnRuOmhvdmVyOjphZnRlciB7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjb250ZW50OiBhdHRyKGRhdGEtdG9vbHRpcCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwb3NpdGlvbjogYWJzb2x1dGU7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBib3R0b206IDEyNSU7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBsZWZ0OiA1MCU7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0cmFuc2Zvcm06IHRyYW5zbGF0ZVgoLTUwJSk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBiYWNrZ3JvdW5kLWNvbG9yOiAjMzMzOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgY29sb3I6IHdoaXRlOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgcGFkZGluZzogNXB4IDEwcHg7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBib3JkZXItcmFkaXVzOiA0cHg7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB3aGl0ZS1zcGFjZTogbm93cmFwOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgZm9udC1zaXplOiAxMnB4OwogICAgICAgICAgICAgICAgICAgICAgICAgICAgei1pbmRleDogMTsKICAgICAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgICAgICAgICA8L3N0eWxlPgoKICAgICAgICAgICAgICAgICAgICAgICAgPGJ1dHRvbiBvbmNsaWNrPSJ3aW5kb3cub3BlbignaHR0cHM6Ly9wYXl1LmluL2ludGVncmF0aW9ubGFiL3NlYW1sZXNzL2NhcmRzJywgJ19ibGFuaycpIiAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjbGFzcz0idG9vbHRpcC1idG4iIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRhdGEtdG9vbHRpcD0iQ2xpY2sgaGVyZSB0byBzZWUgdGhlIE1lcmNoYW50IEhvc3RlZCBDaGVja291dCBlbmQtdG8tZW5kIGludGVncmF0aW9uIGFuZCBpbnN0YW50bHkgZ2VuZXJhdGUgdGhlIGNvbXBsZXRlIGNvZGUgbmVlZGVkIGZvciBhIHplcm8tY29kaW5nIHNldHVwIG9uIHlvdXIgd2Vic2l0ZS4iPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgRXhwZXJpZW5jZSB0aGUgZmxvdyBhbmQgZ2V0IHRoZSBjb2RlCiAgICAgICAgICAgICAgICAgICAgICAgIDwvYnV0dG9uPgogIA==:RDMX_HTMLBLOCK*/}</HTMLBlock>
</Callout>

  ```json
  {
      "metaData": {
          "message": null,
          "referenceId": "c99a6455b3e0dc5cd7167ab8c8cc10d2fa153cb509e3f64c6cd0ed9c5b64a8c9",
          "statusCode": null,
          "txnId": "my_order_26075",
          "txnStatus": "pending",
          "unmappedStatus": "pending"
      },
      "result": {
          "paymentId": "403993715535965242",
          "merchantName": "Sudhanshu",
          "merchantVpa": "payutest@hdfcbank",
          "amount": "1.00",
          "intentURIData": "pa=payutest@hdfcbank&pn=Kumar&tr=403993715535965242&tid=PPPL403993715535965242080126220900&am=1.00&cu=INR&tn=UPIIntent",
          "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vdGVzdC5wYXl1LmluL2M5OWE2NDU1YjNlMGRjNWNkNzE2N2FiOGM4Y2MxMGQyYzgzYTk5NmFhNDhiYTk4MmZjMGQ4MTI1MGY1ODgxZjMvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0b2tlbiIgdmFsdWU9IjhERDNFRUFFLUI5NTktQzY1RS03MDczLTYzQTNGQUUxMjZGRiI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYW1vdW50IiB2YWx1ZT0iMS4wMCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0ibWlocGF5aWQiIHZhbHVlPSJjOTlhNjQ1NWIzZTBkYzVjZDcxNjdhYjhjOGNjMTBkMmZhMTUzY2I1MDllM2Y2NGM2Y2QwZWQ5YzViNjRhOGM5Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJkaXNhYmxlSW50ZW50U2VhbWxlc3NGYWlsdXJlIiB2YWx1ZT0iMCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVWcGEiIHZhbHVlPSJwYXl1dGVzdEBoZGZjYmFuayI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVOYW1lIiB2YWx1ZT0iU3VkaGFuc2h1Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJhZGRpdGlvbmFsQ2hhcmdlcyIgdmFsdWU9IjAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InRyYW5zYWN0aW9uRmVlIiB2YWx1ZT0iMS4wMCI+PC9mb3JtPjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0Jz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5vbmxvYWQ9ZnVuY3Rpb24oKXsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb2N1bWVudC5mb3Jtc1sncGF5bWVudF9wb3N0J10uc3VibWl0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvc2NyaXB0PjwvYm9keT48L2h0bWw+",
          "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
      }
  }
  ```
</Accordion>

<Accordion title="Step 4: Set the Package Name" icon="fa-code">
  Set the packageName as per the app selected by the customer on your checkout page. and start the activity.

  ```java
  fun makePayment(packageName: String,mActivity: Activity,intentUri:String) {
        val i = Intent()
        i.setPackage(packageName)
        i.action = Intent.ACTION_VIEW
        i.data = Uri.parse("upi://pay" + intentUri)
        if (null != mActivity && !mActivity.isFinishing() && !mActivity.isDestroyed()) {
            mActivity.startActivityForResult(i, 101)
        }
    }
  ```
</Accordion>

<Accordion title="Step 5: Handle the response" icon="fa-code">
  Once the user completes the payment the UPI app will be closed, and then handle the response onActivityResult.

  ```java
  override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == 101) {
            data?.getStringExtra("Status")?.let { Log.d("result", it) }
            data?.getStringExtra("response")?.let { Log.d("response", it) }
            //get Status
            //if Status == Success
            // Call Verify Payemnt//
        }
  }
  ```
</Accordion>

<Accordion title="Step 6: Verify the payment" icon="fa-code">
  <Verify_Payment_Tabs />
</Accordion>

## Specific Intent Flow

> 📘
>
> **Notes**: Specific Intent flow works with m-web, Webview, Android or iOS apps. As per **NPCI** mandate, **Pay by any UPI App** option must be shown by all the merchants in their app on all Android devices (app/m-web/webview), Use the generic deeplink, without specific `packageName` to trigger the Pay by any UPI app.

### Workflow


<Image src="https://files.readme.io/b1767cf25bf9c6ca94e7cbf0de8ef28e2518ade4919b5df5f6d6ad41537ba1fd-UPI_One_time_Intent_-_m-web_or_IOS_App.png" align="center" />


### Steps to Integrate

<Accordion title="Step 1: Fetch the List of UPI and Smart Intent Supported Apps" icon="fa-code">
  You need to get the list of UPI and smart intent supported applications installed in the device.

  ```java
  private fun getSmartIntentUPIApps(context: Context?):ArrayList<HashMap<String,String>>?{
        val upiApps = ArrayList<HashMap<String, String>>()
        if (context == null)
            return null

        val intent = Intent()
        intent.data = Uri.parse("upi://pay")
        val activityList = context.packageManager.queryIntentActivities(intent, PackageManager.MATCH_DEFAULT_ONLY)
        for (resolveInfo in activityList){
            var packageInfo: PackageInfo? = null
            try {
                packageInfo = context.packageManager
                    .getPackageInfo(resolveInfo.activityInfo.packageName, 0)
                val name =
                    context.packageManager.getApplicationLabel(packageInfo.applicationInfo) as String
              val appInfo = HashMap<String, String?>()
                appInfo["bankName"] = name ?: "NA"
                appInfo["packageName"] = packageInfo.packageName
                upiApps.add(appInfo)
            } catch (e: PackageManager.NameNotFoundException) {
                e.printStackTrace()
                return upiApps
            }
        }
        return UPI apps
    }
    /* to get icon of psp app*/
    fun getUpiAppBitmap(context: Context?, packageName: String): Bitmap? {

        var upiAppBitmap: Bitmap? = null
        if (context == null)
            return upiAppBitmap
        upiAppBitmap = context.packageManager.getApplicationIcon(packageName).toBitmap()
        return upiAppBitmap
    }

  ```

  <br />
</Accordion>

<Accordion title="Step 2: Get Intent URI" icon="fa-code">
  Use the **\_payment** API to get Intent URI and transaction details for the UPI app selected by the customer. For more information, refer to <Anchor label="Collect Payment API > UPI Collection with S2S Integration" target="_blank" href="https://docs.payu.in/docs/upi-intent-server-to-server">UPI Intent with S2S Integration</Anchor>.

  <Accordion title="Request Parameters" icon="fa-table">
<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>key<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Merchant key provided by PayU during onboarding.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>JPg****f</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnid<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The transaction ID is a reference number for a specific order that is generated by the merchant.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ypl938459435</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The payment amount for the transaction.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>10.00</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>productinfo<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> A brief description of the product.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>iPhone</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>firstname<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The first name of the customer.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Ashish</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>lastname<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The last name of the customer.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Kumar</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>email<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The email address of the customer.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="mailto:abc@payu.in">abc@payu.in</a></p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>phone<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The phone number of the customer.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p></p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>address1<br/><code>optional but recommended for higher approval rate</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The first line of the billing address. H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai <strong>Note</strong>: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>34 Saikripa-Estate, Tilak Nagar</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>address2<br/><code>optional but recommended for higher approval rate</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The second line of the billing address.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p></p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>city<br/><code>optional but recommended for higher approval rate</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The city where your customer resides as part of the billing address.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Mumbai</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>state<br/><code>optional but recommended for higher approval rate</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The state where your customer resides as part of the billing address.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Maharashtra</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>country<br/><code>optional but recommended for higher approval rate</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The country where your customer resides.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>India</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>zipcode<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Billing address zip code is mandatory for the cardless EMI option. Character Limit-20</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>400004</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>pg<br/><code>mandatory for seamless/s2s flow</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> It defines the payment category and post <strong>UPI</strong>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>UPI</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankcode<br/><code>mandatory for seamless/s2s flow</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Each payment option is identified with a unique bank code at PayU. For UPI Autopay, post <strong>UPI</strong>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>UPI</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>surl<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The success URL, which is the page PayU will redirect to if the transaction is successful.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p></p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>furl<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The Failure URL, which is the page PayU will redirect to if the transaction is failed.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p></p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>vpa<br/><code>conditional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Customer's VPA handle. Mandatory for UPI Collect flow.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>customer@upi</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>si<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Signifies successful consent taken from the user. Must be <code>1</code> for subscription setup.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>si_details<br/><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON String</code> JSON object containing mandate details (billingAmount, billingCurrency, billingCycle, etc.). Refer to si_details JSON Object below.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>See si_details accordion</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txn_s2s_flow<br/><code>conditional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Integer</code> Parameter to enable S2S flow. Must be <code>4</code> for Legacy Decoupled flow (UPI Intent).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>4</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>s2s_client_ip<br/><code>conditional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Source IP of the customer. Required for UPI Intent flow.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>10.200.12.12</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>s2s_device_info<br/><code>conditional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Customer agent's device information. Required for UPI Intent flow.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Mozilla/5.0 (Windows NT 10.0; Win64; x64)</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf1<br/><code>mandatory if AD bank request this detail</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the Buyer's PAN and date of birth in the following format (separated by two pipe characters): Buyer's PAN||Buyer's DOB</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>AAAPZ1234C||22/08/1972</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>udf3<br/><code>mandatory if AD bank request this detail</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the invoice ID of the transaction (generated by the merchant) and merchant name in the following format (separated by two pipe characters): Invoice ID||MerchantName</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>INV-123_1231||MerchantName</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>buyer_type_business<br/><code>optional in case of B2B transaction for cross-border payments</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Binary</code> To be sent as "1" in case the buyer is a business. In case of individual buyers, it can be skipped. Default is "0". <strong>Note</strong>: This will be included in hash if posted (covered in next section).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p></td>
</tr>
</tbody>
</table>

`}</HTMLBlock>


### 

  </Accordion>

  <Accordion title="Sample Request" icon="fa-code">
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
    --data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0' \
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
    --data-urlencode 'upiAppName=gpay/phonepe/paytm/qr/amazonpay' \
    --data-urlencode 'udf_params={"udf7":"asdf","udf8":"12"}' \
    --data-urlencode 'buyer_type_business=1'
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 3: Retrieve Deeplink(uriIntentData) from the response," icon="fa-code">
  If metaData.unmappedStatus = pending, then get the result.intentURIData and add the prefix upi://pay?to make it to create a fully qualified deeplink to trigger the UPI App.

  ```json
  {
    "metaData": {
        "message": null,
        "referenceId": "c99a6455b3e0dc5cd7167ab8c8cc10d2fa153cb509e3f64c6cd0ed9c5b64a8c9",
        "statusCode": null,
        "txnId": "my_order_26075",
        "txnStatus": "pending",
        "unmappedStatus": "pending"
    },
    "result": {
        "paymentId": "403993715535965242",
        "merchantName": "Sudhanshu",
        "merchantVpa": "payutest@hdfcbank",
        "amount": "1.00",
        "intentURIData": "pa=payutest@hdfcbank&pn=Kumar&tr=403993715535965242&tid=PPPL403993715535965242080126220900&am=1.00&cu=INR&tn=UPIIntent",
        "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vdGVzdC5wYXl1LmluL2M5OWE2NDU1YjNlMGRjNWNkNzE2N2FiOGM4Y2MxMGQyYzgzYTk5NmFhNDhiYTk4MmZjMGQ4MTI1MGY1ODgxZjMvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0b2tlbiIgdmFsdWU9IjhERDNFRUFFLUI5NTktQzY1RS03MDczLTYzQTNGQUUxMjZGRiI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYW1vdW50IiB2YWx1ZT0iMS4wMCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0ibWlocGF5aWQiIHZhbHVlPSJjOTlhNjQ1NWIzZTBkYzVjZDcxNjdhYjhjOGNjMTBkMmZhMTUzY2I1MDllM2Y2NGM2Y2QwZWQ5YzViNjRhOGM5Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJkaXNhYmxlSW50ZW50U2VhbWxlc3NGYWlsdXJlIiB2YWx1ZT0iMCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVWcGEiIHZhbHVlPSJwYXl1dGVzdEBoZGZjYmFuayI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVOYW1lIiB2YWx1ZT0iU3VkaGFuc2h1Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJhZGRpdGlvbmFsQ2hhcmdlcyIgdmFsdWU9IjAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InRyYW5zYWN0aW9uRmVlIiB2YWx1ZT0iMS4wMCI+PC9mb3JtPjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0Jz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5vbmxvYWQ9ZnVuY3Rpb24oKXsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb2N1bWVudC5mb3Jtc1sncGF5bWVudF9wb3N0J10uc3VibWl0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvc2NyaXB0PjwvYm9keT48L2h0bWw+",
        "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
    }
  }
  ```
</Accordion>

<Accordion title="Step 4: Add the prefix" icon="fa-code">
  Add the prefix as per the Android/IOS to it to create a fully qualified deeplink to trigger the UPI App.

  #### Android Specific Intent prefix

  ```
  androidPrefix="intent://pay?"
  intentUriData="pa=myntra.payu@axisbank&pn=NIMIT%20BHATIA&tr=26156866365&tid=PPPL2615686636525112512114769254fab&am=10.00&cu=INR&tn=UPIIntent"
  suffix = "#Intent;scheme=upi;package=<package name>;"
  suffixForFallback="S.browser_fallback_url=<base64decoded result.acsTemplate can be used to redirect to Payu for UPI fallback>;end"
  //use androidPrefix+intentUriData+suffix+suffixForFallback to trigger the App in specific deeplink integration
  ```

  #### IOS Specific Intent prefix (Limited availability)

  ```
  phonepe = phonepe://upi/pay? 
  paytm = paytm://upi/pay? 
  googlepay = gpay://upi/pay? 
  bhim = bhim://upi/pay?
  credpay = credpay://upi/pay?
  ```
</Accordion>

<Accordion title="Step 5: Verify the payment" icon="fa-code">
  <Verify_Payment_Tabs />
</Accordion>

<br />