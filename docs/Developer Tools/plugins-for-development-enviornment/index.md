---
title: Plugins for Development Enviornment
deprecated: false
hidden: false
metadata:
  robots: index
---
PayU offers plugins for Visual Studio Code and IntelliJ Idea development environments. This part of the documentation includes the following sections, which includes plugin installation and troublshooting procedures:

* [Visual Studio Code Plugin](https://docs.payu.in/v2/docs/visual-studio-code-plugin)
* [IntelliJ IDEA Plugin](https://docs.payu.in/v2/docs/intellij-idea-plugin)

## Step 1: Initial Setup

1. Clone or create your project
2. Install the appropriate plugin
3. Configure your IDE settings

## Step 2: Development Process

1. **Generate Base Code**
   * Use plugin commands to create boilerplate
   * Configure environment variables
   * Set up project dependencies

2. **Customize Integration**
   * Modify generated code as needed
   * Add business logic
   * Implement error handling

3. **Testing**
   * Use test environment endpoint: `https://apitest.payu.in/v2/payments`
   * Test with sample credentials
   * Validate payment flows

## Step 3: Deployment Preparation

1. Switch to production endpoint: `https://api.payu.in/v2/payments`
2. Update with production credentials
3. Perform final testing

***