Name : Amruta Varsha Yadav Pigili

OctaNet Python Internship

Task: 1 - ATM Interface

Description :
The ATM's in our cities are built on python, as we have all seen them. It is a console-based application with five different classes. In order to use the system, the user must enter his or her userID and pin whwn it starts. Once the details are entered successfully, ATM functionality is unlocked. As a result of the project, the following operations can be performed:
Updated Balance

Transaction History

Withdraw

Deposit

Transfer

Quit

This code is a simple ATM (Automated Teller Machine) application implemented using the Tkinter library in Python. Let's break down the code step by step:

1.Account Class: This class represents individual bank accounts. It has attributes such as user_id, pin, balance, and transactions to store account details and transaction history. The record_transaction method is used to add a new transaction to the account's transaction history.

2.TransactionHistory Class: This class contains a static method show_history to display the transaction history of an account using Tkinter's messagebox.

3.Withdraw, Deposit, Transfer Classes: These classes handle withdrawal, deposit, and transfer functionalities, respectively. Each class contains a static method to perform the corresponding operation on an account.

4.ATMApp Class: This is the main Tkinter GUI class for the ATM application. It initializes the GUI window, creates a login window, and provides methods to handle user interactions such as login, displaying options, withdrawing funds, depositing funds, transferring funds, etc.

5.create_login_window Method: This method creates the login window where users can enter their user ID and PIN.

6.login Method: This method is called when the user clicks the "Login" button. It checks if the entered user ID and PIN are valid and unlocks the ATM functionality if the credentials are correct.

7.show_options Method: This method displays the main options available to the user after successful login, such as checking balance, viewing transaction history, withdrawing funds, depositing funds, transferring funds, and quitting.

8.update_balance_label Method: This method updates the balance label on the GUI to reflect the current balance of the logged-in account.

9.withdraw_funds_gui, deposit_funds_gui, transfer_funds_gui Methods: These methods are called when the user selects the corresponding options from the menu. They prompt the user to enter the required information (e.g., amount to withdraw/deposit, recipient user ID for transfer) and perform the respective operations.

10.Main Block: This block creates an instance of the Tkinter Tk class, initializes the ATMApp, and starts the main event loop using root.mainloop().

Overall, this code provides a basic ATM application with functionalities for login, viewing balance, transaction history, withdrawing funds, depositing funds, and transferring funds, all implemented using Tkinter for the graphical interface.






