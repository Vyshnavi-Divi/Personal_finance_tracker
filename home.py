from datetime import *


class FinanceTracker:
    _transactions = []

    def __init__(self):
        self.transactions = FinanceTracker._transactions

    def add_income(self, source, amount, date, description=""):
        if amount <= 0:
            return False, "Amount must be greater than 0"

        transaction = {
            "type": "Income",
            "source": source,
            "amount": float(amount),
            "date": date.strftime("%d-%m-%Y"),
            "description": description,
            "timestamp": datetime.now()
        }

        self.transactions.append(transaction)
        return True, f"Income of ₹{amount:.2f} added successfully"

    def add_expense(self, category, amount, date, description=""):
        if amount <= 0:
            return False, "Amount must be greater than 0"

        transaction = {
            "type": "Expense",
            "category": category,
            "amount": float(amount),
            "date": date.strftime("%d-%m-%Y"),
            "description": description,
        }

        self.transactions.append(transaction)
        return True, f"Expense of ₹{amount:.2f} added successfully"

    def get_all_transactions(self):
        return self.transactions

    def calculate_total_income(self):
        return sum(
            t["amount"] for t in self.transactions
            if t["type"] == "Income"
        )

    def calculate_total_expense(self):
        return sum(
            t["amount"] for t in self.transactions
            if t["type"] == "Expense"
        )

    def get_remaining_balance(self):
        return self.calculate_total_income() - self.calculate_total_expense()

    def get_category_wise_spending(self):
        category_spending = {}

        for t in self.transactions:
            if t["type"] == "Expense":
                category = t["category"]
                category_spending[category] = (
                    category_spending.get(category, 0) + t["amount"]
                )

        return category_spending