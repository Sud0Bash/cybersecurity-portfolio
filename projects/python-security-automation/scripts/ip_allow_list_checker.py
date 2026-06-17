"""Check simulated source IP addresses against an approved allow list.

Sample output:
192.0.2.10: allowed
198.51.100.23: review
203.0.113.44: allowed
198.51.100.77: review
"""

ALLOW_LIST = [
    "192.0.2.10",
    "203.0.113.44",
    "10.10.5.25",
]

LOGIN_SOURCE_IPS = [
    "192.0.2.10",
    "198.51.100.23",
    "203.0.113.44",
    "198.51.100.77",
]


def check_ip_address(ip_address, allow_list):
    """Return whether an IP address appears in the approved list."""
    if ip_address in allow_list:
        return "allowed"
    return "review"


def main():
    """Print one allow-list decision per simulated login source."""
    for ip_address in LOGIN_SOURCE_IPS:
        status = check_ip_address(ip_address, ALLOW_LIST)
        print(f"{ip_address}: {status}")


if __name__ == "__main__":
    main()
