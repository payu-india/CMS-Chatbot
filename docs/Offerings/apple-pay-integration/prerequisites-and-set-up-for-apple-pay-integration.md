---
title: Prerequisites and Set up
deprecated: false
hidden: false
metadata:
  title: Prerequisites and Set up for Apple Pay Integration
  robots: index
---
To enable Apple Pay on your website:

<Callout icon="📘" theme="info">
  **Notes**:

  * The file path must be exactly as specified (case-sensitive).
  * File hosting is required on websites where PayU Checkout loads as an overlay/iframe. This includes WooCommerce, Magento, and other ecommerce platforms where PayU appears as an overlay, or any website where PayU Checkout iframe is embedded.
  * File hosting is required if you use both hosted checkouts and overlay iframe integration on your merchant account. Do not activate Apple Pay if you have both these kinds of checkouts unless you have hosted the file at the exact path.
</Callout>

## Domain Verification Process

1. Download the verification file.

<Callout icon="📘" theme="info">
  **Note**: Contact your PayU Key Account Manager or <Anchor label="PayU Support" target="_blank" href="help.payu.in">PayU Support</Anchor> for the verification file.
</Callout>

<br />

2. Upload the file so that it is hosted the file on your server:
   * Upload the file to this exact path on your website:
     ```
     /.well-known/apple-developer-merchantid-domain-association
     ```
   * For example, if your domain is `https://www.yourstorename.com`, the file must be accessible at:
     ```
     https://www.yourstorename.com/.well-known/apple-developer-merchantid-domain-association
     ```

<Callout icon="📘" theme="info">
  Ensure correct configuration. When setting up Apple Pay domain verification, follow these requirements:

  <Accordion title="File Path and Response" icon="fa-info-circle">
    * The verification file must be accessible at the exact path `/.well-known/apple-developer-merchantid-domain-association`.
    * The file must return a direct HTTP 200 status code and not a 301, 302, or any 3xx redirects.
    * Apple does not support HTTP URL redirects for the domain association file.
  </Accordion>

  <Accordion title="Server Configuration" icon="fa-info-circle">
    * The file must be served via HTTPS 1.1 protocol.
    * The HTTP response can be as plaintext or a file (binary object).
    * Set the Content-Type header to `application/octet-stream` to indicate this is a binary file download.
  </Accordion>

  <Accordion title="Network Access" icon="fa-info-circle">
    * Ensure the file is not behind a firewall or access restrictions.
    * If using a firewall, configure it to allow Apple's IP addresses. For more information on Apple's IP address, refer to [Apple documentation](https://developer.apple.com/documentation/applepayontheweb/setting-up-your-server%23Allow-Apple-IP-Addresses-for-Domain-Verification)
  </Accordion>
</Callout>

3. Verify each domain separately:
   * Repeat this process for all domains and subdomains from where checkout is initiated with an overlay iframe.
   * This includes:
     * Top-level domains (for example, `yourdomain.com`)
     * Subdomains (for example, `shop.yourdomain.com`, `checkout.yourdomain.com`, `us.yourdomain.com`, `uk.yourdomain.com`, and so on)

4. Confirm with PayU:
   * After the files are uploaded, notify your PayU Key Account Manager(KAM) or contact [PayU Integration Support](mailto:integration@payu.in).
   * PayU will verify the setup and activate Apple Pay on your account.