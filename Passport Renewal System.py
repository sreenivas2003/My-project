from datetime import datetime, timedelta
import random
import string

class PassportRenewalSystem:
    def __init__(self):
        self.renewal_records = {}
        self.progress_reports = {}

    def generate_renewal_id(self):
        prefix = random.choice(string.ascii_uppercase)
        random_numbers = ''.join(random.choices(string.digits, k=10))
        renewal_id = prefix + random_numbers
        return renewal_id

    def create_renewal_record(self, details):
        renewal_id = self.generate_renewal_id()
        details['name'] = input("Enter name: ")
        details['nationality'] = input("Enter nationality: ")
        details['date_of_birth'] = input("Enter date of birth (DD-MM-YYYY): ")
        details['passport_number'] = input("Enter passport number: ")
        details['expiry_date'] = input("Enter expiry date (DD-MM-YYYY): ")
        details['application_date'] = datetime.now().strftime('%d-%m-%Y')  # Generate application date
        self.renewal_records[renewal_id] = details
        print(f"Renewal record created for ID {renewal_id}.")

    def retrieve_renewal_record(self, renewal_id):
        return self.renewal_records.get(renewal_id)

    def read_renewal_record(self, renewal_id):
        record = self.retrieve_renewal_record(renewal_id)
        if record:
            print(f"Renewal Record ID: {renewal_id}")
            for key, value in record.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print(f"No renewal record found for ID {renewal_id}.")

    def update_renewal_record(self, renewal_id):
        if renewal_id in self.renewal_records:
            current_expiry_date = self.renewal_records[renewal_id].get('expiry_date')
            if current_expiry_date:
                current_expiry_date = datetime.strptime(current_expiry_date, '%d-%m-%Y')
                if current_expiry_date < datetime.now():
                    # Expiry date is in the past, update it to 10 years later
                    new_expiry_date = (datetime.now() + timedelta(days=3650)).strftime('%d-%m-%Y')
                    self.renewal_records[renewal_id]['expiry_date'] = new_expiry_date
                    print(f"Expiry date has passed. Updated to {new_expiry_date}")
                    print(f"Renewal record with ID {renewal_id} updated.")
                else:
                    print("Expiry date is not in the past. No update needed.")
                    print(f"Current expiry date: {current_expiry_date.strftime('%d-%m-%Y')}")
            else:
                print("No expiry date found for this record.")
        else:
            print(f"No renewal record found for ID {renewal_id}.")

    def delete_renewal_record(self, renewal_id):
        if renewal_id in self.renewal_records:
            del self.renewal_records[renewal_id]
            print(f"Renewal record with ID {renewal_id} deleted.")
        else:
            print(f"No renewal record found for ID {renewal_id}.")

    def handle_passport_renewals(self, renewal_id):
        record = self.retrieve_renewal_record(renewal_id)
        if record:
            expiry_date = record.get('expiry_date')
            if expiry_date:
                expiry_date = datetime.strptime(expiry_date, '%d-%m-%Y')
                if expiry_date < datetime.now():
                    fee_paid = input("Has the fee been paid? (yes/no): ").lower()
                    if fee_paid == 'yes':
                        print(f"Passport renewal for ID {renewal_id} is being processed.")
                        self.progress_reports[renewal_id] = "In Progress"
                    else:
                        print("Fee not paid. Passport renewal process aborted.")
                else:
                    print("Passport is not expired yet. Renewal process cannot proceed.")
            else:
                print("No expiry date found for this record.")
        else:
            print(f"No renewal record found for ID {renewal_id}. Record may have been deleted or not found.")

    def monitor_renewal_progress(self, progress_id):
        if progress_id in self.progress_reports:
            expiry_date = self.renewal_records.get(progress_id, {}).get('expiry_date')
            if expiry_date:
                expiry_date = datetime.strptime(expiry_date, '%d-%m-%Y')
                if expiry_date < datetime.now():
                    application_date = self.renewal_records.get(progress_id, {}).get('application_date')
                    application_date = datetime.strptime(application_date, '%d-%m-%Y')
                    days_passed = (datetime.now() - application_date).days
                    if days_passed <= 15:
                        print(f"Renewal process with ID {progress_id} has just started.")
                    elif 15 < days_passed <= 30:
                        print(f"Renewal process with ID {progress_id} is making progress.")
                    elif 30 < days_passed <= 60:
                        print(f"Renewal process with ID {progress_id} is almost completed.")
                    else:
                        print(f"Renewal process with ID {progress_id} has taken longer than usual.")
                        print("Please check the status.")
                else:
                    print("Passport is not expired yet. Renewal process cannot proceed.")
            else:
                print("No expiry date found for this record.")
        else:
            print(f"No progress report found for ID {progress_id}.")

# Example usage:
passport_system = PassportRenewalSystem()

while True:
    print("\n1. Create Renewal Record\n2. Read Renewal Record\n3. Update Renewal Record")
    print("4. Delete Renewal Record\n5. Handle Passport Renewals\n6. Monitor Renewal Progress\n7. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        details = {}
        passport_system.create_renewal_record(details)
    elif choice == '2':
        renewal_id = input("Enter renewal ID to read: ")
        passport_system.read_renewal_record(renewal_id)
    elif choice == '3':
        renewal_id = input("Enter renewal ID to update: ")
        passport_system.update_renewal_record(renewal_id)
    elif choice == '4':
        renewal_id = input("Enter renewal ID to delete: ")
        passport_system.delete_renewal_record(renewal_id)
    elif choice == '5':
        renewal_id = input("Enter renewal ID to handle passport renewals: ")
        passport_system.handle_passport_renewals(renewal_id)
    elif choice == '6':
        progress_id = input("Enter progress ID to monitor renewal progress: ")
        passport_system.monitor_renewal_progress(progress_id)
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please enter a valid option.")

output:
1. Create Renewal Record
2. Read Renewal Record
3. Update Renewal Record
4. Delete Renewal Record
5. Handle Passport Renewals
6. Monitor Renewal Progress
7. Exit
Enter your choice: 1
Enter name: Shraddha
Enter nationality: INDIAN
Enter date of birth (DD-MM-YYYY): 11-05-2004
Enter passport number: 237890456729
Enter expiry date (DD-MM-YYYY): 28-04-2024
Renewal record created for ID L5662745043.

1. Create Renewal Record
2. Read Renewal Record
3. Update Renewal Record
4. Delete Renewal Record
5. Handle Passport Renewals
6. Monitor Renewal Progress
7. Exit
Enter your choice: 2
Enter renewal ID to read: L5662745043
Renewal Record ID: L5662745043
Name: Shraddha
Nationality: INDIAN
Date_of_birth: 11-05-2004
Passport_number: 237890456729
Expiry_date: 28-04-2024
Application_date: 03-05-2024

1. Create Renewal Record
2. Read Renewal Record
3. Update Renewal Record
4. Delete Renewal Record
5. Handle Passport Renewals
6. Monitor Renewal Progress
7. Exit
Enter your choice: 5
Enter renewal ID to handle passport renewals: L5662745043
Has the fee been paid? (yes/no): yes
Passport renewal for ID L5662745043 is being processed.

1. Create Renewal Record
2. Read Renewal Record
3. Update Renewal Record
4. Delete Renewal Record
5. Handle Passport Renewals
6. Monitor Renewal Progress
7. Exit
Enter your choice: 6
Enter progress ID to monitor renewal progress: L5662745043
Renewal process with ID L5662745043 has just started.

1. Create Renewal Record
2. Read Renewal Record
3. Update Renewal Record
4. Delete Renewal Record
5. Handle Passport Renewals
6. Monitor Renewal Progress
7. Exit
Enter your choice: 3
Enter renewal ID to update: L5662745043
Expiry date has passed. Updated to 01-05-2034
Renewal record with ID L5662745043 updated.

1. Create Renewal Record
2. Read Renewal Record
3. Update Renewal Record
4. Delete Renewal Record
5. Handle Passport Renewals
6. Monitor Renewal Progress
7. Exit
Enter your choice: 4
Enter renewal ID to delete: L5662745043
Renewal record with ID L5662745043 deleted.

1. Create Renewal Record
2. Read Renewal Record
3. Update Renewal Record
4. Delete Renewal Record
5. Handle Passport Renewals
6. Monitor Renewal Progress
7. Exit
Enter your choice: 7

=== Code Execution Successful ===
