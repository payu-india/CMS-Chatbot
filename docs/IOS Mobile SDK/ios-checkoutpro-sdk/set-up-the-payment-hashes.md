---
title: Set up the Payment Hashes
excerpt: (Mandatory Step)
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
For details on static and dynamic hashes, check [Generate Hash](doc:ioscheckoutpro-generate-hash)

## Passing dynamic hashes

For passing dynamic hashes, merchant will receive a call on the method generateHash of `PayUCheckoutProListener`.

For passing dynamic hashes, you will receive a call on the generateHash method of PayUCheckoutProListener.

In the method parameter, you will receive a dictionary or hashMap, extract the value of hashString from that. Pass that value to the server, and now the server will append salt at the end and generate sha512 hash over it. The server will give that hash back to your app, and the app will provide that hash to PayU through a callback mechanism.

There is no need to know the formula for dynamic hashes because PayU SDK gives you the string containing all the required parameters. Your server has to append salt at the end and generate sha512 hash over it.

For passing dynamic hashes during integration, use the following code snippet:

```Text Swift
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
    let hashFetchedFromServer = <String>
    
    onCompletion([hashName : hashFetchedFromServer])
}
```
```Text Objective-C
/// Use this function to provide hashes
/// @param param NSDictionary that contains key as HashConstant.hashName & HashConstant.hashString
/// @param onCompletion Once you fetch the hash from server, pass that hash with key as param[HashConstant.hashName]
- (void)generateHashFor:(NSDictionary<NSString *, NSString *> * _Nonnull)param onCompletion:(void (^ _Nonnull)(NSDictionary<NSString *, NSString *> * _Nonnull))onCompletion {
    // Send below string hashStringWithoutSalt to your backend and append the salt at the end and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
    NSString *hashStringWithoutSalt = [param objectForKey:HashConstant.hashString];
    // Or you can send below string hashName to your backend and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
    NSString * hashName = [param objectForKey:HashConstant.hashName];
    
    // Set the hash in below string which is fetched from your server
    NSString *hashFetchedFromServer = <#(NSString)#>;
    
    NSDictionary *hashResponseDict = [NSDictionary dictionaryWithObjectsAndKeys:hashFetchedFromServer, hashName, nil];
    onCompletion(hashResponseDict);
}
```

Here,

           **param ->** Dictionary that contains key as **HashConstant.hashName** & **HashConstant.hashString**

**onCompletion ->** Once you fetch the **hash** from server, pass that hash with key as **param\[HashConstant.hashName]**

## Getting Hash Data to calculate hash

Checkout Pro SDK will give a callback in `generateHash`**()** method whenever any hash is needed by it. Merchant need to calculate that hash and pass back to the SDK. Below is the process of doing so:

To extract hash string and hash name from dictionary received in generateHash() method, use below keys -

**HashConstant.hashString ->** This will contain complete hash string excluding salt. Merchant can append their salt at end of hash string to calculate the hash.

**HashConstant.hashName ->** This will contain hash name.

## Passing generated hash to SDK

Prepare a dictionary, where key should be **param\[HashConstant.hashName]** and value should be generated **hash** value and pass this dictionary in **onCompletion()**