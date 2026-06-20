# Seeded vulnerabilities (DEMO)

> ⚠️ These dependency downgrades were **planted intentionally** to demonstrate an
> automated CVE-remediation pipeline (Devin). They are **not** undiscovered
> vulnerabilities in Apache Superset, and exist only on this fork.

| Package | Seeded (vulnerable) version | CVE | Issue |
|---|---|---|---|
| `pyyaml` | `5.3.1` | CVE-2020-14343 | Arbitrary code execution via full_load |
| `requests` | `2.19.1` | CVE-2018-18074 | Authorization header leak on redirect |
| `certifi` | `2022.12.7` | CVE-2023-37920 | Bundles compromised e-Tugra root cert |
| `urllib3` | `1.25.8` | CVE-2020-26137 | CRLF injection via request method |
| `idna` | `2.8` | CVE-2024-3651 | DoS via resource consumption in idna.encode |
