# Phishing Email Investigation

## Scenario

A simulated user reported a suspicious email claiming that their account would be locked unless they verified their password through an external link. The email included urgent language, a mismatched sender domain, and a link that did not match the claimed service.

This project documents a beginner-level phishing investigation using safe, simulated email details. No real user mailbox, company data, or live malicious content is included.

## Objective

- Review a suspicious email for common phishing indicators
- Analyze sender, subject, message content, links, and headers at a beginner level
- Document evidence and determine whether the message should be treated as phishing
- Recommend safe response actions for users and security teams

## Tools Used

- Simulated phishing email sample
- Email header review concepts
- VirusTotal or safe URL reputation lookup concepts
- Browser safe preview methods
- Markdown documentation

## Methodology

1. Reviewed the email subject, sender display name, and sender address.
2. Checked whether the sender domain matched the claimed organization.
3. Reviewed the message body for urgency, credential requests, spelling issues, and suspicious formatting.
4. Inspected the visible link text and compared it with the simulated destination URL.
5. Reviewed mock header details for source inconsistencies.
6. Checked the simulated URL reputation result.
7. Documented indicators, findings, severity, and recommended response actions.
8. Treated the email as suspicious without clicking links or downloading attachments.

## Findings

- The email used urgent language to pressure the recipient into immediate action.
- The sender domain did not match the organization the email claimed to represent.
- The link destination was different from the visible link text.
- The message requested credential verification, which is a common phishing indicator.
- Simulated reputation review marked the destination as suspicious.
- No attachment analysis was required because the sample did not include an attachment.

## Recommendations

- Do not click links or submit credentials from the suspicious email.
- Report the email through the approved phishing reporting process.
- Block or monitor the sender domain in a lab or simulated control list.
- Search for similar messages sent to other users in the simulated environment.
- Provide user awareness guidance about urgent credential-request emails.
- If credentials were entered, reset the password and review account activity.

## Skills Demonstrated

- Phishing indicator identification
- Sender and domain review
- URL inspection
- Basic email header analysis
- Reputation-check documentation
- User-focused security recommendations
- Clear SOC-style written reporting

## Screenshots

Screenshots should be added to the `screenshots/` folder after sanitization.

Recommended screenshots:

- Sanitized phishing email sample
- Header review output with private data removed
- Safe URL reputation result
- Highlighted suspicious link mismatch

Example:

```markdown
![Sanitized phishing email indicators](screenshots/phishing-indicators.png)
```

## Lessons Learned

- Phishing investigations should focus on observable indicators, not assumptions.
- Urgency, sender mismatch, and credential requests are important warning signs.
- Links should be inspected safely without visiting unknown destinations directly.
- Clear recommendations help users and analysts understand what action to take next.

## Notes

This project uses simulated and sanitized phishing data only. It does not include real user emails, credentials, private mailbox content, or live malicious links.
