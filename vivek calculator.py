class Calculator:

    def add(self, x: float, y: float,)-> float:
        return x + y

    def subtract(self, x: float, y: float)-> float:
        return x - y

    def multiply(self, x: float, y: float)-> float:
        return x * y

    def devision(self, x: float, y: float) -> float | str:
        if y == 0:
            return "error not defined by zero"
        return x / y

def main():
    calc = Calculator()

    print("Welcome to the OOP Calculator!")
    print("select an operation:")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. divide")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ").strip()

        if choice == '5':
            print("exiting caclculator. goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("enter first number: "))
                num2 = float(input("enter second number: "))
            except ValueError:
                print("invalid input. please enter valid numeric values.")
                continue
        if choice == '1':
            print(f"result: {num1}+{num2} = {calc.add(num1,num2)}")
        elif choice == '2':
            print(f"result: {num1} - {num2} = {calc.subtract(num1,num2)}")
        elif choice =='3':
            print (f"result: {num1} * {num2} = {calc.multiply(num1,num2)}")
        elif choice == '4':
            print(f"result: {num1} / {num2} = {calc.devision(num1, num2)}")
    else:
        print("invalid choice. please select a valid option.")

if __name__ == "__main__":
    main()
