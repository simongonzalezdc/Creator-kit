# Security Policy

## Supported Versions

Security fixes target the current `main` branch. Older snapshots are not supported unless the same issue appears in current public files.

## Reporting a Vulnerability

Please do not open a public issue with private drafts, client material, account strategy, credentials, or exploit details.

Report security concerns through GitHub Security Advisories or email `security@kyanitelabs.tech` with:

- affected document, workflow, or template;
- impact and reproduction steps;
- whether private content, credentials, or personal data was exposed.

Expected response: acknowledgement within 3 business days, triage within 7 business days, and a fix or mitigation plan based on severity.

## Project Security Notes

Creator Kit is a public documentation and workflow repository. It should contain reusable prompts, sanitized examples, and reviewable process docs only. Do not commit private drafts, client data, `.env` files, account tokens, generated caches, or private media assets.

Before a release or public update, run:

```bash
bash tests/structural.sh
gitleaks dir . --no-banner --redact
```

