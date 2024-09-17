import re

contacts = {}

def display_menu():
    print("/nwelcome to the Contact Management system!")
    print("Menu:")
    print("1. Add new contact")
    print("2. Add existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a file")
    print("8. Quit")

def validate_phone(phone):
    return re.match(r"^\=?[0-9]{7,15}$",phone)

def validate_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

# Add new contact
def add_contact():
    try:
        phone = input("Enter phone number (unique ID): ")
        if not validate_phone(phone):
            raise ValueError("Invalid phone number format.")
        if phone in contacts:
            print("Contact already exists!")
            return
        
        name = input("Enter contact name: ")
        email = input("Enter email address: ")
        if not validate_email(email):
            raise ValueError("Invalid email format.")
        additional_info = input("Enter additional information (e.g., address, notes): ")
        
        contacts[phone] = {"name": name, "email": email, "additional_info": additional_info}
        print("Contact added successfully!")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Edit contact
def edit_contact():
    phone = input("Enter phone number of the contact to edit: ")
    if phone in contacts:
        try:
            print(f"Editing contact: {contacts[phone]['name']}")
            new_name = input(f"Enter new name (leave blank to keep '{contacts[phone]['name']}'): ") or contacts[phone]['name']
            new_email = input(f"Enter new email (leave blank to keep '{contacts[phone]['email']}'): ") or contacts[phone]['email']
            if not validate_email(new_email):
                raise ValueError("Invalid email format.")
            new_info = input(f"Enter new additional information (leave blank to keep '{contacts[phone]['additional_info']}'): ") or contacts[phone]['additional_info']
            
            contacts[phone] = {"name": new_name, "email": new_email, "additional_info": new_info}
            print("Contact updated successfully!")
        except ValueError as ve:
            print(f"Error: {ve}")
    else:
        print("Contact not found.")

# Delete contact
def delete_contact():
    phone = input("Enter phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

# Search for contact
def search_contact():
    phone = input("Enter phone number of the contact to search: ")
    if phone in contacts:
        contact = contacts[phone]
        print(f"Name: {contact['name']}, Email: {contact['email']}, Additional Info: {contact['additional_info']}")
    else:
        print("Contact not found.")

# Display all contacts
def display_all_contacts():
    if contacts:
        for phone, details in contacts.items():
            print(f"Phone: {phone}, Name: {details['name']}, Email: {details['email']}, Additional Info: {details['additional_info']}")
    else:
        print("No contacts to display.")

# Export contacts to a file
def export_contacts():
    try:
        with open('contacts.txt', 'w') as file:
            for phone, details in contacts.items():
                file.write(f"{phone},{details['name']},{details['email']},{details['additional_info']}\n")
        print("Contacts exported successfully to 'contacts.txt'.")
    except Exception as e:
        print(f"An error occurred during export: {e}")

# Import contacts from a file *BONUS*
def import_contacts():
    try:
        with open('contacts.txt', 'r') as file:
            for line in file:
                phone, name, email, additional_info = line.strip().split(',')
                contacts[phone] = {"name": name, "email": email, "additional_info": additional_info}
        print("Contacts imported successfully from 'contacts.txt'.")
    except Exception as e:
        print(f"An error occurred during import: {e}")

# Main loop
def main():
    while True:
        display_menu()
        try:
            choice = int(input("Select an option (1-8): "))
            if choice == 1:
                add_contact()
            elif choice == 2:
                edit_contact()
            elif choice == 3:
                delete_contact()
            elif choice == 4:
                search_contact()
            elif choice == 5:
                display_all_contacts()
            elif choice == 6:
                export_contacts()
            elif choice == 7:
                import_contacts()
            elif choice == 8:
                print("Goodbye!")
                break
            else:
                print("Invalid option, please choose a valid menu item.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
