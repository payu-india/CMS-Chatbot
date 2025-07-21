---
title: Visual Studio Code Plugin
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes how to install the PayU plugin for Visual Studio IDE.

## Plugin features

* Code snippets for common PayU integration patterns
* Boilerplate generation for different payment methods
* Syntax highlighting for PayU-specific configurations

## Installation Steps

### Method 1: VS Code Marketplace (Recommended)

1. Open Visual Studio Code

2. Navigate to extensions:
   * Select **Extensions**  under **Activity** from the menu on left pane.
   OR
   * Use the keyboard shortcut: `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac)

3. Search for PayU Plugin:
   * Type "PayU Payments" in the search box
   * Look for "PayU Payments" by PayU Payments publisher.

4. Install the Plugin:
   * Click  **Install**.
   * Wait for the installation to complete

### Method 2: Direct Installation via URL

1. Open the command palette:
   * Press the `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) key combinations.

2. Run Install command:
   * Type "Extensions" to  install from VSIX.\
     OR
   * Navigate to the following URL and click **Install** on the marketplace page:

[https://marketplace.visualstudio.com/items?itemName=PayuPayments.Payu-Payments](https://marketplace.visualstudio.com/items?itemName=PayuPayments.Payu-Payments)

## Using the VS Code Plugin

1. Create new project by creating a new directory for your project using the following MS DOS shell commands:

```bash
mkdir payu-integration-project
cd payu-integration-project
```

1. Open project in VS Code
2. Generate boilerplate code:
   * Open command palette using the`Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) key combination.
   * Type "PayU" to see available commands.
   * Select appropriate command based on your integration type.
     * PayU: Generate Payment Form
     * PayU: Generate API Integration
     * PayU: Create Sample Application
   * Configure environment by updating the configuration file similar to the following:

```javascript
// config.js or similar
const config = {
    // For Test Environment
    apiUrl: 'https://apitest.payu.in/v2/payments',
    // For Production Environment  
    // apiUrl: 'https://api.payu.in/v2/payments',
    
    merchantId: 'YOUR_MERCHANT_ID',
    secretKey: 'YOUR_SECRET_KEY'
};
```

1. Code snippets usage
   * Type `payu-` in any JavaScript/HTML file to see available snippets

```
payu-payment-form
payu-api-call
payu-webhook-handler
```

<br />

## Troubleshooting

### Plugin Not Visible

* **Solution**: Restart your IDE after installation
* **Alternative**: Check if plugin is enabled in settings

### Code Snippets Not Working

* **Solution**: Ensure you're in the correct file type (.js, .java, .html)
* **Alternative**: Check snippet trigger keywords

### Template Generation Fails

* **Solution**: Verify project structure and dependencies
* **Alternative**: Check IDE logs for error details