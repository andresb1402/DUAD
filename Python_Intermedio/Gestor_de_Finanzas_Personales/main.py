# main program
from models import *

manager = FinanceManager()

manager.add_category("Salario")
manager.add_category("Transporte")

# 3. Crear 2 transacciones de prueba
# (date, transaction_type, title, category, amount, payment_method)
ingreso = Transaction("20/07/2026", "Income", "Pago Quincena", "Salario", 500000, "SINPE")
gasto = Transaction("20/07/2026", "Expense", "Gasolina XR", "Gasolina", 3500, "Efectivo")

# 4. Agregar las transacciones al gestor
manager.add_transaction(ingreso)
manager.add_transaction(gasto)

# 5. Imprimir transacciones y balance
manager.get_transactions()
manager.get_total_balance()
