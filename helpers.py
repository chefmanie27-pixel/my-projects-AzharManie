#       Grade Calculator:
#       This program calculates the letter grade based on the numeric score input by the user:

#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F

def grade_calculator():
    while True:
        try:
            score = int(input("Please enter your grade score (0-100): "))
            
            # Check if the score is within the realistic 0-100 range
            if score < 0 or score > 100:
                print("[!] Invalid score. Please enter a number between 0 and 100.")
                continue # Restarts the loop to ask the user again
                
            break # Exit the loop if the input is a valid integer between 0 and 100
            
        except ValueError:
            print("[!] Oops! That wasn't a valid number. Please try again.")

    # Your logical conditions (optimized for readability)
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f"The grade for the score {score} is: {grade}")



def budget_tracker():
    print("Welcome to the Budget Tracker!")
    
    # 1. Get the user's total income with basic error handling
    while True:
        try:
            income = float(input("Enter your total monthly income: R"))
            if income < 0:
                print("[!] Income cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("[!] Please enter a valid number for income.")

    total_expenses = 0.0

    # 2. Loop to collect expenses dynamically
    while True:
        action = input("\nWould you like to add an expense? (yes/no): ").strip().lower()
        
        if action in ['no', 'n']:
            break
        elif action in ['yes', 'y']:
            try:
                expense_name = input("What is this expense for? (e.g., Rent, Groceries): ").strip()
                expense_amount = float(input(f"Enter amount for '{expense_name}': R"))
                
                if expense_amount < 0:
                    print("[!] Expense amount cannot be negative.")
                    continue
                
                total_expenses += expense_amount
                print(f"Added R{expense_amount:.2f} for {expense_name}.")
                
            except ValueError:
                print("[!] Invalid amount. Expense not added. Please enter a valid number.")
        else:
            print("[!] Invalid choice. Please type 'yes' or 'no'.")

    # 3. Calculate and display the final budget summary
    remaining_balance = income - total_expenses
    
    print("\n--- Budget Summary ---")
    print(f"Total Income:   R{income:.2f}")
    print(f"Total Expenses: R{total_expenses:.2f}")
    print(f"Remaining:      R{remaining_balance:.2f}")
    
    if remaining_balance < 0:
        print("Warning: You are over budget! Consider cutting back on non-essentials.")
    elif remaining_balance == 0:
        print("You broke perfectly even this month!")
    else:
        print("Great job! You stayed under budget.")