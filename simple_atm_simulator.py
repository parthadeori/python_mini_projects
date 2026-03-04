# 16. Simple ATM Simulator (while Loops, Functions)

# Features
# Your ATM should allow a user to:
# 1️⃣ Check Balance
# 2️⃣ Deposit Money
# 3️⃣ Withdraw Money
# 4️⃣ Exit
# The program should run continuously using a while loop until the user chooses Exit.

balance = 1000


def check_balance(balance):
    print("Your balance is:", balance)


def deposit(balance):
    amount = int(input("Enter amount to deposit: "))
    balance = balance + amount
    print("Deposit successful.")
    return balance


def withdraw(balance):
    amount = int(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient balance!")
    else:
        balance = balance - amount
        print("Withdrawal successful.")

    return balance


while True:

    print("\n------ ATM MENU ------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        check_balance(balance)

    elif choice == "2":
        balance = deposit(balance)

    elif choice == "3":
        balance = withdraw(balance)

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid option. Try again.")
