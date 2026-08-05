---
title: Step 00 — Authentication
excerpt: >-
  # Step 00 — Authentication (OAuth Token)


  Before calling any onboarding API, obtain a bearer token from PayU's OAuth
  endpoint.


  ## Environments


  | Environment | URL |

  |-------------|-----|

  | Test | `https://test-accounts.payu.in/oauth/token` |

  | Production | `https://accounts.payu.in/oauth/token` |


  ## Token Lifecycle


  - Tokens expire after `expires_in` seconds (typically 7200 = 2 hours)

  - Implement refresh logic — do not request a new token per API call

  - Store tokens server-side only


  ## Scopes


  | Scope | Purpose |

  |-------|---------|

  | `refer_merchant` | Create and manage merchant accounts (Steps 01-13) |

  | `client_manage_kyc_details` | KYC documents and verification (Steps 03, 06,
  09, 11, 14, 15) |

  | `client_manage_agreement` | Agreement management (Step 16) |
hidden: false
---