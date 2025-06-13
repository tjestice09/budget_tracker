import os
import json

DATA_FILE = "budget_data.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"income": 0.0, "expenses": 0.0}, f, indent=4)



def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        return {"income": 0.0, "expenses": 0.0}

def save_data(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def main():
    DATA_FILE = "budget_data.json"
    data = load_data(DATA_FILE)

    while True:
        print("\n ------ Budget Tracker Menu ------")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            amount = float(input("Enter Income Amount:"))
            data["income"] += amount
            print(f"Added ${amount:.2f} income.")
        elif choice == "2":
            amount = float(input("Enter Expense Amount:"))
            data["expenses"] += amount
            print(f"Added ${amount:.2f} expenses.")
        elif choice == "3":
            balance = data["income"] - data["expenses"]
            print(f"\nIncome: ${data['income']:.2f}")
            print(f"\nExpenses: ${data['expenses']:.2f}")
            print(f"\nBalance: ${balance:.2f}")
        elif choice == "4":
            save_data(data, DATA_FILE)
            print("Goodbye! Your data has been saved..have a great day!")
            break
        else:
            print("Invalid Option. Please choose a different option")

if __name__ == "__main__":
    main()