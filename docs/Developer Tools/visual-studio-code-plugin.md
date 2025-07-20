---
title: Visual Studio Code Plugin
deprecated: false
hidden: true
metadata:
  robots: index
---
## Installation Steps

### Method 1: VS Code Marketplace (Recommended)

1. **Open Visual Studio Code**

2. **Navigate to Extensions**
   * Click on the Extensions icon in the Activity Bar (left sidebar)
   * Or use keyboard shortcut: `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac)

3. **Search for PayU Plugin**
   * Type "PayU Payments" in the search box
   * Look for "PayU Payments" by PayuPayments publisher

4. **Install the Plugin**
   * Click the "Install" button
   * Wait for the installation to complete

### Method 2: Direct Installation via URL

1. **Open Command Palette**
   * Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)

2. **Run Install Command**
   * Type "Extensions: Install from VSIX"
   * Or visit: [https://marketplace.visualstudio.com/items?itemName=PayuPayments.Payu-Payments](https://marketplace.visualstudio.com/items?itemName=PayuPayments.Payu-Payments)
   * Click "Install" button on the marketplace page

## Using the VS Code Plugin

### 1. Create New Project

```bash
# Create a new directory for your project
mkdir payu-integration-project
cd payu-integration-project
```

### 2. Open Project in VS Code

```bash
code .
```

### 3. Generate Boilerplate Code

1. **Open Command Palette**
   * Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)

2. **Search for PayU Commands**
   * Type "PayU" to see available commands
   * Select appropriate command based on your integration type

3. **Available Commands** (typical examples):
   * `PayU: Generate Payment Form`
   * `PayU: Generate API Integration`
   * `PayU: Create Sample Application`

### 4) Configure Environment

Update the configuration file similar to the following:

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

### 5. Code Snippets Usage

* Type `payu-` in any JavaScript/HTML file to see available snippets
* Common snippets include:
  * `payu-payment-form`
  * `payu-api-call`
  * `payu-webhook-handler`

***