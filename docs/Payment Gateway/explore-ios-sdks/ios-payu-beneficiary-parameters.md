---
title: PayU Beneficiary Parameters
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
To post PayU Beneficiary parameters:

* Create PayUBeneficiaryParams
* Post Parameters

## Create PayUBeneficiaryParams object

Create ​a `PayUBeneficiaryParams` class object using a code snippet similar to the following:

```Text Objective-C
/* Object C */
PayUBeneficiaryParams *beneficiaryParams = [[PayUBeneficiaryParams alloc] initWithBeneficiaryName:<#(NSString * _Nonnull)#>                                                                         beneficiaryAccountNumber:<#(NSString * _Nonnull)#>                                                                                  beneficiaryIFSC:<#(NSString * _Nonnull)#>                                                                           beneficiaryAccountType:<#(enum BeneficiaryAccountType)#>];
```
```Text Swift
//Swift
let beneficiaryParams = PayUBeneficiaryParams(beneficiaryName: <#T##String#>,
                                              beneficiaryAccountNumber: <#T##String#>,
                                              beneficiaryIFSC: <#T##String#>,
                                              beneficiaryAccountType: <#T##BeneficiaryAccountType#>)
```

***

## Post parameters

| Parameter                | Description                                                                                                     |
| :----------------------- | :-------------------------------------------------------------------------------------------------------------- |
| beneficiaryName          | `String` This parameter is used to pass the beneficiary name.                                                   |
| beneficiaryAccountNumber | `String` This parameter is used to pass the beneficiary account number.                                         |
| beneficiaryIFSC          | `String` This parameter is used to pass the beneficiary bank IFSC Code.                                         |
| beneficiaryAccountType   | `BeneficiaryAccountType` This parameter is used to pass the beneficiary account details like saving or current. |
