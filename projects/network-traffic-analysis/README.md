# Network Traffic Analysis

## Scenario

A simulated lab workstation generated unusual outbound network traffic during a controlled analysis exercise. The goal of this project was to review packet capture data, identify common protocols, separate normal traffic from suspicious activity, and document observations in a format similar to an entry-level SOC analyst triage note.

This project uses simulated lab traffic only. No private network data, real credentials, or company traffic are included.

## Objective

- Capture and review network traffic in a controlled lab environment
- Identify DNS, HTTP, TCP, and ICMP traffic patterns
- Use Wireshark and tcpdump filters to isolate relevant events
- Document findings, recommendations, and next steps clearly

## Tools Used

- Wireshark
- tcpdump
- Linux terminal
- Parrot OS or Linux Mint lab system
- Windows 11 lab workstation
- Markdown documentation

## Methodology

1. Started a controlled packet capture from a lab system.
2. Generated basic network activity such as DNS lookups, ICMP requests, and HTTP browsing to safe test resources.
3. Opened the capture in Wireshark and reviewed protocol statistics.
4. Applied display filters for `dns`, `http`, `icmp`, and `tcp`.
5. Used tcpdump to compare command-line packet review with Wireshark analysis.
6. Identified source and destination hosts, protocols, ports, and timing patterns.
7. Documented findings and separated confirmed observations from assumptions.
8. Removed or avoided any sensitive information before publishing documentation.

## Findings

- DNS traffic was observed before outbound web requests, which is expected behavior.
- ICMP traffic showed basic connectivity testing between lab systems.
- HTTP traffic demonstrated clear-text request and response metadata, reinforcing why encrypted protocols are preferred.
- TCP connection setup and teardown were visible through SYN, SYN-ACK, ACK, and FIN packets.
- No confirmed malware traffic, credential exposure, or unauthorized external connection was identified in this simulated lab exercise.

## Recommendations

- Continue practicing Wireshark filters for common SOC workflows.
- Use tcpdump for quick command-line validation before deeper packet review.
- Avoid capturing or publishing sensitive traffic from real networks.
- Build a small reference list of common ports, protocols, and suspicious indicators.
- Add sanitized screenshots showing filters, packet details, and protocol summaries.

## Skills Demonstrated

- Packet capture review
- Protocol identification
- Wireshark display filtering
- tcpdump command-line analysis
- Network troubleshooting
- Evidence-based technical documentation
- Safe handling of lab traffic

## Screenshots

Screenshots should be added to the `screenshots/` folder after sanitization.

Recommended screenshots:

- Wireshark protocol hierarchy or conversations view
- DNS query and response filter
- ICMP packet details
- tcpdump command output with private details removed

Example:

```markdown
![Wireshark DNS filter example](screenshots/wireshark-dns-filter.png)
```

## Lessons Learned

- Packet analysis requires context; a packet is not suspicious by itself without understanding the environment and behavior.
- Wireshark is useful for detailed packet inspection, while tcpdump is useful for fast command-line review.
- DNS and HTTP metadata can provide useful investigative leads.
- Clear documentation should explain what was observed, what it means, and what is still unknown.

## Notes

All traffic reviewed in this project is from a simulated lab environment. Packet captures containing private IP details, credentials, personal data, or real organization traffic should not be published.
