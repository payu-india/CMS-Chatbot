---
title: Create Merchant API
excerpt: ''
api:
  file: partner-apis-26.json
  operationId: create_merchantv3
deprecated: false
hidden: false
metadata:
  title: Create Merchant API
  description: >-
    Learn how to use the PayU Create Merchant API to create new merchant
    accounts. This API reference page provides detailed instructions, request
    parameters, and sample responses for efficient merchant onboarding
  keywords:
    - Create Merchant API
    - ' merchant onboarding'
    - ' KYC details'
    - ' secure merchant creation'
    - ' tokenization'
    - ' manage merchants'
    - ' create merchant accounts'
  robots: index
next:
  description: ''
---
The **Create Merchant** API creates a new merchant account on PayU and posts all KYC details. This API returns the Merchant ID (MID) in the response.

## Authentication

This API is authorised through a client token generated using the client ID and secret. To create a token, call the get token API with `refer merchant` as a scope.  Refer to the  [Get Token API](ref:get_token_api) doc for more information.

> ❗️ Important considerations for using this API
>
> 1. The mobile, Pan number, GSTIN passed in the request has to be valid as checks are performed in real time.
> 2. If Business Entity type is passed in the create merchant API, ensure that the PAN also belong to the same entity.

| \*\* Environment\*\* | \*\* URL\*\*                                                                         |
| :------------------- | :----------------------------------------------------------------------------------- |
| production           | [https://partner.payu.in/api/v3/merchants](https://partner.payu.in/api/v3/merchants) |
| UAT                  | uat-partner.payu.in/api/v3/merchants                                                 |

## Sample response

```
{
	"info": {
		"_postman_id": "ccb9972d-0181-432e-a1c1-add7096cee9a",
		"name": "UAT - Refer merchant apis for partner",
		"schema": "https://schema.getpostman.com/json/collection/v2.0.0/collection.json",
		"_exporter_id": "26476208",
		"_collection_link": "https://solar-capsules.postman.co/workspace/66e4a5a8-a429-422c-ab0e-8593686a98f0/collection/26476208-ccb9972d-0181-432e-a1c1-add7096cee9a?action=share&source=collection_link&creator=26476208"
	},
	"item": [
		{
			"name": "Send and verify",
			"item": [
				{
					"name": "GetToken",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "urlencoded",
							"urlencoded": [
								{
									"key": "client_id",
									"value": "56b16b8f4d16f61929d6596d3c9cfb3e9bfc526c9c906b09c916cc9ea591b66d",
									"description": "uat",
									"type": "text",
									"disabled": true
								},
								{
									"key": "client_secret",
									"value": "f5e0115d5b9f715ce0e8c4ef99d438aa4e7f0203f6e1d5e9be9e36f80a07716b",
									"description": "uat",
									"type": "text",
									"disabled": true
								},
								{
									"key": "grant_type",
									"value": "client_credentials",
									"type": "text"
								},
								{
									"key": "scope",
									"value": "send_sign_in_otp verify_sign_in_otp refer_merchant",
									"type": "text"
								},
								{
									"key": "client_id",
									"value": "23363e3e7abe578e95a3524b52adecfb35ac17975d4e7c8517c310c2785bef53",
									"type": "text"
								},
								{
									"key": "client_secret",
									"value": "b862c1cccb0ded75e5fd2693196eb2231244984401bb8c60ba53294084d2e419",
									"type": "text"
								}
							]
						},
						"url": "{{hub_uat}}/oauth/token"
					},
					"response": []
				},
				{
					"name": "SendOtp",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer aa52f685ef29e8c86aabdccd965c3239cc4ce7bf4c5f98c68ca6fc2d8c641d8a"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "otp[identity]",
									"value": "9916965982",
									"type": "text"
								},
								{
									"key": "otp[scope]",
									"value": "user_profile create_bank_details update_bank_details create_payment_links update_payment_links read_payment_links ",
									"description": "create_payment_links update_payment_links read_payment_links ",
									"type": "text"
								},
								{
									"key": "otp[channels][]",
									"value": "sms",
									"description": "client_manage_agreement",
									"type": "text"
								},
								{
									"key": "otp[type]",
									"value": "SignIn",
									"description": "user_profile create_bank_details update_bank_details create_payment_links update_payment_links read_payment_links ",
									"type": "text"
								}
							]
						},
						"url": "{{hub_prod}}/api/v1/otps/send_otp"
					},
					"response": []
				},
				{
					"name": "VerifyOtp",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer a7db7d87343969e44c4d0b4b602d2738233f6efec0be1088316b70b15a77343c"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "otp[identity]",
									"value": "7292033398",
									"type": "text"
								},
								{
									"key": "otp[email]",
									"value": "test.ob021345@yomail.com",
									"type": "text"
								},
								{
									"key": "otp[code]",
									"value": "4722",
									"type": "text"
								},
								{
									"key": "otp[type]",
									"value": "SignIn",
									"type": "text"
								}
							]
						},
						"url": "{{hub_uat}}/api/v1/otps/verify_otp"
					},
					"response": []
				}
			]
		},
		{
			"name": "Create and Update a merchant",
			"item": [
				{
					"name": "CreateMerchant",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer 3c775c77cffb80a5161aa9a0f31bce3eb3555572e1364f0b2439f6f80fddb2e6"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "[merchant][display_name]",
									"value": "DIVY HARESHKUMAR SHAH",
									"type": "text"
								},
								{
									"key": "merchant[email]",
									"value": "boro13@yomail.com",
									"type": "text"
								},
								{
									"key": "merchant[mobile]",
									"value": "9916965913",
									"type": "text"
								},
								{
									"key": "merchant[business_details][pan]",
									"value": "FANPS6362D",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[business_details][business_entity_type]",
									"value": "Sole Proprietorship",
									"type": "text"
								},
								{
									"key": "merchant[product]",
									"value": "PayUbiz",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[bank_details][account_no]",
									"value": "919010067278549",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[bank_details][account_holder_name]",
									"value": "DIVY HARESHKUMAR SHAH",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[bank_details][ifsc_code]",
									"value": "UTIB0003557",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[business_details][registered_name]",
									"value": "DIVY HARESHKUMAR SHAH",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[business_details][business_category]",
									"value": "Arts, Gifts & Stationery",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[business_details][business_sub_category]",
									"value": "Art Dealers and Galleries",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[website_details][website_url]",
									"value": "https://www.google.com",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[monthly_expected_volume]",
									"value": "12000",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[signing_authority_details][name]",
									"value": "DIVY HARESHKUMAR SHAH",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[signing_authority_details][pancard_number]",
									"value": "FANPS6362D",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[signing_authority_details][email]",
									"value": "email_test1213@yopmail.com",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[business_details][pancard_name]",
									"value": "DIVY HARESHKUMAR SHAH",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[integration_type]",
									"value": "",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[gst_number]",
									"value": "24FANPS6362D1ZE",
									"type": "text"
								},
								{
									"key": "merchant[udyam_number]",
									"value": "UDYAM-UP-19-0002053",
									"description": "Works only for Sole Proprietorship",
									"type": "text",
									"disabled": true
								},
								{
									"key": "merchant[gst_consent]",
									"value": "false",
									"type": "text",
									"disabled": true
								}
							]
						},
						"url": "{{rp_uat}}/api/v3/merchants"
					},
					"response": []
				},
				{
					"name": "UpdateMerchant",
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer 205830ed8ab358e2310bfcde8c3ee0860b74820b794d9b1d2d45819bd5adbff6",
								"description": "Token received from VerifyOtp"
							}
						],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "merchant[pancard_number]",
									"value": "",
									"type": "text"
								},
								{
									"key": "merchant[pancard_name]",
									"value": "",
									"type": "text"
								},
								{
									"key": "merchant[business_entity]",
									"value": "Public Limited",
									"type": "text"
								},
								{
									"key": "merchant[business_category]",
									"value": "Arts, Gifts & Stationery",
									"type": "text"
								},
								{
									"key": "merchant[business_sub_category]",
									"value": "Art Dealers and Galleries",
									"type": "text"
								},
								{
									"key": "merchant[business_name]",
									"value": "PAYU PAYMENTS PRIVATE LIMITED",
									"type": "text"
								},
								{
									"key": "merchant[monthly_expected_volume]",
									"value": "78658",
									"type": "text"
								},
								{
									"key": "merchant[registration_address][address_line]",
									"value": "M1703, banashankari",
									"type": "text"
								},
								{
									"key": "merchant[registration_address][state]",
									"value": "Karnataka",
									"type": "text"
								},
								{
									"key": "merchant[registration_address][city]",
									"value": "Haryana",
									"type": "text"
								},
								{
									"key": "merchant[registration_address][pincode]",
									"value": "122018",
									"type": "text"
								},
								{
									"key": "merchant[operating_address][city]",
									"value": "Bangalore",
									"type": "text"
								},
								{
									"key": "merchant[operating_address][state]",
									"value": "Haryana",
									"type": "text"
								},
								{
									"key": "merchant[operating_address][address_line]",
									"value": "M1703, Banashankari",
									"type": "text"
								},
								{
									"key": "merchant[operating_address][pincode]",
									"value": "122018",
									"type": "text"
								},
								{
									"key": "merchant[gst_number]",
									"value": "",
									"type": "text"
								},
								{
									"key": "merchant[integration_type]",
									"value": "ThirdParty",
									"type": "text"
								},
								{
									"key": "merchant[signing_authority_details][name]",
									"value": "Spoorthi Naik",
									"type": "text"
								},
								{
									"key": "merchant[signing_authority_details][email]",
									"value": "boro@yopmail.com",
									"type": "text"
								},
								{
									"key": "merchant[signing_authority_details][pancard_number]",
									"value": "",
									"type": "text"
								},
								{
									"key": "merchant[signing_authority_details][cin_number]",
									"value": "",
									"type": "text"
								},
								{
									"key": "merchant[website_details][website_url]",
									"value": "www.borosil.com",
									"type": "text"
								},
								{
									"key": "merchant[website_details][android_url]",
									"value": "www.borosil.com",
									"type": "text"
								},
								{
									"key": "merchant[website_details][ios_url]",
									"value": "www.borosil.com",
									"type": "text"
								}
							]
						},
						"url": "{{rp_prod}}/api/v1/merchants/11ef-d968-6b042d6c-9b94-02975f21d323/update"
					},
					"response": []
				},
				{
					"name": "GetMerchant",
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Authorization",
								"value": "bearer aa52f685ef29e8c86aabdccd965c3239cc4ce7bf4c5f98c68ca6fc2d8c641d8a"
							}
						],
						"url": "{{hub_uat}}/api/v1/merchants/760068860"
					},
					"response": []
				}
			]
		},
		{
			"name": "Bank Details API",
			"item": [
				{
					"name": "Add/Update Bank Details",
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Authorization",
								"value": "Bearer a0443a4da184acc528849e4836e03afc81d3a0f2b33fce91570aa5bab915e842"
							},
							{
								"key": "Content-Type",
								"value": "application/x-www-form-urlencoded"
							}
						],
						"body": {
							"mode": "urlencoded",
							"urlencoded": [
								{
									"key": "bank_detail[bank_account_number]",
									"value": "",
									"type": "text"
								},
								{
									"key": "bank_detail[ifsc_code]",
									"value": "",
									"type": "text"
								},
								{
									"key": "bank_detail[holder_name]",
									"value": "Mahi Srivastava",
									"type": "text"
								}
							]
						},
						"url": "{{hub_uat}}/api/v1/merchants/11ef-586f-6bca3ef0-8ff1-021ec077a271/add_bank_detail"
					},
					"response": []
				}
			]
		},
		{
			"name": "Manage KYC documents",
			"item": [
				{
					"name": "AadharApis",
					"item": [
						{
							"name": "Aadhar XML Offline",
							"request": {
								"method": "POST",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer 1e3ca62936ab9565d88cca21ffa1a8f614340cb94f1b7f15bef62193931b916c",
										"type": "text"
									}
								],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "aadhaar_share_code",
											"value": "3456",
											"type": "text"
										},
										{
											"key": "merchant_id",
											"value": "8390925",
											"type": "text"
										},
										{
											"key": "aadhaar_file",
											"type": "file",
											"src": "/Users/mahi.srivastava/Documents/1708429585_1093.zip"
										}
									]
								},
								"url": "{{rp_test}}/api/v3/merchants/kyc_document/aadhaar_xml_offline"
							},
							"response": []
						},
						{
							"name": "Aadhar XML Consent",
							"request": {
								"auth": {
									"type": "noauth"
								},
								"method": "POST",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer dummy",
										"type": "text"
									}
								],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "merchant_id",
											"value": "20997866",
											"type": "text"
										}
									]
								},
								"url": "{{rp_test}}/api/v3/merchants/kyc_document/aadhaar_xml_consent"
							},
							"response": []
						},
						{
							"name": "Aadhar OTP generation",
							"request": {
								"auth": {
									"type": "noauth"
								},
								"method": "POST",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer dummy",
										"type": "text"
									}
								],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "merchant_id",
											"value": "20997866",
											"type": "text"
										},
										{
											"key": "aadhar_number",
											"value": "bbbbbbbbbbbb",
											"type": "text"
										}
									]
								},
								"url": "{{rp_test}}/api/v3/merchants/kyc_document/aadhaar_xml_consent"
							},
							"response": []
						},
						{
							"name": "Aadhar XML Data",
							"request": {
								"auth": {
									"type": "noauth"
								},
								"method": "POST",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer dummy",
										"type": "text"
									}
								],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "merchant_id",
											"value": "20997866",
											"type": "text"
										},
										{
											"key": "otp",
											"value": "",
											"type": "text"
										}
									]
								},
								"url": "{{rp_uat}}/api/v3/merchants/kyc_document/aadhaar_xml_data"
							},
							"response": []
						}
					]
				},
				{
					"name": "Esign apis",
					"item": [
						{
							"name": "GenerateMergedDocumentForEsign",
							"request": {
								"method": "GET",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer 6b4e1b97c6ecb39fa7b13275f740766d32cc3676c1bc773c42b59c9a9270914b",
										"description": "Scope used - client_manage_agreement (generated from GetToken Api"
									}
								],
								"url": "{{ob_uat}}/api/v3/product_accounts/11ef-11e2-162d9d26-af4b-02975f21d323/generate_merged_document_for_esign",
								"description": "Generated from cURL: curl --location 'https://test10-onboarding.payu.in/api/v3/product_accounts/11ef-11e2-162d9d26-af4b-02975f21d323/generate_merged_document_for_esign' \\\n--header 'sec-ch-ua: \"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"' \\\n--header 'Source: Web' \\\n--header 'sec-ch-ua-mobile: ?0' \\\n--header 'Authorization: Bearer 6b4e1b97c6ecb39fa7b13275f740766d32cc3676c1bc773c42b59c9a9270914b' \\\n--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36' \\\n--header 'Accept: application/json' \\\n--header 'Referer: https://test10-onboarding.payu.in/' \\\n--header 'sec-ch-ua-platform: \"macOS\"' \\\n--header 'Cookie: Path=/'"
							},
							"response": []
						},
						{
							"name": "SendSignatoryOtp",
							"request": {
								"method": "POST",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer 7ca663dddab977091645378870644147059bde0d1482e44de3096fcb4fa5f8a"
									}
								],
								"url": "{{ob_uat}}/api/v3/product_accounts/{{product_account_uuid}}/kyc_documents/{{merged_document_uuid}}/send_signatory_otp",
								"description": "Generated from cURL: curl --location -g --request POST '{{onboarding_base_url}}/api/v3/product_accounts/{{product_account_uuid}}/kyc_documents/{{merged_document_uuid}}/send_signatory_otp' \\\n--header 'Authorization: Bearer 7ca663dddab977091645378870644147059bde0d1482e44de3096fcb4fa5f8a'"
							},
							"response": []
						},
						{
							"name": "EsignMergedDocument",
							"request": {
								"method": "POST",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer bba6ab3f402c4a616f688117ffa564b67fde531dfef4f5c037d3e1283c9549d6"
									}
								],
								"body": {
									"mode": "urlencoded",
									"urlencoded": [
										{
											"key": "otp",
											"value": "0025",
											"type": "text"
										}
									]
								},
								"url": "{{ob_uat}}/api/v3/product_accounts/{{product_account_uuid}}/kyc_documents/{{merged_document_uuid}}/esign_merged_document",
								"description": "Generated from cURL: curl --location -g '{{onboarding_base_url}}/api/v3/product_accounts/{{product_account_uuid}}/kyc_documents/{{merged_document_uuid}}/esign_merged_document' \\\n--header 'Authorization: Bearer bba6ab3f402c4a616f688117ffa564b67fde531dfef4f5c037d3e1283c9549d6' \\\n--data-urlencode 'otp=0025'"
							},
							"response": []
						}
					]
				},
				{
					"name": "KycApis",
					"item": [
						{
							"name": "Info KYC document",
							"request": {
								"method": "GET",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer 7851df7f3555ac0b83ef94fdf71bd454f950200020359308ce60576f3144cd79"
									},
									{
										"key": "Content-Type",
										"value": "application/x-www-form-urlencoded"
									}
								],
								"url": {
									"raw": "{{rp_uat}}/api/v3/merchants/kyc_document/info?merchant_id=8756833",
									"host": [
										"{{rp_uat}}"
									],
									"path": [
										"api",
										"v3",
										"merchants",
										"kyc_document",
										"info"
									],
									"query": [
										{
											"key": "merchant_id",
											"value": "8756833"
										}
									]
								}
							},
							"response": [
								{
									"name": "Info KYC document",
									"originalRequest": {
										"method": "GET",
										"header": [
											{
												"key": "Authorization",
												"value": "Bearer ec1b0d6e5e9890950ddfc902c1c18aadc4053653995712300b6a644f82c56d02"
											},
											{
												"key": "Content-Type",
												"value": "application/x-www-form-urlencoded"
											}
										],
										"url": {
											"raw": "https://uat-partner.payu.in/api/v3/merchants/kyc_document/info?merchant_id=8390925",
											"protocol": "https",
											"host": [
												"uat-partner",
												"payu",
												"in"
											],
											"path": [
												"api",
												"v3",
												"merchants",
												"kyc_document",
												"info"
											],
											"query": [
												{
													"key": "merchant_id",
													"value": "8390925"
												}
											]
										}
									},
									"status": "OK",
									"code": 200,
									"_postman_previewlanguage": "json",
									"header": [
										{
											"key": "Date",
											"value": "Mon, 12 Aug 2024 07:34:13 GMT"
										},
										{
											"key": "Content-Type",
											"value": "application/json; charset=utf-8"
										},
										{
											"key": "Transfer-Encoding",
											"value": "chunked"
										},
										{
											"key": "Connection",
											"value": "keep-alive"
										},
										{
											"key": "Server",
											"value": "nginx"
										},
										{
											"key": "X-DNS-Prefetch-Control",
											"value": "on"
										},
										{
											"key": "x-download-options",
											"value": "noopen"
										},
										{
											"key": "x-content-type-options",
											"value": "nosniff"
										},
										{
											"key": "x-xss-protection",
											"value": "1mode=block"
										},
										{
											"key": "Access-Control-Allow-Origin",
											"value": "*"
										},
										{
											"key": "Access-Control-Allow-Methods",
											"value": "*"
										},
										{
											"key": "Access-Control-Allow-Headers",
											"value": "*"
										},
										{
											"key": "x-frame-options",
											"value": "DENY"
										},
										{
											"key": "Strict-Transport-Security",
											"value": "max-age=31536000; includeSubDomains; preload"
										},
										{
											"key": "Strict-Transport-Security",
											"value": "max-age=63072000; includeSubdomains;"
										},
										{
											"key": "ETag",
											"value": "W/\"e85c148364a0bd7dc1e035b816940c21\""
										},
										{
											"key": "Cache-Control",
											"value": "max-age=0, private, must-revalidate"
										},
										{
											"key": "X-Request-Id",
											"value": "5fad05f8-0409-47a0-a2b7-64ffead9e276"
										},
										{
											"key": "X-Runtime",
											"value": "0.113040"
										},
										{
											"key": "Vary",
											"value": "Origin"
										},
										{
											"key": "Content-Encoding",
											"value": "gzip"
										}
									],
									"cookie": [],
									"body": "{\n    \"PAN Card of Signing Authority\": [\n        \"PAN Card\"\n    ],\n    \"Address Proof of Signing Authority\": [\n        \"Passport\",\n        \"Aadhar\",\n        \"Voter's ID\",\n        \"Driving Licence\",\n        \"Utilities Bill (electricity, water, landline, gas connection)\",\n        \"Address Verification Letter from Bank\"\n    ],\n    \"Bank Account Proof\": [\n        \"Cancelled Cheque\",\n        \"Bank Verification Letter\",\n        \"Bank Statement\",\n        \"Passbook\"\n    ],\n    \"Service Agreement\": [\n        \"Service Agreement\"\n    ]\n}"
								}
							]
						},
						{
							"name": "Documents required for KYC",
							"request": {
								"method": "GET",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer ec1b0d6e5e9890950ddfc902c1c18aadc4053653995712300b6a644f82c56d02"
									}
								],
								"url": "{{rp_uat}}/api/v3/merchants/8390925/kyc_document/required_docs"
							},
							"response": [
								{
									"name": "Documents required for KYC",
									"originalRequest": {
										"method": "GET",
										"header": [
											{
												"key": "Authorization",
												"value": "Bearer ec1b0d6e5e9890950ddfc902c1c18aadc4053653995712300b6a644f82c56d02"
											}
										],
										"url": "https://uat-partner.payu.in/api/v3/merchants/8390925/kyc_document/required_docs"
									},
									"status": "OK",
									"code": 200,
									"_postman_previewlanguage": "json",
									"header": [
										{
											"key": "Date",
											"value": "Mon, 12 Aug 2024 07:34:33 GMT"
										},
										{
											"key": "Content-Type",
											"value": "application/json; charset=utf-8"
										},
										{
											"key": "Transfer-Encoding",
											"value": "chunked"
										},
										{
											"key": "Connection",
											"value": "keep-alive"
										},
										{
											"key": "Server",
											"value": "nginx"
										},
										{
											"key": "X-DNS-Prefetch-Control",
											"value": "on"
										},
										{
											"key": "x-download-options",
											"value": "noopen"
										},
										{
											"key": "x-content-type-options",
											"value": "nosniff"
										},
										{
											"key": "x-xss-protection",
											"value": "1mode=block"
										},
										{
											"key": "Access-Control-Allow-Origin",
											"value": "*"
										},
										{
											"key": "Access-Control-Allow-Methods",
											"value": "*"
										},
										{
											"key": "Access-Control-Allow-Headers",
											"value": "*"
										},
										{
											"key": "x-frame-options",
											"value": "DENY"
										},
										{
											"key": "Strict-Transport-Security",
											"value": "max-age=31536000; includeSubDomains; preload"
										},
										{
											"key": "Strict-Transport-Security",
											"value": "max-age=63072000; includeSubdomains;"
										},
										{
											"key": "ETag",
											"value": "W/\"986be36aec460334c1605d2b7cd11262\""
										},
										{
											"key": "Cache-Control",
											"value": "max-age=0, private, must-revalidate"
										},
										{
											"key": "X-Request-Id",
											"value": "e0ff30b8-62df-4e3d-8aa4-8d8f93e90be3"
										},
										{
											"key": "X-Runtime",
											"value": "0.140811"
										},
										{
											"key": "Vary",
											"value": "Origin"
										},
										{
											"key": "Content-Encoding",
											"value": "gzip"
										}
									],
									"cookie": [],
									"body": "{\n    \"business_entity\": \"Individual\",\n    \"document_categories\": [\n        {\n            \"id\": 81,\n            \"name\": \"Bank Account Proof\",\n            \"uuid\": \"11e8-748f-297c6048-9081-020aca9875be\",\n            \"name_on_frontend\": \"BANK_PROOF\",\n            \"re_fetch\": false,\n            \"document_types\": [\n                {\n                    \"name\": \"Passbook\",\n                    \"id\": 92,\n                    \"uuid\": \"11eb-d01a-456b15f8-adc5-0242a53cdb42\",\n                    \"name_on_frontend\": \"PB\",\n                    \"issue_date_req\": false,\n                    \"expiry_date_req\": false\n                },\n                {\n                    \"name\": \"Bank Statement\",\n                    \"id\": 91,\n                    \"uuid\": \"11eb-d01a-8322997a-adc5-0242a53cdb42\",\n                    \"name_on_frontend\": \"BS\",\n                    \"issue_date_req\": false,\n                    \"expiry_date_req\": false\n                },\n                {\n                    \"name\": \"Cancelled Cheque\",\n                    \"id\": 48,\n                    \"uuid\": \"ca0a-9047-28d705a1-7e97-b530fbec4c41\",\n                    \"name_on_frontend\": \"CC\",\n                    \"issue_date_req\": false,\n                    \"expiry_date_req\": false\n                },\n                {\n                    \"name\": \"Bank Verification Letter \",\n                    \"id\": 49,\n                    \"uuid\": \"f912-b658-610ce46f-796b-14a515e41ad7\",\n                    \"name_on_frontend\": \"BC\",\n                    \"issue_date_req\": false,\n                    \"expiry_date_req\": false\n                }\n            ],\n            \"kyc_document\": null\n        },\n        {\n            \"id\": 82,\n            \"name\": \"PAN Card of Signing Authority\",\n            \"uuid\": \"11e8-748f-297824ce-9081-020aca9875be\",\n            \"name_on_frontend\": \"PANCARD_SIGNED_AUTHORITY\",\n            \"re_fetch\": false,\n            \"document_types\": [\n                {\n                    \"name\": \"PAN Card\",\n                    \"id\": 50,\n                    \"uuid\": \"11e8-748f-2946799c-9081-020aca9875be\",\n                    \"name_on_frontend\": \"PANCARD\",\n                    \"issue_date_req\": false,\n                    \"expiry_date_req\": false\n                }\n            ],\n            \"kyc_document\": null\n        },\n        {\n            \"id\": 89,\n            \"name\": \"Address Proof of Signing Authority\",\n            \"uuid\": \"11e8-748f-297a15b8-9081-020aca9875be\",\n            \"name_on_frontend\": \"ADDRESS_PROOF_SIGNED_AUTHORITY\",\n            \"re_fetch\": false,\n            \"document_types\": [\n                {\n                    \"name\": \"Passport\",\n                    \"id\": 51,\n                    \"uuid\": \"11e8-748f-2948a29e-9081-020aca9875be\",\n                    \"name_on_frontend\": \"PASSPORT\",\n                    \"issue_date_req\": true,\n                    \"expiry_date_req\": true\n                },\n                {\n                    \"name\": \"Aadhar\",\n                    \"id\": 52,\n                    \"uuid\": \"11e8-748f-294a800a-9081-020aca9875be\",\n                    \"name_on_frontend\": \"AADHAR\",\n                    \"issue_date_req\": false,\n                    \"expiry_date_req\": false\n                },\n                {\n                    \"name\": \"Voter's ID\",\n                    \"id\": 53,\n                    \"uuid\": \"11e8-748f-294c6ef6-9081-020aca9875be\",\n                    \"name_on_frontend\": \"VOTER\",\n                    \"issue_date_req\": false,\n                    \"expiry_date_req\": false\n                },\n                {\n                    \"name\": \"Driving Licence\",\n                    \"id\": 54,\n                    \"uuid\": \"11e8-748f-294e7dea-9081-020aca9875be\",\n                    \"name_on_frontend\": \"DL\",\n                    \"issue_date_req\": true,\n                    \"expiry_date_req\": true\n                },\n                {\n                    \"name\": \"Utilities Bill (electricity, water, landline, gas connection) \",\n                    \"id\": 55,\n                    \"uuid\": \"11e8-748f-29508112-9081-020aca9875be\",\n                    \"name_on_frontend\": \"BMTB\",\n                    \"issue_date_req\": false,\n                    \"expiry_date_req\": false\n                },\n                {\n                    \"name\": \"Address Verification Letter from Bank\",\n                    \"id\": 64,\n                    \"uuid\": \"24d8-a849-14f755a1-d49b-12ca65c5cd7a\",\n                    \"name_on_frontend\": \"AVFB\",\n                    \"issue_date_req\": false,\n                    \"expiry_date_req\": false\n                }\n            ],\n            \"kyc_document\": null\n        }\n    ]\n}"
								}
							]
						},
						{
							"name": "Create KYC Document",
							"request": {
								"method": "POST",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer 27a6389ec4d74fb8c3f2baf68b220a5780bf4cfc4cce004505d2c20ead6e1fba"
									}
								],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "merchant[document_category]",
											"value": "PAN Card of Signing Authority",
											"type": "text"
										},
										{
											"key": "merchant[document_type]",
											"value": "PAN Card",
											"type": "text"
										},
										{
											"key": "merchant[processed_document]",
											"type": "file",
											"src": []
										}
									]
								},
								"url": "{{rp_uat}}/api/v3/merchants/8390925/kyc_document"
							},
							"response": [
								{
									"name": "Create KYC Document",
									"originalRequest": {
										"method": "POST",
										"header": [
											{
												"key": "Authorization",
												"value": "Bearer ec1b0d6e5e9890950ddfc902c1c18aadc4053653995712300b6a644f82c56d02"
											}
										],
										"body": {
											"mode": "formdata",
											"formdata": [
												{
													"key": "merchant[document_category]",
													"value": "PAN Card of Signing Authority",
													"type": "text"
												},
												{
													"key": "merchant[document_type]",
													"value": "PAN Card",
													"type": "text"
												},
												{
													"key": "merchant[processed_document]",
													"type": "file",
													"src": "/Users/Shared/Wallpaper2024/MandatoryComplianceTraining.jpg"
												}
											]
										},
										"url": "https://uat-partner.payu.in/api/v3/merchants/8390925/kyc_document"
									},
									"status": "OK",
									"code": 200,
									"_postman_previewlanguage": "json",
									"header": [
										{
											"key": "Date",
											"value": "Mon, 12 Aug 2024 07:41:19 GMT"
										},
										{
											"key": "Content-Type",
											"value": "application/json; charset=utf-8"
										},
										{
											"key": "Transfer-Encoding",
											"value": "chunked"
										},
										{
											"key": "Connection",
											"value": "keep-alive"
										},
										{
											"key": "Server",
											"value": "nginx"
										},
										{
											"key": "X-DNS-Prefetch-Control",
											"value": "on"
										},
										{
											"key": "x-download-options",
											"value": "noopen"
										},
										{
											"key": "x-content-type-options",
											"value": "nosniff"
										},
										{
											"key": "x-xss-protection",
											"value": "1mode=block"
										},
										{
											"key": "Access-Control-Allow-Origin",
											"value": "*"
										},
										{
											"key": "Access-Control-Allow-Methods",
											"value": "*"
										},
										{
											"key": "Access-Control-Allow-Headers",
											"value": "*"
										},
										{
											"key": "x-frame-options",
											"value": "DENY"
										},
										{
											"key": "Strict-Transport-Security",
											"value": "max-age=31536000; includeSubDomains; preload"
										},
										{
											"key": "Strict-Transport-Security",
											"value": "max-age=63072000; includeSubdomains;"
										},
										{
											"key": "ETag",
											"value": "W/\"63a17dba8c14161dd7529859fc0f9394\""
										},
										{
											"key": "Cache-Control",
											"value": "max-age=0, private, must-revalidate"
										},
										{
											"key": "X-Request-Id",
											"value": "80cddb17-ff07-437f-9225-55823afac95d"
										},
										{
											"key": "X-Runtime",
											"value": "0.518505"
										},
										{
											"key": "Vary",
											"value": "Origin"
										},
										{
											"key": "Content-Encoding",
											"value": "gzip"
										}
									],
									"cookie": [],
									"body": "{\n    \"merchant\": {\n        \"mid\": \"8390925\",\n        \"kyc_document_name\": \"PAN Card of Signing Authority\",\n        \"kyc_document_uuid\": \"11ef-587e-43837330-95b0-021ec077a271\",\n        \"kyc_document_status\": \"DOCUMENT_SUBMITTED\",\n        \"error_message\": null,\n        \"created_at\": \"2024-08-12T07:41:19.000Z\"\n    }\n}"
								}
							]
						},
						{
							"name": "Show KYC Document",
							"protocolProfileBehavior": {
								"disableBodyPruning": true
							},
							"request": {
								"method": "GET",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer ec1b0d6e5e9890950ddfc902c1c18aadc4053653995712300b6a644f82c56d02"
									}
								],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "merchant[document_category]",
											"value": "PAN Card of Signing Authority",
											"type": "text"
										},
										{
											"key": "merchant[document_type]",
											"value": "PAN Card",
											"type": "text"
										},
										{
											"key": "merchant[processed_document]",
											"type": "file",
											"src": []
										}
									]
								},
								"url": "{{rp_uat}}/api/v3/merchants/8390925/kyc_document"
							},
							"response": [
								{
									"name": "Create KYC Document",
									"originalRequest": {
										"method": "POST",
										"header": [
											{
												"key": "Authorization",
												"value": "Bearer ec1b0d6e5e9890950ddfc902c1c18aadc4053653995712300b6a644f82c56d02"
											}
										],
										"body": {
											"mode": "formdata",
											"formdata": [
												{
													"key": "merchant[document_category]",
													"value": "PAN Card of Signing Authority",
													"type": "text"
												},
												{
													"key": "merchant[document_type]",
													"value": "PAN Card",
													"type": "text"
												},
												{
													"key": "merchant[processed_document]",
													"type": "file",
													"src": "/Users/Shared/Wallpaper2024/MandatoryComplianceTraining.jpg"
												}
											]
										},
										"url": "https://uat-partner.payu.in/api/v3/merchants/8390925/kyc_document"
									},
									"status": "OK",
									"code": 200,
									"_postman_previewlanguage": "json",
									"header": [
										{
											"key": "Date",
											"value": "Mon, 12 Aug 2024 07:41:19 GMT"
										},
										{
											"key": "Content-Type",
											"value": "application/json; charset=utf-8"
										},
										{
											"key": "Transfer-Encoding",
											"value": "chunked"
										},
										{
											"key": "Connection",
											"value": "keep-alive"
										},
										{
											"key": "Server",
											"value": "nginx"
										},
										{
											"key": "X-DNS-Prefetch-Control",
											"value": "on"
										},
										{
											"key": "x-download-options",
											"value": "noopen"
										},
										{
											"key": "x-content-type-options",
											"value": "nosniff"
										},
										{
											"key": "x-xss-protection",
											"value": "1mode=block"
										},
										{
											"key": "Access-Control-Allow-Origin",
											"value": "*"
										},
										{
											"key": "Access-Control-Allow-Methods",
											"value": "*"
										},
										{
											"key": "Access-Control-Allow-Headers",
											"value": "*"
										},
										{
											"key": "x-frame-options",
											"value": "DENY"
										},
										{
											"key": "Strict-Transport-Security",
											"value": "max-age=31536000; includeSubDomains; preload"
										},
										{
											"key": "Strict-Transport-Security",
											"value": "max-age=63072000; includeSubdomains;"
										},
										{
											"key": "ETag",
											"value": "W/\"63a17dba8c14161dd7529859fc0f9394\""
										},
										{
											"key": "Cache-Control",
											"value": "max-age=0, private, must-revalidate"
										},
										{
											"key": "X-Request-Id",
											"value": "80cddb17-ff07-437f-9225-55823afac95d"
										},
										{
											"key": "X-Runtime",
											"value": "0.518505"
										},
										{
											"key": "Vary",
											"value": "Origin"
										},
										{
											"key": "Content-Encoding",
											"value": "gzip"
										}
									],
									"cookie": [],
									"body": "{\n    \"merchant\": {\n        \"mid\": \"8390925\",\n        \"kyc_document_name\": \"PAN Card of Signing Authority\",\n        \"kyc_document_uuid\": \"11ef-587e-43837330-95b0-021ec077a271\",\n        \"kyc_document_status\": \"DOCUMENT_SUBMITTED\",\n        \"error_message\": null,\n        \"created_at\": \"2024-08-12T07:41:19.000Z\"\n    }\n}"
								}
							]
						},
						{
							"name": "Delete KYC document",
							"request": {
								"method": "DELETE",
								"header": [
									{
										"key": "Authorization",
										"value": "Bearer ec1b0d6e5e9890950ddfc902c1c18aadc4053653995712300b6a644f82c56d02"
									},
									{
										"key": "Content-Type",
										"value": "application/x-www-form-urlencoded"
									}
								],
								"url": "{{rp_uat}}/api/v3/merchants/8390925/kyc_document/11ef-587e-43837330-95b0-021ec077a271"
							},
							"response": [
								{
									"name": "Delete KYC document",
									"originalRequest": {
										"method": "DELETE",
										"header": [
											{
												"key": "Authorization",
												"value": "Bearer ec1b0d6e5e9890950ddfc902c1c18aadc4053653995712300b6a644f82c56d02"
											},
											{
												"key": "Content-Type",
												"value": "application/x-www-form-urlencoded"
											}
										],
										"url": "https://uat-partner.payu.in/api/v3/merchants/8390925/kyc_document/11ef-587e-43837330-95b0-021ec077a271"
									},
									"status": "No Content",
									"code": 204,
									"_postman_previewlanguage": "plain",
									"header": [
										{
											"key": "Date",
											"value": "Mon, 12 Aug 2024 07:53:36 GMT"
										},
										{
											"key": "Connection",
											"value": "keep-alive"
										},
										{
											"key": "Server",
											"value": "nginx"
										},
										{
											"key": "X-DNS-Prefetch-Control",
											"value": "on"
										},
										{
											"key": "x-download-options",
											"value": "noopen"
										},
										{
											"key": "x-content-type-options",
											"value": "nosniff"
										},
										{
											"key": "x-xss-protection",
											"value": "1mode=block"
										},
										{
											"key": "Access-Control-Allow-Origin",
											"value": "*"
										},
										{
											"key": "Access-Control-Allow-Methods",
											"value": "*"
										},
										{
											"key": "Access-Control-Allow-Headers",
											"value": "*"
										},
										{
											"key": "x-frame-options",
											"value": "DENY"
										},
										{
											"key": "Strict-Transport-Security",
											"value": "max-age=31536000; includeSubDomains; preload"
										},
										{
											"key": "Strict-Transport-Security",
											"value": "max-age=63072000; includeSubdomains;"
										},
										{
											"key": "Cache-Control",
											"value": "no-cache"
										},
										{
											"key": "X-Request-Id",
											"value": "27bcf780-d10a-471b-a3a3-a6e7ee912f6a"
										},
										{
											"key": "X-Runtime",
											"value": "0.515174"
										},
										{
											"key": "Vary",
											"value": "Origin"
										}
									],
									"cookie": [],
									"body": ""
								}
							]
						}
					]
				}
			]
		}
	],
	"variable": [
		{
			"key": "hub_uat",
			"value": "https://uat-accounts.payu.in",
			"type": "default"
		}
	]
}
```

<br />

## Request parameters

<details>
  <summary>Reference information for request parameters</summary>

  | Parameter                          | Reference                                                                                                                  |
  | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
  | merchant\[business\_category]      | For the list of business categories, refer to [Business. Category List](ref:partner-category-list).                        |
  | merchant\[business\_entity\_type]  | For the list of business entity type, refer to [Business Entity Type](ref:partner-category-list#business-entity-type).     |
  | merchant\[business\_sub\_category] | For the list of business subcategories, refer to [Business Sub-Category](ref:partner-category-list#business-sub-category). |
</details>