# 5. Mad Libs Generator

# What Mad Libs Generator Should Do
# Your program should:
# 1️⃣ Ask the user for different words
# For example:
# A name
# A place
# An adjective
# A verb
# A noun
# An animal
# You’ll collect these using input() and store them in variables.
# 2️⃣ Insert those words into a funny story template
# You’ll create a story like this:
# One day, {name} went to {place}.
# It was a very {adjective} day.
# Suddenly, a {animal} started to {verb} near a {noun}!
# And that’s how the adventure began.
# 3️⃣ Print the Final Story
# After inserting the words, print the complete story nicely formatted.

print("🎉 Welcome to Mad Libs Generator! 🎉")

while True:
    print("\nPlease enter the following words:\n")

    name = input("Enter a name: ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    noun = input("Enter a noun: ")
    animal = input("Enter an animal: ")

    print("\n--- Your Story ---\n")

    story = f"""
One day, {name} went to {place}.
It was a very {adjective} day.
Suddenly, a {animal} started to {verb} near a {noun}!
And that’s how the adventure began!
"""

    print(story)

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing! Goodbye 👋")
        break
