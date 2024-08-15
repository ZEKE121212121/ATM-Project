class Atm:
    def __init__(self):
        """
        Initializes the ATM with a default PIN (None) and balance (0),
        then calls the menu method to start user interaction.
        """
        self.__pin = None  # attribute
        self.__balance = 0  #  balance attribute
        self.__menu()  # Start the ATM menu

    def __menu(self):
        """
        Displays the ATM menu and handles user input to navigate through different options.
        """
        while True:
            print("\n--- ATM Menu ---")
            print("1. Generate PIN")
            print("2. Change PIN")
            print("3. Check Balance")
            print("4. Withdraw")
            print("5. Deposit")
            print("6. Exit")

            choice = input("Select an option: ")

            if choice == '1':
                self.__generate_pin()
            elif choice == '2':
                self.__change_pin()
            elif choice == '3':
                self.__check_balance()
            elif choice == '4':
                self.__withdraw()
            elif choice == '5':
                self.__deposit()
            elif choice == '6':
                print("Exiting... Thank you for using the ATM.")
                break
            else:
                print("Invalid option. Please try again.")

    def __get_pin(self):
        """
        Prompts the user to enter a 4-digit PIN and validates its format.

        Returns:
            str: The valid 4-digit PIN entered by the user, or None if invalid.
        """
        pin = input("Enter a 4-digit PIN: ")
        if pin.isdigit() and len(pin) == 4:
            return pin
        else:
            print("Invalid PIN format. Please ensure it's a 4-digit number.")
            return None

    def __verify_pin(self):
        """
        Prompts the user to enter the current PIN and checks if it matches the stored PIN.

        Returns:
            bool: True if the entered PIN matches the stored PIN, False otherwise.
        """
        if self.__pin is None:
            print("No PIN is set. Please generate a PIN first.")
            return False
        pin = input("Enter your current PIN: ")
        if pin == self.__pin:
            return True
        else:
            print("Incorrect PIN.")
            return False

    def __generate_pin(self):
        """
        Allows the user to generate a new PIN if one is not already set.
        """
        if self.__pin is not None:
            print("PIN is already set. Use the 'Change PIN' option to modify it.")
            return
        new_pin = self.__get_pin()
        if new_pin:
            confirm_pin = input("Confirm your PIN: ")
            if new_pin == confirm_pin:
                self.__pin = new_pin
                print("PIN set successfully!")
            else:
                print("PINs do not match. PIN generation failed.")

    def __change_pin(self):
        """
        Allows the user to change the existing PIN after verifying the current PIN.
        """
        if self.__verify_pin():
            new_pin = self.__get_pin()
            if new_pin:
                confirm_pin = input("Confirm your new PIN: ")
                if new_pin == confirm_pin:
                    self.__pin = new_pin
                    print("PIN changed successfully!")
                else:
                    print("PINs do not match. PIN change failed.")

    def __check_balance(self):
        """
        Displays the current account balance after successful PIN verification.
        """
        if self.__verify_pin():
            print(f"Your current balance is: ${self.__balance}")

    def __withdraw(self):
        """
        Allows the user to withdraw money from the account after PIN verification.
        Ensures that the withdrawal amount is a multiple of 100 and does not exceed the current balance.
        """
        if self.__verify_pin():
            try:
                amount = int(input("Enter the amount to withdraw (multiple of 100): "))
                if amount <= 0:
                    print("Withdrawal amount must be greater than zero.")
                elif amount % 100 != 0:
                    print("Amount must be a multiple of 100.")
                elif amount > self.__balance:
                    print("Insufficient balance.")
                else:
                    self.__balance -= amount
                    print(f"Withdrawn ${amount}. Current balance: ${self.__balance}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def __deposit(self):
        """
        Allows the user to deposit money into the account after PIN verification.
        Ensures that the deposit amount is a multiple of 100 and greater than zero.
        """
        if self.__verify_pin():
            try:
                amount = int(input("Enter the amount to deposit (multiple of 100): "))
                if amount <= 0:
                    print("Deposit amount must be greater than zero.")
                elif amount % 100 != 0:
                    print("Amount must be a multiple of 100.")
                else:
                    self.__balance += amount
                    print(f"Deposited ${amount}. Current balance: ${self.__balance}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

# start the program
if __name__ == "__main__":
    Atm()

