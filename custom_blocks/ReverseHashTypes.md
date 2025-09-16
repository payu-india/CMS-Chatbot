---
name: ReverseHashTypes
---
### Regular integration

The order of the parameters is similar to the following code block:

```
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

### With additional charges

```
sha512(additional_charges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

### With split transactions

```
sha512(SALT|status|splitInfo||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

### With combined split and additional charges

```
sha512(additional_charges|SALT|status|splitInfo||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

> 📘 PayU SDK Github resource for Hashing:
>
> You can use the Hash API of the PayU node SDK on Github to perform reverse hashing. Refer to the <Anchor label="PayU node SDK Readme" target="_blank" href="https://github.com/payu-india/payu-sdk-node/blob/main/README.md">PayU node SDK Readme</Anchor>, download and install the PayU node SDK from the <Anchor label="PayU node SDK Github location" target="_blank" href="https://github.com/payu-india/payu-sdk-node">PayU node SDK Github location</Anchor>.
