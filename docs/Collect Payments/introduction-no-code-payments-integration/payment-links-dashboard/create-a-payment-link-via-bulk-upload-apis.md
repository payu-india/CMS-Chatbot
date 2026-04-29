---
title: Create Payment Links via Bulk Upload - APIs
excerpt: Know how to create payment links via bulk upload option using APIs.
deprecated: false
hidden: true
metadata:
  robots: index
---
The bulk upload option using APIs lets you create many payment links by uploading a `.csv` file.

## Integration Steps

Below are the integration steps:

<Cards columns={3}>
  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-key" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Fetch the Access Token</h4>

      <p style={{ margin: 0 }}>
        Fetch the Bearer Token.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-file-upload" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Bulk Upload</h4>

      <p style={{ margin: 0 }}>
        Upload the Bulk File.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-link" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Get Payment Links</h4>

      <p style={{ margin: 0 }}>
        Get the Created Payment Links Using the Batch ID.
      </p>
    </div>
  </Card>
</Cards>

### Step 1. Get the Access Token

The first step is to obtain an access token using the following API:

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /oauth/token
  </Card>
</Cards>

<Accordion title="Environment Details" icon="fa-cogs">
  |                |                                                              |
  | :------------- | :----------------------------------------------------------- |
  | **Test**       | [https://uat-accounts.payu.in](https://uat-accounts.payu.in) |
  | **Production** | [https://accounts.payu.in](https://accounts.payu.in)         |
</Accordion>

<br />
