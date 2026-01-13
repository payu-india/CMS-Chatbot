---
title: MCP Troubleshooting
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: MCP Troubleshooting
deprecated: false
hidden: false
metadata:
  title: Remote MCP for Merchants - Troubleshooting
  keywords:
    - MCP Troubleshooting
    - Connection Issues
    - Authentication Errors
    - MCP Debug
  robots: index
---

This page helps you diagnose and resolve common issues when using PayU Remote MCP for Merchants.

## Connection Issues

### Can't Connect to Service

**Issue:** Client can't reach the service or times out.

**Symptoms:**

* Connection timeout errors
* "Unable to connect" messages
* No response from service

**Solutions:**

1. **Verify the service URL is correct:**
   ```
   https://api.payu.in/mcp
   ```

2. **Check your internet connection:**
   * Test connectivity to other websites
   * Verify your network allows HTTPS traffic

3. **Ensure your firewall allows outbound HTTPS:**
   * Port 443 must be open for outbound connections
   * Check corporate firewall or VPN settings

4. **Check service status:**
   * The service may be temporarily unavailable
   * Contact PayU support for service status updates

### Slow Response Times

**Issue:** Requests take a long time to complete.

**Solutions:**

* Check your internet connection speed
* Reduce the scope of your queries (e.g., shorter date ranges)
* Verify no network congestion or proxy issues

## Authentication Issues

### Authentication Fails

**Issue:** Login doesn't work or keeps asking for credentials.

**Symptoms:**

* Login page appears repeatedly
* "Authentication failed" errors
* Browser opens but login doesn't complete

**Solutions:**

1. **Clear your client's cache and retry:**
   * Restart your MCP client
   * Clear browser cookies for PayU domains

2. **Verify your PayU account credentials:**
   * Ensure you're using the correct username/password
   * Try logging in directly at PayU dashboard

3. **Check if your account has MCP access:**
   * Contact your PayU account manager
   * Verify MCP service is enabled for your account

### "Unauthorized" Error (401)

**Issue:** Getting 401 errors on requests.

**Symptoms:**

* `HTTP 401 Unauthorized` response
* "Token invalid" or "Token expired" messages
* Previously working requests now fail

**Solution:** Token has expired. Re-authenticate by:

1. Restarting your MCP client
2. Making a new request (authentication will trigger automatically)
3. Complete the login flow in your browser

> 📘 Note
>
> Tokens typically last several hours. If you're getting frequent 401 errors, check that your system clock is accurate.

### OAuth Flow Doesn't Complete

**Issue:** Browser opens but nothing happens after login.

**Solutions:**

* Ensure pop-ups are not blocked for the PayU domain
* Check that JavaScript is enabled in your browser
* Try a different browser
* Disable browser extensions that might interfere

## Merchant Account Issues

### "Merchant Selection Required" Error

**Issue:** Error message asking to select a merchant account.

**Symptoms:**

```
Error: Merchant selection required. You have multiple merchant accounts.
Please select which account to use.
```

**Solution:** You have multiple merchant accounts. Select one:

```
"What merchant accounts do I have access to?"
"Switch to merchant account [YOUR_MERCHANT_ID]"
```

### Wrong Merchant Account Selected

**Issue:** Operations are affecting the wrong merchant account.

**Solution:** Verify and switch accounts:

```
"Which merchant account am I currently using?"
"Switch to merchant account [CORRECT_MERCHANT_ID]"
```

### Can't See Expected Merchant Account

**Issue:** A merchant account you expect to have access to isn't listed.

**Solutions:**

* Verify your PayU account has access to that merchant
* Contact your PayU account administrator
* Check if there are permission restrictions

## Tool Execution Issues

### Tool Call Fails

**Issue:** Tool execution returns an error.

**Symptoms:**

* "Tool not found" errors
* "Invalid arguments" errors
* "Permission denied" errors

**Solutions:**

1. **Verify you have the correct permissions:**
   * Some tools require specific permissions
   * Contact your account administrator

2. **Check that you've selected the correct merchant account:**
   ```
   "Which merchant account am I currently using?"
   ```

3. **Ensure the tool arguments are valid:**
   * Use correct transaction IDs
   * Use valid date formats
   * Check required parameters

### Tool Not Found

**Issue:** Requested tool doesn't exist.

**Solutions:**

* Check the tool name spelling
* Verify the tool is available for your account:
  ```
  "What tools do I have access to?"
  ```
* The tool may require additional permissions

### Invalid Arguments

**Issue:** Tool rejects the provided arguments.

**Common Causes:**

* Invalid date format (use YYYY-MM-DD)
* Invalid transaction ID format
* Missing required parameters
* Amount out of valid range

### No Results Returned

**Issue:** Query returns empty results when you expect data.

**Solutions:**

* Verify you're querying the correct merchant account
* Check the date range is correct
* Ensure transactions exist for the specified criteria
* Try broadening the search criteria

## Error Messages Reference

| Error                       | Meaning                    | Solution                  |
| --------------------------- | -------------------------- | ------------------------- |
| `401 Unauthorized`          | Token expired or invalid   | Re-authenticate           |
| `403 Forbidden`             | Permission denied          | Check account permissions |
| `404 Not Found`             | Tool or resource not found | Verify tool name          |
| `429 Too Many Requests`     | Rate limit exceeded        | Wait and retry            |
| `500 Internal Server Error` | Server-side issue          | Contact support           |

## Getting Help

If you've tried the above solutions and still have issues:

1. **Gather Information:**
   * Error messages (exact text)
   * Steps to reproduce the issue
   * Your MCP client and version
   * Approximate time the issue occurred

2. **Contact Support:**
   * Reach out to your PayU service administrator
   * Include all gathered information

## Next Steps

* [FAQ](doc:remote-mcp-faq) - Common questions and answers
* [Security & Privacy](doc:remote-mcp-security-privacy) - Security-related concerns
