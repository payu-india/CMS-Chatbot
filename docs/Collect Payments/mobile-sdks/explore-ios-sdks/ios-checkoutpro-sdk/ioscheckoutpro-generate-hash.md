---
title: Generate Dynamic Hash
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The dynamic hashes must be generated at runtime for each transaction and will vary based on the transaction parameters.

> 📘 Hashing logic for SDK and Web Integration is different
>
> For the hashing logic for web integration, refer to [Generate Hash](doc:generate-hash-payu-hosted).

## Recommended workflow for Dynamic Hashing

<Image align="center" className="border" width="75% " border={true} src="https://files.readme.io/4878cbbef311b7f916e2cc5db202912e549a84ae80f10365a039b0f67a365cd3-dynamic_hash_1.png" />

1. Checkout Pro SDK will generate hash like `generateHash(Map<String, String> hashMap).` `PayUHashGenerationResult` method is called with the prepared map.
2. Merchant App will: 
   * Extract values for keys `PayUCheckoutProConstants.CP_HASH_NAME` and `PayUCheckoutProConstants.CP_HASH_STRING` from the hashmap received in the `generateHash()` method.
   * Pass this hash string to your server (Merchant Server) for hash calculation.
3. Merchant Server will append the hash string that was received with a salt at the end to form a pipe-separated string.
4. Merchant Server will generate a SHA-512 hash from this string.
5. Merchant App will: 
   * Prepare a map with the key as the value of `PayUCheckoutProConstants.CP_HASH_NAME` received in step 2 and its value as the hash received in Step 3. 
   * Send this map instead of `PayUHashGenerationResult` that was received in Step 1.

## Procedure

For passing dynamic hashes, you will receive a call on the generateHash method of PayUCheckoutProListener.

In the method parameter, you will receive a dictionary or hashMap, extract the value of hashString from that. Pass that value to the server, and now the server will append salt at the end and generate sha512 hash over it. The server will give that hash back to your app, and the app will provide that hash to PayU through a callback mechanism.

There is no need to know the formula for dynamic hashes because PayU SDK gives you the string containing all the required parameters. Your server has to append salt at the end and generate sha512 hash over it.

The following table provides the list of dynamic hashes:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Hash Name
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        getBinInfo
      </td>

      <td>
        It is used to fetch Bin details. If not passed, card payments will not happen. For more info refer to: [GetBinInfo](https://docs.payu.in/reference/get_bin_info_api)
      </td>
    </tr>

    <tr>
      <td>
        get\_eligible\_payment  

        * options
      </td>

      <td>
        It is used when verifying Phone number in OlaMoney Section. If not passed, phone number will not be verified and hence user will not be able to proceed. For more info refer to: get\_eligible\_payment\_options
      </td>
    </tr>

    <tr>
      <td>
        validateVPA
      </td>

      <td>
        It is used for validating VPA on UPI Collect screen. If not passed, VPA will not be verified and hence user will not be able to proceed. For more info refer to: [VPA Validation](https://docs.payu.in/reference/validate_vpa_api)
      </td>
    </tr>

    <tr>
      <td>
        get\_checkout\_details
      </td>

      <td>
        It is used to get detail of additional charges, down status, tax info, offer.
      </td>
    </tr>

    <tr>
      <td>
        lookup api hash
      </td>

      <td>
        It is used to fetch the Multi Currency Conversion details. This is used in MCP Integration.  

        * \*Note\*\*: You need to calculate HMAC-SHA1 instead of SHA512 only for this hash.
      </td>
    </tr>

    <tr>
      <td>
        checkBalanceApiHash
      </td>

      <td>
        It is used to get sodexocard detail.
      </td>
    </tr>

    <tr>
      <td>
        postSalt
      </td>

      <td>
        It is required to split payment during transaction
      </td>
    </tr>
  </tbody>
</Table>

## V2 Hashes

For passing V2 dynamic hashes, you will receive a call on the generateHash method of `PayUCheckoutProListener`.

In the method parameter, you will receive a dictionary or hashMap, and extract the value of hashString and hashType from that. if hashType is “V2” Pass that value to the server, and now the server generate sha256 hash with salt as key and hashString as signedString over it. The server will give that hash back to your app, and the app will provide that hash to PayU through a callback mechanism.
