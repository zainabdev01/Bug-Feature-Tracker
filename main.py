"""Bug & Feature Tracker - a simple terminal application."""

entries = []


def add_entry():
    """Add a new bug or feature request."""
    print("\n--- Add Entry ---")
    title = input("Title / short description: ")
    entry_type = input("Type (Bug/Feature): ")
    priority = input("Priority (Low/Medium/High): ")
    status = input("Status (Open/Resolved): ")

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


def main():
    """Show the menu and run the chosen option."""
    while True:
        print("\n=== Bug & Feature Tracker ===")
        print("1. Add an entry")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_entry()
        elif choice == "4":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()