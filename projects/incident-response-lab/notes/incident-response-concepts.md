# Incident Response Concepts

## Incident Response Lifecycle

### Preparation

Preparation includes policies, contact lists, logging, response checklists, backups, and user training. Good preparation makes response faster and more consistent.

### Detection

Detection is when suspicious activity is identified through alerts, logs, user reports, or monitoring tools.

### Analysis

Analysis reviews the available evidence to decide what happened, what may be affected, and what still needs investigation.

### Containment

Containment limits further harm. Examples include disabling an account, revoking sessions, isolating an endpoint, or blocking a malicious sender.

### Eradication

Eradication removes the cause of the incident, such as malware, unauthorized access, malicious inbox rules, or vulnerable configurations.

### Recovery

Recovery restores normal operations and verifies that affected systems or accounts are safe to use again.

### Lessons Learned

Lessons learned identify what worked, what was missing, and what should improve before the next incident.

## Observation vs. Indicator vs. Finding vs. Assumption

- **Observation:** Something directly seen in the evidence.
- **Indicator:** A data point that may suggest suspicious or malicious activity.
- **Finding:** A supported conclusion based on multiple observations or indicators.
- **Assumption:** A possible explanation that has not been confirmed.

Clear reports should separate these categories so the next responder knows what is confirmed and what still needs validation.

## Why Timelines Matter

Timelines help responders:

- Understand event order.
- Connect related activity.
- Identify gaps in evidence.
- Communicate quickly during escalation.
- Avoid confusing assumptions with observed sequence.

## Why Documentation Matters

Good documentation supports:

- Faster handoff.
- Better escalation decisions.
- Clear severity rationale.
- Repeatable response steps.
- Lessons learned after the event.

## Public Sanitization

Evidence should be sanitized before public sharing. Public documentation should not include real usernames, company names, IP addresses, hostnames, credentials, customer data, private logs, or sensitive business details.
