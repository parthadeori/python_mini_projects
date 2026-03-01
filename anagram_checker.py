# 14. Anagram Checker

# What is an Anagram?
# Two words are anagrams if:
# -> They contain the same letters
# -> In the same frequency
# -> But possibly in different order
# Example:
# listen → silent ✅
# triangle → integral ✅
# apple → papel ✅
# rat → car ❌

# Basic Idea:
# -> Take two words as input
# -> Convert both to lowercase
# -> Sort both words
# -> Compare
# If sorted words are equal → Anagram
# Else → Not anagram

while True:
    word1 = input("Enter first word (or type 'exit' to stop): ").lower()
    
    if word1 == "exit":
        print("Program ended.")
        break

    word2 = input("Enter second word: ").lower()

    if word2 == "exit":
        print("Program ended.")
        break

    # If lengths are different → not anagram
    if len(word1) != len(word2):
        print("Not an Anagram ❌")
        continue

    char_count = {}

    # Count characters in word1
    for char in word1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Subtract using word2
    for char in word2:
        if char in char_count:
            char_count[char] -= 1
        else:
            print("Not an Anagram ❌")
            break
    else:
        # This runs only if loop didn't break
        for value in char_count.values():
            if value != 0:
                print("Not an Anagram ❌")
                break
        else:
            print("Anagram ✅")
