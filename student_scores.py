students = {}

while True:
    action = input("\nOptions: add, show, quit\nWhat do you want to do? ").lower()

    if action == "add":
        name = input("Enter student's name: ")
        score = int(input("Enter score: "))
        students[name] = score
        print(f"{name} added with score {score}")

    elif action == "show":
        print("\n📋 Student Scores:")
        for student, score in students.items():
            print(f"{student}: {score}")

    elif action == "quit":
        print("Exiting...")
        break

    else:
        print("Invalid option.")
