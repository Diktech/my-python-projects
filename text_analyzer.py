text = input("Enter a sentence: ")

# Cleaned version for vowel counting
cleaned = text.strip().lower()

vowels = "aeiou"
vowel_count = sum(1 for char in cleaned if char in vowels)
word_count = len(cleaned.split())

print("\n--- Text Analysis ---")
print(f"Original: {text}")
print(f"Characters (with spaces): {len(text)}")
print(f"Words: {word_count}")
print(f"Vowels: {vowel_count}")
print(f"UPPERCASE: {text.upper()}")
print(f"lowercase: {text.lower()}")
