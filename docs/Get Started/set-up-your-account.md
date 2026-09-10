---
title: Set Up Your Account
excerpt: >-
  Create your PayU merchant account, complete KYC, and get your integration
  credentials.
deprecated: false
hidden: true
metadata:
  title: Set Up Your PayU Account
  description: >-
    Step-by-step guide to creating a PayU merchant account, completing KYC
    verification, and accessing your Merchant Key and Salt for test and
    production environments.
  keywords:
    - create payu account
    - payu merchant registration
    - payu kyc activation
    - payu merchant key salt
    - payu test credentials
    - payu production key
    - payu onboarding
    - activate payu account
  robots: index
---
{/*
=============================================================================
CONTENT PROVENANCE — for SME / editorial review
=============================================================================
SOURCE       — drawn from an existing repo file (path shown).
               Lightly rewritten for tone and clarity; facts unchanged.
NEW CONTENT  — written fresh; no equivalent exists in the repo.
               Must be validated by a PayU SME before publishing.
=============================================================================
*/}

{/* NEW CONTENT — this intro paragraph is new. The existing pages jump
     straight into steps without a brief orientation sentence.
     Needs SME review. */}

Before you can integrate with PayU, you need these three:&#x20;

- A merchant account
- A completed KYC
- Merchant secrets
- API credentials.

{/* NEW CONTENT — the sequential step overview below is new. It helps
     users understand the full setup journey before they start.
     Needs SME review. */}

<Callout icon="📘" theme="info">
  ### **How long does this take?**

  - **Create an account**: 5 minutes
  - **Complete KYC**: 15–30 minutes (Keep your business documents ready)
  - **Test credentials**: Available immediately after account creation
  - **Production credentials**: Available after PayU verifies your website (up to 2 business days)
</Callout>

***

## Step 1: Create a PayU Account

{/* SOURCE — content sourced from:
     docs/getting started/register-with-payu/register-for-a-merchant-account-on-dashboard.md
     Rewritten for brevity and consistent tone. Steps, field names, and
     notes are faithful to the original. */}

To create a PayU account:

1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin">PayU dashboard</Anchor> in your browser.

2. Provide the following details on the **Create your PayU account** page:

   <Table>
     <thead>
       <tr>
         <th>
           Field
         </th>

         <th>
           Details
         </th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>
           **Email**
         </td>

         <td>
           Your email address. This will be your login username and receives PayU communications
         </td>
       </tr>

       <tr>
         <td>
           **Password**
         </td>

         <td>
           Your password should contain:

           - At least 8 characters,&#x20;
           - At least 1 uppercase&#x20;
           - At least 1 lowercase
           - At least 1 number
           - At least 1 special character
         </td>
       </tr>

       <tr>
         <td>
           **Mobile**
         </td>

         <td>
           Your 10-digit mobile number
         </td>
       </tr>

       <tr>
         <td>
           **Do you want to collect payments for your website? (optional)**
         </td>

         <td>
           Select **Yes** and enter your website URL if applicable
         </td>
       </tr>
     </tbody>
   </Table>

3. Click **Send OTP & Create Account**. An OTP is sent to your mobile number.

4. Enter the OTP and click **VERIFY OTP&#x20;**&#x6F;n the **OTP Verification&#x20;**&#x70;age.

You can continue to complete your KYC or choose to complete it later. Click **Go to Dashboard&#x20;**&#x74;o access your test credentials.&#x20;

<Callout icon="far fa-diagram-next" theme="success">
  ### **What Happens Next:**

  - Your **Test Key and Salt** are available immediately. You can start building and testing right away.
  - Your **Production Key and Salt** become available after PayU verifies your website. This takes up to 2 business days.
  - You must complete KYC (Step 2 below) before you can accept real payments.
</Callout>

***

## Step 2: Complete KYC and Activate Your Account

{/* SOURCE — content sourced from:
     docs/getting started/register-with-payu/complete-your-kyc.md
     Steps, section names, and UI labels are faithful to the original.
     Rewritten for brevity; verbose sub-sections condensed where the
     original had redundant prose. */}

PayU requires all merchants to complete KYC (Know Your Customer) to comply with regulatory guidelines. Your account cannot accept live payments until you complete the KYC.

**Before you start**, keep these documents ready:

- **Business PAN Card Number:&#x20;**&#x42;usines&#x73;**&#x20;**&#x50;AN card details to verify your business identity.
- **Proof of identity** (Aadhaar card, passport, or PAN card)
- **Proof of address** (Aadhaar card, passport, or utility bill)
- **Business proof** (GST registration certificate or business license)

For the full list of required documents based on your business type, refer to the [Documents checklist](#documents-checklist) below.

To complete your KYC:

<Accordion title="1. Resume Onboarding" icon="far fa-chart-pie-simple-circle-currency">
  Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin">PayU dashboard</Anchor> and click **Resume Onboarding** at the top of the page (or under **Onboarding Progress**)
</Accordion>

<Accordion title="2. Business PAN Card Number" icon="far fa-id-card">
  Enter your business PAN, verify the details and click **Confirm & Proceed**.

  ![](https://files.readme.io/aa16d8fba3f835de17fb687aba2ee0b1b67b369e7c810e642bdbb07303d9cb10-image.png)
</Accordion>

<br />

<Accordion title="3. Please confirm your Business entity" icon="far fa-buildings">
  Select any of the following business entity type and click **Confirm & Proceed:**

  - **Individual**

  - **Sole Proprietorship**
</Accordion>

<Accordion title="Provide phone number to complete CKYC" icon="far fa-phone">
  1. Verify the mobile number associated with your business PAN and click **Proceed with CKYC.**


  <Image src="https://files.readme.io/6da5617a549d6e068c976f393385c639e74ecb3bea90e18c7f93241b8c189497-image.png" align="center" caption="Verify or Update Mobile Number" border={true} />


  <Callout icon="📘" theme="info">
    ### **Note:**

    - You can update the mobile number in this screen.
    - You can choose to skip CKYC by clicking **Skip CKYC.**
  </Callout>

  2. Verify your mobile number with the OTP to proceed.
</Accordion>

<Accordion title="4. What category does your business fall under?" icon="far fa-crate-empty">
  Search and select your business category from the search drop-down list and click **Confirm & Proceed.**


  <Image src="https://files.readme.io/5d603e11dd7d574234d96483157b20aae9da6fb3c635ecabdb0fae802cbc95c0-image.png" align="center" caption="Select your Business Category" border={true} />

</Accordion>

<Accordion title="5. Share your business details" icon="far fa-business-time">
  Provide the following details and click **Confirm & Proceed.**

  - **Expected Sales per month**
  - **Do you have a GSTIN number?:&#x20;**&#x55;se the radio button to select your option.
  - **GSTIN&#x20;**(if applicable)

  ![](https://files.readme.io/1f448bf4c6099d0e879ac7f94337ad3594f8c7f5d003db253e156dece1609456-Screenshot_2026-09-08_at_6.23.41_PM.png)
</Accordion>

<Accordion title="6. Connect Mobile App or Website" icon="far fa-page">
  How do you want to collect payments? Select any of the following option, provide the required details and click **Confirm & Proceed**:

  - **I have a website:&#x20;**&#x73;elect this option if you have a website to collect payments and provide the following details:
    - **Website URL**
    - **Android app:&#x20;**&#x59;our android application URL if available.
    - **iOS app:&#x20;**&#x59;our iOS application URL if available.
    ![](https://files.readme.io/04c04050a2e7049bd03e0598b57b071d936a320ab60ae897f701452fa2e499ee-Screenshot_2026-09-09_at_12.54.40_PM.png)


  - **I don't have a website:&#x20;**&#x53;elect this option if you do not have a website to collect payments and provide any of the following details:
    - **Instagram Business Profile**
    - **Whatsapp store**

</Accordion>

1. **How you accept payments** — Select one of the following:
   - **On my website/app** — enter your website URL, Android app URL, or iOS app URL.
   - **I don't have a website/app** — you can use Payment Links, Invoices, or Payment Buttons from the Dashboard.

2. **Signing authority details** — Verify the name, PAN, and email of your signing authority. Update the email if needed, then click **Proceed to KYC**.

3. **KYC documents** — Choose one of the following methods:
   - **Fetch from cKYC** — enter your date of birth / incorporation date and authorise PayU to fetch documents automatically.
   - **Fetch from Aadhaar** — accept Aadhaar terms and click Submit.
   - **Upload manually** — verify your address details and upload PAN card, address proof, and any other requested documents.

4. Click **Submit Documents**.

<Callout icon="📘" theme="info">
  ### **Note:**

  If you cannot complete KYC, contact your PayU Key Account Manager or visit [PayU Support](https://help.payu.in/knowledge-center).
</Callout>

***

### Documents checklist

{/* SOURCE — content sourced from:
     docs/getting started/register-with-payu/documents-checklist-for-account-activation.md
     The full per-entity-type document requirements are preserved below
     as collapsible accordions, matching the original structure.
     Table content for industry-specific and compliance documents is
     sourced verbatim. */}

Expand the section that matches your business entity type.

<Accordion title="Individual">
  1. PAN Card of the Signing Authority
  2. Address Proof of the Signing Authority
  3. Bank Account Proof
</Accordion>

<Accordion title="Sole Proprietorship">
  1. Bank Account Proof
  2. Any two government proofs (GSTIN, MSME, IEC, FSSAI, ITR, Shop establishment, Trade licence, Tax document, Utility bill)
  3. Address Proof of the Signing Authority
  4. PAN Card of Signing Authority
</Accordion>

<Accordion title="Partnership">
  1. Bank Account Proof
  2. PAN Card of Signing Authority
  3. Address Proof of Signing Authority
  4. Partnership Deed (complete, signed by all partners, on stamp paper, including profit-sharing ratios)
  5. Government Issued Certificate
  6. PAN Card of Partnership
  7. Authorization Letter / Board Resolution Letter
  8. Latest Shareholding Pattern
</Accordion>

<Accordion title="LLP">
  1. PAN Card of Signing Authority
  2. Address Proof of Signing Authority
  3. Bank Account Proof
  4. Certificate of Incorporation
  5. LLP Deed (notarized or verified by registrar, including profit-sharing ratios)
  6. PAN Card of LLP
  7. Authorization Letter / Board Resolution Letter
  8. Latest Shareholding Pattern
</Accordion>

<Accordion title="Private Limited">
  1. PAN Card of Signing Authority
  2. Address Proof of Signing Authority
  3. Bank Account Proof
  4. Certificate of Incorporation
  5. Memorandum of Association (complete, all pages)
  6. Articles of Association (complete, all pages)
  7. PAN Card of Company
  8. Authorization Letter (on company letterhead, signed/stamped by a director)
  9. Latest Shareholding Pattern
</Accordion>

<Accordion title="Public Limited">
  1. PAN Card of Signing Authority
  2. Address Proof of Signing Authority
  3. Bank Account Proof
  4. Certificate of Incorporation
  5. Memorandum of Association (complete, all pages)
  6. Articles of Association (complete, all pages)
  7. PAN Card of Company
  8. Authorization Letter
  9. Latest Shareholding Pattern
</Accordion>

<Accordion title="Trust">
  1. PAN Card of Signing Authority
  2. Address Proof of Signing Authority
  3. Bank Account Proof
  4. Government Issued Certificate
  5. Trust Deed (notarized or verified by registrar)
  6. List of trustees/beneficiaries/settlor/members (on letterhead, signed and stamped)
  7. PAN Card of Trust
  8. Authorization Letter
  9. List of Trustees with Shareholding Pattern
</Accordion>

<Accordion title="Society">
  1. PAN Card of Signing Authority
  2. Address Proof of Signing Authority
  3. Bank Account Proof
  4. Government Issued Certificate
  5. Bye-Laws / Memorandum of Association (complete, all pages)
  6. PAN Card of Society
  7. Authorization Letter
  8. List of members certified by Registrar of Society with shareholding
</Accordion>

<Accordion title="Government">
  1. PAN Card of Signing Authority
  2. Address Proof of Signing Authority
  3. Bank Account Proof
  4. Authorization Letter
  5. Registration Certificate / UGC Care certificate / GST
</Accordion>

<Accordion title="One Person Company">
  1. PAN Card of Signing Authority
  2. Address Proof of Signing Authority
  3. Bank Account Proof
  4. Certificate of Incorporation
  5. Memorandum of Association (complete, all pages)
  6. Articles of Association (complete, all pages)
  7. PAN Card of Company
</Accordion>

<Accordion title="Hindu Undivided Family (HUF)">
  1. PAN Card of Signing Authority
  2. Address Proof of Signing Authority
  3. Authorization Letter (signed and stamped by Karta)
  4. Bank Account Proof
  5. HUF Deed (if applicable); Power of attorney or suitable authorisation
</Accordion>

<Accordion title="Additional documents — industry-specific">
  **Educational institutions (Schools, Colleges, Universities)**

  - Affiliation Certificate — must be active, valid, and name must match your KYC details

  **E-Commerce (Food, Groceries, Restaurants, Nutritional Supplements)**

  - FSSAI Certificate — must be active and valid

  **Donations / Crowdfunding (NGOs)**

  - Forms 80G, 12A, and 10AC issued by the Income Tax Department

  **Healthcare (Nutrition and Supplements)**

  - FSSAI Certificate
</Accordion>

<Accordion title="Additional compliance documents — regulated industries">
  | Industry                  | Required document  |
  | ------------------------- | ------------------ |
  | Stock Advisory / Trading  | SEBI Approval      |
  | Prescribed Medicine       | Form 20/21B        |
  | Ayurvedic products        | Ayush Certificate  |
  | Jewellery (Gold/Silver)   | BIS                |
  | Diamond                   | GIA                |
  | Insurance                 | IRDA               |
  | Real Estate               | RERA               |
  | Bill Payment              | BBPS               |
  | Forex                     | RBI Approval       |
  | Mutual Funds Broker       | SEBI Approval      |
  | Banking / NBFC            | RBI Approval       |
  | Drop Shipping             | Supplier Agreement |
  | Payment Facilitator       | RBI Approval       |
  | Internet Service Provider | ISP                |
  | Cable TV Operator         | DAS Licence        |
  | Bulk Messages             | DLT Certificate    |
</Accordion>

***

## Step 3: Get your credentials

{/* SOURCE — content sourced from:
     docs/getting started/payu-dashboard/generate-merchant-key-and-salt-copy.md
     (currently hidden=true — this is the combined test+production page
     recommended for promotion as the canonical credential page).
     Tab structure, steps, field descriptions, and notes are faithful
     to the original. Security notes preserved verbatim. */}

Your Merchant Key and Salt are the credentials used by every PayU integration to authenticate requests and generate hashes. You need them before you can write any integration code.

{/* NEW CONTENT — the "What are Key and Salt?" explanation below does not
     exist as a standalone explanation in any single page. The field
     descriptions in the original are footnotes under the tabs, not a
     clear upfront explanation. This intro is new. Needs SME review. */}

<Callout icon="📘" theme="info">
  ### **What are Merchant Key and Salt?**

  - **Key** — a unique identifier for your merchant account. It is included in every payment request you send to PayU.
  - **Salt (32-bit / v1)** — used to generate the SHA-512 hash that authenticates your requests. Use Salt v1 for standard integrations.
  - **Salt (256-bit / v2)** — a stronger variant of the Salt for integrations that require it.

  Each environment (Test and Production) has a separate Key–Salt pair. Never use Test credentials in production or vice versa.
</Callout>

{/* NEW CONTENT — Test vs Production comparison block.
     The repo documents test and production credentials separately across
     multiple pages but nowhere has a side-by-side comparison that helps
     a new merchant understand which to use and when. This block is new.
     Needs SME review. */}

## Test vs Production Secrets

<Tabs>
  <Tab title="Test secrets">
    |                       |                                                                                                   |
    | --------------------- | ------------------------------------------------------------------------------------------------- |
    | **Where to get them** | [PayU Test Dashboard](https://test.payu.in/) → Developer → API Details                            |
    | **Available**         | Immediately after account creation — no KYC required                                              |
    | **What they do**      | Authenticate requests in the test environment only. No real money moves.                          |
    | **Use when**          | Building your integration, running test transactions, validating your hash generation             |
    | **Key prefix**        | Starts with a test-environment merchant key (different from your live key)                        |
    | **Transactions**      | Use [test cards and UPI IDs](doc:test-cards-and-credentials) — real payment methods will not work |

    <Callout icon="📘" theme="info">
      ### Always build and test with Test secrets first. Your test key and live key are different values — double-check which you have loaded before going live.
    </Callout>
  </Tab>

  <Tab title="Production secrets">
    |                       |                                                                                |
    | --------------------- | ------------------------------------------------------------------------------ |
    | **Where to get them** | [PayU Merchant Dashboard](https://merchant.payu.in/) → Developer → API Details |
    | **Available**         | After PayU verifies your website — up to 2 business days after registration    |
    | **What they do**      | Authenticate live payment requests. Real money moves.                          |
    | **Use when**          | Your integration is tested and you are ready to accept real customer payments  |
    | **Key prefix**        | Starts with your live-environment merchant key (different from your test key)  |
    | **Transactions**      | Real customer payment methods (cards, UPI, net banking, wallets)               |

    <Callout icon="🚧" theme="warn">
      ### **Production secrets are sensitive.** Never expose them in frontend code, client-side JavaScript, or a public repository. Store them in environment variables on your server. If you share access with a developer or agency, ask your Key Account Manager about the correct way to do this securely.
    </Callout>
  </Tab>
</Tabs>

***

### How to get your credentials

<Tabs>
  <Tab title="Test credentials">
    {/* SOURCE: docs/getting started/payu-dashboard/generate-merchant-key-and-salt-copy.md — Test Environment tab */}

    Test credentials are available immediately after you create your account. You do not need to complete KYC first.

    1. Log in to the [PayU Test Dashboard](https://test.payu.in/).

    2. Switch to **Test Mode** using the toggle on the menu bar.

    3. Select **Developer** from the left menu, then open the **API Details** tab.

       Your Test Key and Salt are displayed here and generated automatically on first access.

    <Callout icon="📘" theme="info">
      ### Test credentials only work in the test environment. They cannot be used for live payments.
    </Callout>
  </Tab>

  <Tab title="Production credentials">
    {/* SOURCE: docs/getting started/payu-dashboard/generate-merchant-key-and-salt-copy.md — Production Environment tab */}

    Production credentials become available once your KYC is complete and PayU has verified your website (up to 2 business days after registration).

    1. Log in to the [PayU Merchant Dashboard](https://merchant.payu.in/).

    2. Switch to **Live Mode** using the toggle on the menu bar.

    3. Select **Developer** from the left menu, then open the **API Details** tab.

       Your Production Key and Salt are displayed here.

    <Callout icon="🚧" theme="warn">
      ### **These credentials are sensitive.**

      - Do not share them publicly or in frontend code.
      - Store them securely on your server — use environment variables, not hardcoded values.
      - If you share access with a developer or agency, ask your Key Account Manager about the correct way to do this securely.
    </Callout>
  </Tab>
</Tabs>

### Regenerate your Salt

If your Salt is compromised or you need to rotate it:

1. Log in to the PayU Dashboard and switch to the relevant environment (Live or Test).
2. Select **Developer** from the left menu → **API Details**.
3. Click **Regenerate Salt** and confirm.
4. Click **Activate** next to the new Salt under the **Actions** column.

<Callout icon="📘" theme="info">
  **Important:**

  - A regenerated Salt expires in 15 days if not activated.
  - After activation, the new Salt replaces Salt v1.
  - Update your application immediately after activating a new Salt to avoid payment failures.
</Callout>

***

{/* NEW CONTENT — the "What's next" section below is new.
     It closes the setup journey and points the user forward.
     Needs SME review. */}

## What's next

You now have everything you need to start integrating.

- **Haven't chosen an integration yet?** Go back to [Start Here](doc:start-here) and run the wizard.
- **Ready to integrate?** Open your product's integration guide and use your Test Key and Salt to build and test your first payment.
- **Ready to go live?** See the [Pre-Launch Checklist](doc:go-live) to make sure your integration is production-ready.
