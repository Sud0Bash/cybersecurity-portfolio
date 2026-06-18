# DNS / Port 53 Outage Summary

## Objective

Explain a simulated DNS outage scenario involving port 53 and unreachable-message behavior using original, portfolio-safe wording.

## What DNS / Port 53 Is Used For

DNS translates human-readable domain names into IP addresses. Most basic DNS queries use UDP port 53, although DNS can also use TCP port 53 in some cases.

If DNS resolution fails, users may be unable to reach a website by name even if other parts of the network are working.

## Symptoms Observed

The simulated scenario showed users unable to reach a website. Network troubleshooting output indicated that DNS traffic to UDP port 53 was unreachable.

Observed symptoms included:

- Website access failure from the user perspective.
- DNS resolution not completing successfully.
- Unreachable-message behavior related to UDP port 53.
- Need to determine whether the issue was service availability, filtering, misconfiguration, or malicious traffic.

## ICMP / UDP Unreachable Behavior

UDP does not use a connection handshake like TCP. When a UDP packet is sent to a destination or service that cannot be reached, an ICMP unreachable message may be returned.

For DNS troubleshooting, an unreachable response involving UDP port 53 can suggest that DNS service traffic is being blocked, the DNS service is down, or the destination path is not available.

## Possible Causes

The evidence supported several possible causes:

- DNS service outage or stopped resolver process.
- Firewall rule blocking UDP port 53.
- Network misconfiguration affecting the DNS server path.
- DNS server overload or denial-of-service condition.
- Routing or infrastructure issue between the client and DNS service.

The available evidence was not enough to prove one cause by itself. It supported escalation and additional checks.

## Findings

- DNS was the key service involved because port 53 was unreachable.
- The user-facing symptom was website access failure.
- The technical symptom was failed DNS resolution or inability to reach the DNS service.
- A denial-of-service condition was possible, but service outage, firewall rule issues, and misconfiguration also needed review.

## Beginner-Level Recommendations

- Check DNS server service status.
- Review firewall rules for UDP and TCP port 53.
- Check DNS server logs and network device logs.
- Confirm whether other domains or users are affected.
- Test alternate resolvers in a controlled lab context.
- Escalate to network or infrastructure support if the service remains unreachable.
- Preserve timestamps, command output, and packet summaries for investigation notes.

## Lessons Learned

- DNS failures can appear to users as a website outage.
- ICMP unreachable messages can provide useful troubleshooting clues.
- Port 53 issues should be investigated carefully before assuming an attack.
- A good report separates observed symptoms from possible causes.
