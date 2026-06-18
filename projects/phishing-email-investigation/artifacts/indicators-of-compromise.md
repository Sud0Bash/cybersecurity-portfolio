# Sanitized Indicators of Compromise

## Purpose

This file provides a portfolio-safe IOC summary for the simulated phishing investigation. It uses generalized indicators and sanitized details.

## IOC Categories

| Category | Sanitized Indicator | Why It Matters |
| --- | --- | --- |
| Sender identity | Untrusted external sender with inconsistent identity details | Sender mismatch can support phishing suspicion. |
| Recipient context | Recruiting or HR-style mailbox | This mailbox type commonly receives attachments, making social engineering more believable. |
| Message theme | Job-application or resume-themed email | The theme attempts to make an attachment look expected. |
| Attachment type | Executable-style attachment disguised as business content | Executable attachments are high-risk when presented as documents. |
| File reputation | Attachment hash identified as suspicious/malicious in the simulated scenario | Hash/reputation context supports escalation. |
| User action | Attachment may have been opened | Possible execution requires endpoint review. |

## Findings

- The attachment was the strongest technical indicator.
- Sender inconsistency and message theme supported the phishing assessment.
- Possible user execution made this more than a simple spam or nuisance email.
- The case should be escalated for endpoint and mailbox review.

## Recommended Searches

- Similar sender identity or sending domain patterns.
- Similar subject or recruiting-themed messages.
- Matching attachment filenames or hashes.
- Endpoint process activity around the time of possible execution.
- Other users who received or interacted with similar messages.

## Sanitization Note

Source-specific values and private details are intentionally excluded from this public artifact.
