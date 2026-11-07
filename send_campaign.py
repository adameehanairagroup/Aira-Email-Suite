#!/usr/bin/env python3
"""
🚀 Aira Email Dispatcher & Automated Campaign System
Supports: noreply@airaaigroup.in & support@airaaigroup.in
Engineered for Er. Adam Eehan (Founder & CEO, Aira Group of Technology)
"""

import os
import sys
import argparse
from pathlib import Path

# Optional Resend integration
try:
    import resend
    RESEND_AVAILABLE = True
except ImportError:
    RESEND_AVAILABLE = False

TEMPLATES_DIR = Path(__file__).parent / "templates"
DEFAULT_RESEND_KEY = os.getenv("RESEND_API_KEY", "")

def render_template(template_name, context):
    """Loads an HTML template and replaces merge tags."""
    tpl_path = TEMPLATES_DIR / template_name
    if not tpl_path.exists():
        raise FileNotFoundError(f"Template not found: {tpl_path}")
    
    with open(tpl_path, "r", encoding="utf-8") as f:
        html = f.read()

    for k, v in context.items():
        html = html.replace(f"{{{{{k}}}}}", str(v))
    return html

def send_via_resend(from_email, to_email, subject, html_content, api_key=None):
    """Sends email via Resend API."""
    if not RESEND_AVAILABLE:
        print("[!] Resend library not installed. Run: pip install resend")
        return False

    resend.api_key = api_key or DEFAULT_RESEND_KEY
    try:
        params = {
            "from": from_email,
            "to": [to_email] if isinstance(to_email, str) else to_email,
            "subject": subject,
            "html": html_content
        }
        resp = resend.Emails.send(params)
        print(f"✅ [Resend] Dispatched successfully! ID: {resp.get('id')}")
        return True
    except Exception as e:
        print(f"❌ [Resend Error]: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Aira Automated Email Dispatcher")
    parser.add_argument("--type", choices=["ad", "support", "welcome"], default="ad", help="Campaign/template type")
    parser.add_argument("--to", default="delivered@resend.dev", help="Recipient email address")
    parser.add_argument("--name", default="Developer", help="Recipient first name")
    parser.add_argument("--subject", default=None, help="Custom subject line")
    parser.add_argument("--from-email", default=None, help="Sender email address")
    parser.add_argument("--preview", action="store_true", help="Render template to output.html without sending")
    args = parser.parse_args()

    context = {
        "FIRST_NAME": args.name,
        "UNSUBSCRIBE_URL": "https://airaaigroup.in/unsubscribe",
        "TICKET_ID": "AIRA-7892",
        "SUBJECT": args.subject or "Technical Inquiry"
    }

    if args.type == "ad":
        tpl = "target_advertisement.html"
        subj = args.subject or "🚀 Introducing Aira Sovereign AI: 100% Rate-Limit Free OpenAI-Compatible Gateway"
        sender = args.from_email or "Aira Sovereign AI <noreply@airaaigroup.in>"
    elif args.type == "support":
        tpl = "support_ticket.html"
        subj = args.subject or f"[Aira Support #AIRA-7892] We've received your request"
        sender = args.from_email or "Aira Support Desk <support@airaaigroup.in>"
    else:
        tpl = "developer_welcome.html"
        subj = args.subject or "Welcome to Aira Sovereign AI Gateway — Your API Quickstart 🚀"
        sender = args.from_email or "Aira Developer Hub <noreply@airaaigroup.in>"

    print(f"⚡ Rendering template '{tpl}' for {args.to}...")
    rendered_html = render_template(tpl, context)

    if args.preview:
        out_path = Path(__file__).parent / "preview_output.html"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(rendered_html)
        print(f"📄 Preview rendered to: {out_path}")
        return

    # Check if domain is verified on Resend, else fallback for test
    effective_sender = sender
    print(f"📨 Dispatching email to: {args.to}")
    print(f"📌 From: {effective_sender}")
    print(f"📌 Subject: {subj}")

    send_via_resend(effective_sender, args.to, subj, rendered_html)

if __name__ == "__main__":
    main()
