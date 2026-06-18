# Network Traffic Analysis

## Project Overview

This project documents beginner-level network traffic analysis using simulated and sanitized investigation scenarios. The public evidence is original Markdown documentation that explains network concepts, observed symptoms, findings, and recommended next steps.

The public-facing portfolio evidence is the original Markdown documentation linked below.

## Scenario Summaries

### SYN Flood Denial-of-Service Scenario

A simulated web service began failing for normal users while a high volume of repeated TCP SYN traffic was observed. The traffic pattern suggested that the server was being overwhelmed before normal TCP sessions could complete.

Public report:

- [SYN Flood Analysis Summary](reports/syn-flood-analysis-summary.md)

### DNS / Port 53 Outage Scenario

A simulated website became unreachable because DNS resolution was failing. Network output indicated that UDP port 53, which is commonly used for DNS queries, was unreachable.

Public report:

- [DNS / Port 53 Outage Summary](reports/dns-port53-outage-summary.md)

## Skills Demonstrated

- Network traffic interpretation.
- TCP handshake review.
- SYN flood denial-of-service reasoning.
- DNS and port 53 troubleshooting.
- ICMP unreachable-message interpretation.
- Evidence-based findings and recommendations.
- Clear separation of confirmed observations, possible causes, and follow-up actions.

## Tools and Concepts Used

- TCP three-way handshake concepts: SYN, SYN-ACK, ACK.
- TCP reset and timeout behavior.
- DNS over UDP port 53.
- ICMP destination/port unreachable messages.
- Packet-capture and protocol-analysis concepts.
- Wireshark and tcpdump as analysis tools in a lab context.
- Markdown reporting.

## Evidence Reviewed

Public Markdown evidence:

- [SYN Flood Analysis Summary](reports/syn-flood-analysis-summary.md)
- [DNS / Port 53 Outage Summary](reports/dns-port53-outage-summary.md)
- [Network Analysis Concepts](notes/network-analysis-concepts.md)

Supporting folders:

- `packet-captures/` is currently a placeholder for future sanitized captures.
- `screenshots/` is currently a placeholder for future sanitized screenshots.

## Key Findings

- Normal TCP connections require a completed handshake before application traffic can flow reliably.
- Repeated SYN traffic without normal completion can consume server resources and disrupt legitimate users.
- DNS failures can prevent users from reaching a website even when the web server itself may not be the original issue.
- ICMP unreachable messages can help identify whether a service, port, route, or firewall path may be blocking communication.
- More evidence is needed before claiming a confirmed attacker, confirmed DDoS, or production incident impact.

## Recommendations

- For SYN flood symptoms:
  - Review firewall, load balancer, and server logs for repeated SYN patterns.
  - Consider SYN rate limiting, SYN cookies, firewall/IPS rules, and upstream mitigation.
  - Escalate if legitimate users are unable to connect or traffic volume exceeds normal baselines.

- For DNS / port 53 symptoms:
  - Check DNS service status and resolver health.
  - Review firewall rules affecting UDP/TCP port 53.
  - Check network device logs and DNS server logs.
  - Escalate to network or infrastructure support if resolution remains unavailable.

## Ethical and Sanitization Note

This project uses simulated and sanitized learning material. It does not include private packet captures, real credentials, real company network traffic, production incident data, or claims of professional SOC/network operations experience.

The public documentation is written in original wording to show analysis process, technical reasoning, and beginner-level recommendations.

## Lessons Learned

- Packet analysis depends on context; one packet rarely proves an incident by itself.
- TCP handshake behavior is important for understanding connection failures and denial-of-service symptoms.
- DNS availability is critical because users may experience a service as down when name resolution fails.
- Recommendations should be tied to observed symptoms and should avoid overclaiming when evidence is limited.
