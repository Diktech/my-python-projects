shopping_list = []

while True:
    print("\nOptions: add, remove, show, quit")
    action = input("What do you want to do? ").lower()

    if action == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to your list.")

    elif action == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed.")
        else:
            print(f"{item} not in your list.")

    elif action == "show":
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")

    elif action == "quit":
        print("Exiting... Bye!")
        break

    else:
        print("Invalid option. Try again.")
