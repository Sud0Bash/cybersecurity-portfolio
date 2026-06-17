"""Generate simple simulated employee IDs for lab account setup.

Sample output:
SEC-0500
SEC-0505
SEC-0510
SEC-0515
SEC-0520
"""

ID_PREFIX = "SEC"
START_ID = 500
STOP_ID = 520
STEP = 5


def format_employee_id(number):
    """Convert a number into a consistent portfolio-safe employee ID."""
    return f"{ID_PREFIX}-{number:04d}"


def generate_employee_ids(start_id, stop_id, step):
    """Return a list of generated IDs from start_id through stop_id."""
    employee_ids = []

    for number in range(start_id, stop_id + 1, step):
        employee_ids.append(format_employee_id(number))

    return employee_ids


def main():
    """Print a small set of simulated employee IDs."""
    for employee_id in generate_employee_ids(START_ID, STOP_ID, STEP):
        print(employee_id)


if __name__ == "__main__":
    main()
