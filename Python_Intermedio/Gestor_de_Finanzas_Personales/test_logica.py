import pytest
from datetime import datetime
from models import Transaction, FinanceManager

# Fixtures

@pytest.fixture
def empty_manager():
    fm = FinanceManager()
    categories = ["Food", "Savings", "General", "Salary", "Services"]
    for cat in categories:
        fm.add_category(cat)
    return fm

@pytest.fixture
def populated_manager(empty_manager):
    fm = empty_manager
    
    # Test transactions
    t1 = Transaction("Income", "Salary", "Salario Enero", 1000000, "Transfer", "15/01/2026")
    t2 = Transaction("Expense", "Food", "Supermercado", 150000, "Credit Card", "20/01/2026")
    t3 = Transaction("Expense", "Savings", "Ahorro Quincenal", 100000, "Transfer", "25/01/2026")
    t4 = Transaction("Expense", "Services", "Luz y Agua", 45000, "SINPE", "05/02/2026")
    t5 = Transaction("CC Payment", "General", "Pago Tarjeta", 50000, "Transfer", "10/02/2026")
    
    fm.add_transaction(t1)
    fm.add_transaction(t2)
    fm.add_transaction(t3)
    fm.add_transaction(t4)
    fm.add_transaction(t5)
    
    return fm


# Transactions tests

def test_transaction_initialization():
    t = Transaction("Expense", "Food", "Almuerzo", 5000.0, "Cash", "12/03/2026")
    assert t.trans_type == "Expense"
    assert t.amount == 5000.0
    assert t.month == 3
    assert t.year == 2026

def test_transaction_set_date_updates_month_and_year():
    t = Transaction("Expense", "Food", "Almuerzo", 5000.0, "Cash", "12/03/2026")
    t.set_date("01/11/2025")
    
    assert t.date == "01/11/2025"
    assert t.month == 11
    assert t.year == 2025

def test_transaction_invalid_date_fallback():
    t = Transaction("Expense", "Food", "Almuerzo", 5000.0, "Cash", "invalid date")
    now = datetime.now()
    assert t.month == now.month
    assert t.year == now.year


# Finance Manager tests

def test_add_transaction_without_categories():

    fm = FinanceManager()
    t = Transaction("Income", "Salary", "Pago", 1000, "Cash", "01/01/2026")
    with pytest.raises(ValueError, match="No categories available."):
        fm.add_transaction(t)

def test_filter_by_date(populated_manager):
    # Filter only Jan 2026
    jan_transactions = populated_manager._filter_by_date("01/01/2026", "31/01/2026")
    assert len(jan_transactions) == 3
    
    # Filter only Feb
    feb_transactions = populated_manager._filter_by_date("01/02/2026", "28/02/2026")
    assert len(feb_transactions) == 2

def test_get_summary_metrics_without_filter(populated_manager):
    metrics = populated_manager.get_summary_metrics()
    metrics_dict = dict(metrics)
    
    assert metrics_dict["Total Income"] == "₡1,000,000.00"
    assert metrics_dict["Total Expenses"] == "₡195,000.00"  # 150,000 (Food) + 45,000 (Services)
    assert metrics_dict["Savings"] == "₡100,000.00"
    assert metrics_dict["CC Payments"] == "₡50,000.00"
    assert metrics_dict["Net Balance"] == "₡705,000.00"  # 1,000,000 - 195,000 - 100,000

def test_get_summary_metrics_with_date_filter(populated_manager):
    metrics = populated_manager.get_summary_metrics("01/01/2026", "31/01/2026")
    metrics_dict = dict(metrics)
    
    assert metrics_dict["Total Income"] == "₡1,000,000.00"
    assert metrics_dict["Total Expenses"] == "₡150,000.00"
    assert metrics_dict["Savings"] == "₡100,000.00"
    assert metrics_dict["Net Balance"] == "₡750,000.00"

def test_get_expenses_by_category(populated_manager):
    expenses = populated_manager.get_expenses_by_category()
    exp_dict = dict(expenses)
    
    assert "Food" in exp_dict
    assert exp_dict["Food"] == "₡150,000.00"
    assert "Services" in exp_dict
    assert exp_dict["Services"] == "₡45,000.00"
    assert "Savings" not in exp_dict 

def test_get_income_by_category(populated_manager):
    incomes = populated_manager.get_income_by_category()
    inc_dict = dict(incomes)
    
    assert "Salary" in inc_dict
    assert inc_dict["Salary"] == "₡1,000,000.00"