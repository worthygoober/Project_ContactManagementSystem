import re

def add_contact(contacts):
    try:
        email_address = input("\nEnter the new contact's email address: ")
        name = input("Enter the new contact's name: ")
        phone_number = input("Enter the new contact's phone number (eg. 123-456-7890): ")
        address = input("Enter the new contact's address: ")
        if validate_email(email_address):
            if email_address not in contacts:
                contacts[email_address] = {"Name" : name, "Phone Number" : phone_number, "Address" : address}
                print(f"\n{name} has been added to contacts under e-mail address '{email_address}'.")
            else:
                print(f"\n{name} already exists.")
        else:
            print("\nInvalid email address for new contact. Please try again.")
    except Exception as e:
        print(f"\nUnexpected error occured: {e}")

def edit_contact(contacts):
    try:
        email_address = input("\nEnter the contact's e-mail address to edit: ")
        if email_address in contacts:
            detail_to_edit = input("Enter the detail you'd like to edit (Email Address, Name, Phone Number, Address): ")
            if detail_to_edit.lower() == "Email Address":
                new_email = input("Enter the contact's new email address: ")
                if validate_email(new_email):
                    contacts[email_address] = new_email
                    print(f"\n'{new_name}' has been set as the contact name for {email_address}.")
            elif detail_to_edit.lower() == "Name":
                new_name = input("Enter the contact's new name: ")
                contacts[email_address]["Name"] = new_name
                print(f"\n'{new_name}' has been set as the contact name for {email_address}.")
            elif detail_to_edit.lower() == "Phone Number":
                new_phone_number = input("Enter the contact's new phone number: ")
                contacts[email_address]["Phone Number"] = new_phone_number
                print(f"\n'{new_phone_number}' has been set as the contact phone number for {email_address}.")
            elif detail_to_edit.lower() == "Address":
                new_address = input("Enter the contact's new address: ")
                contacts[email_address]["Address"] = new_address
                print(f"\n'{new_address}' has been set as the contact address for {email_address}.")
            else:
                print("\nInvalid input.")
        else:
            print(f"\n'{email_address}' not found in contacts.")
    except Exception as e:
        print(f"\nUnexpected error occured: {e}")

def delete_contact(contacts):
    try:
        email_address = input("\nEnter the contact's e-mail address to delete: ")
        if email_address in contacts:
            del contacts[email_address]
            print(f"\nContact info for '{email_address}' has been deleted.")
        else:
            print("\nContact not found.")
    except Exception as e:
        print(f"\nUnexpected error occured: {e}")

def search_contacts(contacts):
    try:
        email_address = input("\nEnter the email address to search: ")
        if email_address in contacts:
            for email_address, details in contacts.items():
                print(f"\nEmail Address: {email_address}\n    -Name: {details["Name"]}\n    -Phone Number: {details["Phone Number"]}\n    -Address: {details["Address"]}")
                break
        else:
            print("\nE-mail address not found.")
    except Exception as e:
        print(f"\nUnexpected error occured: {e}")

def display_contacts(contacts):
    try:
        for email_address, details in contacts.items():
            print(f"\nEmail Address: {email_address}\n    -Name: {details["Name"]}\n    -Phone Number: {details["Phone Number"]}\n    -Address: {details["Address"]}")
    except:
        print("\nContact list is empty.")

def export_contacts(contacts):
    with open('my_email_contacts.txt','w') as file:
        for email_address, details in contacts.items():
            file.write(f"Email Address: {email_address}\n    -Name: {details["Name"]}\n    -Phone Number: {details["Phone Number"]}\n    -Address: {details["Address"]}\n\n")

def validate_email(email):
    email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-za-z]{2,}$"
    if re.match(email_pattern, email):
        return True
    else:
        return False

email_contacts = {}

while True:
    print("\nWelcome to the Contact Management System!\nMenu:")
    print("1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact(email_contacts)
    elif choice == '2':
        edit_contact(email_contacts)
    elif choice == '3':
        delete_contact(email_contacts)
    elif choice == '4':
        search_contacts(email_contacts)
    elif choice == '5':
        display_contacts(email_contacts)
    elif choice == '6':
        export_contacts(email_contacts)
    elif choice == '7':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")