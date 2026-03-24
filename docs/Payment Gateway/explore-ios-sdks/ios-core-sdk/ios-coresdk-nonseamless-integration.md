---
title: Non-seamless Integration
excerpt: Use the prebuilt checkout UI provided by the Core SDK
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
To integrate with iOS SDK, download the latest sample app from GitHub using the following link: [https://github.com/payu-intrepos/iOS-SDK-Sample-App/releases/​](https://github.com/payu-intrepos/iOS-SDK-Sample-App/releases/​)

> 📘 Note:
>
> Before proceeding further, make sure you have read SDK Integration document.​

Perform the following steps as prerequisites:

1. Add `libz.tbd` libraries into your project (Project > Build Phases > Link Binary with Libraries).
2. Add -ObjC and $(OTHER\_LDFLAGS) in Other Linker Flags in the project build settings (Project->Build Settings->Other Linker Flags).
3. To run the app on Apple iOS 9, add the following code snippet in info.plist:

```Text XML
<key>NSAppTransportSecurity</key>
   <dict>
   <key>NSAllowsArbitraryLoads</key>
   <true/>
   </dict>
```

## Integration steps

To integrate with SDK’s inbuilt UI:

1. Drag and drop the PayU folder into your app and Add the following property in `AppDelegate.h`: `@property (weak, nonatomic) UIViewController *paymentOptionVC;`
2. Open the checkout view controller of your app from where you want to start the payment process and import the following file:

```Text Swift
#import "PUUIPaymentOptionVC.h
```

3. Set the `paymentparam` on the Pay button similar to the following code block:

```Text Swift
PayUModelPaymentParams *paymentParam = [[PayUModelPaymentParams alloc] init];
PayUModelHashes *hashes = [[PayUModelHashes alloc] init];// Set the hashes here
paymentParam.key = @"gtKFFx";
paymentParam.transactionID = @"txnID20170220";
paymentParam.amount = @"10";
paymentParam.productInfo = @"iPhone";
paymentParam.SURL = @"https://payu.herokuapp.com/success";
paymentParam.FURL = @"https://payu.herokuapp.com/failure";
paymentParam.firstName = @"Baalak";
paymentParam.email = @"Baalak@gmail.com";
paymentParam.udf1 = @"";
paymentParam.udf2 = @"";
paymentParam.udf3 = @"";
paymentParam.udf4 = @"";
paymentParam.udf5 = @"";            
​
paymentParam.hashes = hashes;
  // Set this property if you want to get the stored cards:
paymentParam.userCredentials = @"gtKFFx:Baalak@gmail.com";
​
// Set the environment according to merchant key ENVIRONMENT_PRODUCTION for Production & 
// ENVIRONMENT_TEST for test environment:
paymentParam.environment = ENVIRONMENT_TEST;
​
// Set this property if you want to give offer:
paymentParam.offerKey = @"";
```

4. Call the `getPayUPaymentRelatedDetailForMobileSDK:paymentParam` method of `PayUWebServiceResponse `class to get the payment-related details:

```Text Swift
PayUWebServiceResponse *webServiceResponse =[[PayUWebServiceResponse alloc]init];
 [webServiceResponse 
 getPayUPaymentRelatedDetailForMobileSDK:paymentParam
 withCompletionBlock:^(PayUModelPaymentRelatedDetail *paymentRelatedDetails,
 NSString *errorMessage, id extraParam) {
​
 if (!errorMessage) {
 UIStoryboard *stryBrd = [UIStoryboard
 storyboardWithName:@"PUUIMainStoryBoard" bundle:nil];
 PUUIPaymentOptionVC * paymentOptionVC = 
 [stryBrd instantiateViewControllerWithIdentifier:VC_IDENTIFIER_PAYMENT_OPTION];
​
 paymentOptionVC.paymentParam = paymentParam;
 paymentOptionVC.paymentRelatedDetail = paymentRelatedDetails;
​
 [self.navigationController pushViewController:paymentOptionVC animated:true];
​
 }
 else{
 // error occurred while creating the request
 }
 }];
```

5. Add an observer similar to the following code snippet so that after the payment gets successful, fails, cancels or any stored card gets deleted, the SDK fires a notification to any registered observers.

```Text Swift
[[NSNotificationCenter defaultCenter]
 addObserver:self selector:@selector(responseReceived:) 
 name:kPUUINotiPaymentResponse object:nil];
​
 -(void)responseReceived:(NSNotification *) notification{
​
 NSString *strConvertedRespone = [NSString stringWithFormat:@"%@",notification.object];
NSLog(@"Response Received %@",strConvertedRespone);
```

6. Calculate the hashes. For example, refer to the following code snippet:

> ❗️ Callout
>
> Calculate all the hashes and assign `tostrEmail` using the `paymentOptionsVC.allHashDict method`. For more information on how to calculate the hash.Hashes and provided to `paymentOptionsVC.allHashDict` in Key-Value Pair, refer to Hash Generation.

```Text Swift
{
         "check_offer_status_hash" = 22e773e2079e9c2249c230b1ee096efcc2555b214fe291293d5a109e65030dda2cd355d4db97751d9c1f43c5e055b347e3d4e2939830bdc1f5f48845899e5bf1;
         "delete_user_card_hash" = 793eed65afe4aaf1ddf89506093a57907a16fdd38e5c52050d7b5380e658c4300e221fa5f7da7b40ac213238b427e8d0dcc6a33bd5efe075d4261c01f143cb4e;
         "edit_user_card_hash" = 20d3ea6b9bc964e8548c8fd3fc1a9e3daa948a0226511abdd3679d77c8c54131775b7f6d3dc3589389f47edaec2906b2381033d88c1aef1920204b4989f636c9;
         "get_merchant_ibibo_codes_hash" = 307374123fb8d720d41361470984947f7f5c33ac4832598149bf1d108ea9b2ccefd7b46fe4ee4c021f67838a67f355a74f3c2d79bb37373d3b248a802c7159e2;
         "get_user_cards_hash" = dfac3cd3fe9599ceba79efc9ddd48e28cbd8fd47ab2e4ae8a3b5f6f5be559e9dbbc8328298fb224a4e0769b1c328d1b87f59354bbec3c4eb101acc968fde0508;
         "payment_hash" = 19c70354c7184da415a3a22c380235727e8d1e0aa3422e0b1cb6f40d9258e363a0dd37d611563e67fc8bd3be26960a54cba97de5b7588f323151f97c4f11dd06;
         "payment_related_details_for_mobile_sdk_hash" = 633369f45e3b98c100871be3cb8f5c631132a5d06b83c2fc1e6a12302ab7386fc23ca53fb9f9182518b6affca6b6fe5dad170ae087b7716b11f8ddc07899590e;
         "save_user_card_hash" = 09fb415be88e40de0d5c746f2ca4f7620dcf62eb2cf0da7cb0c2080eb36fed3290607b5b4bf890f2f8f5399bd72a41db18160c430c16079131272e7ce0c17a56;
          "vas_for_mobile_sdk_hash" = 7da0f4fef5bab0e5034f37f9503bdcbede00cc2cd0cf6cbb4e43baa9d57f05680305885199e2b0d38e8cf12895fd06f4d3dd3fb422535feeb555adc58e2cf3cc;
}
```
