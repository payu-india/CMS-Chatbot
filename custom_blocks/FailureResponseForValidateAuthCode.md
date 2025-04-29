---
name: Failure response for Validate Auth Code
---
The following response is displayed for the following failure scenarios:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Error Code
      </th>

      <th style={{ textAlign: "left" }}>
        Reason
      </th>

      <th style={{ textAlign: "left" }}>
        Result
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        401
      </td>

      <td style={{ textAlign: "left" }}>
        Without client secret
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
          "error": "invalid\_client",\
          "error\_description": "Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method."\
        }
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        401
      </td>

      <td style={{ textAlign: "left" }}>
        Without redirect URL
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
          "error": "invalid\_request",\
          "error\_description": "The request is missing a required parameter, includes an unsupported parameter value, or is otherwise malformed."\
        }
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        401
      </td>

      <td style={{ textAlign: "left" }}>
        With an invalid client secret
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
          "error": "invalid\_client",\
          "error\_description": "Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method."\
        }
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        401
      </td>

      <td style={{ textAlign: "left" }}>
        Without grant type
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
          "error": "invalid\_request",\
          "error\_description": "The request is missing a required parameter, includes an unsupported parameter value, or is otherwise malformed."\
        }
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        401
      </td>

      <td style={{ textAlign: "left" }}>
        With an invalid grant type
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
          "error": "invalid\_client",\
          "error\_description": "Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method."\
        }
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        401
      </td>

      <td style={{ textAlign: "left" }}>
        Without authorization code
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
          "error": "invalid\_grant",\
          "error\_description": "The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client."\
        }
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        401
      </td>

      <td style={{ textAlign: "left" }}>
        With an invalid auth code
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
          "error": "invalid\_grant",\
          "error\_description": "The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client."\
        }
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        401
      </td>

      <td style={{ textAlign: "left" }}>
        With an invalid client secret
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
          "error": "invalid\_client",\
          "error\_description": "Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method."\
        }
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        401
      </td>

      <td style={{ textAlign: "left" }}>
        With an invalid redirect URL
      </td>

      <td style={{ textAlign: "left" }}>
        \{\
          "error": "invalid\_grant",\
          "error\_description": "The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client."\
        }
      </td>
    </tr>
  </tbody>
</Table>
