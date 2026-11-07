# 🛡️ Hostinger DNS Records Guide for airaaigroup.in

To ensure 100% inbox delivery (bypassing Spam & Promotions filters) for:
- `noreply@airaaigroup.in`
- `support@airaaigroup.in`

Add the following records into your **Hostinger DNS Zone**:

---

## 1. SPF Record (Sender Policy Framework)
* **Type:** `TXT`
* **Name / Host:** `@`
* **Value / Content:** `v=spf1 include:resend.com ~all`
* **TTL:** `3600` (or Default)

---

## 2. DKIM Record (DomainKeys Identified Mail)
* **Type:** `TXT` / `CNAME`
* **Name / Host:** `resend._domainkey` (or value shown in Resend Domains dashboard)
* **Value / Content:** *(Obtain exact key from resend.com/domains)*
* **TTL:** `3600`

---

## 3. DMARC Record
* **Type:** `TXT`
* **Name / Host:** `_dmarc`
* **Value / Content:** `v=DMARC1; p=none; rua=mailto:support@airaaigroup.in`
* **TTL:** `3600`

---

## 4. Inbound MX Records (For receiving emails on support@airaaigroup.in)
If using Hostinger Titan Mail:
* **MX 1:** Host `@` | Value `mx1.titan.email` | Priority `10`
* **MX 2:** Host `@` | Value `mx2.titan.email` | Priority `20`
