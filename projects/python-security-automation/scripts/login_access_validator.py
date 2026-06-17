"""Validate simulated login attempts against approved users and devices.

Sample output:
ALLOW: analyst_a used assigned device laptop-101 during business hours.
REVIEW: analyst_b is approved, but tablet-404 is not their assigned device.
DENY: guest_user is not on the approved user list.
REVIEW: analyst_c attempted access outside business hours.
"""

APPROVED_DEVICES = {
    "analyst_a": "laptop-101",
    "analyst_b": "laptop-202",
    "analyst_c": "laptop-303",
}

LOGIN_ATTEMPTS = [
    {"username": "analyst_a", "device_id": "laptop-101", "business_hours": True},
    {"username": "analyst_b", "device_id": "tablet-404", "business_hours": True},
    {"username": "guest_user", "device_id": "laptop-999", "business_hours": True},
    {"username": "analyst_c", "device_id": "laptop-303", "business_hours": False},
]


def validate_login(username, device_id, business_hours):
    """Return a simple access decision for one simulated login attempt."""
    if username not in APPROVED_DEVICES:
        return f"DENY: {username} is not on the approved user list."

    if not business_hours:
        return f"REVIEW: {username} attempted access outside business hours."

    assigned_device = APPROVED_DEVICES[username]

    if device_id != assigned_device:
        return (
            f"REVIEW: {username} is approved, but {device_id} is not their "
            "assigned device."
        )

    return f"ALLOW: {username} used assigned device {device_id} during business hours."


def main():
    """Run the sample access checks."""
    for attempt in LOGIN_ATTEMPTS:
        result = validate_login(
            attempt["username"],
            attempt["device_id"],
            attempt["business_hours"],
        )
        print(result)


if __name__ == "__main__":
    main()
