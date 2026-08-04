---
title: Step 06 — Upload Bank Proof (Conditional)
excerpt: >-
  # Step 06 — Upload Bank Proof (Conditional)


  Upload bank account proof document if auto-verification from Step 05 failed.


  ## Prerequisite Steps

  - Step 05 (Bank Details) — bank auto-verification must have failed

  - Check via GetMerchant → `bank_verification_status` = `failed` or `pending`


  ## Entity Applicability

  **All entities** — but only if bank auto-verification fails.


  ## Accepted Bank Proof Documents


  | Document Type | UUID |

  |---------------|------|

  | Cancelled Cheque | `ca0a-9047-28d705a1-7e97-b530fbec4c41` |

  | Bank Verification Letter | `f912-b658-610ce46f-796b-14a515e41ad7` |

  | Bank Statement | `11eb-d01a-8322997a-adc5-0242a53cdb42` |

  | Passbook | `11eb-d01a-456b15f8-adc5-0242a53cdb42` |


  Document Category: **Bank Account Proof** (UUID:
  `11e8-748f-297c6048-9081-020aca9875be`)
hidden: false
---