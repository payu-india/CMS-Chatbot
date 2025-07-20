---
title: IntelliJ IDEA Plugin
deprecated: false
hidden: false
metadata:
  robots: index
---
## Installation Steps

## Method 1: JetBrains Marketplace (Recommended)

1. **Open IntelliJ IDEA**

2. **Navigate to Plugins**
   * Go to `File` → `Settings` (Windows/Linux) or `IntelliJ IDEA` → `Preferences` (Mac)
   * Select `Plugins` from the left sidebar

3. **Search and Install**
   * Click on `Marketplace` tab
   * Search for "PayU Payments Code Snippets"
   * Click `Install` button
   * Restart IntelliJ IDEA when prompted

#### Method 2: Direct Installation

1. **Download Plugin**
   * Visit: [https://plugins.jetbrains.com/plugin/27588-payu-payments-code-snippets](https://plugins.jetbrains.com/plugin/27588-payu-payments-code-snippets)
   * Click "Get" or "Install to IntelliJ IDEA"

2. **Manual Installation** (if needed)
   * Download the plugin file (.jar)
   * Go to `File` → `Settings` → `Plugins`
   * Click gear icon ⚙️ → `Install Plugin from Disk`
   * Select the downloaded file

## Using the IntelliJ IDEA Plugin

### 1. Create New Project

1. **Start New Project**
   * `File` → `New` → `Project`
   * Choose your preferred project type (Java, Spring Boot, etc.)

2. **Configure Project Settings**
   * Set project name and location
   * Configure SDK and dependencies

### 2) Access PayU Templates

1. **File Templates**
   * Right-click on project folder
   * Select `New` → look for PayU templates
   * Choose appropriate template

2. **Live Templates**
   * Start typing in your code editor
   * Type `payu` and press `Tab` to see available templates

### 3) Code Generation

1. **Payment Integration Templates**
   * `payu-payment-request`: Generates payment request code
   * `payu-payment-response`: Generates response handling code
   * `payu-webhook`: Generates webhook endpoint code

2. **Configuration Templates**

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

#### 4. **Environment Configuration**

1. **Application Properties**

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

***

<br />

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

### Getting Help

1. **Plugin Documentation**
   * VS Code: Check extension details in marketplace
   * IntelliJ: Visit plugin page on JetBrains marketplace

2. **PayU Developer Resources**
   * API Documentation: [https://docs.payu.in/](https://docs.payu.in/)
   * Support: Contact PayU developer support

***

## 🎯 Next Steps

After installing and configuring the plugins:

1. **Explore Generated Code**: Review the boilerplate to understand the structure
2. **Customize Integration**: Modify code according to your business requirements
3. **Test Integration**: Use test environment for initial testing
4. **Implement Security**: Add proper validation and security measures
5. **Deploy**: Move to production environment when ready

***

## 📚 Additional Resources

* **PayU API Documentation**: [https://docs.payu.in/](https://docs.payu.in/)
* **VS Code Plugin**: [https://marketplace.visualstudio.com/items?itemName=PayuPayments.Payu-Payments](https://marketplace.visualstudio.com/items?itemName=PayuPayments.Payu-Payments)
* **IntelliJ Plugin**: [https://plugins.jetbrains.com/plugin/27588-payu-payments-code-snippets](https://plugins.jetbrains.com/plugin/27588-payu-payments-code-snippets)
* **PayU Developer Portal**: [https://developer.payu.in/](https://developer.payu.in/)

***

*This guide provides a comprehensive overview of installing and using PayU payment plugins. For specific integration requirements, refer to the PayU API documentation and plugin-specific help resources.*