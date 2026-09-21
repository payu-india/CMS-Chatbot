---
name: Verify_Payment_Partner
---
<Accordion title="Verify Payment for Partner Integration" icon="fa-info-circle">
  ### Generate Hash for Verify Payment

  Generate the hash using the following logic and then use it Verify Payment for Partners API:

  **Hash Formula:**

  ```
  merchant_id|verify_payment|txnid|client_secret
  ```

  **Sample Python:**

  ```python
  import hashlib

  def generate_verify_hash(merchant_id, txnid, client_secret):
      hash_string = f"{merchant_id}|verify_payment|{txnid}|{client_secret}"
      return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()

  verify_hash = generate_verify_hash(8739528, "PPHOST20240315001", "your_client_secret")
  ```

  ### Call the Verify Payment API

  #### **Endpoint**

  | Environment | URL                                                                   |
  | ----------- | --------------------------------------------------------------------- |
  | Test        | `https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment` |
  | Production  | `https://api.payu.in/partner/verifyPayment`                           |

  #### **Request Parmeters**

  **Mandatory Parameters**

  | Parameter   | Description                                              | Example                   |
  | :---------- | :------------------------------------------------------- | :------------------------ |
  | txnid       | The unique transaction ID of the payment to be verified. | PPHOST20240315001         |
  | merchant_id | The unique numeric ID of the merchant.                   | 8739528                   |
  | hash        | The SHA-512 hash computed as: sha512(key\|txnid\|salt)   | computed_verify_hash_here |

  **Optional Parameters**

  | Parameter   | Description                                                      | Example                              |
  | :---------- | :--------------------------------------------------------------- | :----------------------------------- |
  | reseller_id | The unique UUID of the reseller associated with the transaction. | 11ee-0e7e-5403fde2-9523-0a696b110fde |

  #### **Sample Request**

  ```bash
  curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/verifyPayment' \
  --header 'Authorization: Bearer your_access_token_here' \
  --header 'Content-Type: application/json' \
  --data '{
    "txnid": "PPHOST20240315001",
    "merchant_id": 8739528,
    "reseller_id": "11ee-0e7e-5403fde2-9523-0a696b110fde",
    "hash": "computed_verify_hash_here"
  }'
  ```

  #### **Sample Response**

  ```json
  {
    "status": "success",
    "unmappedstatus": "captured",
    "mihpayid": "403993715521899234",
    "txnid": "PPHOST20240315001",
    "amount": "1500.00",
    "mode": "CC",
    "bankcode": "VISA",
    "productinfo": "Premium Subscription - Monthly",
    "firstname": "Priya",
    "email": "priya.sharma@example.com",
    "phone": "919876543210"
  }
  ```
</Accordion>
