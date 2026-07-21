from data import *
from datetime import datetime


class Transaction:
    def __init__(self, trans_type, category, title, amount, payment_method, date):
        self.trans_type = trans_type
        self.category = category
        self.title = title
        self.amount = float(amount)
        self.payment_method = payment_method
        self.set_date(date)  

    def set_date(self, date_str: str):
        if not date_str or not date_str.strip():
            raise ValueError("Date cannot be empty.")

        try:
            dat_obj = datetime.strptime(date_str.strip(), "%d/%m/%Y")
        except ValueError:
            raise ValueError("Invalid format. Use dd/mm/yyyy.")

        if dat_obj.date() > datetime.now().date():
            raise ValueError("Future dates are not allowed.")

        self.date = date_str.strip()
        self.month = dat_obj.month
        self.year = dat_obj.year

    def to_dict(self):
        return {
            "trans_type": self.trans_type,
            "title": self.title,
            "category": self.category,
            "amount": self.amount,
            "payment_method": self.payment_method,
            "date": self.date
        }


class FinanceManager:
    def __init__(self):
        self.list_of_transactions = []
        self.list_of_categories = {}


    def add_category(self, name):
        self.list_of_categories[name] = name


    def add_transaction(self, transaction):
        if not self.list_of_categories:
            raise ValueError("No categories available.")
        self.list_of_transactions.append(transaction)


    def get_transactions(self):
        return self.list_of_transactions


    def get_income_db(self):
        return [t for t in self.list_of_transactions if t.trans_type.lower() == "income"]


    def get_total_balance(self):
        if not self.list_of_transactions:
            return 0.0
        
        total_income = sum(t.amount for t in self.get_income_db())
        total_expense = sum(t.amount for t in self.list_of_transactions if t.trans_type.lower() != "income")
        return total_income - total_expense


    def get_savings_db(self):
        return [
            t for t in self.list_of_transactions 
            if t.trans_type.lower() == "expense" and t.category.lower() == "savings"
        ]


    def get_savings_total(self):
        return sum(t.amount for t in self.get_savings_db())


    def get_expenses_db(self):
        return [
            t for t in self.list_of_transactions 
            if t.trans_type.lower() == "expense" and t.category.lower() != "savings"
        ]


    def get_cc_db(self):
        return [
            t for t in self.list_of_transactions 
            if t.trans_type.lower() in ["cc payment", "cc partial payment"] 
            or t.payment_method.lower() == "credit card"
        ]


    def get_credit_card_summary(self):
        cc_expenses = sum(
            t.amount for t in self.list_of_transactions 
            if t.payment_method.lower() == "credit card" and t.trans_type.lower() == "expense"
        )
        cc_payments = sum(
            t.amount for t in self.list_of_transactions 
            if t.trans_type.lower() in ["cc partial payment", "cc payment"] or t.category.lower() == "credit card"
        )
        
        return {
            "total_charged": cc_expenses,
            "total_reimbursed": cc_payments,
            "net_debt": cc_expenses - cc_payments
        }


    def get_monthly_summary(self, month, year):
        trans_month = [t for t in self.list_of_transactions if t.month == month and t.year == year]
        
        income = sum(t.amount for t in trans_month if t.trans_type.lower() == "income")
        expense = sum(t.amount for t in trans_month if t.trans_type.lower() == "expense" and t.category.lower() != "savings")
        savings = sum(t.amount for t in trans_month if t.category.lower() == "savings")
        
        return {
            "income": income,
            "total_expenses": expense,
            "savings": savings,
            "balance": income - expense - savings
        }

    # --- Métodos de Métricas para la GUI ---

    def _filter_by_date(self, date_from_str="", date_to_str=""):
        if not date_from_str or not date_to_str:
            return self.list_of_transactions
        try:
            d_start = datetime.strptime(date_from_str, "%d/%m/%Y")
            d_end = datetime.strptime(date_to_str, "%d/%m/%Y")
            
            filtered = []
            for t in self.list_of_transactions:
                try:
                    t_date = datetime.strptime(t.date, "%d/%m/%Y")
                    if d_start <= t_date <= d_end:
                        filtered.append(t)
                except ValueError:
                    continue
            return filtered
        except ValueError:
            return self.list_of_transactions


    def get_summary_metrics(self, date_from_str="", date_to_str=""):
        transactions = self._filter_by_date(date_from_str, date_to_str)
        
        income = sum(t.amount for t in transactions if t.trans_type.lower() == "income")
        expenses = sum(t.amount for t in transactions if t.trans_type.lower() == "expense" and t.category.lower() != "savings")
        savings = sum(t.amount for t in transactions if t.category.lower() == "savings")
        cc_payments = sum(t.amount for t in transactions if t.trans_type.lower() in ["cc payment", "cc partial payment"])

        return [
            ["Total Income", f"₡{income:,.2f}"],
            ["Total Expenses", f"₡{expenses:,.2f}"],
            ["Savings", f"₡{savings:,.2f}"],
            ["CC Payments", f"₡{cc_payments:,.2f}"],
            ["Net Balance", f"₡{(income - expenses - savings):,.2f}"]
        ]


    def get_expenses_by_category(self, date_from_str="", date_to_str=""):
        transactions = self._filter_by_date(date_from_str, date_to_str)
        totals = {}
        for t in transactions:
            if t.trans_type.lower() == "expense" and t.category.lower() != "savings":
                totals[t.category] = totals.get(t.category, 0.0) + t.amount
        
        results = [[cat, f"₡{amt:,.2f}"] for cat, amt in sorted(totals.items(), key=lambda x: x[1], reverse=True)]
        if totals:
            total_sum = sum(totals.values())
            results.append(["TOTAL", f"₡{total_sum:,.2f}"])
        
        return results


    def get_income_by_category(self, date_from_str="", date_to_str=""):
        transactions = self._filter_by_date(date_from_str, date_to_str)
        totals = {}
        for t in transactions:
            if t.trans_type.lower() == "income":
                totals[t.category] = totals.get(t.category, 0.0) + t.amount
        
        results = [[cat, f"₡{amt:,.2f}"] for cat, amt in sorted(totals.items(), key=lambda x: x[1], reverse=True)]
        if totals:
            total_sum = sum(totals.values())
            results.append(["TOTAL", f"₡{total_sum:,.2f}"])
        
        return results