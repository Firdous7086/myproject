
history = []


def add_history(calculation):
    history.append(calculation)


def show_history():

    print("\n----- CALCULATION HISTORY -----")

    if len(history) == 0:
        print("No calculations available.")

    else:
        for item in history:
            print(item)


def clear_history():

    if len(history) == 0:
        print("History is already empty.")

    else:
        history.clear()
        print("History cleared successfully!")
