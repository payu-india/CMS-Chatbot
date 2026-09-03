---
title: Initialize SDK Client
excerpt: 'PayU Go SDK guide: Initialize SDK Client'
deprecated: false
hidden: false
metadata:
  title: 'Initialize SDK Client | PayU Go SDK'
  description: 'PayU Go SDK guide: Initialize SDK Client'
  keywords:
    - payu go sdk
    - initialize sdk client
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Initialize the PayU client with merchant credentials.

## Step-by-Step Guide

```go
package main

import (
	"log"
	"os"

	payu "github.com/payu-india/web-sdk-go"
)

func main() {
	key := os.Getenv("PAYU_MERCHANT_KEY")
	salt := os.Getenv("PAYU_MERCHANT_SALT")
	env := os.Getenv("PAYU_ENV")

	if key == "" || salt == "" {
		log.Fatal("PAYU credentials not set")
	}

	if env == "" {
		env = "test"
	}

	client, err := payu.NewClient(key, salt, env)
	if err != nil {
		log.Fatalf("Failed to initialize: %v", err)
	}

	log.Println("✅ PayU client ready")
}
```

**Run:** `go run main.go`  
**Expected:** `✅ PayU client ready`

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Verify Installation](doc:verify-installation)
