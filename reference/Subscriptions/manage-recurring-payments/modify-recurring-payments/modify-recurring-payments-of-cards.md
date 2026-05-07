---
title: Modify Recurring Payments of Visa and Mastercard Cards
excerpt: >-
  Modify card recurring payments and mandates of Visa and Mastercard using PayU
  APIs. Update billing rules, subscription settings, mandate details, and
  recurring payment configurations securely for card-based transactions.
deprecated: false
hidden: true
metadata:
  robots: index
---
Use this endpoint to modify card recurring payments and mandates of Visa and Mastercard.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /_payment
  </Card>
</Cards>

<PaymentAPIEnvironment />

## Sample Request

<Accordion title="Request Payload" icon="fa-code">

```curl
curl --location 'https://secure.payu.in/_payment' \
  --header 'accept: application/json' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642; PHPSESSID=68edd726c95b4' \
  --data-urlencode 'key=BmTY3G' \
  --data-urlencode 'txnid=my_order_47719' \
  --data-urlencode 'amount=1.00' \
  --data-urlencode 'firstname=Payu-Admin' \
  --data-urlencode 'email=test@example.com' \
  --data-urlencode 'phone=1234567890' \
  --data-urlencode 'productinfo=my_order_47719' \
  --data-urlencode 'api_version=7' \
  --data-urlencode 'si=3' \
  --data-urlencode 'pg=CC' \
  --data-urlencode 'bankcode=UTIBENCC' \
  --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'ccnum=5123456789012346' \
  --data-urlencode 'ccexpmon=05' \
  --data-urlencode 'ccexpyr=2030' \
  --data-urlencode 'ccvv=123' \
  --data-urlencode 'ccname=Test User' \
  --data-urlencode 'si_details={"action":"modify","paymentEndDate":"2030-04-13","billingAmount":"400.00","authPayuId":"999990000006391"}' \
  --data-urlencode 'YOUR_HASH_VALUE'
```

</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">

```php
Array
(
    [mihpayid]         => 25603951365
    [mode]             => CC
    [status]           => success
    [unmappedstatus]   => captured
    [key]              => BmTY3G
    [txnid]            => 5527fc7d02f2bfc00eb4
    [amount]           => 1.00
    [cardCategory]     => signature_premium
    [discount]         => 0.00
    [net_amount_debit] => 1
    [addedon]          => 2025-10-14 15:44:41
    [productinfo]      => Product Info
    [firstname]        => Payu-Admin
    [lastname]         => 
    [address1]         => 
    [address2]         => 
    [city]             => 
    [state]            => 
    [country]          => 
    [zipcode]          => 
    [email]            => test@example.com
    [phone]            => 1234567890
    [udf1]             => 
    [udf2]             => 
    [udf3]             => 
    [udf4]             => 
    [udf5]             => 
    [udf6]             => 
    [udf7]             => 
    [udf8]             => 
    [udf9]             => 
    [udf10]            => 
    [hash]             => YOUR_HASH_VALUE
    [field1]           => CBC10141015051509EGR573
    [field2]           => 185869
    [field3]           => 
    [field4]           => 
    [field5]           => 
    [field6]           => 05
    [field7]           => AUTHPOSITIVE
    [field8]           => 0 | Transaction Completed
    [field9]           => Transaction Completed
    [payment_source]   => payu
    [meCode]           => {
                                "wibmo_merchant_id":"16329672",
                                "hash_key":"YOUR_HASH_VALUE",
                                "acquirer_merchant_id":"175645866049780",
                                "mcc":"5499"
                            }
    [PG_TYPE]          => CC-PG
    [bank_ref_num]     => 528710004895
    [bankcode]         => CC
    [error]            => E000
    [error_Message]    => No Error
    [cardnum]          => XXXXXXXXXXXX4879
)
```

</Accordion>

<br />

<br />
