print(">>> Starting script...")

name = input("What's your name? ")
age = int(input("How old are you? "))
height = float(input("What's your height (in meters)? "))
is_happy = input("Are you happy today? (yes/no): ") == "yes"

print("\nProfile Summary:")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Happy today?", is_happy)
