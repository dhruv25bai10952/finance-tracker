# =============================================================================
# Project       : Personal Net Worth & Expense Tracker
# Domain        : Finance & Banking
# Language      : Python 3 (Standard libraries only)
# Author        : [Your Full Name]
# Roll No       : [Your Roll Number]
# Course        : Introduction to Problem Solving & Programming
# =============================================================================
# Structured Development Process followed:
# 1. Problem Definition
# 2. Requirement Analysis
# 3. Top-Down Design
# 4. Algorithm Development
# 5. Implementation
# 6. Testing & Refinement
# =============================================================================

import csv
import os
from datetime import datetime

# ==================== ENTITY CLASSES ====================
class Asset:
    def __init__(self, name, value, category="General"):
        self.name = name
        self.value = float(value)
        self.category = category
        self.date = datetime.now().strftime("%Y-%m-%d")

class Liability:
    def __init__(self, name, amount, due_date):
        self.name = name
        self.amount = float(amount)
        self.due_date = due_date

class Expense:
    def __init__(self, category, amount, description):
        self.category = category
        self.amount = float(amount)
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")

# ==================== FILE PATHS ====================
ASSET_FILE = os.path.join("data", "assets.csv")
LIABILITY_FILE = os.path.join("data", "liabilities.csv")
EXPENSE_FILE = os.path.join("data", "expenses.csv")

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

# ==================== LOAD FUNCTIONS ====================
def load_assets():
    assets = []
    if os.path.exists(ASSET_FILE):
        with open(ASSET_FILE, mode='r') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                if len(row) == 4:
                    assets.append(Asset(row[0], row[1], row[2]))
    return assets

def load_liabilities():
    liabilities = []
    if os.path.exists(LIABILITY_FILE):
        with open(LIABILITY_FILE, mode='r') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if len(row) == 3:
                    liabilities.append(Liability(row[0], row[1], row[2]))
    return liabilities

def load_expenses():
    expenses = []
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, mode='r') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if len(row) == 4:
                    expenses.append(Expense(row[0], row[1], row[2]))
    return expenses

# ==================== SAVE FUNCTIONS ====================
def save_assets(assets):
    with open(ASSET_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Value", "Category", "Date"])
        for a in assets:
            writer.writerow([a.name, a.value, a.category, a.date])

# (Similar save functions for liabilities and expenses – omitted for brevity but included in full file)

# ==================== MENU FUNCTIONS ====================
def add_asset(assets):
    print("\n=== Add New Asset ===")
    name = input("Asset Name (e.g., Savings Account): ")
    value = float(input("Current Value (₹): "))
    category = input("Category (Cash/Investment/Property): ")
    assets.append(Asset(name, value, category))
    save_assets(assets)
    print("Asset added successfully!")

# (Similar functions for liability, expense, view, and report – full code provided in final file)

# ==================== MAIN MENU ====================
def main():
    assets = load_assets()
    liabilities = load_liabilities()
    expenses = load_expenses()

    while True:
        print("\n" + "="*50)
        print("   PERSONAL FINANCE & NET WORTH TRACKER")
        print("="*50)
        print("1. Add Asset")
        print("2. Add Liability")
        print("3. Add Expense")
        print("4. View All Assets")
        print("5. View All Liabilities")
        print("6. View All Expenses")
        print("7. Generate Complete Financial Report")
        print("8. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            add_asset(assets)
        elif choice == '2':
            add_liability(liabilities)
        elif choice == '3':
            add_expense(expenses)
        elif choice == '4':
            view_assets(assets)
        elif choice == '5':
            view_liabilities(liabilities)
        elif choice == '6':
            view_expenses(expenses)
        elif choice == '7':
            generate_full_report(assets, liabilities, expenses)
        elif choice == '8':
            print("Thank you! Stay financially aware!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
