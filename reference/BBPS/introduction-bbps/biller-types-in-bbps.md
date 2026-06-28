---
title: Biller Types in BBPS
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The following table outlines the various Biller integration scenarios in BBPS. These fields are passed on as Biller MDM Response parameters. Here, **T**=true and **F**=false.

<Callout icon="📘" theme="info">
  ### Note:

  The following combination is only valid if the agent is using the **Validation** API for validating the payment.
</Callout>

| **S.No** | **Type**  | **Accepts Ad-hoc** | **Fetch Requirement** | **Support**Validation\*\* | **Support Plan MOM** | **QuickPay**value in Pay Request\*\* | **Transaction**                                                                                                       |
| -------- | --------- | ------------------ | --------------------- | ------------------------- | -------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| 1        | ONLINE    | T                  | OPTIONAL              |                           |                      | • Yes                                | • Ad-hoc Payment can be done (for any amount).                                                                        |
|          |           |                    | OPTIONAL              |                           |                      | • No                                 | • Payment against fetch can also be done for any amount.                                                              |
| 2        | ONLINE    | T                  | NOT\_SUPPORTED        | OPTIONAL                  | Yes (T/F)            | • Yes                                | • Ad hoc Payment can be done (for any amount).                                                                        |
|          |           |                    | NOT\_SUPPORTED        | OPTIONAL                  | Yes (T/F)            | • No                                 | • Payment against validation can also be done for any amount.                                                         |
| 3        | ONLINE    | T                  | NOT\_SUPPORTED        | MANDATORY                 | Yes (T/F)            | • No                                 | • Payment against validation can also be done for any amount.                                                         |
| 4        | ONLINE    | T                  | NOT\_SUPPORTED        | NOT\_SUPPORTED            | Yes (T/F)            | • Yes                                | • Ad- hoc Payment can be done (for any amount).                                                                       |
| 5        | ONLINE    | T                  | MANDATORY             |                           |                      | • No                                 | • Ad-hoc Payment cannot be done.Payment against fetch can be done for any amount.                                     |
| 6        | ONLINE    | F                  | MANDATORY             |                           |                      | • No                                 | • Ad-hoc Payment cannot be done. EXACT, EXACT\_UP, EXACT\_DOWN can be paid against fetched bill as per configuration. |
| 7        | OFFLINE A | T                  | OPTIONAL              |                           |                      | • Yes                                | • Ad-hoc Payment can be done (for any amount).                                                                        |
|          |           |                    | OPTIONAL              |                           |                      | • No                                 | • Payment against fetch can also be done for any amount.                                                              |
| 8        | OFFLINE A | T                  | NOT\_SUPPORTED        | OPTIONAL                  | Yes (T/F)            | • Yes                                | • Ad-hoc Payment can be done (for any amount).                                                                        |
|          |           |                    | NOT\_SUPPORTED        | OPTIONAL                  | Yes (T/F)            | • No                                 | • Payment against validation can also be done for any amount.                                                         |
| 9        | OFFUNE A  | T                  | NOT\_SUPPORTED        | MANDATORY                 | Yes (T/F)            | • No                                 | • Payment against validation can also be done for any amount.                                                         |
| 10       | OFFUNE A  | T                  | NOT\_SUPPORTED        | NOT\_SUPPORTED            | Yes (T/F)            | • Yes                                | • Ad-hoc Payment can be done (for any amount).                                                                        |
| 11       | OFFUNE A  | T                  | MANDATORY             |                           |                      | • No                                 | • Ad-hoc Payment cannot be done.Payment against fetch can be done for any amount.                                     |
| 12       | OFFUNE A  | F                  | MANDATORY             |                           |                      | • No                                 | • Ad-hoc Payment cannot be done. EXACT, EXACT\_UP, EXACT\_DOWN can be paid against fetched bill as per configuration. |
| 13       | OFFUNE B  | T                  | NOT\_SUPPORTED        | OPTIONAL                  | Yes (T/F)            | • Yes                                | • Ad-hoc Payment can be done (for any amount).                                                                        |
|          |           |                    | NOT\_SUPPORTED        | OPTIONAL                  | Yes (T/F)            | • No                                 | • Payment against validation can also be done for any amount.                                                         |
| 14       | OFFUNE B  | T                  | NOT\_SUPPORTED        | MANDATORY                 | Yes (T/F)            | • No                                 | • Payment against validation can also be done for any amount.                                                         |
| 15       | OFFUNE B  | T                  | NOT\_SUPPORTED        | NOT\_SUPPORTED            | Yes (T/F)            | • Yes                                | • Ad-hoc Payment can be done (for any amount).                                                                        |

<br />
