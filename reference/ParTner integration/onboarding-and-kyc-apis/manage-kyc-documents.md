---
title: Manage KYC Documents
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
The following APIs are used to manage KYC documents:

- [Info KYC Document API](ref:info_kyc_document_api)
- [Documents Required API](ref:docs_required_api)
- [Create KYC Document](ref:create_kyc_document_api)
- [Delete KYC Document API](ref:delete_kyc_document_api)
- [Post CKYC API](ref:post_ckyc_api)
- [Upload Aadhaar XML Offline API](ref:upload_aadhaar_xml_offline_api)

After the bank and KYC verification, the **Info KYC Document** API is used to fetch the documents submitted for KYC. If the KYC verification has failed, delete the existing KYC documents in the PayU database (using the **Delete KYC Document** API) and then submit KYC documents (using the **Create KYC Document** API). Also, you can upload Aadhaar from an XML file using the **Aadhaar XML Offline** API.

> 📘 Note:
> 
> If the **bank\_verification\_status** parameter of the **Get Merchant API** response is unsuccessful, the [Create KYC Document](ref:create_kyc_document_api) is used to submit the KYC details.

After the merchant details are verified, the following APIs are used to verify the bank details and the KYC for the merchant:

- [Penny Verify API](ref:penny_verify_api)
- [Send OTP API](ref:send_otp_api)
- [Verify OTP API](ref:verify_otp_api)

> 📘 Notes:
> 
> The following verification is required for individuals or sole proprietors. For more information, refer to [Create KYC Document](ref:create_kyc_document_api).

[block:parameters]
{
  "data": {
    "h-0": "",
    "h-1": "",
    "0-0": "Individuals",
    "0-1": "- For individuals, merchant KYC can be done through Aadhaar or CKYC.  \n- In case validation fails through the above two mechanisms, the merchant will have to submit document proofs ( POI, POA)",
    "1-0": "Sole Proprietors",
    "1-1": "For sole proprietors, merchant KYC can be done through Aadhaar or CKYC.In case validation fails through the above two mechanisms, the  merchant will have to submit document proofs ( POI, POA & government certificate)."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]