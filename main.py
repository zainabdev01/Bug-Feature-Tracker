"""Bug & Feature Tracker - a simple terminal application.

Records bugs and feature requests in memory, lists them,
and shows summary statistics.
"""

VALID_TYPES = ("Bug", "Feature")
VALID_PRIORITIES = ("Low", "Medium", "High")
VALID_STATUSES = ("Open", "Resolved")

entries = []


def read_title():
    """Ask for a non-empty title; return None if the user leaves it empty."""
    title = input("Title / short description: ").strip()
    if not title:
        print("Error: the title cannot be empty.")
        return None
    return title


def read_choice(prompt, options):
    """Ask the user to pick one of `options` (case-insensitive)."""
    lookup = {option.lower(): option for option in options}
    answer = input(f"{prompt} ({'/'.join(options)}): ").strip().lower()
    if answer not in lookup:
        print(f"Error: please enter one of: {', '.join(options)}.")
        return None
    return lookup[answer]


def add_entry():
    """Feature 1: add a new bug or feature request."""
    print("\n--- Add Entry ---")
    title = read_title()
    if title is None:
        return
    entry_type = read_choice("Type", VALID_TYPES)
    if entry_type is None:
        return
    priority = read_choice("Priority", VALID_PRIORITIES)
    if priority is None:
        return
    status = read_choice("Status", VALID_STATUSES)
    if status is None:
        return

    entries.append(
        {
            "id": len(entries) + 1,
            "title": title,
            "type": entry_type,
            "priority": priority,
            "status": status,
        }
    )
    print("Entry added successfully.")


def view_entries():
    """Feature 2: display all entries in a readable table."""
    print("\n--- All Entries ---")
    if not entries:
        print("No entries recorded yet.")
        return
    print(f"{'ID':<4}{'Type':<10}{'Priority':<10}{'Status':<10}Title")
    print("-" * 60)
    for e in entries:
        print(f"{e['id']:<4}{e['type']:<10}{e['priority']:<10}{e['status']:<10}{e['title']}")


def show_statistics():
    """Feature 3: display summary statistics."""
    print("\n--- Summary Statistics ---")
    print(f"Total entries:     {len(entries)}")
    print(f"Bugs:              {sum(e['type'] == 'Bug' for e in entries)}")
    print(f"Feature requests:  {sum(e['type'] == 'Feature' for e in entries)}")
    print(f"Open entries:      {sum(e['status'] == 'Open' for e in entries)}")
    print(f"Resolved entries:  {sum(e['status'] == 'Resolved' for e in entries)}")


def main():
    """Feature 4: menu and navigation loop."""
    actions = {"1": add_entry, "2": view_entries, "3": show_statistics}
    while True:
        print("\n=== Bug & Feature Tracker ===")
        print("1. Add an entry")
        print("2. View all entries")
        print("3. View summary statistics")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "4":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please enter a number from 1 to 4.")
        else:
            action()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")

