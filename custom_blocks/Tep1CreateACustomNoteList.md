---
name: Tep1CreateACustomNoteList
---
Create a list of custom notes that you want to pass to the CheckoutPro SDK. For each custom note, custom_note and custom_note_category need to be passed.  

```swift Swift
class func paymentTypeFrom(paymentType: String?) -> PaymentType? {
        if (paymentType?.caseInsensitiveCompare("Cards") == .orderedSame) {
            return .ccdc
        } else if (paymentType?.caseInsensitiveCompare("NetBanking") == .orderedSame) {
            return .netBanking
        } else if (paymentType?.caseInsensitiveCompare("UPI") == .orderedSame) {
            return .upi
        } else if (paymentType?.caseInsensitiveCompare("Wallet") == .orderedSame) {
            return .wallet
        } else if (paymentType?.caseInsensitiveCompare("EMI") == .orderedSame) {
            return .emi
        } else if (paymentType?.caseInsensitiveCompare("SavedCard") == .orderedSame) {
            return .savedCard
        } else if (paymentType?.caseInsensitiveCompare("NeftRtgs") == .orderedSame) {
            return .neftRtgs
        } else if (paymentType?.caseInsensitiveCompare("Sodexo") == .orderedSame) {
            return .sodexo
        } else {
            return nil
        }
    }
```
