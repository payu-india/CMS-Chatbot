---
title: IntelliJ IDEA Plugin
deprecated: false
hidden: true
metadata:
  robots: index
---
## Installation Steps

## Method 1: JetBrains Marketplace (Recommended)

1. Open IntelliJ IDEA

2. Navigate to Plugins
   * Select the **File** > **Settings** (Windows/Linux) or **IntelliJ IDEA** > **Preferences** (Mac) from menu.
   * Select **Plugins** from the menu on left pane.

3. Search and Install:
   * Select the **Marketplace** tab.
   * Search for "PayU Payments Code Snippets"
   * Click **Install**.
   * Restart IntelliJ IDEA when prompted

#### Method 2: Direct Installation

1. Download Plugin:
   * Navigate to the marketplace page:\
     [https://plugins.jetbrains.com/plugin/27588-payu-payments-code-snippets](https://plugins.jetbrains.com/plugin/27588-payu-payments-code-snippets)
   * Click **Get** or **Install to IntelliJ IDEA**.

2. Manual Installation\*\* (if needed):
   * Download the plugin file (.jar).
   * Select the **File** > **Settings** > **Plugins** menu.
   * Click the **Configure** button ⚙️ > **Install Plugin from Disk**
   * Double-click the downloaded file to install.

## Using the IntelliJ IDEA Plugin

### Step 1: Create a new project

1. Select the **File > New > Project** menu.

2. Choose your preferred project type (Java, Spring Boot, etc.)

3. Configure the project settings:
   * Set project name and location
   * Configure SDK and dependencies

### Step 2: Access PayU templates

1. Right-click the project folder.

2. Select **New** and look for PayU templates.

3. Choose the appropriate template

4. Type `payu` and press the `Tab` key to see available templates.

### Step 3: Code generation

1. Payment Integration templates:
   * **payu-payment-request**: Generates payment request code
   * **payu-payment-response**: Generates response handling code
   * **payu-webhook**: Generates webhook endpoint code

2. Configuration templates:

```java
// Example generated configuration
@Configuration
public class PayUConfig {
    
    @Value("${payu.merchant.id}")
    private String merchantId;
    
    @Value("${payu.secret.key}")
    private String secretKey;
    
    // Test Environment
    private static final String TEST_URL = "https://apitest.payu.in/v2/payments";
    
    // Production Environment  
    private static final String PROD_URL = "https://api.payu.in/v2/payments";
}
```

### Step 4: Environment configuration

* Configure the **application.properties** file.

```properties
# application.properties for Test Environment
payu.api.url=https://apitest.payu.in/v2/payments
payu.merchant.id=YOUR_MERCHANT_ID
payu.secret.key=YOUR_SECRET_KEY
payu.environment=test

# For Production, change to:
# payu.api.url=https://api.payu.in/v2/payments
# payu.environment=prod
```

* Perform final testing

***

## 📝 Plugin Features

### Visual Studio Code Plugin Features

* ✅ Code snippets for common PayU integration patterns
* ✅ Boilerplate generation for different payment methods
* ✅ Syntax highlighting for PayU-specific configurations
* ✅ IntelliSense support for PayU API parameters

### IntelliJ IDEA Plugin Features

* ✅ Live templates for rapid code generation
* ✅ File templates for entire integration modules
* ✅ Code completion for PayU API endpoints
* ✅ Integration with Spring Boot and other frameworks

***

## 🔍 Troubleshooting

### Common Issues

#### Plugin Not Visible

* **Solution**: Restart your IDE after installation
* **Alternative**: Check if plugin is enabled in settings

#### Code Snippets Not Working

* **Solution**: Ensure you're in the correct file type (.js, .java, .html)
* **Alternative**: Check snippet trigger keywords

#### Template Generation Fails

* **Solution**: Verify project structure and dependencies
* **Alternative**: Check IDE logs for error details