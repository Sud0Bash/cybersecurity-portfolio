# Indicators of Compromise

## Objective

Summarize the indicators of compromise identified during the phishing investigation and organize them into a format that can support alert triage, escalation, and follow-up investigation.

## Tools Used

- Completed alert ticket
- Original alert ticket
- Incident handler journal
- Phishing incident response playbook
- VirusTotal/file hash analysis notes
- Pyramid of Pain reference

## Methodology

1. Reviewed the completed alert ticket for sender, recipient, attachment, hash, IP, subject, and message indicators.
2. Reviewed the original alert ticket to confirm initial alert details and ticket status before escalation.
3. Reviewed the incident handler journal for additional investigation notes, VirusTotal observations, and related malware context.
4. Reviewed the phishing playbook to understand which indicators supported escalation.
5. Grouped indicators by type and documented only artifacts referenced in the provided source materials.

## IOC Summary

| Indicator Type | Indicator | Source Context | Analyst Note |
| --- | --- | --- | --- |
| Ticket ID | A-2703 | Alert ticket | Phishing alert involving possible malware download |
| Alert source | SERVER-MAIL | Alert ticket | Mail security alert source |
| Severity | Medium | Alert ticket | Original and completed ticket severity |
| Recipient email | hr@inergy.com | Alert ticket | Targeted HR mailbox |
| Recipient IP | 176.157.125.93 | Alert ticket | Recipient-side IP listed in email details |
| Sender display name | Def Communications | Alert ticket | Does not match message signer |
| Sender identity used in body | Clyde West | Alert ticket and journal | Claimed job applicant identity |
| Sender domain/address indicator | 76tguyhh6tgftrt7tg.su | Alert ticket | Suspicious sender indicator |
| Sender IP | 114.114.114.114 | Alert ticket | Sender-side IP listed in email details |
| Subject line | Re: Infrastructure Egnieer role | Alert ticket | Contains spelling error |
| Attachment filename | bfsvc.exe | Alert ticket | Executable attachment disguised as job application material |
| SHA256 hash | 54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b | Alert ticket and journal | Identified in source materials as known malicious |
| Password provided | paradise10789 | Alert ticket | Password supplied to open attachment |
| Delivery method | Phishing email with attachment | Journal and alert ticket | Social engineering through HR job application theme |
| User action | Attachment downloaded and opened | Completed alert ticket and journal | Triggered escalation concern |
| Malware context | Flagpro/BlackTech activity | Incident handler journal | Associated with the investigated hash in journal notes |

## Email Indicators

- Sender display name: `Def Communications`
- Sender domain/address indicator: `76tguyhh6tgftrt7tg.su`
- Sender IP: `114.114.114.114`
- Recipient: `hr@inergy.com`
- Recipient IP: `176.157.125.93`
- Subject: `Re: Infrastructure Egnieer role`
- Claimed sender name in body: `Clyde West`
- Password supplied in message: `paradise10789`

## File Indicators

- Filename: `bfsvc.exe`
- File type indicated by filename: Windows executable
- SHA256: `54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b`
- Hash status in source materials: known malicious

## URL and Domain Indicators

- Suspicious sender domain/address indicator: `76tguyhh6tgftrt7tg.su`

No separate malicious URL was provided in the source documents.

## Behavioral Indicators

- Phishing email impersonated a job applicant.
- Message claimed to include a resume and cover letter.
- Attachment was an executable file rather than a standard document.
- Message included password-protected attachment language.
- User reportedly downloaded and opened the attachment.
- Source notes describe unauthorized executable file creation after malicious attachment execution in the related investigation context.

## Findings

- The most important confirmed IOC is the SHA256 hash associated with `bfsvc.exe`.
- The sender identity was inconsistent across display name, sender indicator, and message signature.
- The HR mailbox was targeted with a job-application theme, which is a plausible social engineering approach.
- The attachment type did not match the claimed business purpose of a resume and cover letter.
- The playbook-supported response was escalation because the attachment was confirmed malicious in the source documents.

## Recommendations

- Search email logs for the SHA256 hash, `bfsvc.exe`, sender indicator, sender IP, and subject line.
- Search endpoint logs for execution of `bfsvc.exe`.
- Identify whether additional users received or opened the same attachment.
- Block or monitor the sender indicator and related message pattern.
- Preserve the email and attachment metadata for further analysis.
- Escalate to a level-two SOC analyst for containment and endpoint review.

## Skills Demonstrated

- IOC extraction
- Email artifact analysis
- Hash-based indicator documentation
- Phishing investigation support
- Evidence organization
- Playbook-based escalation support
- Professional security reporting

## Lessons Learned

- IOCs should be grouped by type so they can be searched and acted on efficiently.
- Hashes, filenames, sender details, and behavior all provide useful investigation context.
- Indicators should not be overstated beyond what the evidence supports.
- Documenting both technical and behavioral indicators helps explain why an alert was escalated.
