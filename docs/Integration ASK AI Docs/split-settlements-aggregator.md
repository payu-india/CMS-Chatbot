---
title: Split Settlements / Aggregator
excerpt: 'SPLIT SETTLEMENT/ AGGREGATOR MODEL '
deprecated: false
hidden: false
metadata:
  robots: index
---
Split Settlements enable your business to make, collect and receive payments. Split a transaction based on the number of sellers involved in the particular transaction.

Integration: -
The APIs involved in the entire split settlement journey is shared in the below link.

Link:
To start splitting the amount, you first need to create a child account. There are two methods to create child merchant IDs/sub accounts using the PayU account.

STEP 1:
Method 1: -
You can create a child account using your PayU dashboard.

Adding sub accounts involves an onboarding process of the sub merchant ID/vendor ID with some mandatory details.

Method 2: -
You can create a sub account using API.

CREATE SUB ACCOUNT
You need to first generate a token for creating a sub account.

 •GET CLINET TOKEN API
SAMPLE API REQUEST: -
curl --location
\--header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json'

\--data-urlencode
'client\_id=db8828218cd62be78e1e59517cb39a116ed74fcea35dc7702646fdc7cc5e25b5' --data-urlencode
'client\_secret=3a4df058d5ce5b3debc2f2888c63cdb605990d75e132cbc26db0e4c187eb981b' --data-urlencode 'grant\_type=client\_credentials'
\--data-urlencode 'scope=fetch\_child\_merchants refer\_child\_merchant'

SUCCESS RESPONSE: - {"access_token":"1c1965b24ac5f62c73c1c8724413830dc80e1dfb259d9c6477192f5fe9de368f"," token_type":"Bearer","expires_in":7199,"scope":"fetch_child_merchants 
refer_child_merchant","created_at":1738999123}

•CREATE CHILD MERCHANT API
You need to pass unique mobile number and email ID for creating a new sub account.

SAMPLE  REQUEST: -
curl --location --header 'Content-Type: application/json'
\--header 'Authorization: Bearer
1c1965b24ac5f62c73c1c8724413830dc80e1dfb259d9c6477192f5fe9de368f'
\--header 'Cookie: Path=/'
\--data-raduct":"PayUbiz", "name":"Shreejoy Chatterjee", "email":"", "mobile":"9220145471",
"aggregator\_parent\_mid":"8314310", "merchant\_type":"aggregator",
"pancard\_number":"BSTPC4369J", "pancard\_name":"Shreejoy Chatterjee",
"business\_entity\_id":14 } }'

CHILD CREATION SUCCESS RESPOINSE: -

{ "product\_account": { "id": 236948, "uuid": "11ef-e5ee-4786de38-8c65-021ec077a271", "identifier": 8666069, "product\_id": 1, "type": "PayUbizAccount", "merchant\_account\_id": 370137, "active": true, "status": null, "business\_entity\_id": 14, "business\_category\_id": null, "business\_sub\_category\_id": null, "business\_name": null, "pancard\_name": "Shreejoy
: "BSTPC4369J", "gst\_number": null, "notification\_email": ", "flag": 1072, "settlement\_status": "Active", "merchant\_type": "child\_aggregator", "onboarding\_status": "Settlement Enables", "account\_id": null,
"pan\_verification\_status": "Success", "admin\_user\_id": 218185,
"terms\_and\_condition\_accepted\_at": null, "created\_at": "2025-02-08T07:28:25.000Z",
"updated\_at": "2025-02-08T07:28:27.000Z", "partner\_uuid": null, "business\_origin": "SMB-ENT", "shop\_number": null, "area\_code": null, "gst\_verification\_status": "Pending",
"cin\_number": null, "vkyc\_exemption": "not\_applicable", "sf\_payload\_version": -1, "stop\_txns": null, "copy\_mid\_parent": null, "flag1": 0, "mid": 8666069, "name": "Shreejoy Chatterjee", "email": "", "first\_name": "Shreejoy", "last\_name": "Chatterjee", "business\_type": "LongTail", "bank\_update\_attempt\_count": 0, "merchant\_vertical": null, "partner\_source": null, "android\_url": null, "ios\_url": null, "integration\_type": "Tools",
"integration\_status": "Not Integrated", "monthly\_expected\_volume": null, "gmv\_amount": null, "website\_approval\_status": null, "website\_url": null, "website\_remarks": null,
"registered\_mobile": "9220145471", "product": "PayUbiz", "bank\_update\_attempt\_left": 11, "is\_service\_agreement\_accepted": false, "is\_service\_agreement\_esigned": false,
"is\_sbqr\_addendum\_accepted": true, "acl\_role\_name": null, "is\_authorisation\_letter\_required": false, "saved\_kyc\_address": null, "kyc\_status": { "status": "LOCKED", "kyc_status": 
, "document\_status": "Docs Approved", "service\_intent": "default", "nb\_eligible": false, "lending\_eligible": false, "offer\_engine\_enabled": false, "revamp\_merchant": true, "is\_cs\_eligible": false, "onboarding\_completed": true, "re\_kyc\_required": false,
"dashboard\_preference": "one\_dashboard", "migration\_status": 0,
"is\_service\_agreement\_present": false, "next\_bank\_update\_time": "2025-02-
08T12:58:27.519+05:30", "business\_pan\_name\_match": false, "mfa\_enabled": false,
"team\_mfa\_enabled": false, "business\_category\_name": null, "business\_sub\_category\_name": null, "device": "Desktop", "display\_name": "Shreejoy Chatterjee", "campaign\_name": null, "campaign\_medium": null, "campaign\_source": null, "campaign\_term": null, "source\_url": null, "source\_type": null, "sub\_source": null, "source\_details": null, "ubo\_exist": false, "mobile": "9220145471", "new\_settlement\_embargo": false, "lending\_interest": false, "mobile\_disabled": false, "re\_kyc\_document\_status": "Docs Approved", "re\_kyc\_kyc\_status": { "status": 
, "dormancy\_date": null, "is\_dormant": false,
"priority\_settlement\_eligible": false, "is\_working\_hours": true, "vkyc\_status": null, "vkyc": null, "working\_hours\_start\_end": "10:00 am - 06:30 pm", "stop\_onboarding": false, "prob\_tools": false, "logo": null, "offline\_merchant": false, "sf\_agent\_comments": { "latest_comment": null, "latest_sf_comment": null, "agent_remarks": null, "req_doc_category": null }, "allow\_vkyc": true, "unlock\_steps\_till\_website": null, "allow\_sole\_prop\_tools\_onboarding": null,
"is\_good\_quality\_lead": null, "outlet\_flow\_enabled": false, "bundle\_subscription\_eligible": f0100116", "br\_exemption": false, "dashboard\_url": " "business\_entity\_uuid": "1f52-d683-0b1384e5-d7e4-4bb3c2dc7468", "business\_category\_uuid": null, "business\_sub\_category\_uuid": null, "account\_uuid": null, "merchant\_account\_uuid": "11ef-e5ee-48696e2e-8c65-021ec077a271", "product\_uuid": "a12c-f114-ce1bac7d-058c-0f95d535aca3", "admin\_user\_uuid": "11ef-e5ee-

3ff9ed2c-a59e-02d98f5fcb07", "bank\_detail": null, "operating\_address": null,
"registration\_address": null, "business\_entity": { "id": 14, "name": "Individual" },
"product\_account\_statuses": \[ { "status_type": "WEBSITE", "status_value": null, "updated_at": "2025-02-08T07:28:25.000Z" }, { "status_type": "KYC_DOCUMENTS", "status_value": "Docs Approved", "updated_at": "2025-02-08T07:28:26.000Z" }, { "status_type": "Agreement", "status_value": "Approved", "updated_at": "2025-02-08T07:28:26.000Z" }, { "status_type": "RE_KYC_DOCUMENTS", "status_value": "Docs Approved", "updated_at": "2025-02-08T07:28:26.000Z" } ], "website\_detail": null, "attached\_configs": \[ { "id": 3425, "name": "skip_onboarding_steps", "config": { "onboarding_steps": { "documentation": 



&#x20;],
"kyc\_documents": \[

],
"cs\_plan": null,
"product\_account\_detail": {
"id": 236955,
"merchant\_id": null,
"dob": null,
"pep": null,
"aml\_flag": false,
"uuid": "11ef-e5ee-489aa39a-8c65-021ec077a271",  "created\_at": "2025-02-08T07:28:25.000Z",
"updated\_at": "2025-02-08T07:28:26.000Z",
"sign\_up\_ip": null,
"gst\_addendum\_status": null,
"max\_same\_day\_settlement\_amt": null,
"product\_account\_id": 236948,
"integration\_type": "Tools",
"integration\_status": "Not Integrated",
"monthly\_expected\_volume": null,
"gmv\_amount": null,
"average\_delivery\_time": null,
"emi\_approval\_status": null,
"mcp\_approval\_status": null,
"next\_rekyc\_date": null,
"industry\_type": null,
"annual\_turnover": null,
"lead\_id": null,
"city\_of\_incorporation": null,
"country\_of\_incorporation": null,

"purpose\_of\_payouts": null,
"pg\_key": "FgUSQm",
"team\_mfa\_enabled": false,
"team": null,
"flag": 0,
"uat\_merchant\_detail": null,
"dormancy\_date": null,
"priority\_settlement\_plan": null,
"mcp\_ticket\_id": null,
"business\_details\_rekyced": null,
"pep\_onboarding\_status": null,
"copy\_mid": null,
"uat\_mid": null,
"lob\_status\_prerisk": null,
"screenza\_response": null,
"taxation\_id": null,
"clw\_ticket\_id": null,
"copy\_mid\_type": null,
"cin\_doc\_request\_id": null,
"cin\_doc\_requested\_at": null,
"cin\_doc\_fetched\_at": null,
"npo": false
},
"custom\_parameters": \[

],
"ultimate\_beneficiaries": \[

],
"business\_members": \[

],
"consents": \[

],
"signatory\_contact\_details": \[

]

} }

STEP 2: - Once the child merchant ID is created, now its time to split the amount. There are two types of split transaction.

• SPLIT DURING TRANSACTION:
1.Absolute Split During Transaction
2.Split by Percentage During Transaction

• SPLIT AFTER TRANSACTION:
1.Absolute Split After Transaction
2.Split by Percentage after Transaction

SPLIT DURING TRANSACTION:
•Absolute Split During Transaction

REQUEST:
hash:
bdec8f559b5fd1e93bcfa26408ec0c3d32c22a9a60d8b44b929678e4b0bdf47d3617d4c356ab8753 588ddbdd662cbf4384c5bf173474488e65ee82b98eed89d3
key: rUOyVO
txnid: 0668625da86f8ebe8a01
api\_version: 1
amount: 100
firstname: Payu-Admin
salt\_version: 1
email:
phone: 1234567890
productinfo: Product Info

surl:

txtid: afb82b0dc86628a66f7fc4eb5b166786

furl:

ipurl:

splitRequest: {"type":"absolute","splitInfo":{"FgUSQm":{"aggregatorSubTxnId":"0668625da86f8ebe8a01","a ggregatorSubAmt":"70","aggregatorCharges":"30"}   }}

RESPONSE:

Array
(
  \[mihpayid] => 403993715533339172
  \[mode] => UPI
  \[status] => success
  \[unmappedstatus] => captured
  \[key] => rUOyVO
  \[txnid] => 0668625da86f8ebe8a01
  \[amount] => 100.00
  \[discount] => 0.00
  \[net\_amount\_debit] => 100
  \[addedon] => 2025-02-11 13:18:31
  \[productinfo] => Product Info
  \[firstname] => Payu-Admin
  \[lastname] =><br />  \[address1] =><br />  \[address2] =><br />  \[city] =><br />  \[state] =><br />  \[country] =><br />  \[zipcode] =
  \[email] =>
  \[phone] => 1234567890
  \[udf1] =><br />  \[udf2] =><br />  \[udf3] =>

  \[udf4] =><br />  \[udf5] =><br />  \[udf6] =><br />  \[udf7] =><br />  \[udf8] =><br />  \[udf9] =><br />  \[udf10] =><br />  \[hash] =>
a76496e939aa19ce1a57abc05215f7946725d50500b51063614d22d0c12b63f28300e2dfb911bae5 812c037b73641762e6e7153db2cb456faefc52382f070099
  \[field1] => 9999999999\@upi
  \[field2] => 0668625da86f8ebe8a01
  \[field3] =><br />  \[field4] => Payu-Admin
  \[field5] => AXIpPDS6S0hxobKS8JIywkfamshcHILyxVg
  \[field6] =><br />  \[field7] => Transaction completed successfully
  \[field8] => generic
  \[field9] => Transaction completed successfully
  \[payment\_source] => payu
  \[pa\_name] => PayU
  \[PG\_TYPE] => UPI-PG
  \[bank\_ref\_num] => 0668625da86f8ebe8a01
  \[bankcode] => UPI
  \[error] => E000
  \[error\_Message] => No Error
  \[splitInfo] => {"splitStatus":"success","splitSegments":[{"merchantKey":"FgUSQm","amount":70,"subvention _amount":0,"txnId":"0668625da86f8ebe8a01","additional_charges":0,"transaction_fee":70},{"m erchantKey":"rUOyVO","amount":30,"subvention_amount":0,"txnId":"0668625da86f8ebe8a01" ,"additional_charges":0,"transaction_fee":30}]}
)

• Split by Percentage During Transaction

REQUEST:

hash:
9dfdaa28579f013a163f040083cf51cf20609df8148a73b08b37cc4bab9215a5c36e2bc4124ae4abca 4403e0b053c14f80d4e6684b9d156e7e6e559d6356047e

key: rUOyVO

txnid: 795990edfec62eb41acf

api\_version: 1

pre\_init\_mode: 0

amount: 100

firstname: Payu-Admin

salt\_version: 1

email:

phone: 1234567890

productinfo: Product Info

surl:

txtid: afb82b0dc86628a66f7fc4eb5b166786

furl:

splitRequest: {"type":"percentage","splitInfo":{"FgUSQm":{"aggregatorSubTxnId":"9a70ea015512681010"," aggregatorSubAmt":"70","aggregatorCharges":"30"}}}

RESPONSE:

Array
(
  \[mihpayid] => 403993715533339284
  \[mode] => UPI
  \[status] => success
  \[unmappedstatus] => captured
  \[key] => rUOyVO
  \[txnid] => 795990edfec62eb41acf
  \[amount] => 100.00
  \[discount] => 0.00
  \[net\_amount\_debit] => 100
  \[addedon] => 2025-02-11 13:28:48
  \[productinfo] => Product Info
  \[firstname] => Payu-Admin

  \[lastname] =><br />  \[address1] =><br />  \[address2] =><br />  \[city] =><br />  \[state] =><br />  \[country] =><br />  \[zipcode] =><br />  \[email] =>
  \[phone] => 1234567890
  \[udf1] =><br />  \[udf2] =><br />  \[udf3] =><br />  \[udf4] =><br />  \[udf5] =><br />  \[udf6] =><br />  \[udf7] =><br />  \[udf8] =><br />  \[udf9] =><br />  \[udf10] =><br />  \[hash] =>
a2acef7da89824e1f532c2aca502c8f1eadb95cc990422ea40a7f4fec9cc065a6f7eb218bf9ddb7f32c e455df05333a488f0de3796ac2896f87bf4e0873d7234
  \[field1] => 9999999999\@upi
  \[field2] => 795990edfec62eb41acf
  \[field3] =><br />  \[field4] => Payu-Admin
  \[field5] => AXI6nrOfGe13USk8osrbdCBIsRyJerqvrB4
  \[field6] =><br />  \[field7] => Transaction completed successfully
  \[field8] => generic
  \[field9] => Transaction completed successfully
  \[payment\_source] => payu
  \[pa\_name] => PayU
  \[PG\_TYPE] => UPI-PG
  \[bank\_ref\_num] => 795990edfec62eb41acf
  \[bankcode] => UPI
  \[error] => E000
  \[error\_Message] => No Error
  \[splitInfo] => {"splitStatus":"success","splitSegments":[{"merchantKey":"FgUSQm","amount":70,"subvention _amount":0,"txnId":"9a70ea015512681010","additional_charges":0,"transaction_fee":70},{"mer chantKey":"rUOyVO","amount":30,"subvention_amount":0,"txnId":"795990edfec62eb41acf","a dditional_charges":0,"transaction_fee":30}]}
)

SPLIT AFTER TRANSACTION:
•Absolute Split After Transaction
DEV GUIDE DOCUMENT LINK:
