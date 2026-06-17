# Alert Triage Lab

## Overview

This project documents a beginner-level SOC-style alert triage exercise using a simulated failed-login alert from a lab Windows workstation. The goal is to practice reviewing alert details, checking supporting evidence, assessing severity, deciding whether escalation is needed, and writing a clear analyst report.

This lab uses mock data only. No real company systems, user accounts, IP addresses, or incidents are included.

## Objectives

- Review alert details and identify relevant evidence
- Classify alert severity
- Decide whether escalation is needed
- Write concise triage notes

## Scenario

A simulated security monitoring rule generated an alert after multiple failed login attempts were observed against a Windows 11 lab workstation. The alert suggests possible password guessing or unauthorized access attempts against a local user account.

The analyst must determine whether the activity appears suspicious, whether there is evidence of a successful login, what severity should be assigned, and whether the alert should be escalated for further review.

## Lab Environment

- Operating systems: Windows 11 lab workstation and Linux analysis system
- Tools used: Simulated Windows authentication logs, Markdown report, triage checklist
- Lab type: Simulated SOC alert triage
- Data source: Mock authentication events created for portfolio documentation

## Tools Used

- Simulated authentication logs
- Windows Event Viewer concepts
- Basic log review workflow
- Markdown documentation
- Security report templates

## Alert Summary

| Field | Value |
| --- | --- |
| Alert name | Multiple Failed Login Attempts |
| Alert ID | LAB-SOC-001 |
| Date | 2026-06-16 |
| Source host | WIN11-LAB-01 |
| Target account | j.smith |
| Source IP | 192.168.56.24 |
| Alert rule | 5 or more failed logins within 10 minutes |
| Initial severity | Medium |
| Final severity | Medium |
| Status | Escalated for review |

## Evidence Reviewed

- Simulated failed-login events showing repeated authentication failures
- Source IP address and target account
- Time window of failed login attempts
- Follow-up event showing one successful login after the failures
- No confirmed malware, data access, or persistence evidence in this beginner lab scenario

See [simulated-authentication-events.md](notes/simulated-authentication-events.md) for the mock evidence used in this exercise.

## Investigation Steps

1. Reviewed the alert name, timestamp, host, target account, and initial severity.
2. Checked the simulated authentication events for repeated failed logins.
3. Compared event timestamps to confirm the failures happened within the alert rule window.
4. Reviewed whether the failed attempts came from the same source IP address.
5. Checked for a successful login after the failed attempts.
6. Looked for additional indicators such as multiple targeted accounts, unusual hostnames, or signs of malware.
7. Assigned final severity based on the available evidence.
8. Documented the escalation decision and recommended next steps.

## Findings

- Six failed login attempts were recorded against the same account within approximately six minutes.
- All failed attempts came from the same simulated source IP address.
- One successful login occurred shortly after the failed attempts.
- The activity could represent password guessing, a user mistyping a password repeatedly, or unauthorized access followed by a successful login.
- Because the successful login occurred after repeated failures, the alert should not be closed as a false positive without additional review.

## Severity Assessment

Final severity: **Medium**

Rationale: The alert shows repeated failed logins followed by a successful login to the same account. There is not enough evidence in this lab to confirm account compromise, malware activity, or data loss, so the severity is not High. However, the pattern is suspicious enough to require escalation and account validation.

## Escalation Decision

Decision: **Escalate**

Reason: A successful login after multiple failures may indicate that an attacker guessed the correct password or that a legitimate user eventually authenticated. The activity needs additional validation, such as user confirmation, source host review, and account activity review.

## Recommendations

- Confirm whether the user attempted to log in during the alert window.
- Review the source host or source IP for expected lab activity.
- Check for additional successful logins, privilege changes, or unusual access after authentication.
- Reset the account password if the login cannot be verified as legitimate.
- Enable or review account lockout policy for repeated failed login attempts.
- Continue monitoring for additional authentication failures from the same source.

## Completed Report

- [Sample Alert Triage Report: Multiple Failed Login Attempts](reports/sample-failed-login-alert.md)

## Screenshots

No screenshots are included yet. Future screenshots should be sanitized and may include:

- Example SIEM alert view
- Simulated authentication log view
- Timeline of failed and successful login events

## Skills Demonstrated

- Alert review
- Evidence gathering
- Severity assessment
- Escalation documentation
- Written SOC-style reporting

## Lessons Learned

- Repeated failed logins become more concerning when followed by a successful login.
- Severity should be based on evidence, not assumptions.
- A clear escalation decision should explain what is known, what is unknown, and what should be checked next.
- Even simulated alerts should be documented in a consistent, professional format.

## Future Improvements

- Add screenshots from a simulated SIEM or log viewer
- Add a second alert scenario involving suspicious PowerShell activity
- Create a reusable triage checklist
- Add a false positive example for comparison

## Notes

This project uses simulated lab data only. The usernames, hostnames, IP addresses, timestamps, and events are fictional and created for training documentation.
