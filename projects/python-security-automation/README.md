# Python Security Automation

## Project Overview

This project contains beginner-friendly Python security automation examples. The scripts are original portfolio-safe adaptations based on Python learning practice, not direct copies of course prompts, lab instructions, or answer text.

The examples use simulated data only. They are designed to show core Python concepts in security-support scenarios such as access checks, allow-list review, user reporting, ID formatting, and event summaries.

## Skills Demonstrated

- Writing and calling Python functions
- Using `if`, `elif`, and `else` logic
- Looping through lists and dictionaries
- Checking list membership
- Returning values from functions
- Formatting strings for readable reports
- Separating sample data from script logic
- Explaining beginner security automation clearly and honestly

## Scripts Included

| Script | What it does |
| --- | --- |
| `scripts/login_access_validator.py` | Checks simulated login attempts against approved users, assigned devices, and business-hours status. |
| `scripts/ip_allow_list_checker.py` | Compares simulated source IP addresses against an approved allow list. |
| `scripts/employee_id_generator.py` | Generates fake employee IDs with a consistent prefix and number format. |
| `scripts/approved_users_report.py` | Builds a readable report from simulated approved-user records. |
| `scripts/security_event_summary.py` | Summarizes simulated security event counts and highlights categories needing review. |

## Example Usage

Run the scripts from this project folder:

```bash
python3 scripts/login_access_validator.py
python3 scripts/ip_allow_list_checker.py
python3 scripts/employee_id_generator.py
python3 scripts/approved_users_report.py
python3 scripts/security_event_summary.py
```

Example output from `login_access_validator.py`:

```text
ALLOW: analyst_a used assigned device laptop-101 during business hours.
REVIEW: analyst_b is approved, but tablet-404 is not their assigned device.
DENY: guest_user is not on the approved user list.
REVIEW: analyst_c attempted access outside business hours.
```

Example output from `security_event_summary.py`:

```text
Security Event Summary
Total events: 33
Highest category: failed_login with 18 events
Categories needing review:
- failed_login: 18
- blocked_ip: 7
```

## Lessons Learned

- Small scripts can make repetitive security checks easier to review.
- Lists and dictionaries are useful for modeling users, devices, IP addresses, and event counts.
- Conditional logic can express simple allow, deny, and review decisions.
- Functions make scripts easier to read and reuse.
- Portfolio work should explain the concept without exposing course-specific prompts or answer text.

## Notes on Originality and Scope

Raw course notebooks are kept private as learning/reference material and are not intended to be committed or presented as public portfolio artifacts. The public-facing work in this project is the rewritten script set in `scripts/`, with original data, original structure, and original explanations.

These examples do not use real credentials, real employee records, real company data, or live security logs. They are not production-ready security tools. They demonstrate beginner Python concepts applied to realistic security-support tasks.

Additional review notes are documented in `notes/notebook-review.md`.
