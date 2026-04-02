import sys
import calculator

def print_menu():
    print("\n--- Python Git-Flow Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

def _ab():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def main():
    while True:
        print_menu()
        choice = input("Select: ")
        if choice == '0': print("Goodbye!"); break
        try:
            if   choice == '1':  a,b = _ab(); print(calculator.add(a,b))
            # elif choice == '2':  a,b = _ab(); print(calculator.subtract(a,b)) # hotfix 1
            # elif choice == '3':  a,b = _ab(); print(calculator.multiply(a,b)) # hotfix 2
            elif choice == '4':  a,b = _ab(); print(calculator.divide(a,b))
            else: print('Invalid option') # bugfix 1
        except Exception as e:
            print(f'Error: {e}') # bugfix 2
            pass

if __name__ == "__main__":
    main()
