# Escalation Summary

## Why Escalation May Be Needed

Escalation may be needed when an alert suggests possible account compromise, user impact, or access to sensitive resources, but the first reviewer does not have enough evidence or permissions to confirm the full scope.

In this simulated case, escalation was recommended because:

- A suspicious login occurred shortly after phishing-like activity.
- Shared files were accessed after the login.
- The available evidence did not confirm whether the activity was legitimate.
- Additional identity, mailbox, endpoint, and file-access logs were needed.

## Information to Include

An escalation should include:

- Alert type and current status.
- Affected account or asset.
- Timeline of key events.
- Observed indicators.
- Initial severity and rationale.
- Actions already taken.
- Open questions.
- Recommended next steps.
- Any evidence that has been preserved.

## Typical Recipient in a Simulated Organization

In a small simulated organization, this escalation would typically go to:

- Security analyst or senior IT responder.
- IT administrator responsible for identity and endpoint systems.
- Incident response lead, if one exists.
- Manager or business owner only if business impact is likely or confirmed.

## What Should Not Be Overclaimed

The escalation should not claim:

- Confirmed account compromise without evidence.
- Confirmed data theft without logs or proof.
- Malware execution without endpoint evidence.
- Attribution to a specific attacker.
- Operational impact when the scenario is simulated.

## Example Escalation Decision

**Decision:** Escalate for deeper account, mailbox, endpoint, and file-access review.

**Reason:** The sequence of phishing-like email, suspicious login, and shared-file access creates credible risk. More evidence is needed to determine whether the activity was legitimate or malicious.

## Recommended Follow-Up

- Confirm user activity.
- Reset password if activity is suspicious.
- Revoke active sessions if compromise is suspected.
- Verify MFA status.
- Review mailbox rules and forwarding.
- Review endpoint process and login activity.
- Review shared-file access and changes.
