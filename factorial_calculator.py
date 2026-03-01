# 12. Factorial Calculator (Recursion)

# Factorial of a number n:
# n! = n × (n-1) × (n-2) × ... × 1
# 5! = 5 × 4 × 3 × 2 × 1 = 120

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)


while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("Program ended.")
        break
    
    if not user_input.isdigit():
        print("Please enter a valid positive number.")
        continue
    
    num = int(user_input)
    
    print("Factorial of", num, "is", factorial(num))
