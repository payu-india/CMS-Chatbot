---
name: Closed_Loop_HMAC
---
This API uses HMAC-SHA512 authentication on the header.

<HTMLBlock>{`
<table class="api-parameters">
  <thead>
    <tr>
      <th scope="col">Parameter</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <strong>walletIdentifier</strong><br />
        <span class="required-badge">mandatory</span>
      </td>
      <td>
        <code>String</code> Program Type (e.g., CLW)
      </td>
    </tr>
    <tr>
      <td>
        <strong>date</strong><br />
        <span class="required-badge">mandatory</span>
      </td>
      <td>
        <code>String</code> GMT formatted date (e.g., Thu, 17 Feb 2022 08:17:59 GMT)
      </td>
    </tr>
    <tr>
      <td>
        <strong>Authorization</strong><br />
        <span class="required-badge">mandatory</span>
      </td>
      <td>
        <code>String</code> HMAC-SHA512-based authentication token
      </td>
    </tr>
    <tr>
      <td>
        <strong>Content-Type</strong><br />
        <span class="required-badge">mandatory</span>
      </td>
      <td>
        <code>String</code> application/json
      </td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

<Callout icon="↩️">
  If you do not post the authentication, you will get error in response. For the list of error codes, refer to [Status Codes](ref:status-codes-clw)
</Callout>

### hmac authentication logic

```
hmac username="smsplus", algorithm="sha512", headers="date", signature="7ff938849aa79265a3de63fe241dfecb1c680f58c6d11e9f9ca08512afea374705eb9f8995ef6c4584e16eca2e1dc688262bb0937a36cc0f75ec22a9eea33523"
```

Where, the fields in this example are:

* **username**: The merchant key of the merchant.
* **algorithm**: This must have the value as hmac-sha512 that is used for this API.
* **headers**: This must have the value as date digest.
* **signature**: This must contain the hmacsha512 of (signing_string, merchant_secret), where:
* **signing_string**: It must be in the "date: \{dateValue}"format. Here, the dateValue is the same values in the fields listed in this table For example, "date: Thu, 17 Feb 2022 08:17:59 GMT"
* **merchant_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to Generate Merchant Key and Salt.
