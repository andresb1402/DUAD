# main program
from models import *

manager = FinanceManager()

manager.add_category("Salario")
manager.add_category("Transporte")

# 3. Crear 2 transacciones de prueba
# (date, title, category, transaction_type, amount, payment_method)
ingreso = Transaction("20/07/2026", "Pago Quincena", "Income", "Salario", 500000, "SINPE")
gasto = Transaction("20/07/2026", "Gasolina XR", "Expense", "Gas", 3500, "Efectivo")

# 4. Agregar las transacciones al gestor
manager.add_transaction(ingreso)
manager.add_transaction(gasto)

# 5. Imprimir transacciones y balance
manager.get_transactions()
manager.get_total_balance()
