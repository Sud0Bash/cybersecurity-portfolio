# Simulated Incident Report

## Executive Summary

A simulated suspicious-login alert was generated for a user account after the user received a phishing-like email. The account then accessed shared files from an unusual login context. The evidence did not confirm data loss or malware execution, but the sequence of events was suspicious enough to recommend escalation.

This report documents a beginner-level incident response workflow using fictional evidence.

## Alert Summary

| Field | Simulated Value |
| --- | --- |
| Alert type | Suspicious login after phishing-like email |
| Initial severity | Medium |
| Affected asset | User account and shared file access |
| Detection source | Simulated identity and email alerts |
| Status | Escalation recommended |
| Data sensitivity | Fictional/sanitized only |

## Scope

In scope:

- Suspicious login review.
- Related phishing-like email context.
- Shared-file access after login.
- Severity and escalation recommendation.
- Documentation of open questions and next steps.

Out of scope:

- Malware reverse engineering.
- Real endpoint forensics.
- Identity-provider review in an operational environment.
- Legal or HR investigation.
- Confirming real-world compromise.

## Observed Indicators

- User received a phishing-like message before the suspicious login.
- Login occurred from an unfamiliar location or device context.
- Shared files were accessed after the unusual login.
- Available evidence did not confirm whether files were downloaded or modified.
- MFA status was unknown in the simulated evidence.

## Initial Severity Assessment

**Initial severity:** Medium

Rationale:

- The suspicious login and phishing context created credible account-compromise concern.
- Shared-file access increased the potential impact.
- The evidence did not confirm data exfiltration, privilege escalation, persistence, or malware execution.
- More logs were needed before assigning a higher severity.

## Investigation Steps

1. Reviewed the suspicious-login alert.
2. Checked the timeline for related phishing-like email activity.
3. Noted account and shared-file access after the login.
4. Identified available indicators and open questions.
5. Assessed severity based on observed behavior and evidence gaps.
6. Recommended escalation for deeper identity, mailbox, endpoint, and file-access review.

## Findings

- The login was suspicious because it followed phishing-like activity and did not match expected user context.
- Shared-file access after the login made the event more concerning.
- The available evidence supported escalation, but not a final compromise determination.
- Additional logs would be needed to confirm user action, session behavior, file changes, or data exposure.

## Containment or Escalation Recommendations

- Escalate to the simulated security or IT response owner.
- Preserve identity, mailbox, endpoint, and file-access logs.
- Confirm whether the user recognizes the login and email.
- Reset the password and revoke active sessions if compromise is suspected.
- Verify MFA enrollment and enforce MFA where missing.
- Review shared-file activity for download, modification, or deletion.
- Search for similar phishing messages across other users.

## Lessons Learned

- A suspicious login becomes more concerning when it appears near phishing activity.
- Evidence gaps should be clearly documented instead of filled with assumptions.
- Medium severity can be appropriate when risk is credible but impact is not confirmed.
- Escalation summaries should include enough context for the next responder to continue quickly.

## Limitations

This is a simulated documentation exercise. It does not include private logs, real accounts, real endpoint evidence, or production incident response data.
