---
name: Partner Authentication Response Parameters
---
| Parameters     | Description                                                                                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| access\_token  | Indicates the Security Token used to get access in Partner/Payouts API calls.                                                      |
| token\_type    | Type of authorization token                                                                                                        |
| expire\_in     | Indicates the TTL i.e., the time limit (in seconds) after which the Security Token will expire                                     |
| refresh\_token | Used to refresh the access\_token. To know more, read Refresh Token section                                                        |
| scope          | Represents the allowed scopes in generated security token. For e.g., the generated token can be used only for Payouts API requests |
| created\_at    | Indicates the Time of Creation in milliseconds                                                                                     |
| user\_uuid     | Indicates the Unique Identifier for the user.                                                                                      |
