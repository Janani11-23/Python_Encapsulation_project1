# 🏦 Bank Management System – Python Encapsulation Project

## 📌 Project Overview

This is a **Python-based Bank Management System** developed to demonstrate the concept of **Encapsulation in Object-Oriented Programming (OOP)**.

The project provides basic banking operations such as depositing money, withdrawing money, checking account balance, viewing customer details, and displaying the last transaction.

## 🎯 Objective

The main objective of this project is to understand and implement **Encapsulation** in Python by restricting direct access to sensitive account information and providing controlled access through methods.

## 🔐 OOP Concept Used – Encapsulation

Encapsulation is implemented by keeping sensitive account data as **private attributes** using double underscores (`__`).

Private attributes used in this project include:

* `__Acc_no` – Account number
* `__pin` – PIN number
* `__initial_balance` – Account balance
* `__Last_transaction` – Last transaction details

The project also uses private methods for operations such as authentication, deposit, withdrawal, and receipt generation.

This demonstrates how data can be protected and accessed through controlled methods.

## ⚙️ Features

* 💰 Deposit Money
* 💸 Withdraw Money
* 💳 Check Account Balance
* 👤 View Customer Details
* 🧾 View Last Transaction
* 🔐 Account Number and PIN Authentication
* 🧾 Transaction Receipt Generation
* 🚪 Exit the Banking System

The main menu provides these banking operations through a simple console-based interface.

## 🛠️ Technologies Used

* **Python**
* **Object-Oriented Programming (OOP)**
* **Encapsulation**
* **Conditional Statements**
* **Functions / Methods**
* **While Loop**
* **User Input & Console Output**

## 📂 Project Structure

```text
Python_Encapsulation_project1/
│
├── Python_Encapsulation_project1.py
├── README.md
└── output.png
```

## 🔄 How the System Works

1. The user selects an operation from the banking menu.
2. For protected operations, the system asks for the account number and PIN.
3. The entered credentials are authenticated.
4. If authentication is successful, the selected banking operation is performed.
5. The updated balance and transaction information are displayed.
6. The system generates and stores the latest transaction receipt.

The authentication method checks the entered account number and PIN against the stored private values.

## 💡 Key Learning Outcomes

Through this project, I learned:

* How to create classes and objects in Python.
* How to implement **Encapsulation** using private attributes.
* How to use private methods for controlled operations.
* How authentication can be implemented for account-related operations.
* How to perform basic banking transactions using Python.
* How to maintain and display transaction information.

## 📸 Sample Output

Add a screenshot of the program output here.

```text
🏦 =============================
       WELCOME TO SBI BANK
🏦 =============================

💰 1. Deposit Money
💸 2. Withdraw Money
💳 3. Show Balance
👤 4. Show Details
🧾 5. Last Transaction
🚪 6. Exit
```

## 👩‍💻 Author

**Janani S**

### ⭐ Project Focus

**Python | OOP | Encapsulation | Bank Management System**

