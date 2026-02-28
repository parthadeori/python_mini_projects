# 6. Even/Odd Checker for a Range of Numbers

print("=================================")
print("      EVEN / ODD CHECKER")
print("=================================")

while True:

    # Input section with validation
    try:
        start = int(input("\nEnter start number: "))
        end = int(input("Enter end number: "))
    except ValueError:
        print("❌ Invalid input! Please enter integers only.")
        continue

    # If start is greater than end
    if start > end:
        print("⚠ Start number should be less than or equal to end number.")
        continue

    print("\nResult:")
    print("-----------------")

    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

    # Ask user to try again
    choice = input("\nDo you want to try again? (y/n): ").lower()
    if choice != "y":
        print("\nThank you for using Even / Odd Checker 👋")
        break
