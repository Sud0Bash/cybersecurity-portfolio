# Phishing Investigation Report

## Objective

Document the investigation of phishing alert `A-2703`, determine whether the reported email contained malicious content, summarize analyst findings, and explain the escalation decision using professional SOC documentation standards.

## Tools Used

- Completed alert ticket
- Original alert ticket details
- Phishing incident response playbook
- Incident handler journal
- VirusTotal/file hash analysis notes
- Pyramid of Pain reference

## Alert Summary

| Field | Value |
| --- | --- |
| Ticket ID | A-2703 |
| Alert source | SERVER-MAIL |
| Alert message | Phishing attempt - possible download of malware |
| Severity | Medium |
| Ticket status | Escalated |
| Recipient | hr@inergy.com |
| Recipient IP | 176.157.125.93 |
| Sender display name | Def Communications |
| Sender address/domain indicator | 76tguyhh6tgftrt7tg.su |
| Sender IP | 114.114.114.114 |
| Subject | Re: Infrastructure Egnieer role |
| Attachment | bfsvc.exe |
| Known malicious SHA256 | 54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b |

## Scenario

A phishing alert was generated after an employee may have downloaded and opened a suspicious email attachment. The email was sent to the HR mailbox and appeared to impersonate a job applicant submitting a resume and cover letter for an engineering role.

The email contained several suspicious indicators, including sender inconsistencies, grammar errors, a password-protected file claim, and an executable attachment named `bfsvc.exe`. The provided SHA256 hash was identified in the source documents as a known malicious file hash.

## Methodology

1. Reviewed alert `A-2703` and confirmed the alert source, severity, ticket status, recipient, sender, subject line, and attachment details.
2. Reviewed the phishing playbook to determine the expected level-one SOC workflow.
3. Evaluated sender information for inconsistencies between display name, sender address, and message identity.
4. Reviewed the message body for phishing indicators such as grammar issues, urgency or social engineering, and suspicious attachment handling.
5. Confirmed that the email contained an attachment and did not treat it as safe to open.
6. Reviewed the known malicious SHA256 hash documented in the alert materials.
7. Used the playbook escalation criteria to determine whether the ticket should be escalated.
8. Documented findings, recommendations, and skills demonstrated.

## Findings

- The email was sent to `hr@inergy.com`, which is a plausible target for resume-themed phishing.
- The sender display name was `Def Communications`, while the message body used the name `Clyde West`.
- The sender domain indicator `76tguyhh6tgftrt7tg.su` appeared suspicious and did not align with the claimed job applicant identity.
- The subject line contained a spelling error: `Re: Infrastructure Egnieer role`.
- The message body contained grammar and wording issues.
- The email claimed to include a resume and cover letter, but the attachment was an executable file: `bfsvc.exe`.
- The message stated that the file was password protected and provided the password `paradise10789`.
- The source documents identify the attachment hash as known malicious.
- Based on the phishing playbook, a confirmed malicious attachment requires the ticket to be updated and escalated.

## Severity Assessment

Final severity: **Medium**

The alert remained Medium because the source ticket classified it as Medium and the available documentation confirms a malicious attachment was downloaded and opened. The event requires escalation because the attachment is malicious, but the source materials do not provide enough additional evidence to confirm broader compromise, lateral movement, data exfiltration, or business impact.

## Escalation Decision

Decision: **Escalate to a level-two SOC analyst**

Reason: The email contained an executable attachment with a known malicious SHA256 hash. The phishing playbook directs analysts to escalate when a link or attachment is confirmed malicious.

## Recommendations

- Isolate or review the affected endpoint according to internal response procedures.
- Preserve the email, attachment metadata, and relevant logs for further investigation.
- Search for other recipients who received similar sender, subject, attachment, or hash indicators.
- Block or monitor the suspicious sender domain indicator and sender IP where appropriate.
- Review endpoint activity after the attachment was opened.
- Reset affected user credentials if there is evidence of credential exposure or unauthorized access.
- Provide user awareness guidance about executable attachments disguised as resumes or cover letters.

## Skills Demonstrated

- Phishing alert triage
- Sender and message analysis
- Attachment risk identification
- Hash-based malware investigation
- Playbook-driven escalation
- IOC extraction
- SOC-style report writing
- Separating confirmed facts from assumptions

## Lessons Learned

- HR-themed phishing emails can use realistic job-application language to make attachments appear expected.
- Executable attachments should be treated as high concern when disguised as resumes or business documents.
- Password-protected attachments can be suspicious because they may reduce automated scanning visibility.
- A clear escalation decision should be tied to documented evidence and playbook criteria.
- Investigation notes should avoid assuming full compromise unless supporting evidence is available.
