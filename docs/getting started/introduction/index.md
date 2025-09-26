---
title: Introduction
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  keywords:
    - checkout integration
    - ' API reference'
    - ' payment gateway API integration'
    - ' payment aggregator API integration'
    - ' payment gateway integration'
    - ' UPI payment integration'
    - ' card payment integration'
    - ' NetBanking integration'
  robots: index
next:
  description: ''
---
Integrate TWID pay to enable customers to redeem their TWID loyalty points during checkout.
Follow these sequential steps to implement a complete TWID pay solution.
> 📘 Header-based authentication
>
> All the APIs mentioned in this section uses the following header-based authentication.
Include the following headers in all API requests.
<Accordion title="Header authentication for all APIs" icon="fa-search">
|
Parameter     |
Description                                                                                              
      
                                                                                              
  |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| date          |
The current date and time. For example,  format of the date is Wed, 28 Jun 2023 11:25:19 GMT.                                                                                                                  |
| authorization |
The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data.
For more information, refer to[ authorization fields description](#authorization-fields-description). |

#### authorization fields description

| Parameter |
Description                                                                                                    

                                                                  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| username  |
Represents the username or identifier for the client or merchant, in this case, it's "smsplus". |
| algorithm |
Indicates the hashing algorithm used for the HMAC signature. Here, it is set to "sha512".                                                                                        |
| headers   |
Specifies which headers have been used in generating the hash. In this case, only the "date" header is used.                                                                     |
| signature |
The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data.
For more information, refer to [hashing algorithm](#hashing-algorithm). |

#### hashing algorithm

You must hash the request parameters using the following hash logic:
</Accordion>