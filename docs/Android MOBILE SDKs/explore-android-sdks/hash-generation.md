---
title: Hash Generation
excerpt: >-
  Every transaction (payment or non-payment) needs a hash by the merchant before
  sending the transaction details to PayU. This is required for PayU to validate
  the authenticity of the transaction.
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 📘 Hash should always be calculated at your server.

## Payment Hash

Hash required to make payment.

> sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)

Code samples to generate hash are present here - [JAVA](https://docs.google.com/document/d/18iaMVr5oq2bjuzTJvMvSpAyFrbQVLJegz5CdmdwBzIs/edit), [PHP](https://docs.google.com/document/d/1wby1TStudKuOtIRmUIc3ZqDVOg20mks8q5mT40i60qw/edit).

## For SI Payment

When doing Recurring(SI) transaction, Payment hash need to be calculated as mentioned [here](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk#for-si-payment)

## WebService Hash

To call any PayU API, you need to generate hash from your server using following pattern :

> sha512(key|command|var1|salt)\
> where\
> key=YOUR KEY\
> command=Api Commands\
> salt= YOUR SALT\
> var1= default(if you want stored cards use var1 as user\_credentials else default)
