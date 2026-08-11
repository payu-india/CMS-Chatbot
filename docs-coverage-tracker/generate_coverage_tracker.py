#!/usr/bin/env python3
"""
PayU Product Documentation Coverage Tracker generator.

Source of truth: PayU Developer Documentation repository (/workspace).
Sample Excel used only for reporting philosophy/format inspiration.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

ROOT = Path("/workspace")
OUT_DIR = Path("/workspace/docs-coverage-tracker")
OUT_FILE = OUT_DIR / "PayU_Product_Documentation_Coverage_Tracker.xlsx"

# Coverage dimensions (equal weight among applicable)
DIMENSIONS = [
    "overview",
    "integration_guide",
    "api_reference",
    "sdk",
    "quick_start",
    "webhooks",
    "error_codes",
    "testing",
    "go_live",
    "troubleshooting",
    "faqs",
    "changelog",
]


@dataclass
class Product:
    name: str
    category: str
    product_type: str
    overview: Optional[str] = None
    integration_guide: Optional[str] = None
    api_reference: Optional[str] = None
    sdk: Optional[str] = None
    quick_start: Optional[str] = None
    webhooks: Optional[str] = None  # path or "Yes"/"Shared" marker via exists
    error_codes: Optional[str] = None
    testing: Optional[str] = None
    go_live: Optional[str] = None
    troubleshooting: Optional[str] = None
    faqs: Optional[str] = None
    changelog: Optional[str] = None
    # Applicability: True=required, False=N/A, None=auto from presence
    applicable: dict = field(default_factory=dict)
    # Integration guide recommendation
    recommend_ig: bool = False
    priority: str = "P3"  # P0/P1/P2/P3 / N/A
    recommended_action: str = ""
    notes: str = ""
    # Extra pages for inventory notes
    existing_pages_note: str = ""

    def path_exists(self, path: Optional[str]) -> bool:
        if not path:
            return False
        if path in {"Yes", "Shared", "Partial", "N/A"}:
            return path in {"Yes", "Shared", "Partial"}
        p = ROOT / path
        return p.exists()

    def flag(self, dim: str) -> str:
        """Return Yes / No / Partial / N/A for a dimension."""
        if self.applicable.get(dim) is False:
            return "N/A"
        val = getattr(self, dim)
        if val == "Partial":
            return "Partial"
        if val == "Shared":
            return "Yes"
        if val == "Yes":
            return "Yes"
        if val == "N/A":
            return "N/A"
        if val and self.path_exists(val):
            return "Yes"
        # If marked applicable False already handled; if no path, Missing
        if self.applicable.get(dim) is False:
            return "N/A"
        return "No"

    def link(self, dim: str) -> str:
        val = getattr(self, dim)
        if not val or val in {"Yes", "No", "Partial", "Shared", "N/A"}:
            return ""
        if self.path_exists(val):
            return val
        return ""

    def coverage_score(self) -> float:
        scores = []
        for dim in DIMENSIONS:
            f = self.flag(dim)
            if f == "N/A":
                continue
            if f == "Yes":
                scores.append(1.0)
            elif f == "Partial":
                scores.append(0.5)
            else:
                scores.append(0.0)
        if not scores:
            return 0.0
        return round(100.0 * sum(scores) / len(scores), 1)

    def status(self) -> str:
        score = self.coverage_score()
        # Missing critical overview + integration for developer-facing products
        overview = self.flag("overview")
        ig = self.flag("integration_guide")
        if overview == "No" and ig == "No" and score < 40:
            return "Missing"
        if score >= 85:
            return "Complete"
        if score < 40:
            return "Missing"
        return "Partial"


def exists(path: str) -> bool:
    return (ROOT / path).exists()


def build_products() -> list[Product]:
    """Build product inventory from repository structure (verified paths)."""
    products: list[Product] = []

    # Shared web checkout assets
    WEB_WEBHOOKS = "docs/Collect Payments/introduction-web/webhooks.md"
    WEB_ERRORS = "docs/Collect Payments/introduction-web/error-handling.md"
    WEB_TESTING = "docs/Collect Payments/introduction-web/test-cards-upi-id-and-wallets.md"
    WEB_FAQS = "docs/Collect Payments/introduction-web/faqs-for-web-checkout-integration.md"
    WEB_ERROR_REF = "reference/Collect Payment/error-codes.md"
    COLLECT_API = "reference/Collect Payment"

    # -------------------------------------------------------------------------
    # Getting Started / Platform
    # -------------------------------------------------------------------------
    products.append(
        Product(
            name="Merchant Onboarding / Sign Up",
            category="Getting Started",
            product_type="Platform / Onboarding",
            overview="docs/getting started/introduction/index.md",
            integration_guide="docs/getting started/register-with-payu/register-for-a-merchant-account-on-dashboard.md",
            api_reference=None,
            sdk=None,
            quick_start="docs/getting started/register-with-payu/index.md"
            if exists("docs/getting started/register-with-payu/index.md")
            else "docs/getting started/register-with-payu/register-for-a-merchant-account-on-dashboard.md",
            webhooks=None,
            error_codes=None,
            testing="docs/getting started/payu-dashboard/generate-test-merchant-key-and-salt.md",
            go_live="docs/getting started/register-with-payu/complete-your-kyc.md",
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={
                "api_reference": False,
                "sdk": False,
                "webhooks": False,
                "error_codes": False,
                "changelog": False,
                "troubleshooting": True,
                "faqs": True,
            },
            recommend_ig=False,
            priority="P2",
            recommended_action="Add FAQs and troubleshooting for KYC/activation blockers; keep onboarding journey as step-by-step guide (not a classic Integration Guide).",
            notes="Covers register, KYC, documents checklist under getting started/register-with-payu.",
        )
    )

    products.append(
        Product(
            name="PayU Dashboard",
            category="Getting Started",
            product_type="Platform / Tool",
            overview="docs/getting started/payu-dashboard/index.md",
            integration_guide=None,
            api_reference=None,
            sdk=None,
            quick_start="docs/getting started/payu-dashboard/log-in-to-dashboard.md",
            webhooks="docs/getting started/payu-dashboard/manage-webhooks-using-dashboard/index.md",
            error_codes=None,
            testing="docs/getting started/payu-dashboard/generate-test-merchant-key-and-salt.md",
            go_live=None,
            troubleshooting=None,
            faqs="docs/getting started/payu-dashboard/faqs-for-dashboard.md",
            changelog=None,
            applicable={
                "integration_guide": False,
                "api_reference": False,
                "sdk": False,
                "error_codes": False,
                "go_live": False,
                "changelog": False,
            },
            recommend_ig=False,
            priority="P2",
            recommended_action="Improve module-level how-to consistency (settlements, reports, users); add troubleshooting for common dashboard access issues.",
            notes="Modules include transactions, settlements, beneficiaries, integrations, banking, reports, webhooks, users/permissions.",
        )
    )

    # -------------------------------------------------------------------------
    # Collect Payments — Core Checkout
    # -------------------------------------------------------------------------
    products.append(
        Product(
            name="PayU Hosted Checkout (Prebuilt)",
            category="Collect Payments / Web Checkout",
            product_type="Core Payment Product",
            overview="docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/index.md",
            integration_guide="docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/prebuilt-checkout-page-integration.md",
            api_reference="reference/Collect Payment/_payment_payu_hosted_checkout.md",
            sdk=None,
            quick_start="docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/prebuilt-checkout-page-integration.md",
            webhooks=WEB_WEBHOOKS,
            error_codes=WEB_ERROR_REF,
            testing=WEB_TESTING,
            go_live="Partial",
            troubleshooting="Partial",
            faqs=WEB_FAQS,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="Strengthen dedicated end-to-end Integration Guide with go-live checklist, troubleshooting, and clearer path from hash → request → callback → verify payment.",
            notes="Also called Prebuilt / Non-Seamless Checkout. Shared webhooks/errors/testing under introduction-web. Recipe exists in recipes/payu-hosted-checkout-curl-request-walkthrough.md. ASK AI duplicate: hosted-checkout-integration-demo.",
        )
    )

    products.append(
        Product(
            name="Merchant Hosted Checkout (Custom / Seamless)",
            category="Collect Payments / Web Checkout",
            product_type="Core Payment Product",
            overview="docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/index.md",
            integration_guide="docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/integration-checklist-merchant-hosted-checkout.md",
            api_reference="reference/Collect Payment/_payment_merchant_hosted",
            sdk=None,
            quick_start="docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/collect-payments-with-cards-seamless.md",
            webhooks=WEB_WEBHOOKS,
            error_codes="reference/Collect Payment/_payment_merchant_hosted/_payment_merchant_hosted_cards/field-7-field-8-error-codes.md",
            testing="docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/test-integration.md",
            go_live="docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/integration-checklist-merchant-hosted-checkout.md",
            troubleshooting="Partial",
            faqs=WEB_FAQS,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="Publish a single merchant-journey Integration Guide that stitches payment-method pages (cards/NB/UPI/wallets/EMI/BNPL), hashing, webhooks, verify payment, and go-live into one narrative.",
            notes="Payment method pages exist individually. Duplicate API surfaces: reference/PayU Merchant Hosted — _payment and General APIs/merchanthostedpostservice.",
        )
    )

    products.append(
        Product(
            name="Server-to-Server (S2S) Checkout",
            category="Collect Payments / Web Checkout",
            product_type="Core Payment Product",
            overview="docs/Collect Payments/introduction-web/server-to-server-integration/index.md",
            integration_guide="docs/Collect Payments/introduction-web/server-to-server-integration/integrate-with-s2s.md",
            api_reference="reference/Collect Payment/_payment_server_to_server",
            sdk=None,
            quick_start="docs/Collect Payments/introduction-web/server-to-server-integration/integrate-with-s2s.md",
            webhooks=WEB_WEBHOOKS,
            error_codes="reference/Collect Payment/_payment_server_to_server/error-codes-for-s2s-link-and-pay.md",
            testing=WEB_TESTING,
            go_live="docs/Collect Payments/introduction-web/server-to-server-integration/integration-checklist-s2s.md",
            troubleshooting="Partial",
            faqs=WEB_FAQS,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="Create a unified S2S Integration Guide covering classic, decoupled, and direct-authorization flows with decision tree, error handling, and go-live checklist.",
            notes="High complexity (classic/decoupled/direct auth/UPI variants). Legacy and old_ API pages exist in reference. Recycle Bin contains decoupled-flow docs.",
        )
    )

    products.append(
        Product(
            name="Checkout Plus (ICP / Bolt Checkout)",
            category="Collect Payments / Web Checkout",
            product_type="Core Payment Product",
            overview="docs/Collect Payments/introduction-web/checkout-plus-integration/index.md",
            integration_guide="docs/Collect Payments/introduction-web/checkout-plus-integration/integrate-checkout-plus.md",
            api_reference="docs/Collect Payments/introduction-web/checkout-plus-integration/apis-used-for-checkout-plus-integration.md",
            sdk=None,
            quick_start="docs/Collect Payments/introduction-web/checkout-plus-integration/integrate-checkout-plus.md",
            webhooks=WEB_WEBHOOKS,
            error_codes=WEB_ERROR_REF,
            testing=WEB_TESTING,
            go_live=None,
            troubleshooting=None,
            faqs=WEB_FAQS,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="Consolidate Checkout Plus / ICP / Bolt naming; expand Integration Guide with testing, go-live, troubleshooting; reduce reliance on ASK AI duplicate page.",
            notes="Naming inconsistency: Checkout Plus vs ICP Checkout vs Bolt Checkout. ASK AI page: Integration ASK AI Docs/checkout-plusicp-checkoutbolt-checkout.md.",
        )
    )

    products.append(
        Product(
            name="CommercePro Checkout (Checkout Express)",
            category="Collect Payments / Web Checkout",
            product_type="Core Payment Product",
            overview="docs/Collect Payments/introduction-web/checkout-express/index.md",
            integration_guide="docs/Collect Payments/introduction-web/checkout-express/integrate-commercepro-checkout-using-callback-url.md",
            api_reference="reference/Checkout Express",
            sdk=None,
            quick_start="docs/Collect Payments/introduction-web/checkout-express/integration-checkout-express-response-handler.md",
            webhooks=WEB_WEBHOOKS,
            error_codes=WEB_ERROR_REF,
            testing=WEB_TESTING,
            go_live=None,
            troubleshooting=None,
            faqs=WEB_FAQS,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Unify CommercePro vs Checkout Express naming; add dedicated go-live + troubleshooting; clarify relationship to plugin CommercePro pages.",
            notes="Folder/reference named Checkout Express; guide titles use CommercePro. Also listed under ecommerce-platform-plugins/commercepro-checkout.md.",
        )
    )

    # -------------------------------------------------------------------------
    # No-code
    # -------------------------------------------------------------------------
    products.append(
        Product(
            name="Payment Links",
            category="Collect Payments / No-Code",
            product_type="Core Payment Product",
            overview="docs/Collect Payments/introduction-no-code-payments-integration/payment-links-dashboard/index.md",
            integration_guide="docs/Collect Payments/introduction-no-code-payments-integration/payment-links-dashboard/integration-api-for-payment-links.md",
            api_reference="reference/payment links",
            sdk=None,
            quick_start="docs/Collect Payments/introduction-no-code-payments-integration/payment-links-dashboard/index.md",
            webhooks=WEB_WEBHOOKS,
            error_codes=None,
            testing=WEB_TESTING,
            go_live=None,
            troubleshooting=None,
            faqs="docs/Collect Payments/introduction-no-code-payments-integration/payment-links-dashboard/faqs-payment-links.md",
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="Ship a dedicated Payment Links Integration Guide covering dashboard + API creation, webhooks, TPV variant, WhatsApp EPL, and go-live.",
            notes="Also appears in partner APIs, WhatsApp Enhanced Payment Links, TPV payment-link guide, WooCommerce payment links.",
        )
    )

    products.append(
        Product(
            name="Payment Buttons",
            category="Collect Payments / No-Code",
            product_type="Payment Feature",
            overview="docs/Collect Payments/introduction-no-code-payments-integration/payment-buttons-dashboard.md",
            integration_guide="docs/Collect Payments/introduction-no-code-payments-integration/payment-buttons-dashboard.md",
            api_reference=None,
            sdk=None,
            quick_start="docs/Collect Payments/introduction-no-code-payments-integration/payment-buttons-dashboard.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={
                "api_reference": False,
                "sdk": False,
                "webhooks": False,
                "error_codes": False,
                "changelog": False,
            },
            recommend_ig=False,
            priority="P3",
            recommended_action="Expand dashboard how-to with screenshots and FAQs; dedicated Integration Guide not required (no-code UI product).",
            notes="Single-page documentation under no-code payments.",
        )
    )

    products.append(
        Product(
            name="Invoices (No-Code)",
            category="Collect Payments / No-Code",
            product_type="Payment Feature",
            overview="docs/Collect Payments/introduction-no-code-payments-integration/invoices-dashboard/index.md",
            integration_guide="docs/Collect Payments/introduction-no-code-payments-integration/invoices-dashboard/create-an-invoice.md",
            api_reference=None,
            sdk=None,
            quick_start="docs/Collect Payments/introduction-no-code-payments-integration/invoices-dashboard/create-an-invoice.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={
                "api_reference": False,
                "sdk": False,
                "webhooks": False,
                "error_codes": False,
                "changelog": False,
            },
            recommend_ig=False,
            priority="P2",
            recommended_action="Clarify Invoice vs Payment Link vs Zion subscription invoices; add FAQs.",
            notes="Partner APIs also mention Manage Invoices or Payment Links — naming overlap risk.",
        )
    )

    # -------------------------------------------------------------------------
    # In-person
    # -------------------------------------------------------------------------
    products.append(
        Product(
            name="UPI QR",
            category="Collect Payments / In-Person",
            product_type="Core Payment Product",
            overview="docs/Collect Payments/in-person-payments/integrate-upi-qr/index.md",
            integration_guide="docs/Collect Payments/in-person-payments/integrate-upi-qr/index.md",
            api_reference="reference/In-person payments/integrate-upi-qr-apis",
            sdk=None,
            quick_start="docs/Collect Payments/in-person-payments/integrate-upi-qr/index.md",
            webhooks="Partial",
            error_codes="reference/In-person payments/integrate-upi-qr-apis/error-codes-for-qr-apis-1.md",
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs="docs/Collect Payments/in-person-payments/integrate-upi-qr/faqs-2.md",
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Expand Integration Guide with callback/webhook handling, sandbox testing, and go-live steps.",
            notes="API reference includes dynamic/static QR and error codes.",
        )
    )

    products.append(
        Product(
            name="Dynamic Storefront QR (DBQR)",
            category="Collect Payments / In-Person",
            product_type="Payment Feature",
            overview="docs/Collect Payments/in-person-payments/integrated-dynamic-storefront/index.md",
            integration_guide="docs/Collect Payments/in-person-payments/integrated-dynamic-storefront/integrated-dynamic-storefront-customer-journey.md",
            api_reference=None,
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "api_reference": True, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Publish a dedicated Integration Guide; resolve DBQR / Offline DBQR / Dynamic Bharat QR naming; surface ASK AI offline-dbqr content into canonical docs.",
            notes="ASK AI duplicate: Integration ASK AI Docs/offline-dbqr.md. Limited API mapping in guides.",
        )
    )

    products.append(
        Product(
            name="POS Terminal Integration",
            category="Collect Payments / In-Person",
            product_type="Core Payment Product",
            overview="docs/Collect Payments/in-person-payments/pos-terminal-integration/index.md",
            integration_guide="docs/Collect Payments/in-person-payments/pos-terminal-integration/apis-for-pos-terminal-integration.md",
            api_reference="reference/In-person payments/pos-terminal-integration-apis",
            sdk=None,
            quick_start="docs/Collect Payments/in-person-payments/pos-terminal-integration/apis-for-pos-terminal-integration.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Add end-to-end Integration Guide with device setup, test transactions, error codes, and go-live.",
            notes="Overview + API map exist; operational docs thin.",
        )
    )

    products.append(
        Product(
            name="Android POS SDK",
            category="Collect Payments / In-Person",
            product_type="Integration Channel (SDK)",
            overview="docs/Collect Payments/in-person-payments/android-pos-sdk/index.md",
            integration_guide="docs/Collect Payments/in-person-payments/android-pos-sdk/index.md",
            api_reference="reference/In-person payments/android-pos-sdk-apis",
            sdk="docs/Collect Payments/in-person-payments/android-pos-sdk/index.md",
            quick_start="docs/Collect Payments/in-person-payments/android-pos-sdk/index.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"webhooks": False, "changelog": True},
            recommend_ig=True,
            priority="P1",
            recommended_action="Expand SDK Integration Guide with sample app walkthrough, error handling, testing, and changelog.",
            notes="Installation/activation pages under android-pos-sdk folder.",
        )
    )

    # -------------------------------------------------------------------------
    # Ecommerce plugins
    # -------------------------------------------------------------------------
    plugins = [
        ("Shopify", "shopify", "index.md", "faqs-for-shopify.md", None, "P1", True,
         "High-adoption plugin; ensure CommercePro/offers/reconciliation paths are clear; keep Integration Guide as install→configure→go-live."),
        ("WooCommerce", "woocommerce", "index.md", None, "troubleshooting-woocommerce-integration.md", "P1", True,
         "High-adoption; reconcile duplicate ASK AI woocommerce guide into canonical docs."),
        ("Magento", "magento", "index.md", None, "troubleshooting-magento-integration.md", "P2", True,
         "Maintain install + CommercePro + troubleshooting; Integration Guide valuable for merchants."),
        ("Wix", "wix", "index.md", "faqs-for-wix-integration.md", None, "P2", False,
         "Overview + FAQ sufficient; expand only if support volume warrants."),
        ("BigCommerce", "bigcommerce", "index.md", None, "troubleshooting-bigcommerce-integration.md", "P2", False,
         "Keep troubleshooting current; dedicated IG low value beyond install guide."),
        ("Shopmatic", "shopmatic", "index.md", None, "troubleshooting-shopmatic-integration.md", "P3", False,
         "Maintain troubleshooting; no dedicated IG beyond install."),
        ("Fynd Store", "fynd-integration", "index.md", None, None, "P3", False,
         "Thin docs; expand only with merchant demand."),
        ("OpenCart", "opencart", "index.md", None, "troubleshooting-opencart-integration.md", "P3", False,
         "Install + troubleshooting adequate for plugin channel."),
        ("PrestaShop", "prestashop", "index.md", None, "troubleshooting-prestashop-integration.md", "P3", False,
         "Install + troubleshooting adequate."),
        ("Zoho", "zoho-integration", "index.md", None, None, "P2", True,
         "Multiple Zoho surfaces (Marketplace/One/Billing/Inventory); recommend one Integration Guide with product matrix."),
        ("Odoo", "odoo", "index.md", None, None, "P3", False,
         "Installation page present; expand if adoption grows."),
        ("Bagisto", "bagisto.md", None, None, None, "P3", False,
         "Single-page guide; low priority."),
        ("Interakt for WhatsApp Business", "interakt-for-whatsapp-business", "index.md", None, None, "P2", False,
         "Cross-links with WhatsApp payments; clarify channel boundary."),
    ]

    for name, folder, overview_file, faqs_file, trouble_file, pri, rec_ig, action in plugins:
        base = f"docs/Collect Payments/ecommerce-platform-plugins/{folder}"
        if folder.endswith(".md"):
            overview = f"docs/Collect Payments/ecommerce-platform-plugins/{folder}"
            ig = overview
            faqs = None
            trouble = None
        else:
            overview = f"{base}/{overview_file}" if overview_file else f"{base}/index.md"
            # find a likely integration page
            ig_candidates = [
                f"{base}/index.md",
            ]
            ig = next((c for c in ig_candidates if exists(c)), overview)
            faqs = f"{base}/{faqs_file}" if faqs_file else None
            trouble = f"{base}/{trouble_file}" if trouble_file else None
        products.append(
            Product(
                name=f"{name} Plugin",
                category="Collect Payments / eCommerce Plugins",
                product_type="Integration Channel (Plugin)",
                overview=overview if exists(overview) else None,
                integration_guide=ig if exists(ig) else None,
                api_reference=None,
                sdk=None,
                quick_start=ig if exists(ig) else None,
                webhooks=None,
                error_codes=None,
                testing=None,
                go_live="docs/Collect Payments/ecommerce-platform-plugins/integration-checklist-plugins.md",
                troubleshooting=trouble if trouble and exists(trouble) else None,
                faqs=faqs if faqs and exists(faqs) else None,
                changelog=None,
                applicable={
                    "api_reference": False,
                    "sdk": False,
                    "webhooks": False,
                    "error_codes": False,
                    "changelog": False,
                },
                recommend_ig=rec_ig,
                priority=pri,
                recommended_action=action,
                notes="Shared plugin checklist: ecommerce-platform-plugins/integration-checklist-plugins.md.",
            )
        )

    # -------------------------------------------------------------------------
    # Server SDKs (grouped)
    # -------------------------------------------------------------------------
    for lang, file in [
        ("Go SDK", "go-sdk.md"),
        ("Java SDK", "java-sdk.md"),
        ("PHP SDK", "php-sdk.md"),
        ("Python SDK", "python-sdk.md"),
        ("Node.js SDK", "node-js-sdk.md"),
    ]:
        path = f"docs/Collect Payments/explore-server-integrations/{file}"
        products.append(
            Product(
                name=lang,
                category="Collect Payments / Server-Side SDKs",
                product_type="Integration Channel (SDK)",
                overview="docs/Collect Payments/explore-server-integrations/index.md"
                if exists("docs/Collect Payments/explore-server-integrations/index.md")
                else path,
                integration_guide=path,
                api_reference=COLLECT_API,
                sdk=path,
                quick_start=path,
                webhooks=WEB_WEBHOOKS,
                error_codes=WEB_ERROR_REF,
                testing=WEB_TESTING,
                go_live=None,
                troubleshooting=None,
                faqs=None,
                changelog=None,
                applicable={"changelog": True, "troubleshooting": True, "faqs": True, "go_live": True},
                recommend_ig=True if lang in {"PHP SDK", "Node.js SDK", "Java SDK"} else False,
                priority="P1" if lang in {"PHP SDK", "Node.js SDK", "Java SDK"} else "P2",
                recommended_action="Upgrade from single-page SDK note to full Integration Guide (install, auth, payment sample, verify, errors, changelog) for high-usage languages.",
                notes="Currently thin single-page SDK docs under explore-server-integrations.",
            )
        )

    # -------------------------------------------------------------------------
    # Mobile SDKs — major products (platform-level)
    # -------------------------------------------------------------------------
    mobile = [
        (
            "Android CheckoutPro SDK",
            "docs/Collect Payments/mobile-sdks/explore-android-sdks/android-checkoutpro-sdk/index.md",
            "docs/Collect Payments/mobile-sdks/explore-android-sdks/android-checkoutpro-sdk/index.md",
            "docs/Collect Payments/mobile-sdks/explore-android-sdks/android-checkoutpro-sdk/android-checkoutpro-troubleshoot-errors.md",
            "docs/Collect Payments/mobile-sdks/explore-android-sdks/faqs-android-sdk/index.md",
            None,
            "P0",
            True,
            "Primary Android integration path; ensure Integration Guide covers offers/TPV/sample app and keep troubleshooting current.",
        ),
        (
            "Android Core SDK",
            "docs/Collect Payments/mobile-sdks/explore-android-sdks/android-core-sdk/index.md",
            "docs/Collect Payments/mobile-sdks/explore-android-sdks/android-core-sdk/index.md",
            None,
            "docs/Collect Payments/mobile-sdks/explore-android-sdks/faqs-android-sdk/index.md",
            None,
            "P1",
            True,
            "Document decision: CheckoutPro vs Core; Integration Guide should include TPV and web services.",
        ),
        (
            "iOS CheckoutPro SDK",
            "docs/Collect Payments/mobile-sdks/explore-ios-sdks/ios-checkoutpro-sdk/index.md",
            "docs/Collect Payments/mobile-sdks/explore-ios-sdks/ios-checkoutpro-sdk/index.md",
            None,
            "docs/Collect Payments/mobile-sdks/explore-ios-sdks/ios-sdk-faqs.md",
            None,
            "P0",
            True,
            "Primary iOS path; add explicit go-live checklist and changelog parity with Android.",
        ),
        (
            "iOS Core SDK",
            "docs/Collect Payments/mobile-sdks/explore-ios-sdks/ios-core-sdk/index.md",
            "docs/Collect Payments/mobile-sdks/explore-ios-sdks/ios-core-sdk/index.md",
            None,
            "docs/Collect Payments/mobile-sdks/explore-ios-sdks/ios-sdk-faqs.md",
            None,
            "P1",
            True,
            "Cover recurring/TPV; align release notes.",
        ),
        (
            "iOS Custom Browser SDK",
            "docs/Collect Payments/mobile-sdks/explore-ios-sdks/ios-custombrowser-sdk/index.md",
            "docs/Collect Payments/mobile-sdks/explore-ios-sdks/ios-custombrowser-sdk/index.md",
            None,
            "docs/Collect Payments/mobile-sdks/explore-ios-sdks/ios-sdk-faqs.md",
            "docs/Collect Payments/mobile-sdks/explore-ios-sdks/ios-custombrowser-sdk/ios-custombrowser-golive-checklist.md",
            "P1",
            False,
            "Has go-live checklist and test integration — model for other SDKs; dedicated IG optional if pages stay cohesive.",
        ),
        (
            "React Native CheckoutPro SDK",
            "docs/Collect Payments/mobile-sdks/explore-reactnative-sdks/react-native-checkoutpro-sdk/index.md",
            "docs/Collect Payments/mobile-sdks/explore-reactnative-sdks/react-native-checkoutpro-sdk/index.md",
            None,
            "docs/Collect Payments/mobile-sdks/explore-reactnative-sdks/faqs-react-native-sdk.md",
            None,
            "P1",
            True,
            "High DevEx impact for cross-platform apps; consolidate duplicate FAQ pages.",
        ),
        (
            "Flutter CheckoutPro SDK",
            "docs/Collect Payments/mobile-sdks/flutter-sdk-introduction/flutter-checkoutpro-sdk/index.md",
            "docs/Collect Payments/mobile-sdks/flutter-sdk-introduction/flutter-checkoutpro-sdk/index.md",
            None,
            None,
            None,
            "P1",
            True,
            "Add FAQs/troubleshooting; version history exists — promote as changelog.",
        ),
        (
            "Cordova CheckoutPro SDK",
            "docs/Collect Payments/mobile-sdks/cordova-mobile-sdks/cordova-sdk-introduction/index.md",
            "docs/Collect Payments/mobile-sdks/cordova-mobile-sdks/cordova-sdk-introduction/index.md",
            None,
            None,
            None,
            "P2",
            False,
            "Maintain; lower adoption vs RN/Flutter.",
        ),
        (
            "UPI Bolt SDK (Android/iOS/RN/Flutter/Ionic)",
            "docs/Collect Payments/mobile-sdks/explore-android-sdks/payu-bolt-sdk/index.md",
            "docs/Collect Payments/mobile-sdks/explore-android-sdks/payu-bolt-sdk/index.md",
            None,
            None,
            None,
            "P1",
            True,
            "Resolve Ionic/Capacitor/Cordova naming inconsistency; publish one cross-platform UPI Bolt Integration Guide with platform tabs.",
        ),
    ]

    for name, overview, ig, trouble, faqs, golive, pri, rec_ig, action in mobile:
        products.append(
            Product(
                name=name,
                category="Collect Payments / Mobile SDKs",
                product_type="Integration Channel (SDK)",
                overview=overview if exists(overview) else None,
                integration_guide=ig if exists(ig) else None,
                api_reference=None,
                sdk=overview if exists(overview) else None,
                quick_start=ig if exists(ig) else None,
                webhooks=None,
                error_codes=None,
                testing="docs/Collect Payments/mobile-sdks/explore-ios-sdks/ios-custombrowser-sdk/ios-custombrowser-test-integration.md"
                if "iOS Custom" in name
                else WEB_TESTING,
                go_live=golive if golive and exists(golive) else None,
                troubleshooting=trouble if trouble and exists(trouble) else None,
                faqs=faqs if faqs and exists(faqs) else None,
                changelog=(
                    "docs/Collect Payments/mobile-sdks/flutter-sdk-introduction/flutter-checkoutpro-sdk/flutter-checkout-pro-version-history.md"
                    if "Flutter CheckoutPro" in name
                    and exists(
                        "docs/Collect Payments/mobile-sdks/flutter-sdk-introduction/flutter-checkoutpro-sdk/flutter-checkout-pro-version-history.md"
                    )
                    else (
                        "docs/Collect Payments/mobile-sdks/explore-android-sdks/android-checkoutpro-sdk/change-logs.md"
                        if "Android CheckoutPro" in name
                        and exists(
                            "docs/Collect Payments/mobile-sdks/explore-android-sdks/android-checkoutpro-sdk/change-logs.md"
                        )
                        else (
                            "docs/Collect Payments/mobile-sdks/explore-reactnative-sdks/react-native-checkoutpro-sdk/reactnative-checkoutpro-change-logs.md"
                            if "React Native CheckoutPro" in name
                            and exists(
                                "docs/Collect Payments/mobile-sdks/explore-reactnative-sdks/react-native-checkoutpro-sdk/reactnative-checkoutpro-change-logs.md"
                            )
                            else None
                        )
                    )
                ),
                applicable={
                    "api_reference": False,
                    "webhooks": False,
                    "error_codes": True,
                },
                recommend_ig=rec_ig,
                priority=pri,
                recommended_action=action,
                notes="Sibling SDKs (UPI, Native OTP Assist, PhonePe, Google Pay, 3DS/FlashPay, Ola Money, Custom Browser) also exist under mobile-sdks.",
            )
        )

    # -------------------------------------------------------------------------
    # Offerings
    # -------------------------------------------------------------------------
    offerings = [
        Product(
            name="EMI / Cardless EMI",
            category="Offerings / Affordability",
            product_type="Payment Feature",
            overview="docs/Offerings/introduction-to-affordability/emi-api-integration/index.md",
            integration_guide="docs/Offerings/introduction-to-affordability/emi-api-integration/integration-checklist-emi.md",
            api_reference="reference/General/emi-apis",
            sdk=None,
            quick_start="docs/Offerings/introduction-to-affordability/emi-api-integration/index.md",
            webhooks=WEB_WEBHOOKS,
            error_codes=None,
            testing=None,
            go_live="docs/Offerings/introduction-to-affordability/emi-api-integration/integration-checklist-emi.md",
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="Create dedicated EMI Integration Guide covering hosted/MH/S2S + NTB flow; link Affordability suite.",
            notes="EMI NTB has separate reference under Affordability/emi-ntb-flow-apis.",
        ),
        Product(
            name="Offer Engine / Offers",
            category="Offerings / Affordability",
            product_type="Platform / Payment Feature",
            overview="docs/Offerings/introduction-to-affordability/offers-integration-1/index.md",
            integration_guide="docs/Offerings/introduction-to-affordability/offers-integration-1/offers-integration/integration-checklist-offers.md",
            api_reference="reference/Affordability/offer-apis",
            sdk=None,
            quick_start="docs/Offerings/introduction-to-affordability/offers-integration-1/index.md",
            webhooks=None,
            error_codes="docs/Offerings/introduction-to-affordability/offers-integration-1/offers-integration/error-codes-for-offers-integration.md",
            testing=None,
            go_live="docs/Offerings/introduction-to-affordability/offers-integration-1/offers-integration/integration-checklist-offers.md",
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="Ship Offer Engine Integration Guide (dashboard create → apply at checkout → validate → settle/refund). ASK AI duplicate should redirect to canonical.",
            notes="Dashboard docs under offers-dashboard. ASK AI: affordability-offer-engine-14.md.",
        ),
        Product(
            name="Affordability Widget",
            category="Offerings / Affordability",
            product_type="Platform / Tool",
            overview="docs/Offerings/introduction-to-affordability/affordability-suite/index.md",
            integration_guide="docs/Offerings/introduction-to-affordability/affordability-suite/index.md",
            api_reference=None,
            sdk="docs/Offerings/introduction-to-affordability/affordability-suite/index.md",
            quick_start="docs/Offerings/introduction-to-affordability/affordability-suite/index.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"api_reference": False, "webhooks": False, "error_codes": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Dedicated JS/React widget Integration Guide with plugin variants (Shopify/Woo).",
            notes="JS and React integrations under affordability-suite.",
        ),
        Product(
            name="BNPL / Pay Later",
            category="Offerings / Affordability",
            product_type="Payment Feature",
            overview="docs/Offerings/introduction-to-affordability/payu-bnpl-integration-introduction/index.md",
            integration_guide="docs/Offerings/introduction-to-affordability/payu-bnpl-integration-introduction/index.md",
            api_reference="reference/Affordability/bnpl-integration-apis",
            sdk=None,
            quick_start="docs/Offerings/introduction-to-affordability/payu-bnpl-integration-introduction/index.md",
            webhooks=None,
            error_codes="docs/Offerings/introduction-to-affordability/payu-bnpl-integration-introduction/error-codes-1.md",
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Complete Integration Guide for Link & Pay + quick checkout with testing and go-live.",
            notes="Includes BNPL Link & Pay flows.",
        ),
        Product(
            name="LazyPay Pay-in-3",
            category="Offerings / Affordability",
            product_type="Partner Payment Feature",
            overview="docs/Offerings/introduction-to-affordability/lazypay-pay-in-3/index.md",
            integration_guide="docs/Offerings/introduction-to-affordability/lazypay-pay-in-3/index.md",
            api_reference="reference/Affordability/lazypay-pay-in-3",
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=False,
            priority="P2",
            recommended_action="Expand Merchant Hosted guide; FAQs and testing checklist recommended.",
            notes="Partner product under Affordability.",
        ),
        Product(
            name="MobiKwik Link & Pay",
            category="Offerings / Affordability",
            product_type="Partner Payment Feature",
            overview="docs/Offerings/introduction-to-affordability/mobikwik-link-pay-integration/index.md",
            integration_guide="docs/Offerings/introduction-to-affordability/mobikwik-link-pay-integration/index.md",
            api_reference="reference/Third-Party Wallets/mobikwik-link-wallet-apis",
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing="docs/Offerings/introduction-to-affordability/mobikwik-link-pay-integration/testing-checklist-mobikwik-link-pay.md",
            go_live="docs/Offerings/introduction-to-affordability/mobikwik-link-pay-integration/testing-checklist-mobikwik-link-pay.md",
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=False,
            priority="P2",
            recommended_action="Clarify boundary vs MobiKwik Wallet APIs; keep testing checklist current.",
            notes="Distinct from MobiKwik wallet reference APIs.",
        ),
        Product(
            name="Loyalty Edge",
            category="Offerings / Affordability",
            product_type="Platform / Payment Feature",
            overview="docs/Offerings/introduction-to-affordability/loyalty-edge-introduction/index.md",
            integration_guide=None,
            api_reference=None,
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "api_reference": False, "webhooks": False, "error_codes": False, "changelog": False},
            recommend_ig=False,
            priority="P2",
            recommended_action="Add clear enablement + dashboard journey; Integration Guide only if API/SDK surface expands.",
            notes="Workflow/enablement/dashboard pages under loyalty-edge-introduction.",
        ),
        Product(
            name="Subscriptions / Recurring Payments",
            category="Offerings / Subscriptions",
            product_type="Core Payment Product",
            overview="docs/Offerings/introduction-recurring-payments-integration/index.md",
            integration_guide="docs/Offerings/introduction-recurring-payments-integration/using-api-integration-recurring-payments/index.md",
            api_reference="reference/Subscriptions",
            sdk=None,
            quick_start="docs/Offerings/introduction-recurring-payments-integration/subscriptions-integration/index.md"
            if exists("docs/Offerings/introduction-recurring-payments-integration/subscriptions-integration/index.md")
            else "docs/Offerings/introduction-recurring-payments-integration/using-api-integration-recurring-payments/index.md",
            webhooks="reference/Subscriptions/set-up-webhook-to-receive-cancellation-or-modification-update-from-the-issuer-bank.md",
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs="docs/Offerings/introduction-recurring-payments-integration/faqs-recurring-payments.md",
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="MUST have a single Integration Guide that unifies SI/Recurring/Subscriptions naming, consent→PDN→recurring, UPI AutoPay, eNACH, and cards; retire ASK AI duplicate into canonical.",
            notes="Duplicate aggregate API: reference/Pre-debit and Recurring Payments Transaction API. Naming: Subscriptions vs Recurring vs SI.",
        ),
        Product(
            name="Zion Subscription Automation",
            category="Offerings / Subscriptions",
            product_type="Platform / Tool",
            overview="docs/Offerings/introduction-recurring-payments-integration/using-zion-subscription-automation-platform/index.md",
            integration_guide="docs/Offerings/introduction-recurring-payments-integration/using-zion-subscription-automation-platform/index.md",
            api_reference="reference/ZION",
            sdk=None,
            quick_start=None,
            webhooks="docs/Offerings/introduction-recurring-payments-integration/using-zion-subscription-automation-platform/webhooks-for-subscription.md",
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs="docs/Offerings/introduction-recurring-payments-integration/using-zion-subscription-automation-platform/faqs-zion-integration.md",
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Dedicated Zion Integration Guide (plans, invoices, webhooks lifecycle) with consistent Zion/ZION casing.",
            notes="API category capitalized as ZION.",
        ),
        Product(
            name="Dynamic Currency Conversion / International Payments",
            category="Offerings / International",
            product_type="Payment Feature",
            overview="docs/Offerings/introduction-dynamic-currency-conversion/index.md",
            integration_guide="docs/Offerings/introduction-dynamic-currency-conversion/payu-hosted-checkout-integration-dynamic-currency-conversion.md",
            api_reference="reference/international payments",
            sdk=None,
            quick_start="docs/Offerings/introduction-dynamic-currency-conversion/dynamic-currency-conversion-workflow.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs="docs/Offerings/introduction-dynamic-currency-conversion/faqs-dynamic-currency-conversion.md",
            changelog=None,
            applicable={"sdk": False, "changelog": False, "webhooks": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Unify DCC vs International Payments naming; clarify MCP (multi-currency pricing) vs MCP (Model Context Protocol) collision in docs IA.",
            notes="MCP Lookup API under international payments. ASK AI single-mid-for-mcc-merchants-flow is related.",
        ),
        Product(
            name="Cross-Border Payments Import (PACB)",
            category="Offerings / International",
            product_type="Core Payment Product",
            overview="docs/Offerings/introduction-cross-border-payments-import/index.md",
            integration_guide="docs/Offerings/introduction-cross-border-payments-import/integrate-cross-border-payments-for-payubiz/index.md"
            if exists(
                "docs/Offerings/introduction-cross-border-payments-import/integrate-cross-border-payments-for-payubiz/index.md"
            )
            else "docs/Offerings/introduction-cross-border-payments-import/index.md",
            api_reference="reference/Cross-border Payments",
            sdk=None,
            quick_start="docs/Offerings/introduction-cross-border-payments-import/workflow-for-cross-border-payments-import.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs="docs/Offerings/introduction-cross-border-payments-import/faqs-for-cross-border-payments.md",
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="Dedicated Integration Guide covering card/UPI/NB, LRS, virtual accounts, subscriptions-CB, and onboarding; standardize CB/PACB/Import naming.",
            notes="Sub-products: LRS, CB subscriptions, virtual accounts, merchant onboarding APIs.",
        ),
        Product(
            name="EFTNET / NEFT-RTGS Collect",
            category="Offerings",
            product_type="Payment Feature",
            overview="docs/Offerings/introduction-to-eftnet/index.md",
            integration_guide="docs/Offerings/introduction-to-eftnet/payu-hosted-checkout-eftnet.md",
            api_reference="reference/Collect Payment",
            sdk=None,
            quick_start="docs/Offerings/introduction-to-eftnet/collect-payments-with-eftnet-neftrtgs-seamless.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False, "webhooks": False},
            recommend_ig=False,
            priority="P2",
            recommended_action="Clarify Collect EFTNET vs Payouts Dashboard EFTNET funding feature.",
            notes="Also appears under payouts/payouts-dashboard/eftnet.md.",
        ),
        Product(
            name="Pre-Authorize / Auth & Capture",
            category="Offerings",
            product_type="Payment Feature",
            overview="docs/Offerings/auth-and-capture-pre-authorize-card-payments/index.md",
            integration_guide="docs/Offerings/auth-and-capture-pre-authorize-card-payments/pre-authorize-card-transactions/index.md"
            if exists(
                "docs/Offerings/auth-and-capture-pre-authorize-card-payments/pre-authorize-card-transactions/index.md"
            )
            else "docs/Offerings/auth-and-capture-pre-authorize-card-payments/index.md",
            api_reference="reference/Pre-Authorize Payment",
            sdk=None,
            quick_start="docs/Offerings/auth-and-capture-pre-authorize-card-payments/index.md",
            webhooks=None,
            error_codes="reference/Pre-Authorize Payment/error-codes-pre-authorize-payment.md",
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Integration Guide for card pre-auth + capture/cancel with S2S variant.",
            notes="Includes UPI OTM under same parent folder.",
        ),
        Product(
            name="UPI One-Time Mandate (OTM / Reserve Pay)",
            category="Offerings",
            product_type="Payment Feature",
            overview="docs/Offerings/auth-and-capture-pre-authorize-card-payments/upi-one-time-mandate-integration/index.md",
            integration_guide="docs/Offerings/auth-and-capture-pre-authorize-card-payments/upi-one-time-mandate-integration/index.md",
            api_reference="reference/Pre-Authorize Payment/pre-authorize-payments-for-upi",
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes="reference/Pre-Authorize Payment/error-codes-pre-authorize-payment.md",
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Promote OTM to first-class Integration Guide; merge ASK AI upi-otm into canonical docs.",
            notes="Reserve Pay page under upi-one-time-mandate-integration.",
        ),
        Product(
            name="Split Settlements (Aggregator / Marketplace)",
            category="Offerings",
            product_type="Core Payment Product",
            overview="docs/Offerings/split-settlments/index.md",
            integration_guide="docs/Offerings/split-settlments/introduction-split-settlements/index.md"
            if exists("docs/Offerings/split-settlments/introduction-split-settlements/index.md")
            else "docs/Offerings/split-settlments/split-settlements-payment-integration.md",
            api_reference="reference/split settlements",
            sdk=None,
            quick_start="docs/Offerings/split-settlments/payu-hosted-integration-split-settlements",
            webhooks=None,
            error_codes="docs/Offerings/split-settlments/error-codes-for-refunds-status.md",
            testing="reference/split settlements/split_after_transaction_api/test-the-integration-split-after-transaction-1.md",
            go_live=None,
            troubleshooting=None,
            faqs="docs/Offerings/split-settlments/faqs-for-split-settlements.md",
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="Fix folder typo split-settlments; publish marketplace Integration Guide (parent/child onboarding → split during/after txn → refunds/settlements).",
            notes="ASK AI duplicate: split-settlements-aggregator.md. Strong API coverage with test pages.",
        ),
        Product(
            name="Tokenization / Save Cards (Vault)",
            category="Offerings",
            product_type="Payment Feature / Platform",
            overview="docs/Offerings/introduction-save-cards/index.md",
            integration_guide="docs/Offerings/introduction-save-cards/index.md",
            api_reference="reference/Tokenization",
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="Dedicated Integration Guide for Models 1–3 + push tokenization; critical for PCI-reducing integrations and recurring.",
            notes="Naming: Tokenization / Save Cards / Vault / Store Card across files.",
        ),
        Product(
            name="Third-Party Verification (TPV)",
            category="Offerings",
            product_type="Payment Feature",
            overview="docs/Offerings/introduction-to-payu-tpv/index.md",
            integration_guide="docs/Offerings/introduction-to-payu-tpv/collect-payments-with-tpv-payu-hosted-checkout/index.md"
            if exists(
                "docs/Offerings/introduction-to-payu-tpv/collect-payments-with-tpv-payu-hosted-checkout/index.md"
            )
            else "docs/Offerings/introduction-to-payu-tpv/index.md",
            api_reference="Partial",
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs="docs/Offerings/introduction-to-payu-tpv/faqs-tpv-integration.md",
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="Create TPV Integration Guide covering Hosted/MH/S2S/Payment Link/NEFT; consolidate dispersed API JSON (tpv-*.json) into reference IA; merge ASK AI guides.",
            notes="ASK AI: upi-net-banking-tpv-integration.md, payment-link-tpv-complete-guide.md. API specs dispersed.",
        ),
        Product(
            name="Recommendation Engine",
            category="Offerings",
            product_type="Platform / Payment Feature",
            overview="docs/Offerings/recommendation-engine/index.md",
            integration_guide="docs/Offerings/recommendation-engine/fetch-recommendation-engine-api.md",
            api_reference="docs/Offerings/recommendation-engine/fetch-recommendation-engine-api.md",
            sdk=None,
            quick_start="docs/Offerings/recommendation-engine/re-customer-journey.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "webhooks": False, "changelog": False},
            recommend_ig=False,
            priority="P2",
            recommended_action="Document CheckoutPro/CommercePro embedding paths; light Integration Guide optional.",
            notes="Also embedded in CheckoutPro SDKs.",
        ),
        Product(
            name="Native OTP Flow",
            category="Offerings",
            product_type="Payment Feature",
            overview="docs/Offerings/native-otp-flow-integration/index.md",
            integration_guide="docs/Offerings/native-otp-flow-integration/collect-payments-with-card-native-otp-flow.md",
            api_reference="reference/Collect Payment/native-otp-flow-apis",
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Clarify Native OTP Flow (web/API) vs Native OTP Assist mobile SDKs; ship Integration Guide for card/debit/cardless EMI.",
            notes="Separate from Android/iOS Native OTP Assist SDKs.",
        ),
        Product(
            name="Apple Pay",
            category="Offerings",
            product_type="Partner Payment Method",
            overview="docs/Offerings/apple-pay-integration/index.md",
            integration_guide="docs/Offerings/apple-pay-integration/prerequisites-and-set-up-for-apple-pay-integration.md",
            api_reference="reference/Apple Pay",
            sdk=None,
            quick_start="docs/Offerings/apple-pay-integration/apple-pay-integration-payu-hosted-checkout.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Keep prerequisites + Hosted/MH/session/UI as one Integration Guide with Apple certification/testing steps.",
            notes="Session management and UI seamless pages exist.",
        ),
        Product(
            name="Account Funding Transaction (AFT)",
            category="Offerings",
            product_type="Payment Feature",
            overview="docs/Offerings/account-funding-transaction-integration/index.md",
            integration_guide="docs/Offerings/account-funding-transaction-integration/collection-payments-with-account-funding-transaction.md",
            api_reference="reference/Collect Payment/_payment_merchant_hosted/_payment_api_merchant_hosted_aft.md",
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False, "webhooks": False},
            recommend_ig=False,
            priority="P2",
            recommended_action="Add compliance notes and testing guidance; dedicated IG only if adoption rises.",
            notes="Thin but present guide + API.",
        ),
        Product(
            name="Mutual Fund Payments (WealthTech)",
            category="Offerings",
            product_type="Partner / Vertical Product",
            overview="docs/Offerings/mutual-funds-payments/index.md",
            integration_guide="docs/Offerings/mutual-funds-payments/payu-hosted-integration-mutual-funds-payment.md",
            api_reference="reference/Wealth Tech",
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Align Mutual Fund Payments guide naming with Wealth Tech API category; Integration Guide covering eNACH + UPI AutoPay.",
            notes="Hosted, MH, eNACH, UPI AutoPay pages present.",
        ),
        Product(
            name="Merchant Wallet",
            category="Offerings",
            product_type="Core Payment Product",
            overview="docs/Offerings/introduction-to-merchant-wallet/index.md",
            integration_guide="docs/Offerings/introduction-to-merchant-wallet/closed-loop-wallet-management/index.md",
            api_reference="reference/Merchant Wallet",
            sdk=None,
            quick_start=None,
            webhooks="Partial",
            error_codes="Partial",
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Integration Guides for Closed-Loop vs Open/Semi-Closed issuance journeys; document callbacks/status codes clearly.",
            notes="Closed-loop and open-loop API folders under Merchant Wallet.",
        ),
        Product(
            name="Virtual Cards / GPR Cards",
            category="Offerings",
            product_type="Partner Product",
            overview="docs/Offerings/virtual-cards-introduction/index.md",
            integration_guide="docs/Offerings/virtual-cards-introduction/web-integration-virtual-cards/index.md"
            if exists("docs/Offerings/virtual-cards-introduction/web-integration-virtual-cards/index.md")
            else "docs/Offerings/virtual-cards-introduction/apis-used-in-virtual-cards-integration.md",
            api_reference="docs/Offerings/virtual-cards-introduction/apis-used-in-virtual-cards-integration.md",
            sdk="docs/Offerings/virtual-cards-introduction/virtual-card-integration-in-android.md",
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"changelog": False},
            recommend_ig=True,
            priority="P2",
            recommended_action="One Integration Guide with web + mobile SDK matrix; promote API map to reference section.",
            notes="Android/iOS/Flutter/RN SDK guides exist under virtual-cards-introduction.",
        ),
        Product(
            name="Refunds",
            category="Offerings",
            product_type="Payment Feature",
            overview="docs/Offerings/introduction-refunds/index.md",
            integration_guide="docs/Offerings/introduction-refunds/index.md",
            api_reference="reference/General/refund-apis",
            sdk=None,
            quick_start=None,
            webhooks="docs/Offerings/introduction-refunds/webhooks-for-refunds.md",
            error_codes="reference/General/refund-apis/error-codes-for-refund-initiation.md",
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs="docs/Offerings/introduction-refunds/faqs-for-refunds.md",
            changelog=None,
            applicable={"sdk": False, "changelog": False, "integration_guide": False},
            recommend_ig=False,
            priority="P1",
            recommended_action="Keep API + webhooks + product-specific refund pages strong; cross-link from every collect product. Dedicated IG not needed beyond current structure.",
            notes="Product-specific refunds documented under refunds-in-payu-products. ASK AI refund.md duplicate.",
        ),
        Product(
            name="Chargebacks",
            category="Offerings",
            product_type="Payment Feature",
            overview="docs/Offerings/chargeback/index.md",
            integration_guide=None,
            api_reference="reference/Chargeback",
            sdk=None,
            quick_start=None,
            webhooks="docs/Offerings/chargeback/webhooks-for-chargeback",
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "integration_guide": False, "changelog": False, "quick_start": False},
            recommend_ig=False,
            priority="P2",
            recommended_action="Add FAQs and operational runbooks; Integration Guide not required (ops/API product).",
            notes="Process, types, statuses, reasons, dashboard, webhooks present.",
        ),
        Product(
            name="Rewards / RewardX Partner Integration",
            category="Offerings",
            product_type="Partner Payment Feature",
            overview="docs/Offerings/rewards-partner-integration/index.md",
            integration_guide="docs/Offerings/rewards-partner-integration/rewards-pay-redemption-integration.md",
            api_reference="reference/REWARD PARTNERS",
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P2",
            recommended_action="Consolidate RewardX, Pay with Rewards/TWID, and Flipkart SuperCoins IA to reduce duplication.",
            notes="Overlaps with reference/Pay with rewards and Flipkart supercoins.",
        ),
        Product(
            name="Banking Connect (IBMB / NBBL)",
            category="Offerings",
            product_type="Partner Payment Feature",
            overview="docs/Offerings/banking-connect-ibmb-or-nbbl/index.md",
            integration_guide="docs/Offerings/banking-connect-ibmb-or-nbbl/payu-hosted-customer-journey-banking-connect.md",
            api_reference=None,
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "api_reference": True, "changelog": False, "webhooks": False},
            recommend_ig=False,
            priority="P3",
            recommended_action="Docs appear hidden/limited; expand when product is generally available.",
            notes="NBBL overview present. Naming: Banking Connect / IBMB / NBBL.",
        ),
        Product(
            name="Pluxee Card (Sodexo)",
            category="Collect Payments / Payment Methods",
            product_type="Partner Payment Method",
            overview="docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/integrate-with-merchant-hosted-checkout-for-pluxee-card.md",
            integration_guide="docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/integrate-with-merchant-hosted-checkout-for-pluxee-card.md",
            api_reference="reference/Sodexo",
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False, "webhooks": False},
            recommend_ig=False,
            priority="P3",
            recommended_action="Rename Sodexo reference to Pluxee; keep as method page under Merchant Hosted.",
            notes="Brand Pluxee vs legacy Sodexo API category.",
        ),
    ]
    products.extend(offerings)

    # -------------------------------------------------------------------------
    # Payouts
    # -------------------------------------------------------------------------
    products.append(
        Product(
            name="PayU Payouts",
            category="Payouts",
            product_type="Core Payment Product",
            overview="docs/payouts/introduction-to-payouts.md",
            integration_guide="docs/payouts/payouts-integration/single-transfer-integration-for-payouts.md",
            api_reference="reference/payouts",
            sdk=None,
            quick_start="docs/payouts/process-flow-for-payouts.md",
            webhooks="docs/payouts/payouts-integration/payouts-webhooks.md",
            error_codes="reference/payouts/error-codes-for-payouts.md",
            testing="docs/payouts/test-credentials-for-payouts.md",
            go_live=None,
            troubleshooting=None,
            faqs="docs/payouts/faqs-for-payouts.md",
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="Elevate Single Transfer + Smart Send + Beneficiary + Webhooks into a master Payouts Integration Guide with go-live; remove releasepending- filename residue from Pay to Phone.",
            notes="Sub-features: Smart Send, Pay to Phone, Bulk, Beneficiary, Verification, Partner Onboarding, MCP tools. Custom page duplicate: custom_pages/payouts-introduction.md.",
        )
    )
    products.append(
        Product(
            name="Smart Send",
            category="Payouts",
            product_type="Payment Feature",
            overview="docs/payouts/payouts-integration/smart-send-introduction/index.md",
            integration_guide="docs/payouts/payouts-integration/smart-send-introduction/index.md",
            api_reference="reference/payouts/smart-send-apis",
            sdk=None,
            quick_start=None,
            webhooks="docs/payouts/payouts-integration/payouts-webhooks.md",
            error_codes="reference/payouts/smart-send-apis/smart-send-error-codes.md",
            testing="docs/payouts/test-credentials-for-payouts.md",
            go_live=None,
            troubleshooting=None,
            faqs="docs/payouts/faqs-for-payouts.md",
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=False,
            priority="P1",
            recommended_action="Keep as chapter of Payouts IG rather than separate IG.",
            notes="Error codes present under smart-send-apis.",
        )
    )
    products.append(
        Product(
            name="Pay to Phone",
            category="Payouts",
            product_type="Payment Feature",
            overview="docs/payouts/releasepending-pay-to-phone-integration/index.md"
            if exists("docs/payouts/releasepending-pay-to-phone-integration/index.md")
            else "docs/payouts/releasepending-pay-to-phone-integration/releasepending-pay-to-phone-initiation.md",
            integration_guide="docs/payouts/releasepending-pay-to-phone-integration/releasepending-pay-to-phone-initiation.md",
            api_reference="reference/payouts/releasepending-pay-to-phone-configuration-apis",
            sdk=None,
            quick_start=None,
            webhooks="docs/payouts/payouts-integration/payouts-webhooks.md",
            error_codes="reference/payouts/error-codes-for-payouts.md",
            testing="docs/payouts/test-credentials-for-payouts.md",
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Rename releasepending- paths; complete Integration Guide for initiation/tracking/configuration.",
            notes="Editorial residue in filenames (releasepending-).",
        )
    )

    # -------------------------------------------------------------------------
    # Partners
    # -------------------------------------------------------------------------
    products.append(
        Product(
            name="PayU Partner Program & Portal",
            category="Partners",
            product_type="Partner Product / Platform",
            overview="docs/partners/payu-partner-program-overview.md",
            integration_guide=None,
            api_reference=None,
            sdk=None,
            quick_start="docs/partners/partner-portal/index.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs="docs/partners/faqs-partner-integration.md",
            changelog=None,
            applicable={
                "integration_guide": False,
                "api_reference": False,
                "sdk": False,
                "webhooks": False,
                "error_codes": False,
                "changelog": False,
            },
            recommend_ig=False,
            priority="P2",
            recommended_action="Keep portal how-tos current; link to API onboarding guides.",
            notes="Incentives, referral links, portal user management documented.",
        )
    )
    products.append(
        Product(
            name="Partner Merchant Onboarding (API / OAuth)",
            category="Partners",
            product_type="Partner Product",
            overview="docs/partners/internal-reviewpartner-integration-overview/index.md"
            if exists("docs/partners/internal-reviewpartner-integration-overview/index.md")
            else "docs/partners/refer-merchants-using-api.md",
            integration_guide="docs/partners/internal-reviewpartner-integration-overview/quick-start-partner-integration.md",
            api_reference="reference/ParTner integration",
            sdk=None,
            quick_start="docs/partners/internal-reviewpartner-integration-overview/quick-start-partner-integration.md",
            webhooks="reference/ParTner integration/using-webhooks-for-merchant-status",
            error_codes="reference/ParTner integration/using-webhooks-for-merchant-status/kyc-errors-and-solutions.md",
            testing="docs/partners/internal-reviewpartner-integration-overview/testing-and-go-live-partner-integration.md",
            go_live="docs/partners/internal-reviewpartner-integration-overview/testing-and-go-live-partner-integration.md",
            troubleshooting="docs/partners/internal-reviewpartner-integration-overview/errors-and-troubleshooting-partner-integration.md",
            faqs="docs/partners/faqs-partner-integration.md",
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P0",
            recommended_action="Finalize internal-review partner overview as canonical Integration Guide; merge duplicate Partner Integration - Merchant Onboarding APIs tree; fix ParTner folder casing.",
            notes="Parallel API trees: ParTner integration vs Partner Integration - Merchant Onboarding APIs (16-step). Co-branded OAuth has its own folder.",
        )
    )
    products.append(
        Product(
            name="Partner Payments Integration",
            category="Partners",
            product_type="Partner Product",
            overview="docs/partners/partner-payments-integration.md",
            integration_guide="docs/partners/partner-payments-integration.md",
            api_reference="reference/ParTner integration/partner-payment-integration-apis",
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs="docs/partners/faqs-partner-integration.md",
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Expand Integration Guide for Hosted/UPI S2S/UPI TPV/refunds partner flows.",
            notes="Payment APIs under partner-payment-integration-apis.",
        )
    )

    # -------------------------------------------------------------------------
    # WhatsApp, BBPS, MCP/CLI, Monitoring, Air India
    # -------------------------------------------------------------------------
    products.append(
        Product(
            name="WhatsApp Payments",
            category="WhatsApp Integration",
            product_type="Partner / Integration Channel",
            overview="docs/Whatsapp integration/whatsapp-integration-introduction.md",
            integration_guide="docs/Whatsapp integration/whatsapp-native-payments/index.md",
            api_reference=None,
            sdk=None,
            quick_start="docs/Whatsapp integration/whatsapp-native-payments/integrate-whatsapp-payments-p2m-or-up-intent.md"
            if exists(
                "docs/Whatsapp integration/whatsapp-native-payments/integrate-whatsapp-payments-p2m-or-up-intent.md"
            )
            else None,
            webhooks=WEB_WEBHOOKS,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "api_reference": True, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Dedicated Integration Guide for Native P2M + Enhanced Payment Links; clarify Interakt plugin boundary.",
            notes="Includes Enhanced Payment Links on WhatsApp page.",
        )
    )
    products.append(
        Product(
            name="BBPS Connect Agent",
            category="BBPS",
            product_type="Core / Partner Product",
            overview="docs/BBPS/connect-agent-api-integration/index.md",
            integration_guide="docs/BBPS/connect-agent-api-integration/bbps-integration-flow.md",
            api_reference="reference/BBPS",
            sdk=None,
            quick_start="docs/BBPS/connect-agent-api-integration/bbps-integration-flow.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Expand Integration Guide with auth, bill fetch/pay, complaints, sandbox, error catalog.",
            notes="Rich API reference under reference/BBPS.",
        )
    )
    products.append(
        Product(
            name="BBPS Prepaid Recharge",
            category="BBPS",
            product_type="Payment Feature",
            overview="docs/BBPS/recharge-api-integration/index.md",
            integration_guide="docs/BBPS/recharge-api-integration/prepaid-recharge-workflow.md",
            api_reference="reference/BBPS/bbps-prepaid-apis",
            sdk=None,
            quick_start="docs/BBPS/recharge-api-integration/prepaid-recharge-workflow.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"sdk": False, "changelog": False},
            recommend_ig=False,
            priority="P2",
            recommended_action="Keep as chapter of BBPS IG; add testing/errors.",
            notes="Workflow + prepaid APIs present.",
        )
    )
    products.append(
        Product(
            name="PayU Remote MCP Server",
            category="MCP & CLI",
            product_type="Platform / Tool",
            overview="docs/MCP & CLI/payu-remote-mcp-server-integration.md",
            integration_guide="docs/MCP & CLI/payu-remote-mcp-server-integration.md",
            api_reference=None,
            sdk=None,
            quick_start="docs/MCP & CLI/payu-remote-mcp-server-integration.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"api_reference": False, "sdk": False, "webhooks": False, "error_codes": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Treat current page as Integration Guide seed; add tool catalog, auth (OAuth 2.1), examples, troubleshooting. Disambiguate MCP acronym from Multi-Currency Pricing.",
            notes="Single-page today. Distinct from payouts/mcp-tools.md.",
        )
    )
    products.append(
        Product(
            name="PayU CLI",
            category="MCP & CLI",
            product_type="Platform / Tool",
            overview="docs/MCP & CLI/payu-cli.md",
            integration_guide="docs/MCP & CLI/payu-cli.md",
            api_reference=None,
            sdk=None,
            quick_start="docs/MCP & CLI/payu-cli.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={
                "api_reference": False,
                "sdk": False,
                "webhooks": False,
                "error_codes": False,
                "changelog": False,
            },
            recommend_ig=False,
            priority="P2",
            recommended_action="Expand command reference and examples; dedicated IG optional.",
            notes="Install/config/commands on single page.",
        )
    )
    products.append(
        Product(
            name="PayU Devguide Builder MCP",
            category="MCP & CLI",
            product_type="Platform / Tool (Internal Docs)",
            overview="docs/MCP & CLI/payu-devguide-builder-mcp-configuration.md",
            integration_guide="docs/MCP & CLI/payu-devguide-builder-mcp-configuration.md",
            api_reference=None,
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={
                "api_reference": False,
                "sdk": False,
                "webhooks": False,
                "error_codes": False,
                "testing": False,
                "go_live": False,
                "faqs": False,
                "changelog": False,
            },
            recommend_ig=False,
            priority="P3",
            recommended_action="Internal docs tooling — maintain configuration page only.",
            notes="Documentation authoring tooling, not merchant-facing product.",
        )
    )
    products.append(
        Product(
            name="Agentic Commerce Suite",
            category="MCP & CLI",
            product_type="Platform / Partner Product",
            overview="docs/MCP & CLI/agentic-commerce/index.md",
            integration_guide="docs/MCP & CLI/agentic-commerce/build-your-own-chatgpt-merchant-app.md",
            api_reference=None,
            sdk=None,
            quick_start="docs/MCP & CLI/agentic-commerce/build-your-own-chatgpt-merchant-app.md",
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={"api_reference": True, "sdk": False, "changelog": False},
            recommend_ig=True,
            priority="P1",
            recommended_action="Emerging DevEx surface — invest in Integration Guide covering ChatGPT merchant app and agent-compatible checkout.",
            notes="Overview includes AI-app commerce, WhatsApp commerce, merchant-owned assistants.",
        )
    )
    products.append(
        Product(
            name="PayU Overwatch (Monitoring & Alerts)",
            category="Monitoring & Alerts",
            product_type="Platform / Tool",
            overview="docs/Monitoring & Alerts/payu-monitoring-alerts-overwatch/index.md",
            integration_guide=None,
            api_reference=None,
            sdk=None,
            quick_start=None,
            webhooks="docs/Monitoring & Alerts/payu-monitoring-alerts-overwatch/webhook-alerts.md",
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={
                "integration_guide": False,
                "api_reference": False,
                "sdk": False,
                "error_codes": False,
                "changelog": False,
                "quick_start": False,
            },
            recommend_ig=False,
            priority="P2",
            recommended_action="Add setup guide and alert catalog; IG not required.",
            notes="Webhook alerts documented.",
        )
    )
    products.append(
        Product(
            name="Air India Checkout API Suite",
            category="Merchant-Specific",
            product_type="Partner / Merchant-Specific",
            overview="docs/AIR India/air-india-integration-apis.md",
            integration_guide=None,
            api_reference="docs/AIR India",
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={
                "sdk": False,
                "integration_guide": False,
                "webhooks": False,
                "changelog": False,
                "faqs": False,
            },
            recommend_ig=False,
            priority="P3",
            recommended_action="Keep merchant-specific; do not generalize into public product catalog without product decision.",
            notes="Hidden merchant-specific APIs (order, offers, EMI, capture, refund).",
        )
    )
    products.append(
        Product(
            name="Settlements / Priority Settlements",
            category="Getting Started / Dashboard",
            product_type="Payment Feature / Platform",
            overview="docs/getting started/payu-dashboard/settlements-dashboard/index.md"
            if exists("docs/getting started/payu-dashboard/settlements-dashboard/index.md")
            else "docs/getting started/payu-dashboard/settlements-dashboard/priority-settlements.md",
            integration_guide=None,
            api_reference="reference/Settlements",
            sdk=None,
            quick_start=None,
            webhooks=None,
            error_codes=None,
            testing=None,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={
                "sdk": False,
                "integration_guide": False,
                "webhooks": False,
                "changelog": False,
            },
            recommend_ig=False,
            priority="P2",
            recommended_action="Improve API + dashboard cross-links; Priority Settlements page should link Settlements APIs.",
            notes="Settlement APIs: transaction details, date range, upcoming, release.",
        )
    )
    products.append(
        Product(
            name="General Utility APIs (Verify / BIN / Health / Bank Verification)",
            category="API Basics / Utilities",
            product_type="Utility",
            overview="docs/API basics/rest-api-format.md",
            integration_guide=None,
            api_reference="reference/General",
            sdk=None,
            quick_start="docs/API basics/api-authentication-and-security.md",
            webhooks=WEB_WEBHOOKS,
            error_codes=WEB_ERROR_REF,
            testing=WEB_TESTING,
            go_live=None,
            troubleshooting=None,
            faqs=None,
            changelog=None,
            applicable={
                "sdk": False,
                "integration_guide": False,
                "changelog": False,
                "go_live": False,
            },
            recommend_ig=False,
            priority="P1",
            recommended_action="Do not create product IG; instead improve discoverability from checkout IGs (verify payment, BIN, health check).",
            notes="Includes check-transaction, transaction-detail, bin, get_checkout_details, health-check, bank-verification APIs. Hash tool under API basics.",
        )
    )

    # Validate paths lightly — mark missing explicit paths as None already handled by flag()
    return products

# ---------------------------------------------------------------------------
# Lean workbook (feedback: less noise, less clutter, clear prioritization)
# ---------------------------------------------------------------------------

FILL_HEADER = PatternFill("solid", fgColor="0B3D5C")
FILL_GREEN = PatternFill("solid", fgColor="C6EFCE")
FILL_YELLOW = PatternFill("solid", fgColor="FFEB9C")
FILL_RED = PatternFill("solid", fgColor="FFC7CE")
FILL_GREY = PatternFill("solid", fgColor="F2F2F2")
FILL_P0 = PatternFill("solid", fgColor="C00000")
FILL_P1 = PatternFill("solid", fgColor="FFC000")
FILL_P2 = PatternFill("solid", fgColor="548235")
FILL_P3 = PatternFill("solid", fgColor="808080")
FILL_TITLE = PatternFill("solid", fgColor="072A40")
FILL_KPI = PatternFill("solid", fgColor="E8F4FC")
FILL_ALT = PatternFill("solid", fgColor="F7F9FB")

FONT_HEADER = Font(name="Calibri", bold=True, color="FFFFFF", size=11)
FONT_TITLE = Font(name="Calibri", bold=True, color="FFFFFF", size=16)
FONT_SECTION = Font(name="Calibri", bold=True, color="0B3D5C", size=12)
FONT_KPI = Font(name="Calibri", bold=True, color="0B3D5C", size=18)
FONT_BODY = Font(name="Calibri", size=10)
FONT_BOLD = Font(name="Calibri", bold=True, size=10)

THIN = Border(
    left=Side(style="thin", color="B0B0B0"),
    right=Side(style="thin", color="B0B0B0"),
    top=Side(style="thin", color="B0B0B0"),
    bottom=Side(style="thin", color="B0B0B0"),
)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(wrap_text=True, vertical="center", horizontal="center")

# Explicit ranking weights (documented in workbook)
PRIORITY_TIER_WEIGHT = {"P0": 1000, "P1": 700, "P2": 400, "P3": 100}

# Business-criticality boost for core payment journey / high-revenue surfaces
CORE_JOURNEY_BOOST = {
    "PayU Hosted Checkout (Prebuilt)": 50,
    "Merchant Hosted Checkout (Custom / Seamless)": 50,
    "Server-to-Server (S2S) Checkout": 48,
    "Payment Links": 45,
    "Checkout Plus (ICP / Bolt Checkout)": 42,
    "Android CheckoutPro SDK": 40,
    "iOS CheckoutPro SDK": 40,
    "Subscriptions / Recurring Payments": 45,
    "PayU Payouts": 45,
    "Partner Merchant Onboarding (API / OAuth)": 42,
    "Tokenization / Save Cards (Vault)": 40,
    "Third-Party Verification (TPV)": 40,
    "Split Settlements (Aggregator / Marketplace)": 38,
    "Cross-Border Payments Import (PACB)": 38,
    "EMI / Cardless EMI": 35,
    "Offer Engine / Offers": 35,
}


def missing_critical(p: Product) -> str:
    """Short list of highest-value missing dimensions only."""
    critical = [
        ("Overview", "overview"),
        ("Integration Guide", "integration_guide"),
        ("API Reference", "api_reference"),
        ("Testing", "testing"),
        ("Go Live", "go_live"),
        ("Webhooks", "webhooks"),
        ("Error Codes", "error_codes"),
        ("Troubleshooting", "troubleshooting"),
        ("FAQs", "faqs"),
    ]
    missing = []
    for label, dim in critical:
        if p.flag(dim) == "No":
            missing.append(label)
    return ", ".join(missing[:5]) if missing else "—"


def why_prioritized(p: Product) -> str:
    reasons = []
    if p.priority == "P0":
        reasons.append("P0: core journey / high support dependency")
    elif p.priority == "P1":
        reasons.append("P1: high DevEx or vertical revenue impact")
    elif p.priority == "P2":
        reasons.append("P2: useful later; lower urgency")
    else:
        reasons.append("P3: niche / maintain only")

    if p.recommend_ig:
        reasons.append("needs dedicated Integration Guide")
    cov = p.coverage_score()
    if cov < 55:
        reasons.append(f"large doc gap ({cov}% coverage)")
    elif cov < 75:
        reasons.append(f"moderate doc gap ({cov}% coverage)")

    if any(k in p.name for k in ["S2S", "TPV", "Partner", "Subscriptions", "Tokenization", "Split", "Cross-Border"]):
        reasons.append("high developer complexity")
    if p.name in CORE_JOURNEY_BOOST:
        reasons.append("core payment / revenue surface")
    return "; ".join(reasons)


def ranking_basis_text() -> list[str]:
    return [
        "Products are ranked by a Priority Score (higher = do sooner).",
        "",
        "Priority Score = Tier weight + Gap severity + Core-journey boost + IG need + Complexity signal",
        "",
        "1) Tier weight (primary): P0=1000, P1=700, P2=400, P3=100",
        "   Assigned from: merchant adoption, core payment journey, business/revenue impact,",
        "   developer complexity, support dependency, existing doc gaps, DevEx impact.",
        "",
        "2) Gap severity: (100 − Coverage%) × 2",
        "   Lower coverage rises within the same tier so incomplete critical docs surface first.",
        "",
        "3) Core-journey boost (0–50): Hosted/MH/S2S, Payment Links, mobile CheckoutPro,",
        "   Subscriptions, Payouts, Partner Onboarding, Tokenization, TPV, Split Settlements,",
        "   Cross-Border, EMI, Offers.",
        "",
        "4) Integration Guide need: +30 if a dedicated IG is recommended; else 0",
        "",
        "5) Complexity signal: +20 if product is inherently hard to integrate without support",
        "   (S2S, TPV, Partner, Subscriptions, Tokenization, Split, Cross-Border).",
        "",
        "Coverage % itself is equal-weight across applicable dimensions:",
        "Overview, Integration Guide, API Reference, SDK, Quick Start, Webhooks, Error Codes,",
        "Testing, Go Live, Troubleshooting, FAQs, Changelog (N/A excluded).",
        "Yes=1, Partial=0.5, No=0. Status: Complete≥85%, Partial 40–84.9%, Missing<40%.",
    ]


def priority_score(p: Product) -> float:
    tier = PRIORITY_TIER_WEIGHT.get(p.priority, 0)
    gap = (100.0 - p.coverage_score()) * 2.0
    core = CORE_JOURNEY_BOOST.get(p.name, 0)
    ig = 30 if p.recommend_ig else 0
    complex_names = ("S2S", "TPV", "Partner", "Subscriptions", "Tokenization", "Split", "Cross-Border")
    complexity = 20 if any(k in p.name for k in complex_names) else 0
    return tier + gap + core + ig + complexity


def apply_status_fill(cell):
    v = str(cell.value or "").strip()
    if v == "Complete":
        cell.fill = FILL_GREEN
    elif v == "Partial":
        cell.fill = FILL_YELLOW
    elif v == "Missing":
        cell.fill = FILL_RED
    cell.alignment = CENTER
    cell.border = THIN
    cell.font = FONT_BODY


def apply_priority_fill(cell):
    v = str(cell.value or "").strip()
    if v == "P0":
        cell.fill = FILL_P0
        cell.font = Font(name="Calibri", bold=True, size=10, color="FFFFFF")
    elif v == "P1":
        cell.fill = FILL_P1
        cell.font = Font(name="Calibri", bold=True, size=10)
    elif v == "P2":
        cell.fill = FILL_P2
        cell.font = Font(name="Calibri", bold=True, size=10, color="FFFFFF")
    elif v == "P3":
        cell.fill = FILL_P3
        cell.font = Font(name="Calibri", bold=True, size=10, color="FFFFFF")
    else:
        cell.font = FONT_BODY
    cell.alignment = CENTER
    cell.border = THIN


def style_header(ws, row, cols):
    for c in range(1, cols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill = FILL_HEADER
        cell.font = FONT_HEADER
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        cell.border = THIN


def autosize(ws, widths: dict[str, float]):
    for letter, width in widths.items():
        ws.column_dimensions[letter].width = width


def build_workbook(products: list[Product]) -> Workbook:
    wb = Workbook()

    ranked = sorted(
        products,
        key=lambda p: (-priority_score(p), p.coverage_score(), p.name),
    )

    total = len(products)
    complete = sum(1 for p in products if p.status() == "Complete")
    partial = sum(1 for p in products if p.status() == "Partial")
    missing = sum(1 for p in products if p.status() == "Missing")
    avg_cov = round(sum(p.coverage_score() for p in products) / total, 1) if total else 0
    p0 = [p for p in ranked if p.priority == "P0"]
    p1 = [p for p in ranked if p.priority == "P1"]

    # =========================================================================
    # Sheet 1 — Executive Summary (lean)
    # =========================================================================
    ws = wb.active
    ws.title = "Executive Summary"

    ws.merge_cells("A1:F1")
    ws["A1"] = "PayU Product Docs Coverage — Executive Summary"
    ws["A1"].font = FONT_TITLE
    ws["A1"].fill = FILL_TITLE
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:F2")
    ws["A2"] = (
        f"Repo-sourced · {datetime.now(timezone.utc).strftime('%Y-%m-%d')} UTC · "
        "Goal: developers integrate without support. "
        "Use 'Priority Ranked List' as the working queue."
    )
    ws["A2"].font = Font(name="Calibri", italic=True, size=10)
    ws["A2"].alignment = WRAP
    ws.row_dimensions[2].height = 30

    kpis = [
        ("Products", total),
        ("Avg Coverage", f"{avg_cov}%"),
        ("Complete", complete),
        ("Partial", partial),
        ("Missing", missing),
        ("P0 items", len(p0)),
    ]
    for i, (label, val) in enumerate(kpis):
        c = i + 1
        ws.cell(row=4, column=c, value=label).font = FONT_HEADER
        ws.cell(row=4, column=c).fill = FILL_HEADER
        ws.cell(row=4, column=c).alignment = CENTER
        ws.cell(row=4, column=c).border = THIN
        cell = ws.cell(row=5, column=c, value=val)
        cell.font = FONT_KPI
        cell.fill = FILL_KPI
        cell.alignment = CENTER
        cell.border = THIN

    ws["A7"] = "Top 10 priorities (start here)"
    ws["A7"].font = FONT_SECTION
    top_headers = ["Rank", "Product", "Priority", "Coverage %", "Why this is higher", "Action"]
    for c, h in enumerate(top_headers, 1):
        ws.cell(row=8, column=c, value=h)
    style_header(ws, 8, 6)

    for i, p in enumerate(ranked[:10], 1):
        r = 8 + i
        vals = [
            i,
            p.name,
            p.priority,
            p.coverage_score(),
            why_prioritized(p),
            p.recommended_action,
        ]
        for c, v in enumerate(vals, 1):
            cell = ws.cell(row=r, column=c, value=v)
            cell.border = THIN
            cell.font = FONT_BODY
            cell.alignment = WRAP if c >= 5 else CENTER
            if c == 2:
                cell.alignment = WRAP
        apply_priority_fill(ws.cell(row=r, column=3))
        ws.row_dimensions[r].height = 42

    ws["A20"] = "How priority was decided (short)"
    ws["A20"].font = FONT_SECTION
    short_basis = [
        "Higher rank = higher Priority Score.",
        "Order drivers: (1) P0→P3 tier from business/DevEx impact, (2) bigger documentation gaps within tier,",
        "(3) core payment/revenue surfaces boosted, (4) dedicated Integration Guide needed, (5) high complexity.",
        "Full formula and weights are on sheet: Scoring & Ranking Basis.",
    ]
    for i, line in enumerate(short_basis):
        ws.cell(row=21 + i, column=1, value=line).font = FONT_BODY
        ws.merge_cells(start_row=21 + i, start_column=1, end_row=21 + i, end_column=6)

    ws["A26"] = "Key gaps (portfolio)"
    ws["A26"].font = FONT_SECTION
    gaps = [
        "Go-Live and Changelog docs are rare across products.",
        "Troubleshooting is thin vs FAQs — support still absorbs diagnosis.",
        "Naming/duplicates add noise: Checkout Plus/ICP/Bolt; CommercePro/Express; Partner API trees; ASK AI shadow docs.",
        "Server SDK pages are too thin for zero-support first integration.",
    ]
    for i, g in enumerate(gaps):
        ws.cell(row=27 + i, column=1, value=f"• {g}").alignment = WRAP
        ws.merge_cells(start_row=27 + i, start_column=1, end_row=27 + i, end_column=6)
        ws.row_dimensions[27 + i].height = 28

    autosize(ws, {"A": 8, "B": 40, "C": 10, "D": 12, "E": 48, "F": 52})
    ws.freeze_panes = "A9"

    # =========================================================================
    # Sheet 2 — Priority Ranked List (hero sheet)
    # =========================================================================
    pr = wb.create_sheet("Priority Ranked List")
    pr.merge_cells("A1:I1")
    pr["A1"] = "Priority Ranked Product List — higher rank = do sooner"
    pr["A1"].font = FONT_TITLE
    pr["A1"].fill = FILL_TITLE
    pr.row_dimensions[1].height = 28

    pr.merge_cells("A2:I2")
    pr["A2"] = (
        "Sorted by Priority Score. See 'Scoring & Ranking Basis' for the formula. "
        "Focus on Rank 1–N where Priority is P0/P1 and Coverage is below 75%."
    )
    pr["A2"].font = Font(name="Calibri", italic=True, size=10)
    pr["A2"].alignment = WRAP

    headers = [
        "Rank",
        "Product",
        "Category",
        "Priority",
        "Coverage %",
        "Status",
        "Priority Score",
        "Why prioritized",
        "Recommended action",
    ]
    for c, h in enumerate(headers, 1):
        pr.cell(row=4, column=c, value=h)
    style_header(pr, 4, len(headers))
    pr.freeze_panes = "A5"
    pr.auto_filter.ref = f"A4:I{4 + len(ranked)}"

    for i, p in enumerate(ranked, 1):
        r = 4 + i
        vals = [
            i,
            p.name,
            p.category,
            p.priority,
            p.coverage_score(),
            p.status(),
            round(priority_score(p), 1),
            why_prioritized(p),
            p.recommended_action,
        ]
        for c, v in enumerate(vals, 1):
            cell = pr.cell(row=r, column=c, value=v)
            cell.border = THIN
            cell.font = FONT_BODY
            cell.alignment = WRAP if c in {2, 3, 8, 9} else CENTER
        apply_priority_fill(pr.cell(row=r, column=4))
        apply_status_fill(pr.cell(row=r, column=6))
        cov_cell = pr.cell(row=r, column=5)
        cov = p.coverage_score()
        if cov >= 85:
            cov_cell.fill = FILL_GREEN
        elif cov >= 40:
            cov_cell.fill = FILL_YELLOW
        else:
            cov_cell.fill = FILL_RED

    autosize(
        pr,
        {
            "A": 7,
            "B": 42,
            "C": 28,
            "D": 10,
            "E": 12,
            "F": 11,
            "G": 13,
            "H": 46,
            "I": 50,
        },
    )

    # =========================================================================
    # Sheet 3 — Product Inventory (slim)
    # =========================================================================
    inv = wb.create_sheet("Product Inventory")
    inv.merge_cells("A1:H1")
    inv["A1"] = "Product Inventory (slim)"
    inv["A1"].font = FONT_TITLE
    inv["A1"].fill = FILL_TITLE

    inv_headers = [
        "Product",
        "Category",
        "Type",
        "Coverage %",
        "Status",
        "Priority",
        "Missing critical docs",
        "Overview path",
    ]
    for c, h in enumerate(inv_headers, 1):
        inv.cell(row=3, column=c, value=h)
    style_header(inv, 3, len(inv_headers))
    inv.freeze_panes = "A4"
    inv.auto_filter.ref = f"A3:H{3 + len(products)}"

    # Keep inventory in rank order too (less cognitive jump)
    for i, p in enumerate(ranked, 1):
        r = 3 + i
        vals = [
            p.name,
            p.category,
            p.product_type,
            p.coverage_score(),
            p.status(),
            p.priority,
            missing_critical(p),
            p.link("overview") or "—",
        ]
        for c, v in enumerate(vals, 1):
            cell = inv.cell(row=r, column=c, value=v)
            cell.border = THIN
            cell.font = FONT_BODY
            cell.alignment = WRAP if c in {1, 2, 3, 7, 8} else CENTER
        apply_status_fill(inv.cell(row=r, column=5))
        apply_priority_fill(inv.cell(row=r, column=6))

    autosize(
        inv,
        {"A": 40, "B": 28, "C": 26, "D": 11, "E": 11, "F": 10, "G": 40, "H": 46},
    )

    # =========================================================================
    # Sheet 4 — Scoring & Ranking Basis
    # =========================================================================
    basis = wb.create_sheet("Scoring & Ranking Basis")
    basis.merge_cells("A1:B1")
    basis["A1"] = "Coverage Scoring & Priority Ranking — Basis"
    basis["A1"].font = FONT_TITLE
    basis["A1"].fill = FILL_TITLE
    basis.row_dimensions[1].height = 28

    basis["A3"] = "A. Priority ranking basis (what makes an item higher)"
    basis["A3"].font = FONT_SECTION
    for i, line in enumerate(ranking_basis_text()):
        basis.cell(row=4 + i, column=1, value=line).font = FONT_BODY
        basis.merge_cells(start_row=4 + i, start_column=1, end_row=4 + i, end_column=2)

    start = 4 + len(ranking_basis_text()) + 2
    basis.cell(row=start, column=1, value="B. Worked example — top ranked products").font = FONT_SECTION
    ex_headers = [
        "Rank",
        "Product",
        "Tier",
        "Gap pts",
        "Core boost",
        "IG pts",
        "Complexity",
        "Priority Score",
    ]
    for c, h in enumerate(ex_headers, 1):
        basis.cell(row=start + 1, column=c, value=h)
    style_header(basis, start + 1, len(ex_headers))

    for i, p in enumerate(ranked[:15], 1):
        r = start + 1 + i
        tier = PRIORITY_TIER_WEIGHT.get(p.priority, 0)
        gap = round((100.0 - p.coverage_score()) * 2.0, 1)
        core = CORE_JOURNEY_BOOST.get(p.name, 0)
        ig = 30 if p.recommend_ig else 0
        complex_names = ("S2S", "TPV", "Partner", "Subscriptions", "Tokenization", "Split", "Cross-Border")
        complexity = 20 if any(k in p.name for k in complex_names) else 0
        vals = [i, p.name, p.priority, gap, core, ig, complexity, round(priority_score(p), 1)]
        for c, v in enumerate(vals, 1):
            cell = basis.cell(row=r, column=c, value=v)
            cell.border = THIN
            cell.font = FONT_BODY
            cell.alignment = CENTER if c != 2 else WRAP
        apply_priority_fill(basis.cell(row=r, column=3))

    note_row = start + 18
    basis.cell(row=note_row, column=1, value="C. What we deliberately removed (noise reduction)").font = FONT_SECTION
    removed = [
        "Removed duplicate recommendation sheets (IG Prioritization + Executive Recommendations + Gap Analysis walls of text).",
        "Removed 30+ inventory link/flag columns — kept only decision-useful fields.",
        "Removed Repository Analysis / category charts / pie charts that did not change decisions.",
        "Coverage dimension breakdown is summarized via Coverage % + Missing critical docs instead of a wide matrix.",
    ]
    for i, line in enumerate(removed):
        basis.cell(row=note_row + 1 + i, column=1, value=f"• {line}").alignment = WRAP
        basis.merge_cells(
            start_row=note_row + 1 + i,
            start_column=1,
            end_row=note_row + 1 + i,
            end_column=8,
        )

    autosize(
        basis,
        {"A": 10, "B": 42, "C": 10, "D": 10, "E": 12, "F": 10, "G": 12, "H": 14},
    )
    basis.column_dimensions["A"].width = 12
    basis.column_dimensions["B"].width = 42

    return wb


def main():
    products = build_products()
    problems = []
    for p in products:
        for dim in DIMENSIONS:
            val = getattr(p, dim)
            if val and val not in {"Yes", "No", "Partial", "Shared", "N/A"}:
                if not (ROOT / val).exists():
                    problems.append(f"{p.name} :: {dim} :: {val}")
    if problems:
        print("WARNING: missing paths:")
        for pr in problems[:20]:
            print(" -", pr)
    else:
        print("All explicit paths resolve.")

    wb = build_workbook(products)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    wb.save(OUT_FILE)
    print(f"Wrote {OUT_FILE}")
    ranked = sorted(products, key=lambda p: (-priority_score(p), p.coverage_score(), p.name))
    print("Top 10 priorities:")
    for i, p in enumerate(ranked[:10], 1):
        print(f"  {i}. [{p.priority}] {p.name} — {p.coverage_score()}% — score {priority_score(p):.1f}")


if __name__ == "__main__":
    main()
