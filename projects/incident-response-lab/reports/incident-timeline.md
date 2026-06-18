# Incident Timeline

## Purpose

This timeline organizes a simulated suspicious-login and phishing-related incident. Times are fictional and used only for documentation practice.

| Time | Phase | Event | Analyst note |
| --- | --- | --- | --- |
| 09:10 | Detection | Email filter flags a phishing-like message sent to a user. | Message should be preserved for review. |
| 09:18 | Detection | Identity alert reports a login from an unfamiliar context. | Login timing is close to the phishing-like message. |
| 09:22 | Initial review | Analyst reviews user, login time, and high-level alert details. | No conclusion yet; context is suspicious. |
| 09:30 | Evidence collection | Analyst records related email, login, and file-access indicators. | Evidence must be sanitized before public reporting. |
| 09:42 | Analysis | Shared-file access is observed after the suspicious login. | Increases concern but does not prove data loss. |
| 09:55 | Severity assessment | Initial severity set to Medium. | Credible compromise concern; impact not confirmed. |
| 10:05 | Escalation decision | Analyst recommends escalation for deeper review. | Identity, mailbox, endpoint, and file logs are needed. |
| 10:15 | Recommended follow-up | Suggested password reset, session revocation, MFA check, and file-access review. | Actions depend on response-owner validation. |

## Timeline Notes

- The timeline helps show the relationship between phishing-like activity, suspicious login, and file access.
- The timestamps are simulated and should not be interpreted as real event data.
- The timeline separates observed events from conclusions that require further investigation.
