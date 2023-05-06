# 312project
This is my python banking application project for COMP 312. I did this alone in an attempt to greatly improve my knowledge of python.

<b>Mission Statement</b>     
The Chicago Bank Account System is a class project developed as a demonstration of open source computing with a focus on (at a practical level) applying python programming techniques, engaged learning, and personal growth. The mission of this project is to create a simple yet functional banking system that showcases the core principles of software development, allowing users to manage their financial transactions effectively. Throughout the course, I continuously strived to improve and build on the program's features based on personal bias and user needs, attempting to build from scratch an accessible and reliable system.

One of the main objectives of this project is to enhance my knowledge of Python programming and gain hands-on experience working in a like real-world application. The project serves as a platform for me to apply the concepts I've taught myself in Python, explore and implement new libraries and tools, and teach myself the iterations that stem within software development.

<b>Code of Conduct</b>    
<i>This project was created under a guideline of the following aspects:   </i>
Quality: Code follows proper ethics to meet quality standards, reinforcing the imortance of writing clean code that is organized and effecient.    

Constructive Feedback: Be open to feedback from users and use it to improve project.       

Inclusion: Build an environment that processes input for users, regardless of who they are.   

Responsibility: Ensure project can meet expectations to best of coding ability and build standard around ruleset of project's requirements.   


<b>Documentation and Changelog</b>     

This section is the documentation of features within the project and changelog as to when certain features were edited or added. The guide covers sections of the changelog, giving the user enough information to effectively navigate the system.

<i>February week 3 and 4: Multiple Accounts and Basic Transaction History</i>

- Multiple Accounts: Users can now create and manage multiple bank accounts. To create a new account, simply click the "Create Account" button and input the required account details. You can then perform operations like deposits, withdrawals, and balance checks on each account separately.

- Basic Transaction History: Each account now maintains a transaction history. To view the transaction history for a specific account, click the "Transaction History" button and enter the account number. A list of transactions will be displayed, showing the type, amount, and date of each transaction.

<i>March week 2 and 3: Graphical User Interface using tkinter</i>

- Graphical User Interface: The command-line interface has been replaced by a user-friendly graphical interface using the tkinter library. You can now navigate through the available options by clicking the corresponding buttons and entering the required information in the provided fields.

<i>March week 4: Enhanced Transaction History with Timestamps</i>

- Enhanced Transaction History: The transaction history feature has been improved to include timestamps for each transaction. When viewing an account's transaction history, you will now see the exact date and time each transaction was executed.

<i>April week 2 and 3: Account Balance Checking and Improved Error Handling</i>

- Account Balance Checking: Users can now easily check the balance of any account by clicking the "Check Balance" button and entering the account number. The system will then display the current balance for the specified account.

- Improved Error Handling: Error handling has been improved for invalid user inputs, such as incorrect account numbers or insufficient funds. When an error occurs, a clear and informative error message will be displayed, guiding the user to rectify the issue. Just as a reminder, some specific fields may be case-sensitive. Enter data properly to avoid receiving an error.




<b>Testing Procedure</b>

Test 1: Create Account    

- Press the "Create Account" button.
- Enter a unique account number and an account name.
- Expected result: A new account should be created with the entered account number and name, and an initial balance of 0.

Test 2: Deposit operation

- Press the "Deposit" button.
- Enter a valid account number and deposit amount.
- Expected result: The account balance should increase by the deposit amount, and a transaction should be added to the account's transaction history.

Test 3: Withdraw operation

- Press the "Withdraw" button.
- Enter a valid account number, withdrawal amount, and ensure the account has sufficient funds.
- Expected result: The account balance should decrease by the withdrawal amount, and a transaction should be added to the account's transaction history.

Test 4: Check Balance

- Press the "Check Balance" button.
- Enter a valid account number.
- Expected result: The current account balance should be displayed.

Test 5: Transaction History

- Press the "Transaction History" button.
- Enter a valid account number.
- Expected result: A list of transactions, including timestamps, should be displayed for the specified account.

Test 6: Invalid Account Number

- Perform any operation (e.g., Deposit, Withdraw, Check Balance, or Transaction History) with an invalid account number.
- Expected result: An error message should be displayed, informing the user that the account number is invalid.

Test 7: Insufficient Funds

- Attempt to withdraw an amount greater than the account balance.
- Expected result: An error message should be displayed, informing the user that there are insufficient funds for the withdrawal.

Test 8: Negative Deposit or Withdrawal Amount

- Attempt to deposit or withdraw a negative amount.
- Expected result: An error message should be displayed, informing the user that the entered amount is invalid.
