contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"{name} added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n📇 Contact List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted.")
    else:
        print("Contact not found.")

while True:
    print("\nOptions: add, view, search, delete, quit")
    choice = input("What would you like to do? ").lower()

    if choice == "add":
        add_contact()
    elif choice == "view":
        view_contacts()
    elif choice == "search":
        search_contact()
    elif choice == "delete":
        delete_contact()
    elif choice == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
