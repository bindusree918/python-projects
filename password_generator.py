import random
import string

print("🔐 Password Generator 🔐")

# Get valid password length
while True:
    length_input = input("Enter password length: ")
    if length_input.isdigit() and int(length_input) > 0:
        length = int(length_input)
        break
    else:
        print("❌ Please enter a valid positive number!")

# Get number of passwords
while True:
    count_input = input("How many passwords do you want?: ")
    if count_input.isdigit() and int(count_input) > 0:
        count = int(count_input)
        break
    else:
        print("❌ Please enter a valid positive number!")

# Ask user preferences
print("\nInclude in password:")
use_letters = input("Letters? (yes/no): ").strip().lower()
use_numbers = input("Numbers? (yes/no): ").strip().lower()
use_symbols = input("Symbols? (yes/no): ").strip().lower()

# Build character pool
characters = ""

if use_letters == "yes":
    characters += string.ascii_letters

if use_numbers == "yes":
    characters += string.digits

if use_symbols == "yes":
    characters += string.punctuation

# Check if at least one option selected
if not characters:
    print("❌ You must select at least one character type!")
else:
    print("\n✅ Generated Passwords:\n")

    for i in range(count):
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"{i + 1}: {password}")