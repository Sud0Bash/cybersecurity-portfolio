"""Summarize simulated security event counts.

Sample output:
Security Event Summary
Total events: 33
Highest category: failed_login with 18 events
Categories needing review:
- failed_login: 18
- blocked_ip: 7
"""

EVENT_COUNTS = {
    "failed_login": 18,
    "blocked_ip": 7,
    "malware_alert": 1,
    "password_reset": 4,
    "new_device": 3,
}

REVIEW_THRESHOLD = 5


def find_highest_category(event_counts):
    """Return the event category with the largest count."""
    return max(event_counts, key=event_counts.get)


def categories_needing_review(event_counts, threshold):
    """Return categories with counts greater than or equal to threshold."""
    review_categories = {}

    for category, count in event_counts.items():
        if count >= threshold:
            review_categories[category] = count

    return review_categories


def print_summary(event_counts, threshold):
    """Print a beginner-friendly summary of simulated event totals."""
    total_events = sum(event_counts.values())
    highest_category = find_highest_category(event_counts)
    review_categories = categories_needing_review(event_counts, threshold)

    print("Security Event Summary")
    print(f"Total events: {total_events}")
    print(
        f"Highest category: {highest_category} "
        f"with {event_counts[highest_category]} events"
    )
    print("Categories needing review:")

    for category, count in review_categories.items():
        print(f"- {category}: {count}")


def main():
    """Run the simulated event summary."""
    print_summary(EVENT_COUNTS, REVIEW_THRESHOLD)


if __name__ == "__main__":
    main()
