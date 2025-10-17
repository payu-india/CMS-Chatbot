---
title: Gent Token on Chargeback Dashboard
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

To get token on Charageback Dashbaord:
1. 1. Navigate to the Chargeback dashboard.

   * Log in to PayU Dashboard.
   * Select **Chargeback** on the menu or left-pane.
2. Go to the account section.
2. Enter a descriptive name for the token.
3. Specify an expiry date (for example, October 30).
4. Select **Generate token**.
5. Copy the generated token for use in API calls.


## Troubleshooting

### Token expiry
**Issue:** Token has expired and cannot be used  
**Solution:** Create a new token through the UI. You cannot regenerate expired tokens via API.

### Invalid token errors
**Issue:** System rejects token with "invalid token" error  
**Solution:** 
- Check if the token has expired
- Verify the token format in API headers is correct
- Regenerate the token if necessary

### API integration problems
**Issue:** Token not working in API calls  
**Solution:**
- Confirm you're passing the token in the correct header format
- Verify the API endpoint and request structure
- Test with a known working API call

## Security best practices

### Manage token lifecycle
- Set appropriate expiry dates that balance security and operational needs
- Regenerate tokens periodically for enhanced security
- Monitor token usage and invalidate tokens you're not using

