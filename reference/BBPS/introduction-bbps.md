---
title: Introduction - BBPS
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
This part of the API reference includes the API reference pages for BBPS Agent API Integration and Recharge API Integration.

## About BBPS Environment

|   |                  |                                                               |                                                     |
| - | ---------------- | ------------------------------------------------------------- | --------------------------------------------------- |
|   | **Environments** | **Auth Host Name **                                           | **NBC Host Name **                                  |
| 1 | Test             | [https://uat-accounts.payu.in](https://uat-accounts.payu.in/) | [https://bbps-sb.payu.in](https://bbps-sb.payu.in/) |
| 2 | Production       | Contact your Key Account Manager                              | Contact your Key Account Manager                    |

## Reference ID Format for all APIs

To be compliant with the global standards where all the IDs will contain the date and time, only the format of the reference ID will be changed, retaining the length unchanged. The new format of “Reference ID”  will be starting with 27 random characters (as existing), followed by 8 characters of the Julian date and time as a suffix in the ‘YDDDhhmm’ format. The whole length of both the IDs will continue to be 35 digits as is currently and the data type shall remain alphanumeric.

**Format**: \<random characters of length 27 nos.> \<YDDDhhmm>, where Y will be the last digit of the current year, DDD the nth day of the current year, hh will be in the 24-hour format followed by mm in minutes.

**Example**: **ABCDE12345ABCDE12345ABCDE1A01192345**.