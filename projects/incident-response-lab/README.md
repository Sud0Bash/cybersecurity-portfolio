# Incident Response Lab

## Project Overview

This project is an original simulated incident response documentation exercise. It shows how a beginner-level analyst might organize evidence, build a timeline, assess severity, escalate appropriately, and recommend follow-up actions.

The project uses fictional details and Markdown documentation only. It is not a real incident, professional investigation, forensic engagement, or production incident response case.

## Simulated Scenario Summary

A simulated security alert reported a suspicious login to a user account shortly after a phishing-like email was received. The login came from an unfamiliar location and was followed by access to shared files. The available evidence was limited, so the appropriate response was to document the indicators, assess severity, and escalate for deeper review.

## Skills Demonstrated

- Incident report writing.
- Timeline creation.
- Evidence organization.
- Initial severity assessment.
- Separating observations, findings, assumptions, and open questions.
- Escalation summary writing.
- Beginner-level incident response workflow documentation.
- Sanitized public reporting.

## Tools and Concepts Used

- Incident response lifecycle concepts.
- Suspicious login triage.
- Phishing indicator review.
- Timeline documentation.
- Evidence handling notes.
- Severity and escalation reasoning.
- Markdown reporting.

## Evidence and Reports

- [Simulated Incident Report](reports/simulated-incident-report.md)
- [Incident Timeline](reports/incident-timeline.md)
- [Escalation Summary](reports/escalation-summary.md)
- [Incident Response Concepts](notes/incident-response-concepts.md)
- [Evidence Handling Notes](notes/evidence-handling-notes.md)

## Incident Response Workflow

1. **Detection:** Review the initial suspicious-login alert.
2. **Initial analysis:** Check related phishing, login, and file-access indicators.
3. **Evidence organization:** Record timestamps, affected account, observed behavior, and open questions.
4. **Severity assessment:** Assign an initial severity based on available evidence.
5. **Escalation:** Recommend deeper account, endpoint, and mailbox review.
6. **Follow-up:** Document recommended containment, recovery, and user-awareness steps.
7. **Lessons learned:** Identify documentation and control improvements.

## Key Findings

- A suspicious login occurred after a phishing-like email was reported.
- The login context was unusual for the simulated user account.
- Shared-file access after the login increased concern.
- Evidence was not enough to confirm full account compromise or data loss.
- Escalation was appropriate because additional mailbox, endpoint, and identity logs would be needed.

## Recommendations

- Escalate to the appropriate security or IT response owner in the simulated organization.
- Preserve login, mailbox, and file-access logs.
- Confirm whether the user recognized the login and email.
- Reset the password and revoke sessions if compromise is suspected.
- Enable or verify MFA on the affected account.
- Review shared-file access after the suspicious login.
- Search for similar phishing messages sent to other users.
- Document lessons learned and update response steps.

## Ethical and Sanitization Note

This project uses simulated evidence and fictional entities only. It does not include real names, real IP addresses, real credentials, customer data, private logs, or production incident details.

The public evidence is original Markdown documentation created to demonstrate beginner-level incident response documentation practice.

## Lessons Learned

- A timeline helps connect related events and clarify what happened first.
- Escalation should be based on evidence and uncertainty, not assumptions.
- Incident reports should explain what is known, what is unknown, and what needs follow-up.
- Sanitized documentation makes it possible to share learning publicly without exposing sensitive information.
