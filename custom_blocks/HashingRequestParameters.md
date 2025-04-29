---
name: Hashing Request Parameters
---
### Hashing

You must hash the request parameters using the following hash logic:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

For more information, refer to  <a href="generate-hash-merchant-hosted" target="_blank"> Generate Hash</a>.