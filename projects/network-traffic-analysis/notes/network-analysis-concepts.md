# Network Analysis Concepts

## TCP Handshake

TCP uses a three-way handshake to establish a connection:

1. Client sends `SYN`.
2. Server replies with `SYN-ACK`.
3. Client replies with `ACK`.

If this sequence does not complete, application traffic may fail even if packets are still moving across the network.

## SYN Flooding

A SYN flood is a denial-of-service technique that sends many SYN requests to consume connection resources. It can lead to slow responses, reset connections, or timeouts for legitimate users.

Common defensive ideas include:

- SYN rate limiting.
- SYN cookies.
- Firewall or IPS rules.
- Traffic baselining and alerting.
- Upstream mitigation for large traffic volumes.

## DNS and Port 53

DNS is used to resolve domain names to IP addresses. DNS commonly uses UDP port 53, with TCP port 53 also used in some situations.

If DNS fails, a user may not be able to reach a website by name even if the web server itself is not the original problem.

## ICMP Unreachable Messages

ICMP unreachable messages can indicate that a destination, network, host, protocol, or port cannot be reached. In a DNS scenario, a UDP port 53 unreachable response can point toward a DNS service, firewall, routing, or configuration issue.

## Analysis Habits

- Start with the user-facing symptom.
- Identify the protocol involved.
- Separate confirmed observations from possible causes.
- Preserve timestamps and command output.
- Avoid claiming an attack unless the evidence supports it.
- Escalate when availability is affected or more data sources are needed.
