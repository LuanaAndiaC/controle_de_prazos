# main.py
# Project: Migration Deadline Control with Dates
# Author: Luana Andia da Costa

from datetime import datetime

def calculate_days(start_date, end_date):
    """Calculates the number of days between two dates"""
    delta = end_date - start_date
    return delta.days

def migration_without_adjustment():
    total_deadline = 180
    max_submission_days = 30
    internal_steps = 30
    ccee_deadline = 30
    minimum_required_time = internal_steps + ccee_deadline

    try:
        submission_date_str = input("Submission date of the documentation (dd/mm/yyyy): ")
        submission_date = datetime.strptime(submission_date_str, "%d/%m/%Y")
        today = datetime.today()
        submission_days = calculate_days(today, submission_date)
    except ValueError:
        print("❌ Invalid date format!")
        return

    remaining_days = total_deadline - submission_days

    if submission_days > max_submission_days:
        print("❌ Documentation submitted after the initial deadline.")
    elif remaining_days > minimum_required_time + 30:
        print("✅ Migration without adjustment completed ahead of schedule.")
    elif remaining_days >= minimum_required_time:
        print("⚠️ Migration without adjustment at the deadline limit.")
    else:
        print("❌ Migration without adjustment overdue.")

def migration_with_adjustment():
    total_deadline = 180
    submission_days = 30
    max_adjustment_days = 120
    internal_steps = 30

    try:
        start_date_str = input("Adjustment start date (dd/mm/yyyy): ")
        end_date_str = input("Adjustment end date (dd/mm/yyyy): ")
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
        end_date = datetime.strptime(end_date_str, "%d/%m/%Y")
        adjustment_days = calculate_days(start_date, end_date)
    except ValueError:
        print("❌ Invalid date format!")
        return

    total_used_time = submission_days + adjustment_days + internal_steps

    if adjustment_days < max_adjustment_days:
        remaining = total_deadline - total_used_time
        print(f"✅ Adjustment completed ahead of schedule. {remaining} days remaining.")
    elif adjustment_days == max_adjustment_days:
        print("⚠️ Adjustment at the limit. Migration possible but tight.")
    else:
        print("❌ Adjustment overdue. Migration past the deadline.")

def menu():
    while True:
        print("\n=== MIGRATION DEADLINE CONTROL ===")
        print("1 - Migration without adjustment")
        print("2 - Migration with adjustment")
        print("3 - Exit")

        option = input("Choose an option (1, 2, or 3): ")

        if option == "1":
            migration_without_adjustment()
        elif option == "2":
            migration_with_adjustment()
        elif option == "3":
            print("Exiting the program...")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
