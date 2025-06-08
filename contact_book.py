# Contact Book Project
# Author: Harsh Pawar
# Date: June 2025
# Description: A simple contact book application using Python with file-based storage.

while True:
    print('\nWELCOME TO CONTACT BOOK')
    print('1. Add Contact')
    print('2. View Contact')
    print('3. Delete Contact')
    print('4. Update Contact')
    print('5. Block/Unblock Contact')
    print('6. Exit')

    ask = input("Enter your option: ")

    # Add Contact
    if ask == '1' or ask.lower() == 'add':
        file = open('sample.txt', 'a')
        name = input("Enter name: ")
        number = input("Enter number: ")
        file.write(f"{name}--{number}--Active\n")
        file.close()
        print("Contact added successfully.")

    # View Contact
    elif ask == '2' or ask.lower() == 'view':
        try:
            file = open('sample.txt', 'r')
            lines = file.readlines()
            file.close()

            print("\n--- Your Contacts ---")
            found = False
            for line in lines:
                if "Active" in line:
                    print(line.strip())
                    found = True
            if not found:
                print("No active contacts found.")
        except FileNotFoundError:
            print("No contact file found.")

    # Delete Contact
    elif ask == '3' or ask.lower() == 'delete':
        to_delete = input("Enter name or number to delete: ")
        try:
            file = open('sample.txt', 'r')
            lines = file.readlines()
            file.close()

            new_lines = []
            found = False
            for line in lines:
                if to_delete in line:
                    found = True
                else:
                    new_lines.append(line)

            file = open('sample.txt', 'w')
            file.writelines(new_lines)
            file.close()

            if found:
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")

        except FileNotFoundError:
            print("No contact file found.")

    # Update Contact
    elif ask == '4' or ask.lower() == 'update':
        to_update = input("Enter name or number to update: ")

        file = open('sample.txt', 'r')
        lines = file.readlines()
        file.close()

        updated = []
        found = False
        for line in lines:
            if to_update in line:
                new_name = input("Enter new name: ")
                new_number = input("Enter new number: ")
                status = "Blocked" if "Blocked" in line else "Active"
                updated.append(f"{new_name}--{new_number}--{status}\n")
                found = True
            else:
                updated.append(line)

        file = open('sample.txt', 'w')
        file.writelines(updated)
        file.close()

        if found:
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    # Block/Unblock Contact
    elif ask == '5' or ask.lower() == 'block':
        to_change = input("Enter name or number to block/unblock: ")

        file = open('sample.txt', 'r')
        lines = file.readlines()
        file.close()

        changed = []
        found = False
        for line in lines:
            if to_change in line:
                found = True
                if "Active" in line:
                    changed.append(line.replace("Active", "Blocked"))
                elif "Blocked" in line:
                    changed.append(line.replace("Blocked", "Active"))
            else:
                changed.append(line)

        file = open('sample.txt', 'w')
        file.writelines(changed)
        file.close()

        if found:
            print("Contact status changed (Blocked/Unblocked).")
        else:
            print("Contact not found.")

    # Exit
    elif ask == '6' or ask.lower() == 'exit':
        print("Exiting from contact book...")
        break

    else:
        print("Invalid option. Try again.")
