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
| `werkzeug` | `2.1.2` | CVE-2024-34069 | Debugger RCE; only fixed in 3.x (major bump) |

## Seeded breaking-change fixture (werkzeug)

To demonstrate that the agent fixes the *breakage a bump introduces* — not just the
pinned version — `superset/utils/url_tools.py` (with `tests/unit_tests/utils/test_url_tools.py`)
is intentionally written against `werkzeug.urls.url_quote`, which exists in Werkzeug
2.x but was **removed** in Werkzeug 3.x. Remediating CVE-2024-34069 forces a 2.x → 3.x
upgrade, so the fix requires rewriting that call site (e.g. to `urllib.parse.quote`) and
keeping the test green. Like the pins above, this is **planted for the demo on this fork**.
