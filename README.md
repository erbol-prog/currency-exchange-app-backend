Currency Exchange Backend

This repository contains the backend of a Currency Exchange application built with Django (Python). The frontend is developed separately using Dart (Flutter).

Overview

This project provides a complete solution for cashiers and administrators of currency exchange offices. It includes features for managing currencies, cashiers, transactions, analytics, and more.

Features

Currency Management: Add, remove, and update currencies.

Cashier Management: Add and remove cashiers.

Transaction Operations: Perform and record currency exchange transactions.

Operation History: Keep track of all transactions and actions.

Shift Management: Manage cashier shifts with history tracking.

Analytics & Statistics: View detailed analytics and statistics for operations.

Receipt & Report Functionality: Generate and manage transaction receipts.

Excel Report Export: Convert reports into Excel files.

Secure API: All main API endpoints are protected with JWT tokens.

Database Integrity: The system maintains a flawless transaction history using SQLite.

Modern UI/UX: The application features a beautiful, animated design for an enhanced user experience.


Main Modules

Operations Window

Cash Register Window

Currency Management Window

Statistics & Analytics Dashboard

User & Role Management

Shift Management

Activity Logs


Tech Stack

Backend: Django (Python)

Database: SQLite

Authentication: JWT Tokens

Frontend: Flutter (Dart) (separate repository)


Installation & Setup

1. Clone the repository

git clone
cd currency-exchange-backend


2. Create a virtual environment

python -m venv venv
source venv/bin/activate   # (Linux/macOS)
venv\Scripts\activate      # (Windows)


3. Install dependencies

pip install -r requirements.txt


4. Apply migrations

python manage.py migrate


5. Run the server

python manage.py runserver



Future Improvements

Multi-language support

Advanced analytics and reporting

Integration with external financial APIs


