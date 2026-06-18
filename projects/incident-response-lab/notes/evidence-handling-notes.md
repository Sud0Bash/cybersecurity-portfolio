# Evidence Handling Notes

## Purpose

These notes describe how evidence should be organized in a simulated incident response project. They are written for portfolio documentation practice, not for formal forensic handling.

## Evidence to Preserve

For a suspicious-login and phishing-related incident, useful evidence can include:

- Alert name and timestamp.
- Affected account.
- Email metadata.
- Login context.
- MFA status.
- Session activity.
- Endpoint activity.
- File-access logs.
- Analyst notes and escalation decisions.

## Handling Principles

- Preserve original evidence when possible.
- Record where evidence came from.
- Keep timestamps consistent.
- Avoid editing raw evidence directly.
- Separate facts from assumptions.
- Document who reviewed the evidence in the simulated workflow.

## Sanitization for Public Sharing

Before sharing evidence publicly:

- Remove real names and email addresses.
- Remove real IP addresses and hostnames.
- Remove credentials, tokens, and session identifiers.
- Remove customer or company data.
- Generalize screenshots or recreate examples when needed.
- Use fictional labels for users, systems, and organizations.

## Documentation Tips

- Keep notes concise and chronological.
- Link evidence to findings.
- Record uncertainty clearly.
- Avoid claiming compromise unless the evidence supports it.
- Include next steps for the responder who receives the escalation.

## Scope Note

These notes are for beginner-level lab documentation. They are not a substitute for legal, forensic, regulatory, or production evidence-handling procedures.
