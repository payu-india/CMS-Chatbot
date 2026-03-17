---
title: Collect Payments - Save Card
excerpt: ''
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
      slug: collect-payments-using-a-saved-card
      title: Collect Payments using a Saved Card
---
When your customer has an account on your shopping website, they may store their card details to use when they revisit your website (repeat payment).

***

### **Steps to Integrate:**

1. [Get the saved card details of a customer]
2. [Post the payment to PayU using _payment API][Post the payment to PayU using _payment API]
3. [Check the PayU Response]
4. [Verify the payment]

***

PayU offers you API to save the card details and retrieves them using the Store Card APIs. For example, the stored cards are displayed when your customer performs checkout and lands on the payment page, similar to the following screenshot where they need to enter only the CVV:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/11/save_card_checkout-1024x817.jpeg)

This section explains the procedure for getting a customer’s card details and using a saved card to initiate payment.

***

## Step 1: Get the Saved Card Details

1. Get the customer’s card details your merchant key and customer’s registered mail ID to PayU using the **get_user_details** API:

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2"-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=J****g&command=get_user_cards&var1=yourkey:email@domain.com&hash=22744b991e9719a9823ee71832e37b022a77fce4d53188245114226d0d0d3a01ec0b6adce4aae9b9bd97baf97e3ef76912e29ca0726a57b16c1110dc66ffc653"
```
```python
import requestsurl = "https://test.payu.in/merchant/postservice?form=2"payload = "key=J****g&command=get_user_cards&var1=yourkey:email@domain.com&hash=22744b991e9719a9823ee71832e37b022a77fce4d53188245114226d0d0d3a01ec0b6adce4aae9b9bd97baf97e3ef76912e29ca0726a57b16c1110dc66ffc653"headers = { "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded" }response = requests.request("POST", url, data=payload, headers=headers, params=querystring)print(response.text)
```
```php
import requestsurl = "https://test.payu.in/merchant/postservice?form=2"payload = "key=JP***g&command=get_user_cards&var1=yourkey:email@domain.com&hash=22744b991e9719a9823ee71832e37b022a77fce4d53188245114226d0d0d3a01ec0b6adce4aae9b9bd97baf97e3ef76912e29ca0726a57b16c1110dc66ffc653"headers = { "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded" }response = requests.request("POST", url, data=payload, headers=headers, params=querystring)print(response.text)
```
```java
Request request = Request.Post("https://test.payu.in/merchant/postservice?form=2 -H");String body = "key=J****g&command=get_user_cards&var1=yourkey:email@domain.com&var2=&var3=&var4=&var5=&var6=&var7=&var8=&var9=&hash=22744b991e9719a9823ee71832e37b022a77fce4d53188245114226d0d0d3a01ec0b6adce4aae9b9bd97baf97e3ef76912e29ca0726a57b16c1110dc66ffc653"request.bodyString(body,ContentType.APPLICATION_FORM_URLENCODED);request.setHeader("Content-Type", "application/x-www-form-urlencoded");HttpResponse httpResponse = request.execute().returnResponse();System.out.println(httpResponse.getStatusLine());if (httpResponse.getEntity() != null) {String html = EntityUtils.toString(httpResponse.getEntity());System.out.println(html);}
```

2. Check the response for the last four digits of the card number:

```plaintext
{
      "status": 1,
      "msg": "Cards fetched Succesfully",
      "user_cards": {
            "57cb996f2eaeee525765a": {
                  "expiry_month": "03",
                  "card_mode": "CC",
                  "is_expired": 0,
                  "card_cvv": 0,
                  "card_no": "XXXXXXXXXXXX2346",
                  "card_token": "57cb996f2eaeee525765a",
                  "card_name": "test card",
                  "card_type": "CC",
                  "expiry_year": "2026",
                  "name_on_card": "Test",
                  "card_brand": "MASTERCARD",
                  "card_bin": "512345",
                  "isDomestic": "Y"
            }
      }
}
```

2. List the saved cards if the customer is having more than one card and ask them make a selection.
3. Collect the CVV of the saved card that customer has selected for payment.

***

## Step 2: Post Payment to PayU

Make the transaction request with the payment details along with the card nickname to PayU based on the following scenarios of tokenization:

* [Using Zero Code Change](ref:zero-code-change-payment)
* [Using Complete Card Details](ref:complete-card-details-payment)
* [Using Network Tokens](ref:using-network-tokens)
* [Using Travel Quick Pay with Network Tokens](ref:using-network-tokens-travel-quick-pay)
* [Using Issuer Tokens](ref:using-issuer-tokens)
* [Using Card Tokenized with PayU](ref:using-card-tokenized-with-payu)
* [Using Card on a Decoupled Flow with Network Token or Other Partner Tokenization](ref:using-card-a-decoupled-flow-with-network-token-or-other-partner-tokenization)
* [Using Card on a Decoupled Flow with PayU Tokenization](ref:using-card-on-a-decoupled-flow-with-payu-tokenization)

> 📘 Notes
>
> * In addition to the request parameters used for Merchant Hosted Checkout (Seamless integration) payment request, you need to ensure the additional parameters as specified in each scenario specified in this step. For more information on the complete list of parameters, refer to [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted).
> * The additional response parameters (if any) are specified for each scenario. For the sample response for a card payment using Merchant Hosted Checkout response, refer to [Cards Integration](doc:collect-payments-with-cards-seamless).
> * MOTO is acronym for Mail Order Telephone Order

***

## Step 3: Check the PayU Response

1. Check the response for the status of the transaction. The response for each scenario is specified in [Step 2](#step-2-post-payment-to-payu).
2. Verify the authenticity of the hash value before accepting or rejecting the invoice order. For more information, refer to [Generate Hash](doc:hashing-request-and-response)

***

## Step 4: Verify the Payment

Verify the transaction details using the Verification APIs. Post the transaction ID using the **verify_payment** API to verify the payment. For more information, refer to [Verify Payment API](ref:verify_payment_api)/

> 📘 Note:
>
> The transaction ID that you posted in Step 3 with PayU must be used here.
