---
title: Offer APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Offer APIs - Core iOS SDK
  description: ''
  robots: index
next:
  description: ''
---
This section includes the offer APIs for iOS Core SDK:

* [Fetch Offer Details API](#fetch-offer-details-api)
* [Validate Offer Details API](#validate-offer-details-api)
* ## Fetch Offer Details API

Use the **Fetch Offer Details** API to fetch all the offer list available for the merchant.

> 📘 Hash Generation Logic
>
> In `completionBlockForHashGeneration`, you will get hash string without salt so you need to append the salt at the end of this hash string and convert using sha512 and pass that value in hash completion as passing below in the code. 
>
> For more information, refer to [Generate Static Hash](doc:generate-static-hash-ios).

### Integration

1. Set amount and userToken inside your payment parameters for instance

```Text Swift
        paymentParamForPassing.amount = "amount"
        paymentParamForPassing.offerParams = PayUModelOfferParams()
        paymentParamForPassing.offerParams?.userToken = "Any default Value"
```

2. Call the `getAllOfferDetails()` method to integrate this API as described in the following code block

```Text Swift
 webServiceResponse?.getAllOfferDetails(paymentParamForPassing, completionBlockForHashGeneration: { json, hashcompletion in
                if let hashDict = json as? [String: String] {
                let hashName = hashDict["hashName"] ?? ""
                let hashStringWithoutSalt = hashDict["hashString"] ?? ""
                    let hashWithSalt = hashStringWithoutSalt.appending(kSalt)
                    let hash = hashWithSalt.sha512()
                    hashcompletion!([hashName : hash])
                }
            },
            completionBlockForAPIResponse: { [weak self] offerDetails, errorMsg, _ in
                print("offerDetails......\(offerDetails)")
            })
```

## Validate Offer Details API

Use the **Validate Offer Details** API to validate the offer available for the merchant.

> 📘 Hash Generation Logic
>
> In `completionBlockForHashGeneration`. you will get hash string without salt so you need to append the salt at the end of this hash string and convert using sha512 and pass that value in hash completion as passing below in the code.

### Integration

1. Set amount and userToken inside your payment parameters for instance

```Text Swift
        paymentParamForPassing.amount = "amount"
        paymentParamForPassing.cardNumber = "Card Number"
        paymentParamForPassing.offerParams = PayUModelOfferParams()
        paymentParamForPassing.offerParams?.userToken = "Any default Value"
        paymentParamForPassing.offerParams?.offerKeys = ["Offer Key"]
        paymentParamForPassing.offerParams?.paymentCode = "CC/DC/NB"
        paymentParamForPassing.category = "CREDITCARD"
```

2. Call the `validateOfferDetails()` method to integrate this API as described in the following code block

```Text Swift
webServiceResponse?.validateOfferDetails(paymentParamForPassing, completionBlockForHashGeneration: { json, hashcompletion in
            if let hashDict = json as? [String: String] {
            let hashName = hashDict["hashName"] ?? ""
            let hashStringWithoutSalt = hashDict["hashString"] ?? ""
            let hashWithSalt = hashStringWithoutSalt.appending(kSalt)
            let hash = hashWithSalt.sha512()
            hashcompletion!([hashName : hash])
            }
        }, completionBlockForAPIResponse: { [weak self] offerDetails, errorMsg, json in
            print("offerDetails......\(offerDetails)")
        })
```
