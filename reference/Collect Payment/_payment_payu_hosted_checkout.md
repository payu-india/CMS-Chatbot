---
title: Collect Payment API - PayU Hosted Checkout
excerpt: ''
api:
  file: payuhosted-3.json
  operationId: PayUHostedCheckout
deprecated: false
hidden: false
metadata:
  title: Collect Payment API or _payment API
  description: >-
    Streamline your payment process with PayU’s Hosted Checkout API. Utilize our
    simulator to test and understand payment collection seamlessly. Access
    comprehensive API references for a smooth integration
  keywords:
    - PayU Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - Pre-built Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for PayU Hosted Checkout
    - _payment API for PayU Hosted Checkout
    - _payment API simulation for Pre-built Checkout
    - _payment API simulation for PayU Hosted Checkout
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: prebuilt-checkout-payu-hosted
      title: PayU Hosted Checkout
    - type: basic
      slug: integrate-with-payu-hosted-checkout
      title: 1. Integration Steps
---
The Collect Payment API (**\_payment** API) is used to collect payments for all the Web Checkout integration. This section provides the API Reference for PayU Hosted Checkout or Pre-Built Checkout.

> 📘 Reference:
>
> For an example of how to submit a payment request on your\[website, refer to [Submitting Payment Requ](doc:submitting-payment-request-on-your-website) st-on-your-website). To handle redirect URLs (surl a\[d furl), refer to [Handlin](doc:handling-the-redirect-urls) -the-redirect-urls).

### Environment

|                            |                                                                         |
| :------------------------- | :---------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

## Sample request

```curl
curl -X POST "https://test.payu.in/_payment" \
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d \
"key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00 \
&firstname=PayU User&email=test@gmail.com&phone=9876543210 \
&productinfo=iPhone&surl= \
https://apiplayground-response.herokuapp.com/ \
&furl=https://apiplayground-response.herokuapp.com/ \
&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
```
```python
	import requests

url = "https://test.payu.in/_payment"
payload = "key=JP***g&txnid=Dnh8wYimuCRIdv&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=&bankcode=&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=cb4b8bda5677dbe80f53735b1d0ec5d48164c3654627369268cf6bf266db994db39108ce2e0868c953e66c172f6b2d78836b253d3463d0cc40d9b6a93118ed56"
headers = { 
  "Accept": "application/json", 
  "Content-Type": "application/x-www-form-urlencoded" 
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
```
```php
$url = "https://test.payu.in/_payment";
$req = curl_init($url);
curl_setopt($req, CURLOPT_URL, $url);
curl_setopt($req, CURLOPT_POST, true); 
curl_setopt($req, CURLOPT_RETURNTRANSFER, true);
$headers = array(
  "Content-Type: application/x-www-form-urlencoded"
); 
curl_setopt($req, CURLOPT_HTTPHEADER, $headers);
$data = "key=JP***g&txnid=Dnh8wYimuCRIdv&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=&bankcode=&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=&ccexpmon=&ccexpyr=&ccvv=&ccname=&txn_s2s_flow=&hash=cb4b8bda5677dbe80f53735b1d0ec5d48164c3654627369268cf6bf266db994db39108ce2e0868c953e66c172f6b2d78836b253d3463d0cc40d9b6a93118ed56";
curl_setopt($req, CURLOPT_POSTFIELDS, $data);
$resp = curl_exec($req);
curl_close($req);
var_dump($resp);
```
```java
Request request = Request.Post("https://test.payu.in/_payment");
String body = "key=JP***g&txnid=Dnh8wYimuCRIdv&amount=10.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=&bankcode=&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=&ccexpmon=&ccexpyr=&ccvv=&ccname=&txn_s2s_flow=&hash=cb4b8bda5677dbe80f53735b1d0ec5d48164c3654627369268cf6bf266db994db39108ce2e0868c953e66c172f6b2d78836b253d3463d0cc40d9b6a93118ed56";
request.bodyString(body, ContentType.APPLICATION_FORM_URLENCODED);
request.setHeader("Content-Type", "application/x-www-form-urlencoded");
HttpResponse httpResponse = request.execute().returnResponse();
System.out.println(httpResponse.getStatusLine());
if (httpResponse.getEntity() != null) {
    String html = EntityUtils.toString(httpResponse.getEntity());
    System.out.println(html);
}
```

## Sample response

#### Response

```text
mihpayid=403993715531077182&mode=CC&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=ypl938459435dfdfdf&amount=1000.00&cardCategory=domestic&discount=0.00&net_amount_debit=1000&addedon=2024-02-27+15%3A11%3A37&productinfo=iPhone&firstname=Ashish+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=ashish%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CC-PG&bank_ref_num=7f0d5ada-59bb-41d7-9e41-20a6af2406c9&bankcode=CC&error=E000&error_Message=No+Error&name_on_card=test&cardnum=411111XXXXXX1111&cardhash=This+field+is+no+longer+supported+in+postback+params.
```

#### Parsed response

```json
{
  "mihpayid": "403993715531077182",
  "mode": "CC",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "JPM7Fg",
  "txnid": "ypl938459435dfdfdf",
  "amount": "1000.00",
  "cardCategory": "domestic",
  "discount": "0.00",
  "net_amount_debit": "1000",
  "addedon": "2024-02-27 15:00:42",
  "productinfo": "iPhone",
  "firstname": "Ashish",
  "lastname": "",
  "address1": "",
  "address2": "",
  "city": "",
  "state": "",
  "country": "",
  "zipcode": "",
  "email": "ashish@gmail.com",
  "phone": "9876543210",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "",
  "udf6": "",
  "udf7": "",
  "udf8": "",
  "udf9": "",
  "udf10": "",
  "hash": "84bbbf0fa3ba2a39942f6c3deab234c4d00bc5b6aceee5cda3c8200d6e1714e19c224d47e24d0c4a9a0cce40eddbae1dc46455c69e5e7d5dd62f6636bfab337c",
  "field1": "896193988312194700",
  "field2": "857712",
  "field3": "1000.00",
  "field4": "",
  "field5": "00",
  "field6": "02",
  "field7": "AUTHPOSITIVE",
  "field8": "AUTHORIZED",
  "field9": "Transaction is Successful",
  "payment_source": "payu",
  "PG_TYPE": "CC-PG",
  "bank_ref_num": "896193988312194700",
  "bankcode": "CC",
  "error": "E000",
  "error_Message": "No Error",
  "cardnum": "XXXXXXXXXXXX2346",
  "cardhash": "This field is no longer supported in postback params.",
  "splitInfo": "{\"splitStatus\":\"splitNotReceived\",\"splitSegments\":[]}"
}
```

## Response parameters

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        mihpayid
      </td>

      <td>
        It is a unique reference number created for each transaction at PayU's end which is used to identify a transaction in case of a refund.
      </td>
    </tr>

    <tr>
      <td>
        mode
      </td>

      <td>
        This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:
        • Credit Card – CC
        • Debit Card – DC
        • Net Banking – NB
        • Cash Card – CASH
        • EMI – EMI
        • Cardless EMI – CLEMI
        • Buy Now Pay Later - BNPL
      </td>
    </tr>

    <tr>
      <td>
        bankcode
      </td>

      <td>
        This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        This parameter returns the status of the transaction and must be used to map the order status. Possible values are success, failure, or pending. The significance of the values for these values are:
        • **Success**: If the value of status parameter is 'success', the transaction is successful.
        • **Failed**: If the value of status parameter is 'failure' or 'pending', must only be treated as a failed transaction.
      </td>
    </tr>

    <tr>
      <td>
        unmappedstatus
      </td>

      <td>
        This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to [Payment State Explanations](ref:payment-state-explanations).
      </td>
    </tr>

    <tr>
      <td>
        key
      </td>

      <td>
        This parameter contains the merchant key.
      </td>
    </tr>

    <tr>
      <td>
        error
      </td>

      <td>
        For the failed transactions, this parameter provides the reason for failure.
      </td>
    </tr>

    <tr>
      <td>
        error\_message
      </td>

      <td>
        This parameter contains the error message. For the list of error message, refer to [Error Codes](ref:error-codes).
      </td>
    </tr>

    <tr>
      <td>
        bank\_ref\_num
      </td>

      <td>
        For each successful transaction – this parameter contains the bank reference number generated by the bank.
      </td>
    </tr>

    <tr>
      <td>
        txnid
      </td>

      <td>
        This parameter contains the transaction ID value posted by the merchant during the transaction request.
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        This parameter contains the original amount which was sent in the transaction request by the merchant.
      </td>
    </tr>

    <tr>
      <td>
        cardCategory
      </td>

      <td>
        This parameter contains the card category to indicate whether it is domestic or international.
      </td>
    </tr>

    <tr>
      <td>
        discount
      </td>

      <td>
        This parameter contains the discount amount by the merchant.
      </td>
    </tr>

    <tr>
      <td>
        net\_amount\_debit
      </td>

      <td>
        This parameter contains the net amount debited.
      </td>
    </tr>

    <tr>
      <td>
        addedon
      </td>

      <td>
        The transaction date and time of the transaction.
      </td>
    </tr>

    <tr>
      <td>
        productinfo
      </td>

      <td>
        This parameter contains the same value of product information which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        firstname
      </td>

      <td>
        This parameter contains the same value of first name which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        lastname
      </td>

      <td>
        This parameter contains the same value of last name which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        email
      </td>

      <td>
        This parameter contains the same value of email which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        phone
      </td>

      <td>
        This parameter contains the same value of phone which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
        This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).
      </td>
    </tr>

    <tr>
      <td>
        PG\_TYPE
      </td>

      <td>
        This parameter gives information on the payment gateway used for the transaction.
      </td>
    </tr>

    <tr>
      <td>
        udf1
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf2
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf3
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5 which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf4
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf5
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf6
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf7
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf8
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf9
      </td>

      <td>
        This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        field1
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        field2
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        field3
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        field4
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        field5
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        field6
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        field7
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        field8
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        field9
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        success\_at
      </td>

      <td>
        This parameter contains the date and timestamp when the transaction was successful.
      </td>
    </tr>

    <tr>
      <td>
        cardnum
      </td>

      <td>
        The parameter contains the card number masked and only last 4 digits are returned.
      </td>
    </tr>

    <tr>
      <td>
        issuing\_bank
      </td>

      <td>
        The parameters contains the card issuing bank.
      </td>
    </tr>
  </tbody>
</Table>

## Request parameters

<AddionalCards_paymentRequestParametersInformation />

> 📘 Note:
>
> Collecting the information for the following parameters from customers is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information:
>
> * email
> * phone
> * address1

> 📘 Reference:
>
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

<TransactionStages />

<TutorialTile backgroundColor="#018FF4" emoji="🦉" id="65af7cd8114cd8005335bc30" link="https://docs.payu.in/v1/recipes/payu-hosted-checkout-curl-request-walkthrough" slug="payu-hosted-checkout-curl-request-walkthrough" title="PayU Hosted Checkout cURL Request Walkthrough" />