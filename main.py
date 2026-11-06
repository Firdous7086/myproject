
import operations
import history
import menu
import utils


def calculator():

    while True:

        menu.show_menu()

        choice = utils.get_choice()

        if choice == 10:
            print("Thank you for using Smart Calculator!")
            break

        elif choice == 8:
            history.show_history()
            continue

        elif choice == 9:
            history.clear_history()
            continue

        elif choice == 7:

            num = utils.get_number("Enter a number: ")

            result = operations.square_root(num)

            print("Result:", result)

            if not isinstance(result, str):
                history.add_history(f"Square root of {num} = {result}")

        else:

            num1 = utils.get_number("Enter first number: ")
            num2 = utils.get_number("Enter second number: ")

            if choice == 1:
                result = operations.add(num1, num2)
                symbol = "+"

            elif choice == 2:
                result = operations.subtract(num1, num2)
                symbol = "-"

            elif choice == 3:
                result = operations.multiply(num1, num2)
                symbol = "*"

            elif choice == 4:
                result = operations.divide(num1, num2)
                symbol = "/"

            elif choice == 5:
                result = operations.percentage(num1, num2)
                symbol = "% of"

            elif choice == 6:
                result = operations.power(num1, num2)
                symbol = "^"

            print("Result:", result)

            if not isinstance(result, str):
                calculation = f"{num1} {symbol} {num2} = {result}"
                history.add_history(calculation)


if __name__ == "__main__":
    calculator()
