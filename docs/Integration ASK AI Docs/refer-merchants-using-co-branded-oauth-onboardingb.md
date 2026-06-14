---
title: 'Refer Merchants using Co-Branded (OAuth) Onboardingb '
deprecated: false
hidden: true
metadata:
  robots: index
---
Co-Branded Onboarding (OAuth) flow allows the partners to provide a seamless co-branded onboarding journey for merchants powered by PayU, where the partners can customize the Look & Feel of the onboarding GUI without building the GUI from scratch. At its core, it is a simple but seamless onboarding product for partners who will redirect their users to PayU only to complete onboarding.

OAuth Journey Partner Portal Creation/Configuration Steps :-
1.Partner needs to create partner account on PayU platform using below link and fill all  required details.

Test/ UAT Environment:-
Production Environment:-
2.Once the account is created, the partner will get access to PayU Partner dashboard portal.

3.Partner will share/send request to PayU for enabling Co-Branded (OAuth) flow on their  partner account.

4.We will then enable OAuth flow on Test partner account(from backend) along with few  mandatory scopes:
• Scope name:- credentials\_using\_oauth
• is\_platform\_partner
• OAuth flow
• My App section
• Scopes for PG / payment link (Note:- As per use-case of partner)
• Skip Onboarding flag (recommended for Testing)
5.Steps to configure URLs and logo:-
 a. Log into PayU partner dashboard and navigate to the user menu(Top right corner)

b. Navigate to the user menu(Top right corner) and select “My App” section. Expand “Application Details”, you need to fill redirect URL and other details like below and click on submit.

Redirect uri :- This is the mandatory URL which is required to redirect your merchant to your website/application after the onboarding/consent given from merchant.

<br />

c. Then expand “Branding details“ to update partner logo, click Browse and select brand logo to display.

Note: The brand logo should in JPG/JPEG, less than 5MB in size and width and height should be 90pixels.

d. In order to get Client id , client secret , reseller/UUID in “My App” section, expand “Download client credentials“ and click on Download button.

<br />

OAuth Journey Onboarding Workflow:-

If merchant already has PayU account then partner need to follow login workflow and if merchant is new on PayU platform then partner need to follow Sign-up workflow by creating below links.

Merchant Login / Sign-Up Workflow with Co-Branded Onboarding-

Same link is use for sign-up flow \[For new merchants only], merchant just need to click on sign-up and fill all mandatory details then click on “Activate Account“ button.

Steps for login workflow with Co-Branded (OAuth) \[For those merchants who has
already/existing PayU account]
a. Navigate to the OAuth link appended with the new email id in the following format:
Production Env:- [https://onboarding.payu.in/app/account?reseller\_id=](https://onboarding.payu.in/app/account?reseller_id=)<Merchant ID>\&email=<Merchant mail ID to sign-up>

For example:

Test/ UAT Env:- [https://uat-](https://uat-)
onepayuonboarding.payu.in/app/account?reseller\_id=<Merchant ID>\&email=<Merchant mail ID to sign-up>

For example:

Where <Merchant ID> is substituted with reseller ID and <Merchant mail ID to sign-up> is substituted with merchant mail ID to sign-up.

NOTE:- In OAuth link merchant can append “state” parameter also at the end of url. This is optional parameter & use as identifier and it is add from merchant end in the request url and it will get back in redirect uri along with auth\_code and merchant ID.

\&state=xyz123
b. The Merchant Login page is displayed, enter merchant email id and password and click on login button.

After login/sign up, merchant can fill KYC details or get fully registered with us by uploading/approving documents.

After the Sign Up/login process or after onboarding completion,
Merchant will get a screen display to give the consent to be linked to Partner. 3.Click on Allow access to the account to provide consent.

A confirmation message is displayed, similar to the following screenshot:

<br />

d. Click Back to <app name> app.

4.After giving the consent, the merchant will get redirected to partner's redirect URI and will get “auth code” and “Merchant ID” in return(POST). Partner needs to capture these details.

For Example:-

<br />

5.Next step is calling “Validate Auth Code and Client “ API.

The Validate Auth Code and Client API is used for validating auth code and it will be used to create Payment links and can fetch key/salt of merchants on their behalf.

Sample curl request:-

curl --location  \\
\--header 'Content-Type: application/x-www-form-urlencoded' \\
\--data-urlencode 'client\_id=58234a4xxxxxxxxxxxxxxxxxxx4819b4a8e' \\
\--data-urlencode 'client\_secret=ca42bxxxxxxxxxxx326f68c4f552af9d' \\
\--data-urlencode 'grant\_type=authorization\_code' \\
\--data-urlencode 'code=5ea8x
\--data-urlencode 'redirect\_uri=

Sample curl response:-

{ 
"access_token": "d6403abc97xxxxxxxxxxxxxxx30374d16a600b", "token_type": "Bearer", 
"expires_in": 7200, 
"refresh_token": "16c5b2432acxxxxxxxxxd4a70c747a7ac0cb1e0", "scope": "credentials_using_oauth", 
"created_at": 1553500453, 
"user_uuid": "11e7-a7f6-xxxxxxxx-bbb7-4a020b6b2b14" 
}

6.Next step is calling “Get Merchant Credentials “ API.

The Get Merchant Credentials API is used to perform the following:

• Used to get the merchant credentials to generate the API Key and Salt • Authorized using the Client ID and Client Secret to generate the access token

Sample curl request:-

curl --location ' \ --header 'Content-Type: application/json' \\
\--header 'Authorization: Bearer
bf5ef42165c39b2c21a3ca1717ef612fe1447be504e7a27481d89adf48f5066a'

Sample curl response:-

{ "data":
{
"credentials": {
"prod_key": "JPM7Fg",
"prod_salt": "a*******" }
}
}
