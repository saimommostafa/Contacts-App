import sys
import csv

print("Welcome to Contacts by S. M. Emon")

print("Hi! Would you like to add, check, search, delete contacts, or exit?")

# File to store contacts
contacts_file = "contacts.csv"


# Main function that shows the menu
def start():
    while True:
        try:
            print(
                "\nMenu:"
                "\n1. Add new contacts"
                "\n2. Contacts list"
                "\n3. Search contacts"
                "\n4. Delete a contact"
                "\n5. Exit"
            )
            option = input("Enter option (1/2/3/4/5): ")

            # Ensuring the user enters a valid option
            if option == "1":
                new_contact()

            elif option == "2":
                saved_contacts()

            elif option == "3":
                search_contact()

            elif option == "4":
                delete_contact()

            elif option == "5":
                sys.exit("\nThank you for using Contacts by S. M. Emon.\n")

            else:
                print("\nInvalid option! Please enter a number from 1 to 5.")

        except EOFError:
            sys.exit("\nExiting the program due to EOFError...")
        except KeyboardInterrupt:
            sys.exit("\nThank you for using Contacts by S. M. Emon.\n")


# Load contacts from file into memory
def load_contacts():
    contact_list = []
    try:
        with open(contacts_file, mode="r") as file:
            reader = csv.reader(file)
            contact_list = list(reader)
    except FileNotFoundError:
        print("\nNo contacts found. You can start adding new contacts.")
    return contact_list


# Save contacts to file
def save_contacts():
    with open(contacts_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)


# Global variable to hold all contacts
contacts = load_contacts()


# Add new contacts
def new_contact():
    new = input("\nEnter name and number (comma separated): ")

    # Ensure the input is comma-separated
    if "," in new:
        name, phone = new.split(",", 1)  # Split only once
        contacts.append([name.strip(), phone.strip()])  # Trim spaces
        save_contacts()  # Save the new contact to file
        another()

    else:
        print(
            "Please separate the name and phone with a comma (e.g., Emon, 1234567890)."
        )


# Option for saving another contact with validity of input checked
def another():
    while True:
        response = input("Add another? (y/n): ")
        if response.lower() == "y":
            new_contact()  # Loop to add another contact
            break

        elif response.lower() == "n":
            print("\nContact(s) added successfully!\n")
            break

        else:
            print("\nInvalid option! Choose between y/n")
            continue


# Display all saved contacts
def saved_contacts():
    if not contacts:
        print("\nNo contacts to display.")
    else:
        print("\nContacts list:")
        for index, np in enumerate(contacts, start=1):
            name, phone = np
            print(f"{index}. {name.strip().capitalize()} ➡ {phone.strip()}")


# Search for a contact by name
def search_contact():
    if not contacts:
        print("\nNo contacts to search.")
        return

    search_name = (
        input("\nEnter the name of the contact you want to search for: ")
        .strip()
        .lower()
    )

    # Find matches
    matches = [np for np in contacts if np[0].strip().lower() == search_name]

    if matches:
        print(f"Found {len(matches)} contact(s) matching '{search_name.capitalize()}':")
        for index, contact in enumerate(matches, start=1):
            name, phone = contact
            print(f"{index}. {name.capitalize()} ➡ {phone}")
    else:
        print(f"No contact found with the name '{search_name.capitalize()}'.")


# Delete a contact by name
def delete_contact():
    if not contacts:
        print("\nNo contact to delete.")
        return

    global search_name
    search_name = (
        input("\nEnter the name of the contact you want to delete: ").strip().lower()
    )

    # Find contacts that match the name
    matches = [np for np in contacts if np[0].strip().lower() == search_name]

    if matches:
        print(f"Found {len(matches)} contact(s) matching '{search_name.capitalize()}':")
        for index, contact in enumerate(matches, start=1):
            name, phone = contact
            print(f"{index}. {name.capitalize()} ➡ {phone}")
        dlt_confirmation()

    else:
        print(f"No contact found with the name '{search_name.capitalize()}'.")


# Checking validity of input and then deleting or not
def dlt_confirmation():
    while True:
        confirm = input("\nDo you want to delete these contact(s)? (y/n): ").lower()
        if confirm.lower() == "y":
            # Remove matching contacts
            contacts[:] = [
                np for np in contacts if np[0].strip().lower() != search_name
            ]
            save_contacts()  # Save after deleting
            print(f"\nDeleted contact(s) with the name '{search_name.capitalize()}'.")
            break
        elif confirm.lower() == "n":
            print("\nNo contact was deleted.")
            break
        else:
            print("\nInvalid option! Choose between y/n")
            continue


# Start the program
start()
