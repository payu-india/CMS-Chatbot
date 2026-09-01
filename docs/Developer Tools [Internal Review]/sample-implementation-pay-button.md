---
title: Sample Implementation - Pay Button
deprecated: false
hidden: true
metadata:
  robots: index
---
<br />

### Server-side JS

```javascript
'use strict';

const http = require('http');
const fs = require('fs');
const path = require('path');

const configuredPort = Number.parseInt(process.env.PORT || '8080', 10);

const port =
  Number.isInteger(configuredPort) &&
  configuredPort > 0 &&
  configuredPort <= 65535
    ? configuredPort
    : 8080;

const publicDir = path.join(__dirname, 'public');

const contentTypes = {
  '.css': 'text/css; charset=utf-8',
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.svg': 'image/svg+xml'
};

function send(
  res,
  status,
  body,
  contentType = 'text/plain; charset=utf-8'
) {
  res.writeHead(status, {
    'Content-Type': contentType,
    'Cache-Control': 'no-store',
    'X-Content-Type-Options': 'nosniff',
    'Referrer-Policy': 'no-referrer'
  });

  res.end(body);
}

function serveFile(res, filePath) {
  fs.readFile(filePath, (error, data) => {
    if (error) {
      send(res, 404, 'Not found');
      return;
    }

    const extension = path.extname(filePath).toLowerCase();

    send(
      res,
      200,
      data,
      contentTypes[extension] || 'application/octet-stream'
    );
  });
}

const server = http.createServer((req, res) => {
  let requestUrl;

  try {
    requestUrl = new URL(
      req.url,
      `http://${req.headers.host || 'localhost'}`
    );
  } catch {
    send(res, 400, 'Bad request');
    return;
  }

  if (req.method !== 'GET' && req.method !== 'HEAD') {
    send(res, 405, 'Method not allowed');
    return;
  }

  const requestedPath = decodeURIComponent(requestUrl.pathname);

  const relativePath =
    requestedPath === '/'
      ? 'index.html'
      : requestedPath.slice(1);

  const filePath = path.resolve(publicDir, relativePath);

  // Prevent path traversal outside the public directory.
  if (!filePath.startsWith(publicDir + path.sep)) {
    send(res, 403, 'Forbidden');
    return;
  }

  serveFile(res, filePath);
});

if (require.main === module) {
  server.listen(port, '0.0.0.0', () => {
    console.log(
      `Claude Code course storefront listening on port ${port}`
    );
  });
}

module.exports = {
  server
};

```

`public/assets/app.js`

```javascript
'use strict';

const PAYMENT_LINK = 'https://u.payu.in/wJj9zLV9KyeC';

let activeDialogTrigger = null;

function getDialogParts() {
  const backdrop = document.querySelector(
    '[data-credential-dialog]'
  );

  return {
    backdrop,
    form: backdrop?.querySelector('.credential-form'),
    key: backdrop?.querySelector('#runtime-payu-key'),
    salt: backdrop?.querySelector('#runtime-payu-salt'),
    error: backdrop?.querySelector('#credential-error'),
    submit: backdrop?.querySelector(
      '[data-credential-submit]'
    )
  };
}

function clearCredentialFields() {
  const { key, salt, error } = getDialogParts();

  if (key) {
    key.value = '';
  }

  if (salt) {
    salt.value = '';
  }

  if (error) {
    error.textContent = '';
    error.hidden = true;
  }
}

function closeCredentialDialog() {
  const { backdrop } = getDialogParts();

  if (!backdrop) {
    return;
  }

  clearCredentialFields();

  backdrop.hidden = true;
  document.body.classList.remove('dialog-open');

  if (activeDialogTrigger) {
    activeDialogTrigger.focus();
  }

  activeDialogTrigger = null;
}

function openCredentialDialog(trigger) {
  const {
    backdrop,
    form,
    key,
    salt,
    submit
  } = getDialogParts();

  if (!backdrop || !form || !key || !salt || !submit) {
    return;
  }

  activeDialogTrigger = trigger;

  clearCredentialFields();

  submit.disabled = false;
  submit.innerHTML =
    'Continue to payment ' +
    '<span aria-hidden="true">↗</span>';

  backdrop.hidden = false;
  document.body.classList.add('dialog-open');

  key.focus();
}

function focusableDialogElements() {
  const { backdrop } = getDialogParts();

  return [
    ...(backdrop?.querySelectorAll(
      'button, input:not([type="hidden"])'
    ) || [])
  ].filter((element) => {
    return !element.disabled && !element.hidden;
  });
}

document.addEventListener('click', (event) => {
  const payNowButton = event.target.closest('#pay-now');

  if (payNowButton) {
    event.preventDefault();
    openCredentialDialog(payNowButton);
  }

  const closeButton = event.target.closest(
    '[data-dialog-close]'
  );

  const clickedBackdrop = event.target.matches(
    '[data-credential-dialog]'
  );

  if (closeButton || clickedBackdrop) {
    closeCredentialDialog();
  }
});

document.addEventListener('keydown', (event) => {
  const { backdrop } = getDialogParts();

  if (!backdrop || backdrop.hidden) {
    return;
  }

  if (event.key === 'Escape') {
    event.preventDefault();
    closeCredentialDialog();
    return;
  }

  if (event.key !== 'Tab') {
    return;
  }

  const focusable = focusableDialogElements();

  const first = focusable[0];
  const last = focusable[focusable.length - 1];

  if (!first || !last) {
    return;
  }

  if (event.shiftKey && document.activeElement === first) {
    event.preventDefault();
    last.focus();
  } else if (
    !event.shiftKey &&
    document.activeElement === last
  ) {
    event.preventDefault();
    first.focus();
  }
});

document.addEventListener('submit', (event) => {
  const {
    form,
    key,
    salt,
    error,
    submit
  } = getDialogParts();

  if (!form || event.target !== form) {
    return;
  }

  event.preventDefault();

  const keyValue = key.value.trim();
  const saltValue = salt.value.trim();

  // Require both values or neither value.
  if (Boolean(keyValue) !== Boolean(saltValue)) {
    error.hidden = false;
    error.textContent =
      'Enter both credentials, or leave both fields blank.';

    if (keyValue) {
      salt.focus();
    } else {
      key.focus();
    }

    return;
  }

  submit.disabled = true;
  submit.textContent = 'Opening payment link…';

  /*
   * The credentials are intentionally not:
   * - sent to the server
   * - added to the payment-link URL
   * - stored in localStorage
   * - logged
   * - sent to analytics
   */

  clearCredentialFields();

  document.body.classList.remove('dialog-open');

  window.location.href = PAYMENT_LINK;
});

```

### Button

```javascript
<button id="pay-now" type="button">
  Pay Now
</button>

<div data-credential-dialog hidden>
  <form class="credential-form">
    <input id="runtime-payu-key" name="runtimePayuKey">

    <input
      id="runtime-payu-salt"
      name="runtimePayuSalt"
      type="password"
    >

    <p id="credential-error" role="alert" hidden></p>

    <button type="button" data-dialog-close>
      Cancel
    </button>

    <button type="submit" data-credential-submit>
      Continue to payment
    </button>
  </form>
</div>

```
