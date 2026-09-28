---
name: PLbearertoken
---
<Callout icon="🔑" theme="default">
  ### **Get Your Bearer Token Before Calling this Endpoint**

  This API uses OAuth 2.0 authentication.

  1. Call the <Anchor target="_blank" href="https://docs.payu.in/reference/generate-access-token">Generate an Access Token</Anchor> token with `grant_type=client_credentials` and `scope=create_payment_links`
  2. Copy the `access_token` from the response
  3. Pass it as `Authorization: Bearer {access_token}` in every request

  <Columns layout="fixed">
    <Column>
      **Token Expiry:** Check `expires_in` in the token response and refresh before it lapses.
    </Column>
  </Columns>
</Callout>
