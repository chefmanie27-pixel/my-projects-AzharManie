import helpers  

def main_menu():
    while True:
        # 1. Display the menu options
        print("\n" + "="*35)
        print("Welcome to my program! Please select an option:")
        print("1. Grade Calculator")
        print("2. Budget Tracker")
        print("3. Number Guessing Game")
        print("4. Even or Odd Checker")
        print("5. Exit Program")
        print("="*35)

        # 2. Get clean input from the user
        menu_option = input("Please select an option (1-5): ").strip()

        # 3. Route the user to the correct helper function
        if menu_option == "1":
            print("\n--- Launching Grade Calculator ---")
            helpers.grade_calculator() # Calls the function in helpers.py
            
        elif menu_option == "2":
            print("\n--- Launching Budget Tracker ---")
            helpers.budget_tracker()
            
        elif menu_option == "3":
            print("\n--- Launching Number Guessing Game ---")
            helpers.guessing_game()
            
        elif menu_option == "4":
            print("\n--- Launching Even or Odd Checker ---")
            helpers.even_or_odd()
            
        elif menu_option == "5":
            print("\nThank you for using the program. Goodbye!")
            break # This breaks the while loop and closes the program cleanly
            
        else:
            print("\n[!] Invalid option. Please enter a number between 1 and 5.")

# This line ensures the menu runs when you hit 'Run' on this file
if __name__ == "__main__":
    main_menu()