---
title: API Notifications for Tokenization
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
The API notifications described in this section enable you to know the status of the user’s tokenized card. There are four variations or types of notifications that you can receive from PayU.

> 📘 Note: 
> 
> You must contact your PayU Key Account Manager to enable these API notifications for Tokenization.

- The API response to the merchant for all the scenarios is as follows:
- **Response when Tokenization is failed while we are retrying tokenization.**

```plaintext
{ 
"cardToken": "1****6789", 
"userCredential": "test02:sartajuserid33", 
"merchantId": "3214", 
"notificationType": "TOKEN_RETRY", 
"tokenProvisioningStatus": "FAILED", 
}
```

- **Response to the merchant when Tokenization is successful while we are retrying tokenization.**

```plaintext
{ 
    "cardToken": "123456789", 
    "userCredential": "test02:sartajuserid33", 
    "merchantId": "3214", 
    "notificationType": "TOKEN_RETRY", 
    "tokenProvisioningStatus": "SUCCESS", 
    "issuerToken":{ 
        "tokenExpYr":"2024", 
        "tokenValue":"3****0006134923", 
        "tokenExpMon":"09", 
        "error_code": null, 
        "error_desc": null 
        }, 
    "networkToken":{ 
        "tokenExpYr":"2024", 
        "tokenValue":"3****0006134923", 
        "tokenExpMon":"09", 
        "error_code": null, 
        "error_desc": null 
        } 
}
```

- **Response when Tokenization is failed while we are doing sync/async Tokenization.**

```plaintext
{ 

  "merchantId": "131496", 

  "payuToken": "5bc35da13114ad3b044eb016", 

  "token_provisioning_status": "Failed", 

  "user_credential": "ABC:1234", 

  "notificationType": "TOKEN_CREATED_HTTP", 

  "token_detail": { 

    "status": "1", 

    "msg": "Card not saved", 

    "cardToken": "9****7449926e57ff2662", 

    "card_number": "XXXXXXXXXXXX1165", 

    "card_label": "My_card", 

    "network_token": "4****28710000211", 

    "issuer_token": "Q****zgZOnEjY428" 

  } 

} 
```

- **Response when the token is deleted**

```plaintext
{ 

  "merchantId": 2, 

  "cardToken": "00*****09ff0913c8a27d7fb27efaee4d89a02", 

  "tokenProvisioningStatus": "DELETED", 

  "userCredential": "PayUPaisa1:D***431P", 

  "notificationType": "CARD_LIFE_CYCLE_DELETE", 

  "networkToken": { 

    "token_value": "4****50470517486", 

    "token_exp_mon": "12", 

    "token_exp_yr": "20**", 

    "error_code": null, 

    "error_desc": null 

  } 

} 
```