---
title: Integrate TPV
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
---
title: Integrate TPV
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    Integrate TPV with PayU iOS Core SDK: beneficiary validation, UPI TPV parameters, hash from server, and seamless TPV checkout.
  keywords:
    - payu ios core sdk tpv integration guide india
    - tpv third party verification upi sdk ios integration payu
    - ios payment gateway tpv beneficiary validation payu sdk
    - integrate tpv ios app payu core sdk seamless payment
    - iPhone upi tpv payment sdk integration steps payu
    - payment gateway ios tpv integration developer guide payu
    - payu ios coresdk third party verification flow integration
    - mobile upi tpv sdk ios native integration payu india
    - ios seamless payment tpv verification payu coresdk
    - upi collect intent tpv ios sdk integration payu
    - native ios tpv payment integration payu gateway sdk
    - server side hash tpv ios core sdk integration payu
  robots: index
next:
  description: ''
---
<Callout icon="📘" theme="info">
  **Note**: For TPV transactions, you need to have a different `merchantID`. Contact your key account manager for the same.
</Callout>

To integrate TPV with the BizSDK framework:

<Cards>
  <Card title="Step 1: Calculate hash" href="#step-1-calculate-hash" icon="fa-code">
    Calculate hash as the hash calculation formula is different from the result type of payment
  </Card>

  <Card title="Step 2: Make payment" href="#step-2-make-payment" icon="fa-card">
    Create an object of the class `PayUCreateRequest`
  </Card>

  <Card title="Step 3: Handle Response" href="#step-3-handle-response" icon="fa-reply">
    Handle the response from PayU
  </Card>
</Cards>

## Step 1: Calculate hash

For TPV transactions, the hash calculation formula is different from the result type of payment:

<Callout icon="📘" theme="info">
  **Note**: For multiple account numbers, account numbers should be pipe separated, and max four account numbers are allowed.
</Callout>

```
Hash Formula:
// For single account number
beneficiarydetail = "{'beneficiaryAccountNumber':'123456789'}"
// For multiple account number
beneficiarydetail = "{'beneficiaryAccountNumber':'123456789|54321234|98765673|34767988'}"
// Hash calculation
Hash = sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)
```

<Callout icon="📘" theme="info">
  **Reference**: For more information on Static Hashing, refer to [Generate Static Hash](doc:generate-static-hash-ios).
</Callout>

## Step 2: Make payment

To get a request, create an object of the class `PayUCreateRequest`` as in the following code snippet. The callbacks give you NSURLRequest as well as post parameters (in String). You can use these post parameters to initialize Custom Browser Instance.

```swift Swift
let createRequest = PayUCreateRequest()
```
```objectivec Objective-C
@property (nonatomic, strong) PayUCreateRequest *createRequest;
```

<Tabs>
  <Tab title="Net Banking">
    To pay using NetBanking, you need to configure the Net Banking parameters, for instance:

    ```Text Swift
    paymentParamForPassing.beneficiaryAccountNumbers = "123456789"
    paymentParamForPassing.bankCode = "AXNBTPV" //BankCode
    ```
    ```Text Objective-C
    self.paymentParamForPassing.beneficiaryAccountNumbers = @"123456789";
    self.paymentParamForPassing.bankCode = @"AXNBTPV"; //BankCode
    ```

    After setting the above parameters, you can get the request by using the createRequestWithPaymentParam method similar to the following code snippet:

    ```swift Swift
    createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_NET_BANKING, withCompletionBlock: { request, postParam, error in
    if error == nil {
    //It is good to go state. You can use request parameter in webview to open Payment Page
    } else {
    //Something went wrong with Parameter, error contains the error Message string
    }
    })
    ```
    ```objectivec Objective-C
    self.createRequest = [PayUCreateRequest new];
    [self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing forPaymentType:PAYMENT_PG_NET_BANKING withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
        if (error == nil) {
            //It is good to go state. You can use request parameter in webview to open Payment Page
        }
        else{
            //Something went wrong with Parameter, error contains the error Message string
        }
    }];
    ```
  </Tab>

  <Tab title="UPI">
    To pay using UPI, you need to configure the UPI parameters, for instance:

    ```swift Swift
    createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_UPI, withCompletionBlock: { request, postParam, error in
    if error == nil {
    //It is good to go state. You can use request parameter in webview to open Payment Page
    } else {
    //Something went wrong with Parameter, error contains the error Message string
    }
    })
    ```
    ```objectivec Objective-C
    // For single account number
    self.paymentParamForPassing.beneficiaryAccountNumbers = @"123456789";
    // For multiple account number
    self.paymentParamForPassing.beneficiaryAccountNumbers = @"123456789|54321234|98765673|34767988";
    // Set BankCode
    self.paymentParamForPassing.bankCode = @"UPITPV"; // UPITPV or TEZTPV
    // Set VPA
    self.paymentParamForPassing.vpa = @"umang@axis";
    ```

    After configuring the above parameters, you can get the request by using the `createRequestWithPaymentParam `method, for instance.

    ```swift Swift
    createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_UPI, withCompletionBlock: { request, postParam, error in
    if error == nil {
    //It is good to go state. You can use request parameter in webview to open Payment Page
    } else {
    //Something went wrong with Parameter, error contains the error Message string
    }
    })
    ```
    ```objectivec Objective-C
    self.createRequest = [PayUCreateRequest new];
    [self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing forPaymentType:PAYMENT_PG_UPI withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
        if (error == nil) {
            //It is good to go state. You can use request parameter in webview to open Payment Page
        }
        else{
            //Something went wrong with Parameter, error contains the error Message string
        }
    }];
    ```
  </Tab>
</Tabs>

## Step 3: Handle response

The procedure for response handling is similar to how you handle other payment options.