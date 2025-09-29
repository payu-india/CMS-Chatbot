---
title: Import Plugin Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Cross-Border Import Plugin Integration
  description: ''
  keywords:
    - Cross-Border Import Plugin Integration
    - Cross Border Import Plugin Integration
    - Integrate Cross-Border Import Plugin
  robots: index
next:
  description: ''
---
You can install the Cross-Border Payments Java SDK plugin and integrate it as described in this section.

## Prerequisite

Download the Cross-Border Payments Import plugin and install it from the following GitHub location.

[https://github.com/payu-india/sdk-java/releases/tag/V1.0.0.0](https://github.com/payu-india/sdk-java/releases/tag/V1.0.0.0)

## Procedure

To integrate the Cross-Border Payments Import plugin, refer the following recipe or step-by-step procedure:

<Recipe slug="cross-border-payments-import-plugin-integration" title="Cross-Border Payments Import Plugin Integration" />

1. Import the PayU package:

```java
import com.payu.*;
```

2. Create an object for PayUClient:

```java
PayuClient payuClient = PayuClient.init('<payu_key>', '<payu_salt>');
```

3. Pass the parameters for generating a hash to authenticate a transaction:

```java
HasherParams hasherParams = new HashParams.Builder()
    .setTxnId("<txnId>")
    .setAmount("<amount>")
    .setProductInfo("<productInfo>")
    .setFirstName("<firstName>")
    .setEmail("<email>")
    .build();

String hashStr = payuClient.hasher.generateHash(hasherParams);
```

4. Import the package for an HTTP request:

```java
import okhttp3.*;
```

5. Create hash for the **UDF Update** API:

```java
PayuAPIHash udfUpdateHash = new PayuAPIHash();
udfUpdateHash.key = payuClient.hasher.yourKey;
udfUpdateHash.var1 = "e5b8663df04581c085f9";
udfUpdateHash.salt = payuClient.hasher.yourSalt();

//e.g.
String hashForUdfUpdateApi = udfUpdateHash.generateHashForUdfUpdteApi();
```

6. Create **UDF Update** API with parameters similar to the following. For more information on **UDF Update** API, refer to [UDF Update API](ref:udf_update_api).

```java
PayuUdfs udfUpdate = new PayuUdfs();
udfUpdate.key = "yourKey";
udfUpdate.var1 = "e5b8663df04581c085f9";
udfUpdate.var2 = "8000123";
udfUpdate.var3 = "4334343";
udfUpdate.var4 = "434343";
udfUpdate.var5 = "Abcd123";
udfUpdate.var6 = "INV0000000dd0599100";
```

7. Configure the environment as “Test”:

> **Note**: It is recommended to configure the environment as “Test” for testing the flow before moving to live.

```java
udfUpdate.environment = "Test";
udfUpdate.hash = hashForUdfUpdateApi;
```

8. Perform reverse hash calculation with the response from PayU:

```java
String reverseHash = "<payuHash>"; // hash received after payment from payu
String txnStatus = "<payuTxnStatus>"; // txn status received after payment from payu

boolean isVerified = payu.hash.validateHash(reverseHash, txnStatus, hashParams);

Map<String, String> optionalParams = new HashMap<String, String>();

HashParams hashParams = new HashParams.Builder()
    .setTxnId("<txnId>")
    .setAmount("<amount>")
    .setProductInfo("<productInfo>")
    .setProductInfo("<productInfo>")
    .setFirstName("<firstName>")
    .setEmail("<email>")
    .setUdf1("<userDefinedParam1>")
    .setUdf2("<userDefinedParam2>")
    .setAdditionalCharges("<additionalCharges>")
    .build();

boolean isVerified = payuClient.hasher.validateHash(reverseHash, txnStatus, hashParams);
```

9. Calculate hash for uploading the invoice:

```plaintext
PayuAPIHash hashInvoice = new PayuAPIHash();
hashInvoice.key = payuClient.hasher.yourKey();
hashInvoice.var1 = "403993715525825059";
hashInvoice.salt = payuClient.hasher.yourSalt();

hashForUdfUpdateApi = hashInvoice.generateHashForInvoiceUploadApi();
```

10. Post the **Invoice Upload**API through SDK. For more information on **Invoice Upload** API, refer to [Invoice Upload API](ref:invoice_upload_api).

```java
PayuUpdateInvoice invoiceUpload = new PayuUpdateInvoice();
invoiceUpload.key = "DGy1hY";
invoiceUpload.environment = "Test";
invoiceUpload.var1 = "403993715525825059";
invoiceUpload.var2 = "INV0000000001";
invoiceUpload.var3 = "Invoice";
```

11. Attach your invoice with the file path and file name:

```java
invoiceUpload.file = new File("/Users/ashish.kumar/Desktop/productNeeote.pdf");
invoiceUpload.fileName = new File("productNote.pdf");

invoiceObj.hash = hashForUdfUpdateApi;

String invoiceUpdateStatus = invoiceObj.updateInvoice();
```

<Callout icon="📘" theme="info">
  **Note**: The file size of the invoice to be uploaded must be less than 2MB.
</Callout>
