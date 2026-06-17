# Sample Alert Triage Report: Multiple Failed Login Attempts

## Alert Summary

| Field | Value |
| --- | --- |
| Alert name | Multiple Failed Login Attempts |
| Alert ID | LAB-SOC-001 |
| Date | 2026-06-16 |
| Source | Simulated authentication logs |
| Source host | WIN11-LAB-01 |
| Source IP | 192.168.56.24 |
| Target account | j.smith |
| Initial severity | Medium |
| Final severity | Medium |
| Status | Escalated |

## Scenario

A simulated SOC alert was generated after six failed login attempts were detected against the `j.smith` account on the `WIN11-LAB-01` workstation within a ten-minute window. A successful login was observed shortly after the failed attempts.

This report documents the triage process, evidence reviewed, findings, severity assessment, escalation decision, and recommended next steps.

## Evidence Reviewed

| Time | Evidence | Observation |
| --- | --- | --- |
| 09:14:02-09:20:05 | Failed login events | Six failed login attempts against `j.smith` |
| 09:14:02-09:20:05 | Source IP review | All attempts came from `192.168.56.24` |
| 09:21:18 | Successful login event | Successful login occurred after repeated failures |
| Investigation review | Additional indicators | No malware, privilege escalation, or data access evidence included in this lab |

## Investigation Steps

1. Reviewed the alert details, including alert name, host, account, timestamp, and initial severity.
2. Checked the simulated authentication events for the target account.
3. Confirmed that six failed login attempts occurred within the ten-minute threshold.
4. Verified that the attempts came from the same source IP address.
5. Checked for successful authentication after the failures.
6. Reviewed the scenario for additional suspicious indicators.
7. Assigned a final severity based on the evidence.
8. Documented the escalation decision and recommended follow-up actions.

## Findings

- The alert rule triggered correctly because the failed-login threshold was met.
- Six failed authentication attempts targeted the same account in a short time period.
- The failed attempts came from one source IP address.
- A successful login occurred shortly after the failed attempts.
- The activity may be legitimate user error, but the successful login after repeated failures creates enough concern to require validation.
- There is no evidence in this beginner lab scenario confirming malware activity, data access, privilege escalation, or confirmed account compromise.

## Severity Assessment

Final severity: **Medium**

The alert should remain Medium because repeated failed login attempts followed by a successful login may indicate unauthorized access. The severity is not raised to High because the available evidence does not show confirmed compromise, sensitive data access, lateral movement, or persistence.

## Escalation Decision

Decision: **Escalate**

This alert should be escalated for additional validation. The main reason for escalation is the successful login that occurred after several failed attempts. The next reviewer should confirm whether the login was expected and whether the source IP belongs to an authorized lab system.

## Recommended Next Steps

- Contact or validate with the account owner to confirm whether the login attempts were expected.
- Review additional authentication history for the `j.smith` account.
- Check whether `192.168.56.24` is an expected lab source system.
- Review activity after the successful login for unusual access or changes.
- Reset the password if the activity cannot be confirmed as legitimate.
- Review account lockout settings and monitoring rules for repeated failed logins.
- Continue monitoring for additional failed logins from the same source IP.

## Analyst Notes

This is a simulated beginner-level triage scenario. The correct response is not to assume compromise immediately, but to recognize that the pattern is suspicious enough to require follow-up. The report should clearly separate confirmed facts from possible explanations.

## Final Disposition

True positive security event requiring review. Escalated for user validation and source host review.
