# Phishing Email Investigation

## Project Overview

This project documents a beginner-level phishing investigation using simulated and sanitized evidence. The public portfolio artifacts are original Markdown summaries that explain the investigation process, indicators reviewed, escalation reasoning, and response recommendations.

Source materials were used only as private reference during the rewrite process. The public-facing portfolio evidence is the original Markdown documentation linked below.

## Scenario Summary

A simulated mail-security alert reported a suspicious email sent to a recruiting-style mailbox. The message appeared to impersonate a job applicant and encouraged the recipient to open an attachment. The attachment and sender details were suspicious enough to require triage, indicator review, and escalation recommendation.

No real mailbox, real company data, real user credentials, or live malicious file is included in this project.

## Skills Demonstrated

- Phishing alert triage
- Email sender and message review
- Attachment-risk identification
- IOC extraction and organization
- Hash/reputation-check concepts
- Escalation decision writing
- User-focused response recommendations
- Clear SOC-style documentation using simulated evidence

## Tools and Concepts Used

- Simulated email-alert details
- Email header and sender review concepts
- File hash and reputation-check concepts
- Basic phishing response workflow
- Markdown reporting
- Safe handling of potentially malicious attachments

## Evidence Reviewed

- [Sanitized Alert Summary](artifacts/sanitized-alert-summary.md)
- [Phishing Alert Triage Summary](reports/phishing-alert-triage-summary.md)
- [Incident Handler Summary](reports/incident-handler-summary.md)
- [Phishing Response Workflow](reports/phishing-response-workflow.md)

## Key Indicators

The investigation focused on sanitized indicators:

- Suspicious sender identity that did not clearly match the message context.
- Recruiting-themed social engineering directed at a mailbox likely to receive attachments.
- Executable-style attachment disguised as business or resume-related content.
- Attachment hash documented as suspicious/malicious in the learning scenario.
- User action indicating the attachment may have been opened.
- Need for endpoint review and broader email search.

## Investigation Summary

The email was suspicious because the sender details, message theme, and attachment behavior did not align with normal business expectations. The highest-risk item was the attachment: it was presented as job-application material but used an executable-style filename.

The simulated hash/reputation context supported treating the attachment as malicious. Because the scenario indicated possible user execution, the alert should not be closed as benign. The appropriate beginner-level response is to document the indicators, preserve evidence, and escalate for endpoint and mailbox review.

## Escalation and Response Decision

**Decision:** Escalate for further investigation.

**Reason:** The alert involved a suspicious attachment with malicious-file indicators and possible user execution. A level-one analyst should document the evidence and escalate rather than attempting to fully determine endpoint impact from the email alert alone.

## Recommendations

- Preserve the suspicious email and attachment metadata.
- Search for the same sender, subject pattern, attachment name, and hash in mail logs.
- Identify any other users who received or opened similar messages.
- Review the affected endpoint for process execution, new files, persistence, or unusual network activity.
- Block or monitor confirmed malicious indicators in the simulated environment.
- Provide user awareness guidance about unexpected executable attachments and password-protected files.
- Reset credentials only if follow-up evidence suggests credential exposure.

## Ethical and Sanitization Note

This project uses simulated and sanitized learning material. It does not include real user emails, real credentials, private mailbox content, live malicious links, production security logs, or professional incident-response claims.

The public documentation is written in original wording to show security reasoning and documentation skill.

## Lessons Learned

- Phishing investigations should focus on observable evidence instead of assumptions.
- Attachment type and delivery context can be stronger warning signs than message wording alone.
- Hash indicators are useful, but analysts should also document sender, subject, filename, delivery method, and user action.
- Escalation decisions should explain what is confirmed, what is unknown, and what should be reviewed next.
- Public portfolio work should summarize learning in original wording with clear scope and sanitization.
