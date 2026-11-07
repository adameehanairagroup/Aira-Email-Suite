# 📧 AIRA EMAIL SUITE — Corporate & Automated Campaign System

[![Domain](https://img.shields.io/badge/Domain-airaaigroup.in-blue.svg)](https://airaaigroup.in)
[![Sender](https://img.shields.io/badge/Sender-noreply%40airaaigroup.in-purple.svg)]()
[![Support](https://img.shields.io/badge/Support-support%40airaaigroup.in-green.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> **Architected & Engineered by Er. Adam Eehan (Founder & CEO, Aira Group of Technology)**  
> Production-grade responsive HTML email templates, automated campaign dispatching, and enterprise inbox management.

---

## 🌟 Corporate Inboxes

* **`noreply@airaaigroup.in`**: Outbound automated product marketing, developer onboarding, and platform alerts.
* **`support@airaaigroup.in`**: Inbound customer assistance, developer inquiries, and automated ticket acknowledgments.

---

## 📁 Repository Structure

```
Aira-Email-Suite/
├── config/
│   └── dns_setup_guide.md       # SPF, DKIM, DMARC, MX Hostinger setup
├── previews/
│   ├── 01_Target_Advertisement_Campaign.html
│   ├── 02_Support_Ticket_Confirmation.html
│   └── 03_Developer_Welcome_API_Quickstart.html
├── templates/
│   ├── target_advertisement.html   # Ad campaign with merge tags
│   ├── support_ticket.html         # Automated ticket response
│   └── developer_welcome.html      # Developer API quickstart
├── send_campaign.py             # CLI automated campaign dispatcher
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Usage

### 1. Preview Templates Locally
```bash
python3 send_campaign.py --preview --type ad --name "Developer"
```

### 2. Dispatch Target Developer Advertisement
```bash
python3 send_campaign.py \
  --type ad \
  --to "target_user@example.com" \
  --name "Alex" \
  --from-email "Aira Models <noreply@airaaigroup.in>"
```

### 3. Dispatch Automated Support Ticket Response
```bash
python3 send_campaign.py \
  --type support \
  --to "client@example.com" \
  --name "Rahul" \
  --subject "API Gateway Question"
```

---

## 📜 Sovereign Guarantee
Released under the **MIT License**.  
Architected by **Er. Adam Eehan** for **Aira Group of Technology**. All Sovereign Rights Reserved.
