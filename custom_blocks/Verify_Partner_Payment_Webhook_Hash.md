---
name: Verify_Partner_Payment_Webhook_Hash
---
**Reverse Hash Formula:**

```
client_secret|status|||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|merchant_id
```

<Warning>
**Critical Verification Rules:**
- There are **five consecutive pipes** (`|||||`) between `status` and `udf5`
- Use OAuth **client_secret** (NOT merchant salt)
- Do NOT add a trailing pipe after `merchant_id`
- Compute SHA-512 and compare as **case-insensitive**
- **Reject webhook if hash doesn't match**
</Warning>

<Accordion title="Sample Verification Payload" icon="fa-code">
  ```python
  import hashlib

  def verify_webhook_hash(webhook_payload, client_secret):
      status = webhook_payload.get('status', '')
      udf5 = webhook_payload.get('udf5', '')
      udf4 = webhook_payload.get('udf4', '')
      udf3 = webhook_payload.get('udf3', '')
      udf2 = webhook_payload.get('udf2', '')
      udf1 = webhook_payload.get('udf1', '')
      email = webhook_payload.get('email', '')
      firstname = webhook_payload.get('firstname', '')
      productinfo = webhook_payload.get('productinfo', '')
      amount = webhook_payload.get('amount', '')
      txnid = webhook_payload.get('txnid', '')
      merchant_id = webhook_payload.get('merchant_id', '')
      received_hash = webhook_payload.get('hash', '')
      
      hash_string = f"{client_secret}|{status}|||||{udf5}|{udf4}|{udf3}|{udf2}|{udf1}|{email}|{firstname}|{productinfo}|{amount}|{txnid}|{merchant_id}"
      
      computed_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
      
      return computed_hash.lower() == received_hash.lower()

  # Example
  is_valid = verify_webhook_hash(webhook_data, "your_client_secret")

  if is_valid:
      print("✅ Webhook verified — safe to process")
  else:
      print("❌ Invalid webhook hash — reject")
  ```
  ```java
  import java.security.MessageDigest;
  import java.security.NoSuchAlgorithmException;

  public class WebhookVerifier {
      public static boolean verifyHash(
          String status, String udf5, String udf4, String udf3, String udf2, String udf1,
          String email, String firstname, String productinfo, String amount,
          String txnid, String merchantId, String receivedHash, String clientSecret
      ) throws NoSuchAlgorithmException {
          
          String hashString = clientSecret + "|" + status + "|||||" + 
                            udf5 + "|" + udf4 + "|" + udf3 + "|" + udf2 + "|" + udf1 + "|" +
                            email + "|" + firstname + "|" + productinfo + "|" + 
                            amount + "|" + txnid + "|" + merchantId;
          
          MessageDigest md = MessageDigest.getInstance("SHA-512");
          byte[] hashBytes = md.digest(hashString.getBytes());
          
          StringBuilder hexString = new StringBuilder();
          for (byte b : hashBytes) {
              String hex = Integer.toHexString(0xff & b);
              if (hex.length() == 1) hexString.append('0');
              hexString.append(hex);
          }
          
          return hexString.toString().equalsIgnoreCase(receivedHash);
      }
  }
  ```
</Accordion>

### S
