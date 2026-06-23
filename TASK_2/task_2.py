total = 0
print("Enter expense amounts one by one. Type 'quit' to stop and show the total.")
print("You can enter 5 or more transactions.")

while True:
    new_expense = input("Enter expense amount or 'quit': ")
    if new_expense.lower() == "quit":
        print(f"The Final Total is {total}. Exiting...")
        break

    try:
        new_expense = float(new_expense)
    except ValueError:
        print("Invalid input. Please enter a numeric expense amount.")
        continue

    total += new_expense
    print(f"Added {new_expense:.2f}. Total Spent so far: {total:.2f}")