"""Create a readable report from simulated approved-user records.

Sample output:
Approved Users Report
- analyst_a | device: laptop-101 | role: SOC trainee
- analyst_b | device: laptop-202 | role: help desk
- analyst_c | device: laptop-303 | role: security intern
Total approved users: 3
"""

APPROVED_USERS = [
    {"username": "analyst_a", "device_id": "laptop-101", "role": "SOC trainee"},
    {"username": "analyst_b", "device_id": "laptop-202", "role": "help desk"},
    {"username": "analyst_c", "device_id": "laptop-303", "role": "security intern"},
]


def build_user_line(user_record):
    """Format one user record for display."""
    return (
        f"- {user_record['username']} | device: {user_record['device_id']} | "
        f"role: {user_record['role']}"
    )


def build_report(user_records):
    """Return a multi-line approved-users report."""
    report_lines = ["Approved Users Report"]

    for user_record in user_records:
        report_lines.append(build_user_line(user_record))

    report_lines.append(f"Total approved users: {len(user_records)}")
    return "\n".join(report_lines)


def main():
    """Print the simulated approved-users report."""
    print(build_report(APPROVED_USERS))


if __name__ == "__main__":
    main()
