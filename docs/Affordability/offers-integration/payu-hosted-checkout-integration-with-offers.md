---
title: Integrate with PayU Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integrate with PayU Hosted Checkout for Offers
  description: ''
  keywords:
    - Integrate an Offer with PayU Hosted Checkout
    - Integrate an PayU Hosted Checkout with Offer
    - Integrate an Offer with Non-Seamless Integration
    - Offer with Non-Seamless Integration
  robots: index
next:
  description: ''
---
With the PayU Hosted Checkout integration, the entire payment experience is controlled by PayU. The following sections describe how to use the PayU Hosted Integration to collect payments with various types of offers:

* [Instant Discount or Cashback Offer](#instant-discount-or-cashback-offer)
* [SKU-Based Offer](#sku-based-offer)

## General customer journey

1. Customer clicks **Pay** on your mobile application or website.
2. Customer is redirected to the PayU Hosted Checkout page.

   The PayU Hosted Checkout page on Desktop is similar to the following screenshot. In case offer keys have been passed by the merchant, the same would be filtered and displayed to the customer.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Web.L1.Offers_Without-Global-vault-Copy-1-1024x858.png)

   The PayU Hosted Checkout page on Mobile is similar to the following screenshot:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Mweb.L1.Offers_Without-Global-vault-a-Copy.png)

3. Customer is shown the applicable offers on the checkout page for that transaction.
4. Customer will have an option to apply the offer. If the offer is applicable on a specific payment option, the customer will be redirected to the specific payment option.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Web.L2.Without-Global-Vault_Cards_Filled-Copy-2-1024x863.png)

```
The PayU Hosted Checkout page for specify payment option on Mobile is similar to the following screenshot:
```

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Mweb.L2.Without-Global-Vault_Cards_Filled-Copy.png)

5. Alternatively, the customer can choose the payment option. If only an offer is applicable for that payment option, the offer will be automatically applied.

![Picture 1522098393](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/picture-1522098393.png)

6. For Instant Discount, the amount is reduced after the offer is applied, whereas, in the case of cashback, the amount will not be reduced after the offer is applied.
7. Customer completes the 2FA payment on the adjusted amount.
8. Customer is redirected back to the merchant mobile application or website.

## Instant Discount or Cashback

With the PayU Hosted Checkout integration, the entire payment experience is controlled by PayU. This section describes how to use the PayU Hosted Integration to collect payments with offers.

### **Customer journey on PayU Hosted Checkout**

1. Customer clicks **Pay** on your mobile application or website.
2. Customer is redirected to the PayU Hosted Checkout page.

   The PayU Hosted Checkout page on Desktop is similar to the following screenshot. In case offer keys have been passed by the merchant, the same would be filtered and displayed to the customer.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Web.L1.Offers_Without-Global-vault-Copy-1-1024x858.png)

   The PayU Hosted Checkout page on Mobile is similar to the following screenshot:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Mweb.L1.Offers_Without-Global-vault-a-Copy.png)

3. Customer is shown the applicable offers on the checkout page for that transaction.
4. Customer will have the option to apply the offer. If the offer is applicable to a specific payment option, the customer will be redirected to the specific payment option.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Web.L2.Without-Global-Vault_Cards_Filled-Copy-2-1024x863.png)

   The PayU Hosted Checkout page for specific payment option on Mobile is similar to the following screenshot:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Mweb.L2.Without-Global-Vault_Cards_Filled-Copy.png)

5. Alternatively, the customer can choose the payment option. If only an offer is applicable for that payment option, the offer will be automatically applied.

![Picture 1522098393](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/picture-1522098393.png)

6. For Instant Discount, the amount is reduced after the offer is applied, whereas, in the case of cashback, the amount will not be reduced after the offer is applied.
7. Customer completes the 2FA payment on the adjusted amount.
8. Customer is redirected back to the merchant’s mobile application or website.

### Integration steps

To integrate offers using PayU Hosted Checkout integration:

> 📘 **Reference**:
>
> For the PayU Hosted Checkout flow, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted).

1. Make the payment request to PayU:

   You need to send an additional parameter (**user token)**, **api\_version** as 14, and hash as described in the following table. This user token would be used to identify the customer for applying velocity rules.

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        api\_version
        **mandatory**
      </td>

      <td>
        The API version of the \_payment API must be specified as **14**.
      </td>

      <td>
        14
      </td>
    </tr>

    <tr>
      <td>
        user\_token\
        **mandatory for UPI, NB, Wallet**
      </td>

      <td>
        The use for this param is to allow the offer engine to apply velocity rules at a user level.  

        * **Card Based Offers (CC, DC, EMI)**: In case of card payment mode offers, if this parameter is passed the velocity rules would be applied on this token, if not passed the same would be applied on the card number.
        * **UPI, NB, Wallet**: It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        hash\
        **mandatory**
      </td>

      <td>
        It is used to avoid the possibility of transaction tampering.  

        * \*Note\*\*: The following order must be used for hashing:\
          `key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|udf6\|udf7\|udf8\|udf9\|udf10\|offer_key\|offer_auto_apply\|SALT`\
          For more information on hash generation process, refer to [Generate Hash](doc:generate-hash-payu-hosted) .
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

2. Check the response from PayU.

   You need to understand the following parameters to handle the payment response as the net amount debit may be different from the amount sent by you in the request.

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        discount
      </td>

      <td>
        This will specify the offer value provided to the user.
      </td>

      <td>
        10.00
      </td>
    </tr>

    <tr>
      <td>
        net\_amount\_debit
      </td>

      <td>
        This will specify the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request.
      </td>

      <td>
        100.00
      </td>
    </tr>

    <tr>
      <td>
        offer
      </td>

      <td>
        This parameter is used to post the offer key.
      </td>

      <td>
        newoffer1\@5686
      </td>
    </tr>

    <tr>
      <td>
        offer\_type
      </td>

      <td>
        This parameter is used to post any of the following offer\_type:  

        * instant
        * cashback
      </td>

      <td>
        instant
      </td>
    </tr>
  </tbody>
</Table>

3. Verify the payment.

   Similar to the payment response, the same parameters can be handled as part of the **verify\_payment** API. For more information, refer to [Verify Payment API](ref:verify_payment_api),

| **Parameter**       | **Description**                                                                                                                                                                                  | **Example** |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| transaction\_amount | This parameter contains the total transaction amount before discount.                                                                                                                            | 50000.00    |
| net\_amount\_debit  | This parameter contains the actual amount deducted from the customer’s payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request. | 47500.00    |
| discount            | This parameter contains the offer value provided to the user. This value will specify the offer amount for both Instant discount and Cashback offers.                                            | 2500.00     |

For the sample request and response from PayU, refer to [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

4. If you want to refund the payment to customer. refer to [Refund APIs](ref:refund-apis).

PayU would refund the exact amount passed by you in the Refund request. For more information, refer to [Refunds for Offers](doc:refunds-for-offers). 

> 📘 Note:
>
> You can enable the **Enforce Offer** flag by requesting your PayU Key Account Manager. If you enable the **Enforce Offer** flag, all the offers passed are visible to the customer and the customer chooses an offer that they wish to apply.

## SKU-Based offer

After you create an SKU-based offer on PayU Dashboard, you can start collecting payments for products with an SKU-based offer.

This section describes the customer workflow with an SKU-based offer on the PayU Payment page when redirected from your website for payment and request parameters for the **\_payment** API to collect payments with an SKU-Based Offer.

> 📘 Note:
>
> For payment journey of instant discount offers using Redirection Flow or PayU Hosted Checkout, refer to [Integrate with PayU Hosted Checkout](doc:payu-hosted-checkout-integration-with-offers).

### Customer journey

After your customer selects the items from your website (for example, mobile online shopping), the customer is redirected to the PayU page for payment and involves the following steps:

1. Select **Offers** at the top-right corner.

<Image align="center" width="322px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Mweb.L1.Offers_L1-523x1024.png" />

   All the offers for the products in the shopping cart (if any) are listed.

<Image align="center" width="322px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Mweb.L1.Offers_AllOffers-1-568x1024.png" />

2. Select the **Product Offers** tab.

   The **Product Offers** tab is displayed on the *Offer & Discount* page.

<Image align="center" width="322px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/skuoffers.png" />

3. Apply an offer using the **Use Offer** button for the offer you wish to apply.

   The *Offer Applied!* pop-up page is displayed.

<Image align="center" width="322px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Mweb.L1.Offer_Applied.png" />

4. Click **Thanks.**

   The page to collect your credit card details is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Mweb.L1.Offers_L2_Expanded-350x1024.png)

5. Click **Proceed** to make payment and then enter the OTP sent by bank to your mobile to complete the purchase.
6. Close this page to return back to the merchant website.

### Integration steps

#### Step 1: Post request parameters

**Additional request parameters for SKU-Based Offer**

The following request parameters are posted along with request parameters posted for a PayU Hosted Checkout transaction. For the checkout flow and list of request parameters required for the Offer integration, refer to  [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout).

<Table>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        cart\_details
        **mandatory for SKU**
      </td>

      <td>
        * JSON Object\_ The card details is specified in this parameter in a JSON format.  
        * \*Note\*\*: If given null, no cart will be created for the transaction.
      </td>
    </tr>

    <tr>
      <td>
        cart\_details.amount\
        **mandatory**
      </td>

      <td>
        * String\_ The amount for the SKU-based offer.
      </td>
    </tr>

    <tr>
      <td>
        cart\_details.surcharges\
        **conditional**
      </td>

      <td>
        * String\_ Total txn amount is now increased, but the cart\_details.amount is lesser, to handle the difference, the additonal amount added by the merchant should be passed in surcharges field
      </td>
    </tr>

    <tr>
      <td>
        cart\_details.pre\_discount\
        **conditional**
      </td>

      <td>
        * String\_ If there are any pre discount given by merchant on their checkout page. Total txn amount is now reduced, but the cart\_details.amount is higher, to handle the difference, the discount given by the merchant should be passed in pre\_discount field
      </td>
    </tr>

    <tr>
      <td>
        cart\_details.items\
        **mandatory**
      </td>

      <td>
        * String\_ The number of the items for the SKU-based offer.
      </td>
    </tr>

    <tr>
      <td>
        cart\_details.sku\_details\
        **mandatory**
      </td>

      <td>
        * JSON Object\_ The SKU details is specified in this parameter in a JSON format.
      </td>
    </tr>

    <tr>
      <td>
        cart\_details.sku\_details.sku\_id\
        **mandatory**
      </td>

      <td>
        * String\_ This parameter contains the unique identifier for SKU.  
        * \*Not&#x65;**: The Product ID in the Excel file as described in the[Create a SKU-Based Offer](doc:create-a-sku-based-offer) section and the **&#x73;kuId\*\* request parameter used in the Merchant Hosted Checkout Integration for SKU-based offer have the same function, Hence, after you create Product IDs on Dashboard, use them as values for the skuId parameter.
      </td>
    </tr>

    <tr>
      <td>
        sku\_details.sku\_name\
        **mandatory**
      </td>

      <td>
        * String \_ This parameter contains the SKU name.
      </td>
    </tr>

    <tr>
      <td>
        sku\_details.quantity\
        **mandatory**
      </td>

      <td>
        * String \_ The parameter must contain the quantity of SKU added in cart.
      </td>
    </tr>

    <tr>
      <td>
        sku\_details.amount\_per\_sku\
        **mandatory**
      </td>

      <td>
        * String \_ The parameter must contain the per SKU amount.
      </td>
    </tr>

    <tr>
      <td>
        sku\_details.offer\_key\
        **mandatory**
      </td>

      <td>
        * String\_ This parameter must contain the Offer Key(s) which can be used for this transaction. |
      </td>
    </tr>

    <tr>
      <td>
        sku\_details.offer\_auto\_apply\
        **mandatory**
      </td>

      <td>
        * String\_This parameter contains the flag for when to enable auto application of best offer on this SKU. 
      </td>
    </tr>
  </tbody>
</Table>

#### cart\_details object in sample request

```curl
"cart_details": {
    "amount": 55000,
    "items": 2,
    "surcharges": 10,
    "pre_discount": 5,
    "sku_details": [
      {
        "sku_id": "smartphone234",
        "sku_name": "Smartphone",
        "amount_per_sku": "45000",
        "quantity": 1,
        "offer_key": null,
        "offer_auto_apply": true
      },
      {
        "sku_id": "smartwatch132",
        "sku_name": "Smartwatch",
        "amount_per_sku": "10000",
        "quantity": 1,
        "offer_key": [
          "flat500@2022"
        ],
        "offer_auto_apply": false
      }
    ]
  }
```

Sample request

```curl
curl -X POST "https://test.payu.in/_payment" \
-H "accept: application/json" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "key=JP***g" \
-d "txnid=ewP8oRopzdHEtC" \
-d "amount=10.00" \
-d "firstname=Ashish" \
-d "email=test@gmail.com" \
-d "phone=9876543210" \
-d "productinfo=iPhone" \
-d "surl=https://apiplayground-response.herokuapp.com/" \
-d "furl=https://apiplayground-response.herokuapp.com/" \
-d 'cart_details={
  "amount": 55000,
  "items": 2,
  "surcharges": 10,
  "pre_discount": 5,
  "sku_details": [
    {
      "sku_id": "smartphone234",
      "sku_name": "Smartphone",
      "amount_per_sku": "45000",
      "quantity": 1,
      "offer_key": null,
      "offer_auto_apply": true
    },
    {
      "sku_id": "smartwatch132",
      "sku_name": "Smartwatch",
      "amount_per_sku": "10000",
      "quantity": 1,
      "offer_key": ["flat500@2022"],
      "offer_auto_apply": false
    }
  ]
}' \
-d "hash=bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"

```
```javascript
/**
 * PayU Payment Integration with Cart Details using Fetch API
 * 
 * IMPORTANT: This should be implemented on the server side for security.
 * Never handle payments in browser-side code.
 */

// Cart details object
const cartDetails = {
  "amount": 55000,
  "items": 2,
  "surcharges": 10,
  "pre_discount": 5,
  "sku_details": [
    {
      "sku_id": "smartphone234",
      "sku_name": "Smartphone",
      "amount_per_sku": "45000",
      "quantity": 1,
      "offer_key": null,
      "offer_auto_apply": true
    },
    {
      "sku_id": "smartwatch132",
      "sku_name": "Smartwatch",
      "amount_per_sku": "10000",
      "quantity": 1,
      "offer_key": ["flat500@2022"],
      "offer_auto_apply": false
    }
  ]
};

// Payment data
const paymentData = new FormData();
paymentData.append('key', 'JP***g');
paymentData.append('txnid', 'ewP8oRopzdHEtC');
paymentData.append('amount', '10.00');
paymentData.append('firstname', 'Ashish');
paymentData.append('email', 'test@gmail.com');
paymentData.append('phone', '9876543210');
paymentData.append('productinfo', 'iPhone');
paymentData.append('surl', 'https://apiplayground-response.herokuapp.com/');
paymentData.append('furl', 'https://apiplayground-response.herokuapp.com/');
paymentData.append('cart_details', JSON.stringify(cartDetails));
paymentData.append('hash', 'bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319');

// Convert FormData to URLSearchParams for fetch
const searchParams = new URLSearchParams();
for (const pair of paymentData) {
  searchParams.append(pair[0], pair[1]);
}

// Fetch configuration
const fetchOptions = {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  body: searchParams
};

// Make the API call
fetch('https://test.payu.in/_payment', fetchOptions)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.text(); // PayU may not always return JSON
  })
  .then(data => {
    console.log('Payment initiated:', data);
    // Process the payment response here
  })
  .catch(error => {
    console.error('Payment request failed:', error);
  });

```
```python
import json
import urllib.request
import urllib.parse

def process_payu_payment():
    """Process a PayU payment with cart details"""
    
    # API endpoint
    url = "https://test.payu.in/_payment"
    
    # Cart details as a dictionary
    cart_details = {
        "amount": 55000,
        "items": 2,
        "surcharges": 10,
        "pre_discount": 5,
        "sku_details": [
            {
                "sku_id": "smartphone234",
                "sku_name": "Smartphone",
                "amount_per_sku": "45000",
                "quantity": 1,
                "offer_key": None,
                "offer_auto_apply": True
            },
            {
                "sku_id": "smartwatch132",
                "sku_name": "Smartwatch",
                "amount_per_sku": "10000",
                "quantity": 1,
                "offer_key": ["flat500@2022"],
                "offer_auto_apply": False
            }
        ]
    }
    
    # Payment data dictionary
    data = {
        "key": "JP***g",
        "txnid": "ewP8oRopzdHEtC",
        "amount": "10.00",
        "firstname": "Ashish",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "productinfo": "iPhone",
        "surl": "https://apiplayground-response.herokuapp.com/",
        "furl": "https://apiplayground-response.herokuapp.com/",
        "cart_details": json.dumps(cart_details),
        "hash": "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
    }
    
    # Encode the data dictionary
    data_encoded = urllib.parse.urlencode(data).encode('utf-8')
    
    # Set up request headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    try:
        # Create request object
        req = urllib.request.Request(url, data=data_encoded, headers=headers, method="POST")
        
        # Send request and get response
        with urllib.request.urlopen(req) as response:
            status_code = response.getcode()
            response_body = response.read().decode('utf-8')
            
            print(f"Status code: {status_code}")
            print(f"Response: {response_body}")
            
            return {
                "status_code": status_code,
                "response": response_body
            }
            
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        error_data = e.read().decode('utf-8')
        print(f"Error details: {error_data}")
        
        return {
            "status_code": e.code,
            "error": e.reason,
            "details": error_data
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "status_code": 0,
            "error": str(e)
        }

# Call the function to process payment
if __name__ == "__main__":
    result = process_payu_payment()
    print("Payment processing complete.")

```
```php
<?php
/**
 * Process a PayU payment with cart details
 * 
 * @return array Response data
 */
function processPayuPayment() {
    // API endpoint
    $url = "https://test.payu.in/_payment";
    
    // Cart details as an array
    $cartDetails = [
        "amount" => 55000,
        "items" => 2,
        "surcharges" => 10,
        "pre_discount" => 5,
        "sku_details" => [
            [
                "sku_id" => "smartphone234",
                "sku_name" => "Smartphone",
                "amount_per_sku" => "45000",
                "quantity" => 1,
                "offer_key" => null,
                "offer_auto_apply" => true
            ],
            [
                "sku_id" => "smartwatch132",
                "sku_name" => "Smartwatch",
                "amount_per_sku" => "10000",
                "quantity" => 1,
                "offer_key" => ["flat500@2022"],
                "offer_auto_apply" => false
            ]
        ]
    ];
    
    // Payment data array
    $data = [
        "key" => "JP***g",
        "txnid" => "ewP8oRopzdHEtC",
        "amount" => "10.00",
        "firstname" => "Ashish",
        "email" => "test@gmail.com",
        "phone" => "9876543210",
        "productinfo" => "iPhone",
        "surl" => "https://apiplayground-response.herokuapp.com/",
        "furl" => "https://apiplayground-response.herokuapp.com/",
        "cart_details" => json_encode($cartDetails),
        "hash" => "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
    ];
    
    // Initialize cURL session
    $ch = curl_init($url);
    
    // Set cURL options
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        "Accept: application/json",
        "Content-Type: application/x-www-form-urlencoded"
    ]);
    
    // Execute cURL request
    $response = curl_exec($ch);
    $statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $error = curl_error($ch);
    
    // Close cURL session
    curl_close($ch);
    
    // Check for errors
    if ($error) {
        return [
            "status_code" => 0,
            "error" => $error
        ];
    }
    
    // Return successful response
    return [
        "status_code" => $statusCode,
        "response" => $response
    ];
}

// Process the payment
$result = processPayuPayment();

// Display results
echo "Status Code: " . $result["status_code"] . "\n";
if (isset($result["error"])) {
    echo "Error: " . $result["error"] . "\n";
} else {
    echo "Response: " . $result["response"] . "\n";
}
?>

```
```java
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

public class PayuPaymentProcessor {
    
    public static void main(String[] args) {
        try {
            PaymentResponse response = processPayment();
            System.out.println("Status Code: " + response.getStatusCode());
            if (response.isSuccess()) {
                System.out.println("Response: " + response.getResponse());
            } else {
                System.out.println("Error: " + response.getError());
            }
        } catch (Exception e) {
            System.err.println("Processing failed: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    public static PaymentResponse processPayment() throws IOException {
        // API endpoint
        String url = "https://test.payu.in/_payment";
        
        // Create cart details JSON
        String cartDetailsJson = "{"
            + "\"amount\": 55000,"
            + "\"items\": 2,"
            + "\"surcharges\": 10,"
            + "\"pre_discount\": 5,"
            + "\"sku_details\": ["
            + "{"
            + "\"sku_id\": \"smartphone234\","
            + "\"sku_name\": \"Smartphone\","
            + "\"amount_per_sku\": \"45000\","
            + "\"quantity\": 1,"
            + "\"offer_key\": null,"
            + "\"offer_auto_apply\": true"
            + "},"
            + "{"
            + "\"sku_id\": \"smartwatch132\","
            + "\"sku_name\": \"Smartwatch\","
            + "\"amount_per_sku\": \"10000\","
            + "\"quantity\": 1,"
            + "\"offer_key\": [\"flat500@2022\"],"
            + "\"offer_auto_apply\": false"
            + "}"
            + "]"
            + "}";
        
        // Create parameter map
        Map<String, String> params = new HashMap<>();
        params.put("key", "JP***g");
        params.put("txnid", "ewP8oRopzdHEtC");
        params.put("amount", "10.00");
        params.put("firstname", "Ashish");
        params.put("email", "test@gmail.com");
        params.put("phone", "9876543210");
        params.put("productinfo", "iPhone");
        params.put("surl", "https://apiplayground-response.herokuapp.com/");
        params.put("furl", "https://apiplayground-response.herokuapp.com/");
        params.put("cart_details", cartDetailsJson);
        params.put("hash", "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319");
        
        // Build request body
        StringBuilder postData = new StringBuilder();
        for (Map.Entry<String, String> param : params.entrySet()) {
            if (postData.length() != 0) postData.append('&');
            postData.append(URLEncoder.encode(param.getKey(), "UTF-8"));
            postData.append('=');
            postData.append(URLEncoder.encode(param.getValue(), "UTF-8"));
        }
        byte[] postDataBytes = postData.toString().getBytes(StandardCharsets.UTF_8);
        
        // Create connection
        URL apiUrl = new URL(url);
        HttpURLConnection conn = (HttpURLConnection) apiUrl.openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Accept", "application/json");
        conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
        conn.setRequestProperty("Content-Length", String.valueOf(postDataBytes.length));
        conn.setDoOutput(true);
        
        // Send request
        try (DataOutputStream outputStream = new DataOutputStream(conn.getOutputStream())) {
            outputStream.write(postDataBytes);
        }
        
        // Get response code
        int responseCode = conn.getResponseCode();
        
        // Read response
        StringBuilder response = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(
                    responseCode >= 400 ? conn.getErrorStream() : conn.getInputStream(), 
                    StandardCharsets.UTF_8))) {
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
        }
        
        // Return response data
        return new PaymentResponse(responseCode, response.toString(), null);
    }
    
    public static class PaymentResponse {
        private final int statusCode;
        private final String response;
        private final String error;
        
        public PaymentResponse(int statusCode, String response, String error) {
            this.statusCode = statusCode;
            this.response = response;
            this.error = error;
        }
        
        public int getStatusCode() {
            return statusCode;
        }
        
        public String getResponse() {
            return response;
        }
        
        public String getError() {
            return error;
        }
        
        public boolean isSuccess() {
            return statusCode >= 200 && statusCode < 300;
        }
    }
}

```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace PayuPaymentIntegration
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var paymentProcessor = new PayuPaymentProcessor();
            var result = await paymentProcessor.ProcessPaymentAsync();
            
            Console.WriteLine($"Status Code: {result.StatusCode}");
            if (result.IsSuccess)
            {
                Console.WriteLine($"Response: {result.ResponseContent}");
            }
            else
            {
                Console.WriteLine($"Error: {result.Error}");
            }
        }
    }
    
    public class PayuPaymentProcessor
    {
        private readonly string _apiEndpoint = "https://test.payu.in/_payment";
        
        public async Task<PaymentResponse> ProcessPaymentAsync()
        {
            try
            {
                // Create cart details object
                var cartDetails = new
                {
                    amount = 55000,
                    items = 2,
                    surcharges = 10,
                    pre_discount = 5,
                    sku_details = new[]
                    {
                        new {
                            sku_id = "smartphone234",
                            sku_name = "Smartphone",
                            amount_per_sku = "45000",
                            quantity = 1,
                            offer_key = (object)null,
                            offer_auto_apply = true
                        },
                        new {
                            sku_id = "smartwatch132",
                            sku_name = "Smartwatch",
                            amount_per_sku = "10000",
                            quantity = 1,
                            offer_key = new[] { "flat500@2022" },
                            offer_auto_apply = false
                        }
                    }
                };
                
                // Serialize cart details to JSON
                string cartDetailsJson = JsonSerializer.Serialize(cartDetails);
                
                // Create form parameters
                var formContent = new Dictionary<string, string>
                {
                    { "key", "JP***g" },
                    { "txnid", "ewP8oRopzdHEtC" },
                    { "amount", "10.00" },
                    { "firstname", "Ashish" },
                    { "email", "test@gmail.com" },
                    { "phone", "9876543210" },
                    { "productinfo", "iPhone" },
                    { "surl", "https://apiplayground-response.herokuapp.com/" },
                    { "furl", "https://apiplayground-response.herokuapp.com/" },
                    { "cart_details", cartDetailsJson },
                    { "hash", "bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319" }
                };
                
                // Create HttpClient
                using (var httpClient = new HttpClient())
                {
                    // Set headers
                    httpClient.DefaultRequestHeaders.Add("Accept", "application/json");
                    
                    // Create form content
                    var content = new FormUrlEncodedContent(formContent);
                    
                    // Send request
                    var response = await httpClient.PostAsync(_apiEndpoint, content);
                    
                    // Get response content
                    string responseContent = await response.Content.ReadAsStringAsync();
                    
                    // Return response data
                    return new PaymentResponse
                    {
                        StatusCode = (int)response.StatusCode,
                        IsSuccess = response.IsSuccessStatusCode,
                        ResponseContent = responseContent,
                        Error = response.IsSuccessStatusCode ? null : "Request failed"
                    };
                }
            }
            catch (Exception ex)
            {
                // Return error
                return new PaymentResponse
                {
                    StatusCode = 0,
                    IsSuccess = false,
                    ResponseContent = null,
                    Error = $"Exception: {ex.Message}"
                };
            }
        }
    }
    
    public class PaymentResponse
    {
        public int StatusCode { get; set; }
        public bool IsSuccess { get; set; }
        public string ResponseContent { get; set; }
        public string Error { get; set; }
    }
}

```

<br />

#### Step 2: Check the PayU response

**Success scenario**

The **cart\_details** JSON Object in the response (sample):

```
{"cart_details": {
    "id": "18",
    "payu_id": "999000000000983",
    "total_items": "2",
    "total_cart_amount": "55000",
    "offer_applied": null,
    "offer_availed": null,
    "instant_discount": "1000",
    "cashback_discount": "500",
    "total_discount": "1500",
    "net_cart_amount": "54000",
    "created_at": null,
    "updated_at": null,
    "sku_details": [
      {
        "id": "35",
        "cart_id": "18",
        "payu_id": "999000000000983",
        "mid": "180012",
        "sku_id": "smartphone234",
        "sku_name": "Smartphone",
        "amount_per_sku": "45000.00",
        "quantity": "1",
        "amount_before_discount": "45000",
        "discount": "1000",
        "amount_after_discount": "44000",
        "offer_key": null,
        "offer_status": null,
        "offer_type": null,
        "created_at": null,
        "updated_at": null
      },
      {
        "id": "36",
        "cart_id": "18",
        "payu_id": "999000000000983",
        "mid": "180012",
        "sku_id": "smartwatch132",
        "sku_name": "Smartwatch",
        "amount_per_sku": "10000.00",
        "quantity": "1",
        "amount_before_discount": "10000.00",
        "discount": "500",
        "amount_after_discount": "10000.00",
        "offer_key": null,
        "offer_status": null,
        "offer_type": null,
        "created_at": null,
        "updated_at": null
      }
    ]
  }}
```

**Failure scenarios**

For a list of error messages for the failure scenarios, refer to [Error Codes for Offers Integration](doc:error-codes-for-offers-integration).

#### Step 3: Verify Payment

Verify the payment using the **Verify Payment** API. For more information, For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>. For the sample response using the **Verify Payment** API from PayU involving offers, refer to <a href="addl-info-general-apis#sample-response" target="_blank">Additional Info for General APIsI</a>.
