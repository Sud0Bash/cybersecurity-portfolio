# SYN Flood Analysis Summary

## Objective

Explain a simulated SYN flood denial-of-service scenario using original wording, beginner-level network concepts, and portfolio-safe recommendations.

## Symptoms Observed

The simulated traffic showed a web service becoming unreliable for normal users. Early connections appeared to complete normally, but later connection attempts began failing or timing out while repeated SYN traffic continued.

Observed symptoms included:

- A rising number of TCP SYN packets.
- Normal user traffic receiving failed or reset connections.
- Web requests timing out after the server became overloaded.
- Traffic pattern consistent with resource exhaustion at the connection stage.

## Normal TCP Handshake Behavior

A normal TCP connection begins with a three-way handshake:

1. **SYN:** The client asks to start a connection.
2. **SYN-ACK:** The server acknowledges the request and responds.
3. **ACK:** The client confirms the response and the connection is established.

After this handshake completes, application traffic such as HTTP requests can flow over the connection.

## How SYN Flooding Disrupts Connections

A SYN flood abuses the beginning of the TCP handshake. The attacker sends many SYN packets and creates many half-open connection attempts. If the server reserves resources for those requests faster than it can clear them, normal users may be unable to connect.

In this type of denial-of-service condition, the service may still be online, but it cannot reliably complete new connections for legitimate users.

## Indicators Supporting a DoS Interpretation

The simulated evidence supported a denial-of-service interpretation because:

- Repeated SYN traffic appeared at high volume.
- Legitimate connection attempts began receiving reset or timeout behavior.
- The service became less responsive as SYN traffic continued.
- The issue affected availability rather than confidentiality or integrity in the available evidence.

This summary does not claim a confirmed real attacker or production incident. It documents a simulated traffic pattern consistent with SYN flood behavior.

## Findings

- The strongest indicator was repeated SYN traffic combined with service connection failures.
- Normal users were affected because their connections could not complete reliably.
- The symptoms fit a network-level availability problem.
- Additional logs and baselines would be needed to confirm source, scope, and impact in a real environment.

## Beginner-Level Recommendations

- Enable or tune SYN rate limiting where appropriate.
- Use SYN cookies or similar server protections when supported.
- Review firewall or IPS rules for abnormal SYN patterns.
- Monitor connection states and backlog utilization.
- Escalate to network or infrastructure teams if legitimate users are affected.
- Preserve traffic summaries and logs for follow-up review.

## Lessons Learned

- Understanding the TCP handshake helps explain why SYN floods affect availability.
- Timeout and reset behavior can show that users are not completing normal connections.
- Availability incidents should be documented with symptoms, likely cause, and evidence gaps.
- A careful report should avoid overstating conclusions beyond the available traffic evidence.
