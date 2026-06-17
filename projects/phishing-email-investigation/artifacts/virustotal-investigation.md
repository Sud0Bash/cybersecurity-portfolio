# VirusTotal Investigation

## Objective

Document the hash-based investigation of the suspicious attachment associated with phishing alert `A-2703` and summarize the analyst observations that supported escalation.

## Tools Used

- VirusTotal/file hash analysis notes from the incident handler journal
- Completed alert ticket
- Original alert ticket details
- Phishing incident response playbook
- Pyramid of Pain reference

## Artifact Investigated

| Field | Value |
| --- | --- |
| Ticket ID | A-2703 |
| Attachment filename | bfsvc.exe |
| Artifact type | Executable attachment |
| Hash type | SHA256 |
| SHA256 | 54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b |
| Source | Phishing email sent to HR mailbox |
| Reported status | Known malicious |

## Methodology

1. Identified the attachment filename from the alert ticket: `bfsvc.exe`.
2. Collected the SHA256 hash documented in the alert materials.
3. Reviewed the incident handler journal entry describing VirusTotal and SHA256 file hash analysis.
4. Treated the file as malicious based on the source documents identifying the hash as known malicious.
5. Connected the hash finding to the phishing playbook decision point for malicious attachments.
6. Documented related observable indicators from the alert ticket.
7. Recommended escalation and further endpoint review based on the malicious file finding.

## Findings

- The attachment `bfsvc.exe` was associated with a known malicious SHA256 hash.
- The file was delivered through a phishing email to `hr@inergy.com`.
- The email presented the attachment as a resume and cover letter, but the filename used an executable extension.
- The source documents state that the employee downloaded and opened the malicious file.
- The incident handler journal notes that suspicious executable files were created after a password-protected spreadsheet was opened in a related learning scenario.
- The journal also notes that malware associated with the investigated hash was linked to Flagpro/BlackTech activity.
- The hash result, executable attachment, and phishing delivery method supported escalation.

## Related Analyst Observations

- A SHA256 hash is useful for confirming a known file artifact, but it can be changed by attackers.
- The Pyramid of Pain concept helps explain why hash indicators are useful but not always the strongest long-term detection method.
- The phishing delivery method and user execution behavior are also important because they describe attacker tactics, techniques, and procedures.

## Recommendations

- Escalate the ticket for endpoint containment and deeper investigation.
- Search endpoint and email logs for the SHA256 hash and filename `bfsvc.exe`.
- Review whether other users received the same sender, subject, attachment, or hash.
- Investigate any process creation, persistence, or outbound network activity after the file was opened.
- Preserve the malicious email and attachment metadata for analysis.
- Add detections for the hash, filename, sender indicators, and related phishing pattern where appropriate.

## Skills Demonstrated

- SHA256 hash review
- VirusTotal-style investigation documentation
- Malware indicator handling
- IOC correlation
- Playbook-based decision making
- Understanding of Pyramid of Pain concepts
- Evidence-based escalation writing

## Lessons Learned

- File hashes can help confirm whether an attachment is already known as malicious.
- Hashes are valuable investigation artifacts, but analysts should also document filenames, sender details, domains, IPs, and delivery methods.
- A malicious file attachment in a phishing email should be escalated for containment and deeper endpoint review.
- Investigation reports should clearly identify what is confirmed by source evidence and what requires further analysis.
