# main program
from models import *

manager = FinanceManager()

manager.add_category("Salario")
manager.add_category("Transporte")

# 3. Crear 2 transacciones de prueba
# (trans_type, title, category, amount, date)
ingreso = Transaction("Income", "Pago Quincena", "Salario", 500000, "20/07/2026")
gasto = Transaction("Expense", "Gasolina", "Transporte", 35000, "20/07/2026")

# 4. Agregar las transacciones al gestor
manager.add_transaction(ingreso)
manager.add_transaction(gasto)

# 5. Imprimir transacciones y balance
manager.get_transactions()
manager.get_total_balance()
