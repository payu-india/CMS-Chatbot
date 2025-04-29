---
name: Failure response for Validate Auth Code
---
The following response is displayed for the following failure scenarios:

[block:parameters]
{
  "data": {
    "h-0": "Error Code",
    "h-1": "Reason",
    "h-2": "Result",
    "0-0": "401",
    "0-1": "Without client secret",
    "0-2": "{  \n  \"error\": \"invalid_client\",  \n  \"error_description\": \"Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method.\"  \n}",
    "1-0": "401",
    "1-1": "Without redirect URL",
    "1-2": "{  \n  \"error\": \"invalid_request\",  \n  \"error_description\": \"The request is missing a required parameter, includes an unsupported parameter value, or is otherwise malformed.\"  \n}",
    "2-0": "401",
    "2-1": "With an invalid client secret",
    "2-2": "{  \n  \"error\": \"invalid_client\",  \n  \"error_description\": \"Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method.\"  \n}",
    "3-0": "401",
    "3-1": "Without grant type",
    "3-2": "{  \n  \"error\": \"invalid_request\",  \n  \"error_description\": \"The request is missing a required parameter, includes an unsupported parameter value, or is otherwise malformed.\"  \n}",
    "4-0": "401",
    "4-1": "With an invalid grant type",
    "4-2": "{  \n  \"error\": \"invalid_client\",  \n  \"error_description\": \"Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method.\"  \n}",
    "5-0": "401",
    "5-1": "Without authorization code",
    "5-2": "{  \n  \"error\": \"invalid_grant\",  \n  \"error_description\": \"The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client.\"  \n}",
    "6-0": "401",
    "6-1": "With an invalid auth code",
    "6-2": "{  \n  \"error\": \"invalid_grant\",  \n  \"error_description\": \"The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client.\"  \n}",
    "7-0": "401",
    "7-1": "With an invalid client secret",
    "7-2": "{  \n  \"error\": \"invalid_client\",  \n  \"error_description\": \"Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method.\"  \n}",
    "8-0": "401",
    "8-1": "With an invalid redirect URL",
    "8-2": "{  \n  \"error\": \"invalid_grant\",  \n  \"error_description\": \"The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client.\"  \n}"
  },
  "cols": 3,
  "rows": 9,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]