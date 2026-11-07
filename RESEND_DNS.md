# Resend DNS Records for airaaigroup.in
Domain ID: 3f182b51-7aac-4f9c-b62c-d1030d9b6f8b
Created: 2026-11-07 16:27:02 UTC

## Record 1: DKIM (Authentication)
- Type: TXT
- Name: resend._domainkey
- Value: p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCqd8A6B9WzlC1u2ZHi915YxuH4G0jPuOWGAPiwOKcsQ3AiaT73MdiYzLTo8PAMO/E6rqoANVJDpP1YX1ShSVhss/65srmZCghmtLuWcSLnWwpHMeCaQ80pWRh5B+qsKHh6GdJrZ4U6qtuOek1mVYCI2LyQIs8+GPboaZqqgxa1+wIDAQAB
- TTL: Auto

## Record 2: SPF TXT (Mail Delivery)
- Type: TXT
- Name: send
- Value: v=spf1 include:amazonses.com ~all
- TTL: Auto

## Record 3: SPF MX (Mail Return)
- Type: MX
- Name: send
- Priority: 10
- Value: feedback-smtp.us-east-1.amazonses.com
- TTL: Auto

## Record 4: Return-Path CNAME
- Type: CNAME
- Name: rsend
- Value: send.forge.rmta.net
- TTL: Auto
