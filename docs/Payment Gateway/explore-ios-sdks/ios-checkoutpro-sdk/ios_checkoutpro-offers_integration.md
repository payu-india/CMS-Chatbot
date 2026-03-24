---
title: Create SKU Based Offers for iOS Checkout Pro
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
PayU allows merchants to create offers for specific Products/SKUs in the cart and for whole cart. SKU offers will be shown only when the specific product is added by the user and hence can be used by the merchant to promote specific products.

# Create an offer on dashboard

1. Merchant Creates offers on dashboard. For SKU offers they need to provide product details with skuid, sku price range.
2. Merchant pass these sku details and user token when he initialising CheckoutPro SDK.
3. SDK fetch offers from PayU Server and show list of offers.
4. User can select any offer and can see  the benefit (instant/ cashback) of offer.
5. If user did not select any offer, PayU will auto apply best offer.
6. User can pay offered amount and can avail offers.

# Steps to integrate

<Accordion title="Step 1: Update dependencies" icon="fa-code">
  Add the following dependencies:

  * **Cocoapods**: Use PayUIndia-CheckoutPro version 7.5.1.

  ```
  pod 'PayUIndia-CheckoutPro'
  ```

  * **SPM**: Use PayUIndia-CheckoutPro version 7.5.1.

  ```
  .package(name: "PayUIndia-CheckoutPro", url: "https://github.com/payu-intrepos/PayUCheckoutPro-iOS", from: "7.5.1")
  ```
</Accordion>

<Accordion title="Step 2: Initialise the SDK" icon="fa-code">
  > 🚧 Make sure you integrate with CheckoutPro SDK for iOS
  >
  > For step to integrate Checkoutpro in App, refer to [Checkout Pro Integration Steps](https://docs.payu.in/docs/ios-checkout-pro-sdk-integration-steps/)
</Accordion>

<Accordion title="Step 3: Create SKU Details" icon="fa-code">
  Initalise Object of Sku details with vaild SKU's.

  ```swift
  PayUSkuDetails: It contains below properties
  PayUSkuDetails(skus: [SKU])
  skus: "<Array of SKU's>"

  PayUSku(
      skuId: String,
      skuName: String,
      skuAmount: String,
      quantity: Int,
      offerKeys:[String]? = nil
  )

  skuId: "<Product Id which you use when creating offer on dashboard >"
  skuName: "<Name of product>"
  skuAmount: "<Amount of product>"
  quantity: "<total quantity of product>"
  offerKeys: "<Optional - Provide offer keys only if want to restrict offer for mention products, else set null>"

   
  ```

  <Accordion title="Step 4: Set SKU Details" icon="fa-code">
    Create list of SKU as per products added in cart and add this list in SKU details. and set sku detials to PayUPaymentParams.

    ```swift
    let paymentParam = PayUPaymentParam(key: <String>,
                                        transactionId: <String>,
                                        amount: <String>,
                                        productInfo: <String>,
                                        firstName: <String>,
                                        email: <String>,
                                        phone: <String>,
                                        surl: <String>,//Pass your own surl
                                        furl: <String>,//Pass your own furl
                                        environment: <Environment> /*.production or .test*/)
                                        
    paymentParam.skuDetail = <create SKU Details as mention above and provide here>
    ```

    <Callout icon="📘" theme="info">
      **Note**: If you are adding details of SKU offers, the amount passed in `PayUPaymentParam` must be equal to the sum of quantities \* `skuAmount` of each item.
    </Callout>
  </Accordion>
</Accordion>

<Accordion title="Step 5: Generate the hash" icon="fa-code">
  This integration requires dynamic hashes. You must get hash string in map again `HashConstant.hashString` key in `generateHash`.  You need to send this string to server and append salt there, after appending salt convert string to sha512 hash and return back to SDK.

  ```swift
  /// Use this function to provide hashes
  /// - Parameters:
  ///   - param: Dictionary that contains key as HashConstant.hashName & HashConstant.hashString
  ///   - onCompletion: Once you fetch the hash from server, pass that hash with key as param[HashConstant.hashName]
  func generateHash(for param: DictOfString, onCompletion: @escaping PayUHashGenerationCompletion) {
      // Send this string to your backend and append the salt at the end and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      let hashStringWithoutSalt = param[HashConstant.hashString] ?? ""
      // Or you can send below string hashName to your backend and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      let hashName = param[HashConstant.hashName] ?? ""

      // Set the hash in below string which is fetched from your server
      let hashFetchedFromServer = <#T##String#>
      
      onCompletion([hashName : hashFetchedFromServer])
  }
  ```
</Accordion>
