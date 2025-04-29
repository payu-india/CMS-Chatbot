---
title: UPI TPV Integration API - Partner Integration
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
Integrate TPV through UPI using the procedure described in this section.

## Prerequisites

S2S (Seamless) integration has to be done as per the standard kit. For more information, refer to &lt;https://docs.payu.in/reference/upi-s2s-integration-api&gt;

## Step 1: List the account numbers

Collect or prepare a list of account numbers that must be posted to PayU for TPV at step 2.

## Step 2: Post the parameters to PayU

With the following additional parameters, make the transaction request with the customer’s bank account number to the PayU using the initiate payment (partner/payments) API. For more information, refer to [UPI S2S Integration API - WhatsApp](ref:upi-s2s-integration-api).

**Environment**

|                            |                                                                  |
| -------------------------- | ---------------------------------------------------------------- |
| **Test Environment**       | &lt;https://test-partnerapilayer.payu.in/apilayer/partner/payments&gt; |
| **Production Environment** | &lt;https://api.payu.in/partner/payments&gt;                           |

### Request Parameters

| **Parameter**                | **Description**                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                      |
| :--------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bankcode(optional)           | It defines the bank with which you wish to perform TPV using the bank code.The values can be any one of the following values:**INTTPV**: : Used for UPI Intent                                                                                                                                                        | **INTTPV**                                                                                                                                                           |
| beneficiarydetail(mandatory) | This is a JSON format text and there should be key named **beneficiaryAccountNumber** with the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter. | `{"beneficiaryAccountNumber":"002001600674|00000031957292212|00000035955239352|00000035955239352","ifscCode":"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"}` |

##

|     |                                                   |                                                  |
| --- | ------------------------------------------------- | ------------------------------------------------ |
| 400 | When beneficiarydetail is not a valid json string | `{ "message": "beneficiarydetail is invalid" }` |

Follow step 2 and step 3 of [UPI S2S Integration API - WhatsApp](ref:upi-s2s-integration-api) to invoke UPI intent on customer's device and verify the transaction details.