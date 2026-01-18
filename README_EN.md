from datetime import datetime

# Additional deadlines
INTERNAL_STEPS = 30  # Number of days required for internal steps
CCEE_DEADLINE = 30   # Number of days required for CCEE deadline

def calculate_days(start_date, end_date):
    """Returns the number of days between two dates."""
    return (end_date - start_date).days

def show_explanation(days_remaining):
    """Shows if there is enough time for internal steps and CCEE deadline."""
    total_required = INTERNAL_STEPS + CCEE_DEADLINE

    if days_remaining >= total_required:
        print(f"✅ {days_remaining} days remaining until the migration final deadline.")
        print(f"👍 With {days_remaining} days, there is enough time for:")
        print(f"- Internal steps: {INTERNAL_STEPS} days")
        print(f"- CCEE deadline: {CCEE_DEADLINE} days")
        print("Everything is on schedule!\n")
    elif days_remaining >= 0:
        print(f"⚠️ Only {days_remaining} days remaining until the migration final deadline!")
        print("It may not be enough time to complete:")
        if days_remaining < INTERNAL_STEPS:
            print(f"- Internal steps (missing {INTERNAL_STEPS - days_remaining} days)")
            print(f"- CCEE deadline: {CCEE_DEADLINE} days")
        else:
            print(f"- Internal steps: {INTERNAL_STEPS} days")
            print(f"- CCEE deadline (missing {CCEE_DEADLINE - (days_remaining - INTERNAL_STEPS)} days)")
        print()
    else:
        print("❌ Deadline missed! The action occurred after the migration final deadline.\n")

def ask_date(message):
    """Asks the user for a date until a valid one is provided."""
    while True:
        try:
            date_str = input(message).strip()
            date = datetime.strptime(date_str, "%d/%m/%Y")
            return date
        except ValueError:
            print("Invalid format! Use dd/mm/yyyy, for example 01/03/2026.")

def main():
    # Step 1: initial dates
    print("=== DEADLINE CHECK ===")
    complaint_acceptance_date = ask_date("Date of complaint acceptance (dd/mm/yyyy): ")
    migration_due_date = ask_date("Expected migration completion date (dd/mm/yyyy): ")

    if migration_due_date <= complaint_acceptance_date:
        print("❌ The expected migration date must be after the complaint acceptance date.")
        return

    print(f"\nThe complaint was accepted on {complaint_acceptance_date.strftime('%d/%m/%Y')}.")
    print(f"The migration is expected to occur on {migration_due_date.strftime('%d/%m/%Y')}.\n")

    # Main menu
    while True:
        print("=== MIGRATION DEADLINE CHECK ===")
        print("1 - Migration without adjustment")
        print("2 - Migration with adjustment")
        print("3 - Exit")
        
        option = input("Choose an option (1, 2, or 3): ").strip()
        
        if option == "1":
            # Migration without adjustment
            submission_date = ask_date("Date of initial documentation submission (dd/mm/yyyy): ")
            days_remaining = calculate_days(submission_date, migration_due_date)
            if days_remaining < 0:
                print("❌ Documentation was submitted after the migration final deadline!\n")
            else:
                print("✅ Migration without adjustment is on track.")
                show_explanation(days_remaining)

        elif option == "2":
            # Migration with adjustment
            adjustment_start_date = ask_date("Adjustment start date (dd/mm/yyyy): ")
            adjustment_end_date = ask_date("Adjustment end date (dd/mm/yyyy): ")
            
            if adjustment_end_date > migration_due_date:
                print("❌ The adjustment ends after the migration final deadline!\n")
            else:
                days_remaining = calculate_days(adjustment_end_date, migration_due_date)
                print("✅ Adjustment completed on time." if days_remaining >= 0 else "❌ Adjustment delayed!")
                show_explanation(days_remaining)

        elif option == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid option! Choose 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
