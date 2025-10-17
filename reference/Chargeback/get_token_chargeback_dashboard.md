---
title: Generate Token on Chargeback Dashboard
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
This section provides procedure to generate token on the Chargeback Dashboard. This bearer token must be used in the header with the following Chargeback APIs:

* [Read Chargeback API](https://docs.payu.in/reference/read-chargeback-api)
* [Read Reasons API](https://docs.payu.in/reference/read-reasons-api)
* [Accept Chargeback API](https://docs.payu.in/reference/accept-chargeback-api)
* [Accept/Contest Chargeback API](https://docs.payu.in/reference/accept-contest-chargeback-api)
* [Contest Chargeback API](https://docs.payu.in/reference/contest-chargeback-api)

<Callout icon="📘" theme="info">
  **Note**: Use the **Regenerate Token** API to regenerate token after you generate the token as described in this section. For more information, refer to [Regenerate Token API - Chargeback](ref:regenerate-token-api-chargeback).
</Callout>

To get token on Chargeback Dashboard:

1. 1. Navigate to the Chargeback dashboard.
   * Log in to PayU Dashboard.
   * Select **Chargeback** on the menu or left-pane.
2. Click the user profile drop-down menu and then click your profile photo on the top-right.

<Image align="center" border={true} src="https://files.readme.io/a905273f816f4ad559487b592866f77ac7bcd16b921e08e2de1da752621f2fa7-chargeback_dashboard_profile_menu.png" className="border" />

The _User Profile_ page is displayed with the tokens generated in the bottom.

<Image align="center" border={true} src="https://files.readme.io/dd666556acda33488f8b648b71eabdcb736908c8eeea86349d43ca95f911e99b-chargeback_dashboard_profile_page.png" className="border" />

1. Click the add button against the **Tokens** as in the above screenshot.

   The _Add new token_ pop-up page is displayed.

<Image align="center" border={true} width="450px" src="https://files.readme.io/13aef9cebf985a271533c6f025017a82cf46b3049cd3de7b2c1d4268e441a6de-chargeback_add_new_token.png" className="border" />

1. Enter a descriptive name for the token in the **Name** field.
2. Select an expiry date in the **Expires at** field using the calendar button.
3. Click **generate**.
4. Copy the generated token for use in API calls.
5. Click **Submit**.

## Troubleshooting

### Token expiry

**Issue:** Token has expired and cannot be used
**Solution:** Create a new token through the UI. You cannot regenerate expired tokens via API.

### Invalid token errors

**Issue:** System rejects token with "invalid token" error
**Solution:**

* Check if the token has expired
* Verify the token format in API headers is correct
* Regenerate the token if necessary

### API integration problems

**Issue:** Token not working in API calls
**Solution:**

* Confirm you're passing the token in the correct header format
* Verify the API endpoint and request structure
* Test with a known working API call

## Security best practices

### Manage token lifecycle

* Set appropriate expiry dates that balance security and operational needs
* Regenerate tokens periodically for enhanced security
* Monitor token usage and invalidate tokens you're not using
