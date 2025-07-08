import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

print("🎯 Guess the secret number between 1 and 20!")
print("You have 5 attempts.\n")

for attempt in range(1, 6):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == secret_number:
        print("🎉 You got it! The secret number was", secret_number)
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

# If not guessed in 5 tries
else:
    print(f"\n😢 Sorry, you didn't guess it. The number was {secret_number}")
