# 13. Palindrome Checker (String Methods)

# What is a Palindrome?
# A palindrome is a word that reads the same forward and backward.
# Examples:
# madam ✅
# racecar ✅
# python ❌
# level ✅

# Logic
# Take input from user
# Convert to lowercase
# Remove spaces
# Reverse the string
# Compare original with reversed
# Print result

while True:
    text = input("Enter a word (or type 'exit' to stop): ")

    if text.lower() == "exit":
        print("Program ended 👋")
        break

    text = text.lower()
    text = text.replace(" ", "")

    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    if text == reversed_text:
        print("It is a palindrome ✅")
    else:
        print("It is NOT a palindrome ❌")

    print()
