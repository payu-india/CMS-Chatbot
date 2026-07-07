---
title: Proof Of Concept
excerpt: This page is to try custom components in Readme (DO NOT PUBLISH)
deprecated: false
hidden: true
metadata:
  robots: index
---
<br />

Accelerate your integration workflow with our net banking Postman collection for PayU Hosted Checkout. Click the Download Postman Collection button below to download and get started.

<HTMLBlock>{`
                <style>
                .tooltip-btn {
                    position: relative;
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold; /* Added this line */
                }
                .tooltip-btn:hover::after {
                    content: attr(data-tooltip);
                    position: absolute;
                    bottom: 125%;
                    left: 50%;
                    transform: translateX(-50%);
                    background-color: #333;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 4px;
                    white-space: nowrap;
                    font-size: 12px;
                    z-index: 1;
                }
                </style>

                <button onclick="window.open('https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/overview', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Click to download the Postman collection and explore APIs.">
                    Access Postman Collection
                </button>
`}</HTMLBlock>

<Tabs>
  <Tab title="Method">
    POST
  </Tab>

  <Tab title="Endpoint">
    /v2/payments
  </Tab>
</Tabs>

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /v2/payments
  </Card>
</Cards>

|    |    |    |
| :- | :- | :- |
|    |    |    |
|    |    |    |

<Accordion title="My Accordion Title">
  ```javascript
  var merchant_key = 'smsplus';
  var merchant_secret = 'izF09TlpX4ZOwmf9MvXijwYsBPUmxYHD';
  // date
  var date = new Date();
  date = date.toUTCString();

  // authorization
  var authorization = getAuthHeader(date);

  function getAuthHeader(date) {
      var AUTH_TYPE = 'sha512';
      var data = isEmpty(request['data']) ? "" : request['data'];
      var hash_string = data + '|' + date + '|' + merchant_secret;
      var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
      return `hmac username="${merchant_key}", algorithm="${AUTH_TYPE}", headers="date", signature="${hash}"`;
  }
  ```
</Accordion>

<SearchableTable
  headers={['Bank', 'Type', 'Status']}
  rows={[
    ['HDFC Bank', 'Netbanking / Cards', 'Active'],
    ['ICICI Bank', 'Netbanking / Cards', 'Active'],
    ['State Bank of India', 'Netbanking', 'Active'],
    ['Axis Bank', 'Cards', 'Active'],
  ]}
  placeholder="Search"
/>

<Accordion title="My Accordion Title" icon="fa-info-circle">
  <SearchableTable
    headers={['Bank', 'Type', 'Status']}
    rows={[
    ['HDFC Bank', 'Netbanking / Cards', 'Active'],
    ['ICICI Bank', 'Netbanking / Cards', 'Active'],
    ['State Bank of India', 'Netbanking', 'Active'],
    ['Axis Bank', 'Cards', 'Active'],
  ]}
    placeholder="Search"
  />
</Accordion>

<AccordionOpen title="Request Parameters" icon="fa-info-circle">
  <p>This accordion is open by default. The title is rendered as a heading. You can put any content here: tables, code blocks, or more MDX. Users can collapse or expand by clicking the header.</p>
</AccordionOpen>

<NewBadge title="Getting Started" />

<br />

<NewBadge title="API Reference" headingLevel={2} />

<br />

<Callout icon="📘" theme="info">
  ###

  <br />

  Accelerate your integration workflow with 

  Lorem Ispum
</Callout>

<br />

<HTMLBlock>{`
			<p>Use this tool to generate the forward hash by providing the mandatory parameter values (key, txnid, amount, productinfo, firstname, email, salt. udf1–udf5 are optional).</p><br/>
								<style>
                .tooltip-btn {
                    position: relative;
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold; /* Added this line */
                }
                .tooltip-btn:hover::after {
                    content: attr(data-tooltip);
                    position: absolute;
                    bottom: 125%;
                    left: 50%;
                    transform: translateX(-50%);
                    background-color: #333;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 4px;
                    white-space: nowrap;
                    font-size: 12px;
                    z-index: 1;
                }
                </style>

                <button onclick="window.open('https://timely-dolphin-49e294.netlify.app/', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Click to generate hash.">
                    Generate Forward Hash
                </button>
`}</HTMLBlock>

[Download CSV template](https://github.com/palgunams21/payu-docs-assets/releases/download/AuthN-AuthZ-errors/AuthN_error_list.csv)

<HTMLBlock>{`
<button
  type="button"
  id="payu-csv-download"
  style="padding:10px 18px;background:#2563eb;color:#fff;font:600 14px system-ui,sans-serif;border:none;border-radius:6px;cursor:pointer;"
>
  Download CSV
</button>
<script>
(function () {
  var FILE_URL = 'https://github.com/palgunams21/payu-docs-assets/releases/download/AuthN-AuthZ-errors/AuthN_error_list.csv';
  var FILE_NAME = 'AuthN_error_list.csv';
  var btn = document.getElementById('payu-csv-download');
  if (!btn) return;
  btn.addEventListener('click', function () {
    fetch(FILE_URL)
      .then(function (res) {
        if (!res.ok) throw new Error('fetch failed');
        return res.blob();
      })
      .then(function (blob) {
        var url = URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = FILE_NAME;
        document.body.appendChild(a);
        a.click();
        a.remove();
        URL.revokeObjectURL(url);
      })
      .catch(function () {
        window.location.href = FILE_URL;
      });
  });
})();
</script>
`}</HTMLBlock>

<br />

<HoverCardGrid
  columns={3}
  items={[
    {
      title: 'Guides',
      href: '/docs/guides',
      image: 'https://your-cdn.com/card-guides.png',
      imageAlt: 'Illustration of documentation guides',
      text: 'Step-by-step integration guides.',
    },
    {
      title: 'API',
      href: '/reference',
      icon: 'fa-code',
      text: 'No image — icon only.',
    },
  ]}
/>

<PayUErrorExplorer />

<AdvancedTable
  data={[
    {
      'code': 'APIKEY_EMPTY',
      'status': 'Unauthorized',
      'description': 'An API key was not supplied.',
      'message': 'You must pass in an API key.'
    },
    {
      'code': 'APIKEY_MISMATCH',
      'status': 'Forbidden',
      'description': "The API key doesn't match the project.",
      'message': "The API key doesn't match the project."
    },
    {
      'code': 'APIKEY_NOTFOUND',
      'status': 'Unauthorized',
      'description': "The API key couldn't be located.",
      'message': "We couldn't find your API key."
    },
    {
      'code': 'API_ACCESS_REVOKED',
      'status': 'Forbidden',
      'description': 'Your ReadMe API access has been revoked.',
      'message': 'Your ReadMe API access has been revoked.'
    },
    {
      'code': 'API_ACCESS_UNAVAILABLE',
      'status': 'Forbidden',
      'description': 'Your ReadMe project does not have access to this API. Please reach out to support@readme.io.',
      'message': 'Your ReadMe project does not have access to this API. Please reach out to support@readme.io.'
    },
    {
      'code': 'APPLY_INVALID_EMAIL',
      'status': 'Bad Request',
      'description': 'You need to provide a valid email.',
      'message': 'You need to provide a valid email.'
    },
    {
      'code': 'APPLY_INVALID_JOB',
      'status': 'Bad Request',
      'description': 'You need to provide a job.',
      'message': 'You need to provide a job.'
    },
    {
      'code': 'APPLY_INVALID_NAME',
      'status': 'Bad Request',
      'description': 'You need to provide a name.',
      'message': 'You need to provide a name.'
    },
    {
      'code': 'CATEGORY_INVALID',
      'status': 'Bad Request',
      'description': "The category couldn't be saved.",
      'message': "We couldn't save this category ({error})."
    },
    {
      'code': 'CATEGORY_NOTFOUND',
      'status': 'Not Found',
      'description': "The category couldn't be found.",
      'message': "The category with the slug '{category}' couldn't be found."
    },
    {
      'code': 'CHANGELOG_INVALID',
      'status': 'Bad Request',
      'description': "The changelog couldn't be saved.",
      'message': "We couldn't save this changelog ({error})."
    },
    {
      'code': 'CHANGELOG_NOTFOUND',
      'status': 'Not Found',
      'description': "The changelog couldn't be found.",
      'message': "The changelog with the slug '{slug}' couldn't be found."
    }
  ]}
/>

<br />
