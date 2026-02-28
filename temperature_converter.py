# 3. Temperature Converter

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9


while True:
    print("\n=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Choose option (1/2/3): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        print("Fahrenheit:", c_to_f(c))

    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Celsius:", f_to_c(f))

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
