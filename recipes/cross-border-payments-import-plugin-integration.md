---
title: Cross-Border Payments Import Plugin Integration
description: Recipe Description
hidden: false
recipe:
  color: '#018FF4'
  icon: 🦉
---
```java Java
import com.payu.*;
PayuClient payuClient = PayuClient.init('<payu_key>', '<payu_salt>'); 
HasherParams hasherParams = new HashParams.Builder() 
.setTxnId("<txnId>")  
.setAmount("<amount>") 
.setProductInfo("<productInfo>") 
.setFirstName("<firstName>") 
.setEmail("<email>") 
.build(); 
String hashStr = payuClient.hasher.generateHash(hashParams); 
import okhttp3.*; 
PayuAPIHash udfUpdateHash = new  PayuAPIHash(); 
udfUpdateHash.key = payuClient.hasher.yourKey);  
udfUpdateHash.var1 = "e5b8663df04581c085f9"; 
udfUpdateHash.salt = payuClient.hasher.yourSalt(); 
String hashForUdfUpdateApi =  udfUpdateHash.generateHashForUdfUpdteApi(); 
PayuUdfs udfUpdate = new PayuUdfs(); 
udfUpdate.key = "yourKey"; 
udfUpdate.var1 = "e5b8663df04581c085f9"; 
udfUpdate.var2 = "8000123"; 
udfUpdate.var3 = "4334343"; 
udfUpdate.var4 = "434343"; 
udfUpdate.var5 = "Abcd123"; 
udfUpdate.var6 = "INV0000000dd0599100"; 
udfUpdate.environment = "Test"; 
udfUpdate.hash = hashForUdfUpdateApi; 
String reverseHash = "<payuHash>" // hash received after payment from payu 
String txnStatus = "<payuTxnStatus>"// txn status received after payment from payu 
boolean isVerified = payu.hash.validateHash(reverse_hash, txnStatus, hashParams); 
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
boolean isVerified = payuClient.hasher.validateHash(reverse_hash, txnStatus, hashParams);
PayuAPIHash hashInvoice = new  PayuAPIHash(); 
hashInvoice.key = payuClient.hasher.yourKey();
hashInvoice.var1 = "403993715525825059"; 
hashInvoice.salt = payuClient.hasher.yourSalt();
hashForUdfUpdateApi =  hashInvoice.generateHashForInvoiceUploadApi();
PayuUpdateInvoice invoiceUpload = new PayuUpdateInvoice(); 
invoiceUpload.key = "DGy1hY"; 
invoiceUpload.environment = "Test"; 
invoiceUpload.var1 = "403993715525825059"; 
invoiceUpload.var2 = "INV0000000001"; 
invoiceUpload.var3 = "Invoice"; 
invoiceUpload.file = new File("/Users/ashish.kumar/Desktop/productNeeote.pdf"); 
invoiceUpload.fileName = new File ("productNote.pdf"); 
invoiceObj.hash = hashForUdfUpdateApi;
String invoiceUpdateStatus = invoiceObj.updateInvoice();
```

# Import the PayU package

<!-- java@1 -->



# Create an object for PayUClient

<!-- java@2 -->



# Pass the parameters for generating a hash to authenticate a transaction:

<!-- java@3-10 -->



# Import the package for an HTTP request

<!-- java@11 -->



# Create hash for the UDF Update API:

<!-- java@12-17 -->



# Create UDF Update API with parameters.

<!-- java@17-24 -->

For more information on UDF Update API, refer to UDF Update API.

# Configure the environment as “Test.”

<!-- java@26 -->

Note: It is recommended to configure the environment as “Test” for testing the flow before moving to live.

# Perform reverse hash calculation with the response from PayU.

<!-- java@27-42 -->



# Calculate hash for uploading the invoice.

<!-- java@42-47 -->



# Post the Invoice UploadAPI through SDK.

<!-- java@48-53 -->

For more information on Invoice Upload API, refer to Invoice Upload API.

# Attach your invoice with the file path and file name.

<!-- java@54-57 -->

