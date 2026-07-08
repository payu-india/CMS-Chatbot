---
title: Generate Security Hash
excerpt: 'PayU Go SDK guide: Generate Security Hash'
deprecated: false
hidden: false
metadata:
  title: 'Generate Security Hash | PayU Go SDK'
  description: 'PayU Go SDK guide: Generate Security Hash'
  keywords:
    - payu go sdk
    - generate security hash
    - golang payment integration
  robots: index
next:
  description: ''
---

## Overview

Generate the security hash for payment requests. Hash generation is security-critical.

⚠️ **CRITICAL:** Verify field order against [Hash Field Order](doc:hash-field-order) and [Generate Hash](doc:hashing-request-and-response).

```go
import (
	"crypto/sha512"
	"fmt"
)

func generateHash(request *PaymentRequest, salt string) (string, error) {
	hashInput := fmt.Sprintf("%s|%s|%s|%s|%s|%s|%s|%s",
		request.Key,
		request.Txnid,
		request.Amount,
		request.ProductInfo,
		request.FirstName,
		request.Email,
		"", // udf1
		salt,
	)
	hash := sha512.Sum512([]byte(hashInput))
	return fmt.Sprintf("%x", hash), nil
}
```

## Must Verify

- [ ] Field order matches PayU spec
- [ ] SHA512 algorithm (not SHA256 or MD5)
- [ ] Works with test credentials

## Related Pages

- [Go SDK Overview](doc:go-sdk)
- [Troubleshooting](doc:common-integration-issues)

## Next Steps

- [Redirect To Checkout](doc:redirect-to-checkout)
