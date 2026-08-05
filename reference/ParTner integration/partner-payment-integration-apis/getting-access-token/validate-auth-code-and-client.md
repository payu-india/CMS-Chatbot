---
title: Validate Auth Code and Client API - Partner Integration
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Validate Auth Code and Client** API is used for validating auth code and client.

**Environment**

|                |                                |
| :------------- | :----------------------------- |
| **Test**       | \<https://uat-accounts.payu.in> |
| **Production** | \<https://accounts.payu.in>     |

> 📘 Notes:
> 
> The grant type for the **grant_type** parameter for this API is **authorization_code**.

## Request parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>client_id<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The client identifier is specified in this parameter. </p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>68a276132f82c056a6ed9b5<br>e00e45523c260544b87dd3cc91840d591bd93</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>client_secret<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The client secret code is specified in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>93f29bd09aca64f304ee8380232310f7<br>caa0bc2dcd838f15903dc85b0110b</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>grant_type<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Grant type is used by clients to obtain an access token outside of the context of a user. The grant type is specified in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>authorization_code</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>code<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The client authorization code is specified in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>23e563c95e3c433e38072fef0c8d1<br>8b21d8598c51eb498814e7c9cadd60edc09</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>redirect_uri<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> The redirect URL is specified in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="https://www.abcdefghi/success">https://www.abcdefghi/success</a></p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```curl
curl --location 'https://uat-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: USERTXNINFO=6513cd7fa47ae5.28444661' \
--data-urlencode 'client_id=6f7afb8ad5bc80bb51c7076449b67ee882430c8c06fda6f953d2a51f803c81a2' \
--data-urlencode 'client_secret=4fc4623fdb3e8218ee032d6ec40a7a186d546e57f65b3c7adb4704bcc530e041' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'code=a5a6b9694555ead09c8e024c0ddbe008590344d7e55d6d25af0f6881d7f3c67a' \
--data-urlencode 'redirect_uri=https://abc.in'
```

## Response parameters

<PartnerAuthenticationResponseParameters />

## Sample response

### Success response

- Status - 200

```
{
    "access_token": "e6ff7e34b704be2b14c8ae3c0e776597df4ae7de9e12d3e4c79781fcbbf2c4bb",
    "token_type": "Bearer",
    "expires_in": 7199,
    "refresh_token": "356fe080daa69438e0c2d3b0a80b3fe4aa3f78b264e6092e95e4429ae59486a7",
    "scope": "credentials_using_oauth create_payment_links read_payment_links update_payment_links delete_payment_links",
    "created_at": 1709198191,
    "user_uuid": "11ed-933c-d307ba06-b71a-0a64ecf8a4cc"
}
```

### Failure response

<FailureResponseForValidateAuthCode />