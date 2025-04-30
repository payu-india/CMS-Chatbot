---
title: 1. API Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: 1. API Integration - PayU Hosted Checkout
  description: ''
  keywords:
    - API Integration for PayU Hosted Checkout
    - ' PayU Hosted Checkout API Integration'
    - ' Integrate PayU Hosted Checkout API'
    - Pre-Built Checkout API Integration
    - Integrate Pre-Built Checkout API
  robots: index
next:
  description: ''
---



#### Sample request

<TutorialTile backgroundColor="#018FF4" emoji="🦉" id="65af7cd8114cd8005335bc30" link="https://docs.payu.in/v1/recipes/payu-hosted-checkout-curl-request-walkthrough" slug="payu-hosted-checkout-curl-request-walkthrough" title="PayU Hosted Checkout cURL Request Walkthrough" />

<TutorialTile backgroundColor="#018FF4" emoji="🦉" id="65e1e40cc3b4be003dd7d966" link="https://docs.payu.in/v1/recipes/_payment-request-python-walkthrough" slug="_payment-request-python-walkthrough" title="_payment Request Python Walkthrough" />

<TutorialTile backgroundColor="#018FF4" emoji="🦉" id="65e1e75eb26f100010e62b54" link="https://docs.payu.in/v1/recipes/_payment-request-php-code-walkthrough" slug="_payment-request-php-code-walkthrough" title="_payment request PHP Code Walkthrough" />

<TutorialTile backgroundColor="#018FF4" emoji="🦉" id="65e1ede697a7be005be13a66" link="https://docs.payu.in/v1/recipes/_payment-request-java-code-walkthrough" slug="_payment-request-java-code-walkthrough" title="_payment Request Java Code Walkthrough" />

<PayUHostedSampleRequest />

#### Sample response

The response URL returned from PayU is similar to the following:

```
mihpayid=403993715523615328&mode=CC&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=50QJq6lBJBmx14&amount=10.00&cardCategory=domestic&discount=0.00&net_amount_debit=10&addedon=2021-07-28+15%3A11%3A37&productinfo=iPhone&firstname=PayU+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CC-PG&bank_ref_num=7f0d5ada-59bb-41d7-9e41-20a6af2406c9&bankcode=CC&error=E000&error_Message=No+Error&name_on_card=test&cardnum=411111XXXXXX1111&cardhash=This+field+is+no+longer+supported+in+postback+params.
```
```javascript
/**
 * PayU Payment Response Handling with Fetch API
 * This code processes the PayU response data and sends it to your server
 */

// PayU response data from the callback
const payuResponseData = "mihpayid=403993715523615328&mode=CC&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=50QJq6lBJBmx14&amount=10.00&cardCategory=domestic&discount=0.00&net_amount_debit=10&addedon=2021-07-28+15%3A11%3A37&productinfo=iPhone&firstname=PayU+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CC-PG&bank_ref_num=7f0d5ada-59bb-41d7-9e41-20a6af2406c9&bankcode=CC&error=E000&error_Message=No+Error&name_on_card=test&cardnum=411111XXXXXX1111&cardhash=This+field+is+no+longer+supported+in+postback+params";

// Parse the response data into an object
function parsePayUResponse(responseString) {
  const payuData = {};
  const pairs = responseString.split('&');
  
  for (const pair of pairs) {
    const [key, value] = pair.split('=');
    if (key && value !== undefined) {
      payuData[decodeURIComponent(key)] = decodeURIComponent(value);
    }
  }
  
  return payuData;
}

// Parse the response
const parsedResponse = parsePayUResponse(payuResponseData);

// URL of your server endpoint that will process the payment result
const serverUrl = 'https://your-server.com/api/payment-result';

// Send the parsed response to your server using Fetch API
fetch(serverUrl, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  },
  body: JSON.stringify({
    payuResponse: parsedResponse,
    // You can add additional client-side information here if needed
    clientInfo: {
      browserInfo: navigator.userAgent,
      timestamp: new Date().toISOString()
    }
  })
})
.then(response => {
  if (!response.ok) {
    throw new Error(`Server responded with status: ${response.status}`);
  }
  return response.json();
})
.then(data => {
  console.log('Payment verification successful:', data);
  // Handle successful verification (e.g., show success message, redirect to order confirmation)
  if (parsedResponse.status === 'success') {
    // Redirect to success page or show success message
    // window.location.href = '/payment-success?txnid=' + parsedResponse.txnid;
  }
})
.catch(error => {
  console.error('Payment verification error:', error);
  // Handle error (e.g., show error message)
});

```
```python
		import requestsurl = "https://test.payu.in/_payment"payload = "key=JP***g&txnid=Dnh8wYimuCRIdv&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=&bankcode=&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=cb4b8bda5677dbe80f53735b1d0ec5d48164c3654627369268cf6bf266db994db39108ce2e0868c953e66c172f6b2d78836b253d3463d0cc40d9b6a93118ed56"headers = { "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded" }response = requests.request("POST", url, data=payload, headers=headers, params=querystring)print(response.text)
```
```php
$url = "https://test.payu.in/_payment";$req = req_init($url);req_setopt($req, CURLOPT_URL, $url);req_setopt($req, CURLOPT_POST, true); req_setopt($req, CURLOPT_RETURNTRANSFER, true);$headers = array( "Content-Type: application/x-www-form-urlencoded", ); req_setopt($curl, CURLOPT_HTTPHEADER, $headers);$data = "key=JP***g&txnid=Dnh8wYimuCRIdv&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=&bankcode=&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=&ccexpmon=&ccexpyr=&ccvv=&ccname=&txn_s2s_flow=&hash=cb4b8bda5677dbe80f53735b1d0ec5d48164c3654627369268cf6bf266db994db39108ce2e0868c953e66c172f6b2d78836b253d3463d0cc40d9b6a93118ed56"req_setopt($curl, CURLOPT_POSTFIELDS, $data);$resp = req_exec($req);req_close($req);var_dump($resp);
```
```java
Request request = Request.Post("https://test.payu.in/_payment -H");String body = "key=JP***g&txnid=Dnh8wYimuCRIdv&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=&bankcode=&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=&ccexpmon=&ccexpyr=&ccvv=&ccname=&txn_s2s_flow=&hash=cb4b8bda5677dbe80f53735b1d0ec5d48164c3654627369268cf6bf266db994db39108ce2e0868c953e66c172f6b2d78836b253d3463d0cc40d9b6a93118ed56"request.bodyString(body,ContentType.APPLICATION_FORM_URLENCODED);request.setHeader("Content-Type", "application/x-www-form-urlencoded");HttpResponse httpResponse = request.execute().returnResponse();System.out.println(httpResponse.getStatusLine());if (httpResponse.getEntity() != null) {String html = EntityUtils.toString(httpResponse.getEntity());System.out.println(html);}
```

The response mentioned earlier looks like the following when parsed:

<TutorialTile backgroundColor="#018FF4" emoji="🦉" id="65af80d8138a55003eb96b82" link="https://docs.payu.in/v1/recipes/parse-the-_payment-json-response-using-java" slug="parse-the-_payment-json-response-using-java" title="Parse the _payment JSON response using Java" />

```
mihpayid: 403993715523615328
mode: CC
status: success
unmappedstatus: captured
key: JPM7Fg
txnid: 50QJq6lBJBmx14
amount: 10.00
cardCategory: domestic
discount: 0.00
net_amount_debit: 10
addedon: 2021-07-28 15:11:37
productinfo: iPhone
firstname: PayU User
lastname: 
address1: 
address2: 
city: 
state: 
country: 
zipcode: 
email: test@gmail.com
phone: 9876543210
udf1: 
udf2: 
udf3: 
udf4: 
udf5: 
udf6: 
udf7: 
udf8: 
udf9: 
udf10: 
hash: afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa
field1: 
field2: 
field3: 
field4: 
field5: 
field6: 
field7: 
field8: 
field9: Transaction Completed Successfully
payment_source: payu
PG_TYPE: CC-PG
bank_ref_num: 7f0d5ada-59bb-41d7-9e41-20a6af2406c9
bankcode: CC
error: E000
error_message: No Error
name_on_card: test
cardnum: 411111XXXXXX1111
cardhash: This field is no longer supported in postback params.
```

### Integration security

After receiving a response from PayU, you must calculate the hash again and validate it against the hash that you sent in the request to ensure the transaction is secure. PayU recommends implementing the transaction details APIs and webhook/callback as an extra security measure. For more information on this process, refer to [Get Transaction Details API](ref:get_transaction_details_api)   APIs and [Webhooks](doc:webhooks)   documentation.

You need to ensure that sensitive information related to the integration is not part of the payment request to PayU. The details including — but are not limited to — the following are considered sensitive information:

* salt value
* plain text hash string

Along with the request, the sensitive information should not be a part of any merchant-level URL. The following are considered sources for the merchant-level URL:

* The last web address accessed by a browser before loading PayU’s checkout page.
* URLs shared as part of payment request to PayU in the parameters: surl, furl, curl, nurl, and termUrl.
* Notification URLs configured with the merchant account.
* Invoice Completion URLs configured with the merchant account.

> 📘 Important
>
> Compare the parameters sent by PayU in the response with the ones you sent in the request to make sure none of them have been changed. You should verify specific parameters such as the transaction ID and amount. PayU is not responsible for any security breaches or loss resulting from your failure to implement the necessary security measures.

## Step 2: Verify the payment

PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the Verification APIs. For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a> under API Reference.

> 📘 Tip
>
> The Transaction ID (txnid) value that you passed in request of Step 1 with PayU must be used here.

<TutorialTile backgroundColor="#018FF4" emoji="🦉" id="65afb6e90a4e0500389d3886" link="https://docs.payu.in/v1/recipes/parse-the-verify-payment-api-response" slug="parse-the-verify-payment-api-response" title="Parse the Verify Payment API response" />