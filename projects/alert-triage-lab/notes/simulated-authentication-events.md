# Simulated Authentication Events

This file contains mock authentication evidence for the Alert Triage Lab. The events are fictional and were created for portfolio documentation.

## Scenario

A lab alert was triggered after repeated failed login attempts were observed against a Windows 11 lab workstation.

## Mock Event Timeline

| Time | Host | Source IP | Account | Event Type | Result | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-06-16 09:14:02 | WIN11-LAB-01 | 192.168.56.24 | j.smith | Login attempt | Failed | Incorrect password |
| 2026-06-16 09:15:11 | WIN11-LAB-01 | 192.168.56.24 | j.smith | Login attempt | Failed | Incorrect password |
| 2026-06-16 09:16:08 | WIN11-LAB-01 | 192.168.56.24 | j.smith | Login attempt | Failed | Incorrect password |
| 2026-06-16 09:17:33 | WIN11-LAB-01 | 192.168.56.24 | j.smith | Login attempt | Failed | Incorrect password |
| 2026-06-16 09:18:40 | WIN11-LAB-01 | 192.168.56.24 | j.smith | Login attempt | Failed | Incorrect password |
| 2026-06-16 09:20:05 | WIN11-LAB-01 | 192.168.56.24 | j.smith | Login attempt | Failed | Incorrect password |
| 2026-06-16 09:21:18 | WIN11-LAB-01 | 192.168.56.24 | j.smith | Login attempt | Successful | Successful login after repeated failures |

## Evidence Notes

- The alert threshold was met because more than five failed logins occurred within ten minutes.
- All failed attempts targeted the same account.
- All attempts came from the same source IP address in the simulated lab network.
- The successful login after the failures increases concern because the account may have been accessed after repeated password attempts.
- No additional evidence of malware, privilege escalation, or data access is included in this beginner scenario.

## Analyst Considerations

- Confirm whether the login activity was expected.
- Check whether the source IP belongs to an approved lab system.
- Review account activity after the successful login.
- Escalate if the user cannot confirm the activity or if additional suspicious behavior is found.
