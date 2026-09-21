---
name: Generate_Hash_Partner_Payment
---
<Accordion title="Sample Hash Generation Code" icon="fa-code">
  ```python
  import hashlib

  def generate_payment_hash(merchant_id, txnid, amount, productinfo, firstname, email, udf1, udf2, udf3, udf4, udf5, client_secret):
      hash_string = f"{merchant_id}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{client_secret}"
      return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()

  # Example usage
  payment_hash = generate_payment_hash(
      merchant_id=8739528,
      txnid="PPHOST20240315001",
      amount="1500.00",
      productinfo="Premium Subscription - Monthly",
      firstname="Priya",
      email="priya.sharma@example.com",
      udf1="subscription_plan_premium",
      udf2="monthly_billing",
      udf3="",
      udf4="",
      udf5="partner_web_checkout",
      client_secret="your_client_secret_here"
  )

  print(f"Payment Hash: {payment_hash}")
  ```
  ```java
  import java.security.MessageDigest;
  import java.security.NoSuchAlgorithmException;

  public class HostedCheckoutHashGenerator {
      public static String generateHash(
          int merchantId, String txnid, String amount, String productinfo,
          String firstname, String email, String udf1, String udf2, 
          String udf3, String udf4, String udf5, String clientSecret
      ) throws NoSuchAlgorithmException {
          
          String hashString = merchantId + "|" + txnid + "|" + amount + "|" + 
                            productinfo + "|" + firstname + "|" + email + "|" +
                            udf1 + "|" + udf2 + "|" + udf3 + "|" + udf4 + "|" + 
                            udf5 + "||||||" + clientSecret;
          
          MessageDigest md = MessageDigest.getInstance("SHA-512");
          byte[] hashBytes = md.digest(hashString.getBytes());
          
          StringBuilder hexString = new StringBuilder();
          for (byte b : hashBytes) {
              String hex = Integer.toHexString(0xff & b);
              if (hex.length() == 1) hexString.append('0');
              hexString.append(hex);
          }
          
          return hexString.toString();
      }
  }
  ```
  ```php
  <?php
  function generateHostedCheckoutHash($merchantId, $txnid, $amount, $productinfo, 
                                      $firstname, $email, $udf1, $udf2, $udf3, 
                                      $udf4, $udf5, $clientSecret) {
      
      $hashString = $merchantId . "|" . $txnid . "|" . $amount . "|" . 
                    $productinfo . "|" . $firstname . "|" . $email . "|" .
                    $udf1 . "|" . $udf2 . "|" . $udf3 . "|" . $udf4 . "|" . 
                    $udf5 . "||||||" . $clientSecret;
      
      return hash('sha512', $hashString);
  }

  // Example
  $hash = generateHostedCheckoutHash(
      8739528,
      "PPHOST20240315001",
      "1500.00",
      "Premium Subscription - Monthly",
      "Priya",
      "priya.sharma@example.com",
      "subscription_plan_premium",
      "monthly_billing",
      "",
      "",
      "partner_web_checkout",
      "your_client_secret_here"
  );

  echo "Payment Hash: " . $hash;
  ?>
  ```
</Accordion>
