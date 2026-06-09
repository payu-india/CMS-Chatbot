---
api:
  file: Merchant Hosted Checkout.postman_collection_9th_June.json
  operationId: merchantHostedPayment
hidden: true
---
To process payments with credit/debit card, UPI, wallet, etc. on your website using PayU, collect the payment details on your website and submit them to PayU via API. This eliminates the need for redirection to PayU’s payment page, resulting in a more secure and efficient transaction.

<Callout icon="📘" theme="info">
  **Reference**: For an example of how to submit a payment request on your website, refer to [Submitting Payment Request on your Website](doc:submitting-payment-request-on-your-website). To handle redirect URLs (surl and furl), refer to [Handling the Redirect URLs](doc:handling-the-redirect-urls).
</Callout>

|                            |                                                                         |
| :------------------------- | :---------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

## Sample Request
<Tabs>
  <Tab title="Net banking">

  Source: [`_payment_merchant_hosted_netbanking.md`](./_payment_merchant_hosted_netbanking.md) — “Sample request” (cURL reformatted; the source line was broken).

  **Test env:** that page uses **`pg=TESTPG`** and **`bankcode=TESTPGNB`**. Production net banking typically uses **`pg=NB`** with bank codes from PayU’s list / `getNetBankingStatus`.

  ```bash
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g&txnid=bvRCCBO4YiGGHE&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=TESTPG&bankcode=TESTPGNB&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64"
  ```

  </Tab>

  <Tab title="Cards">

  Source: [`_payment_merchant_hosted_cards.md`](./_payment_merchant_hosted_cards.md) — “Sample request” accordion.

  ```bash
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g&txnid=EaE4ZO3vU4iPsp&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc&bankcode=MAST&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=undefined&hash=fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
  ```

  </Tab>

  <Tab title="UPI">

  Source: [`_payment_merchant_hosted_upi.md`](./_payment_merchant_hosted_upi.md) — this page has **no** embedded cURL sample. The example below matches the companion [`updated_upi_merchant_hosted.json`](../../updated_upi_merchant_hosted.json) and the doc’s test VPA note (`anything@payu` / `9999999999@payu.in`).

  ```bash
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU+User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=anything@payu&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=REPLACE_WITH_SERVER_GENERATED_HASH"
  ```

  </Tab>

  <Tab title="Wallets">

  Source: [`_payment_merchant_hosted_wallets.md`](./_payment_merchant_hosted_wallets.md) — “Sample request” accordion.

  **`productinfo`** is spelled correctly here (the doc’s `-d` string uses `producinfo`).

  ```bash
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&productinfo=iPhone&firstname=Ashish&email=test@gmail.com&phone=9876543210&pg=cash&bankcode=paytm&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
  ```

  </Tab>

  <Tab title="EMI">

  Source: [`_payment_merchant_hosted_emi.md`](./_payment_merchant_hosted_emi.md) — “Sample request” accordion (cURL block only).

  ```bash
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g&txnid=H6mUfE0ccAY94j&amount=20000.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=EMI&bankcode=EMIA3&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=&hash=782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
  ```

  </Tab>

  <Tab title="BNPL">

  Source: [`_payment_merchant_hosted_bnpl.md`](./_payment_merchant_hosted_bnpl.md) — “Sample Request” accordion.

  The doc shows a **JSON** object as `-d` while the header is **`application/x-www-form-urlencoded`**. Below is the **form-urlencoded** equivalent PayU expects.

  ```bash
  curl -X POST "https://test.payu.in/_payment" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=J****g&txnid=5jJ9xYceXX1ydT&amount=1000.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=BNPL&bankcode=LAZYPAY&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
  ```

  </Tab>
</Tabs>
## Sample Response
<Tabs>
  <Tab title="Net banking">

Source: [`_payment_merchant_hosted_netbanking.md`](./_payment_merchant_hosted_netbanking.md) — “Sample response” (successful redirect URL / query string).

```plaintext
mihpayid=403993715524046125&mode=NB&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=bvRCCBO4YiGGHE&amount=10.00&discount=0.00&net_amount_debit=10&addedon=2021-09-06+13%3A59%3A39&productinfo=iPhone&firstname=Ashish&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=fa7bb889d25b2a60bcf32316d1c9346589ff3de012dd0c66aa47ec12f1349837163ef8a603bd8b357de610b768f08dc4fb3bb4702d1ca6d9751300667fd763a6&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=NB-PG&bank_ref_num=ae67e632-f4eb-4121-b47b-2d35dce5ec2e&bankcode=TESTPGNB&error=E000&error_Message=No+Error
```

  </Tab>

  <Tab title="Cards">

Source: [`_payment_merchant_hosted_cards.md`](./_payment_merchant_hosted_cards.md) — “Sample response” → **Normal transaction** (query string). A **parsed JSON** example is on the same page.

```plaintext
mihpayid=403993715531077182&mode=CC&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=ypl938459435dfdfdf&amount=1000.00&cardCategory=domestic&discount=0.00&net_amount_debit=1000&addedon=2024-02-27+15%3A11%3A37&productinfo=iPhone&firstname=Ashish+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=ashish%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CC-PG&bank_ref_num=7f0d5ada-59bb-41d7-9e41-20a6af2406c9&bankcode=CC&error=E000&error_Message=No+Error&name_on_card=test&cardnum=411111XXXXXX1111&cardhash=This+field+is+no+longer+supported+in+postback+params.
```

  </Tab>

  <Tab title="UPI">

[`_payment_merchant_hosted_upi.md`](./_payment_merchant_hosted_upi.md) does **not** include a sample response. Below is an **illustrative** success query string in the same shape as other `_payment` redirects (`mode=UPI`, `bankcode=UPI`, `PG_TYPE=UPI-PG`). Replace values with your live postback and **verify `hash`**.

```plaintext
mihpayid=403993715530000001&mode=UPI&status=success&unmappedstatus=captured&key=JP***g&txnid=xdB9G7qYpfqszo&amount=10.00&discount=0.00&net_amount_debit=10&addedon=2024-06-09+12%3A00%3A00&productinfo=iPhone&firstname=PayU+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=REPLACE_WITH_VERIFIED_RESPONSE_HASH&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=UPI-PG&bank_ref_num=00000000-0000-0000-0000-000000000000&bankcode=UPI&error=E000&error_Message=No+Error
```

  </Tab>

  <Tab title="Wallets">

Source: [`_payment_merchant_hosted_wallets.md`](./_payment_merchant_hosted_wallets.md) — “Sample response” accordion, expressed as the **redirect query string** (same field values as the doc’s PHP sample).

```plaintext
mihpayid=403993715527518775&mode=CASH&status=success&unmappedstatus=captured&key=J*****g&txnid=HC13glcAkssIkl&amount=10.00&discount=0.00&net_amount_debit=10&addedon=2022-10-21+17%3A45%3A24&productinfo=iPhone&firstname=Ashish&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=007435a716982c7f5eec5cff95701f65eb1bdbff8f852e461224e3b5e17126ad26bb3a3ffdb95cded6a87d3515fe86fc58925cad024595a4a6825adfed2dc436&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CASH-PG&bank_ref_num=540898ed-72e7-40a8-a96e-f17de621cbb4&bankcode=CASH&error=E000&error_Message=No+Error&splitInfo=%7B%22splitStatus%22%3A%22splitNotReceived%22%2C%22splitSegments%22%3A%5B%5D%7D
```

  </Tab>

  <Tab title="EMI">

Source: [`_payment_merchant_hosted_emi.md`](./_payment_merchant_hosted_emi.md) — “Sample response” accordion, expressed as the **redirect query string** (same field values as the doc’s PHP sample; **`mode=EMI`** added for consistency with other modes).

```plaintext
mihpayid=403993715523602563&mode=EMI&status=success&unmappedstatus=captured&key=JP***g&txnid=v2tWbbdUOuacK9&amount=20000.00&discount=0.00&net_amount_debit=20000.00&addedon=2021-07-27+11%3A14%3A44&productinfo=iPhone&firstname=Ashish&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40gmail.com&phone=1234567890&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=10f8ead10cdf5f9b7bf9046987de046d63d62d6679dded9d5da8145f459066943570eec4aa184494ae77f99a8bcd55452af3c4eff0d7a7d3ba809c97b7c73045&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=EMI-PG&bank_ref_num=3d7cc4a4-00c8-4705-a0e7-5708d2c2bb75&bankcode=EMIA3&error=E000&error_Message=No+Error&name_on_card=payu&cardnum=512345XXXXXX2346
```

  </Tab>

  <Tab title="BNPL">

Source: [`_payment_merchant_hosted_bnpl.md`](./_payment_merchant_hosted_bnpl.md) — “Sample Response” accordion; the doc excerpt is short, so the line below completes the usual **redirect query-string** shape to match Cards/UPI (**`hash`** placeholder where the doc omits it).

```plaintext
mihpayid=403993715523409521&mode=BNPL&status=success&unmappedstatus=captured&key=J****g&txnid=5jJ9xYceXX1ydT&amount=1000.00&discount=0.00&net_amount_debit=1000&addedon=2021-07-02+15%3A03%3A50&productinfo=iPhone&firstname=PayU+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=&phone=&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=REPLACE_WITH_VERIFIED_RESPONSE_HASH&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=BNPL-PG&bank_ref_num=&bankcode=LAZYPAY&error=E000&error_Message=No+Error
```

  </Tab>
</Tabs>
