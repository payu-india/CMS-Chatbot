---
name: Dynamic Hash Generation
---
The dynamic hashes must be generated at runtime for each transaction and will vary based on the transaction parameters.

> 📘 Hashing logic for SDK and Web Integration is different
> 
> For the hashing logic for web integration, refer to [Generate Hash](doc:generate-hash-payu-hosted).

## Recommended workflow for Dynamic Hashing

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/04949cb-Screenshot_2023-11-16_at_6.14.14_PM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "75% ",
      "border": true
    }
  ]
}
[/block]


1. Checkout Pro SDK will generate hash like `generateHash(Map<String, String> hashMap).` `PayUHashGenerationResult` method is called with the prepared map.
2. Merchant App will: 
   - Extract values for keys `PayUCheckoutProConstants.CP_HASH_NAME` and `PayUCheckoutProConstants.CP_HASH_STRING` from the hashmap received in the `generateHash()` method.
   - Pass this hash string to your server (Merchant Server) for hash calculation.
3. Merchant Server will append the hash string that was received with a salt at the end to form a pipe-separated string.
4. Merchant Server will generate a SHA-512 hash from this string.
5. Merchant App will: 
   - Prepare a map with the key as the value of `PayUCheckoutProConstants.CP_HASH_NAME` received in step 2 and its value as the hash received in Step 3. 
   - Send this map instead of `PayUHashGenerationResult` that was received in Step 1.

## Procedure

For passing dynamic hashes, you will receive a call on the generateHash method of PayUCheckoutProListener.

In the method parameter, you will receive a dictionary or hashMap, extract the value of hashString from that. Pass that value to the server, and now the server will append salt at the end and generate sha512 hash over it. The server will give that hash back to your app, and the app will provide that hash to PayU through a callback mechanism.

There is no need to know the formula for dynamic hashes because PayU SDK gives you the string containing all the required parameters. Your server has to append salt at the end and generate sha512 hash over it.

The following table provides the list of dynamic hashes:

[block:parameters]
{
  "data": {
    "h-0": "Hash Name",
    "h-1": "Description",
    "0-0": "getBinInfo",
    "0-1": "It is used to fetch Bin details. If not passed, card payments will not happen. For more info refer to: [GetBinInfo](https://docs.payu.in/reference/get_bin_info_api)",
    "1-0": "get_eligible_payment  \n\\_options",
    "1-1": "It is used when verifying Phone number in OlaMoney Section. If not passed, phone number will not be verified and hence user will not be able to proceed. For more info refer to: get_eligible_payment_options",
    "2-0": "validateVPA",
    "2-1": "It is used for validating VPA on UPI Collect screen. If not passed, VPA will not be verified and hence user will not be able to proceed. For more info refer to: [VPA Validation](https://docs.payu.in/reference/validate_vpa_api)",
    "3-0": "get_checkout_details",
    "3-1": "It is used to get detail of additional charges, down status, tax info, offer.",
    "4-0": "lookup api hash",
    "4-1": "It is used to fetch the Multi Currency Conversion details. This is used in MCP Integration.  \n**Note**: You need to calculate HMAC-SHA1 instead of SHA512 only for this hash.",
    "5-0": "checkBalanceApiHash",
    "5-1": "It is used to get sodexocard detail.",
    "6-0": "postSalt",
    "6-1": "It is required to split payment during transaction"
  },
  "cols": 2,
  "rows": 7,
  "align": [
    "left",
    "left"
  ]
}
[/block]