
def get_number(message):

    while True:
        try:
            number = float(input(message))
            return number

        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_choice():

    while True:
        choice = input("Enter your choice (1-10): ")

        if choice.isdigit() and 1 <= int(choice) <= 10:
            return int(choice)

        else:
            print("Invalid choice! Please select between 1 and 10.")
