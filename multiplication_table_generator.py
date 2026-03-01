# 10. Multiplication Table Generator.

# This program will:
# Take input from user
# Generate table of the input value

while True:
    # Take input from user
    number = int(input("\nEnter a number: "))

    # Generate multiplication table
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

    # Ask user if they want to continue
    choice = input("\nDo you want to generate another table? (yes/no): ").lower()

    if choice != "yes":
        print("Program ended. 👋")
        break
