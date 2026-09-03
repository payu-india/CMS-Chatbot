---
title: Initialize with Credentials
excerpt: 'PayU Go SDK guide: Initialize with Credentials'
deprecated: false
hidden: false
metadata:
  title: 'Initialize with Credentials | PayU Go SDK'
  description: 'PayU Go SDK guide: Initialize with Credentials'
  keywords:
    - payu go sdk
    - initialize with credentials
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Initialize the PayU client once at application startup.

## Pattern: Initialize Once at Startup

```go
package main

import (
	"log"
	"os"

	payu "github.com/payu-india/web-sdk-go"
)

var payuClient *payu.Client

func init() {
	var err error

	key := os.Getenv("PAYU_MERCHANT_KEY")
	salt := os.Getenv("PAYU_MERCHANT_SALT")
	env := os.Getenv("PAYU_ENV")

	if env == "" {
		env = "test"
	}

	payuClient, err = payu.NewClient(key, salt, env)
	if err != nil {
		log.Fatalf("PayU init failed: %v", err)
	}

	log.Printf("✅ PayU initialized (%s)", env)
}
```

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Configure Test Vs Production](doc:configure-test-vs-production)
