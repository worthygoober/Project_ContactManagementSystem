import re

def add_contact(contacts):
    try:
        email_address = input("Enter the contact's email address: ")
        name = input("Enter the new contact's name: ")
        phone_number = input("Enter the contact's phone number (eg. 123-456-7890): ")
        address = input("Enter the contact's address: ")
        if validate_email(email_address):
            if email_address not in contacts:
                contacts[email_address] = {"Name" : name, "Phone Number" : phone_number, "Address" : address}
                print(f"{name} has been added to contacts under e-mail address '{email_address}'.")
                # print(contacts)
            else:
                print(f"{name} already exists.")
    except Exception as e:
        print(f"Unexpected error occured: {e}")

def edit_contact(contacts):
    pass

def delete_contact(contacts):
    try:
        email_address = input("Enter the contact's e-mail address to delete: ")
        if email_address in contacts:
            del contacts[email_address]
            print(f"Contact info for '{email_address}' has been deleted.")
        else:
            print("Contact not found.")
    except Exception as e:
        print(f"Unexpected error occured: {e}")

def search_contacts(contacts):
    email_address = input("Enter the email address to search: ")
    email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-za-z]{2,}$"
    

    

def display_contacts(contacts):
    try:
        for email_address, details in contacts.items():
            print(f"Email Address: {email_address}\n    -Name: {details["Name"]}\n    -Phone Number: {details["Phone Number"]}\n    -Address: {details["Address"]}")
    except:
        print("Contact list is empty.")

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