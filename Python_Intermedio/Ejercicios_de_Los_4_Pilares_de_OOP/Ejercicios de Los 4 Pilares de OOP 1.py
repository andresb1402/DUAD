# Cree una clase de BankAccount que:

#     Tenga un atributo de balance.
#     Tenga un método para ingresar dinero.
#     Tengo un método para retirar dinero.

# Cree otra clase que herede de esta llamada SavingsAccount que:
    # Tenga un atributo de min_balance que se pueda asignar al crearla.
    # Arroje un error si al intentar retirar dinero, el retiro haría 
    #   que el balance quede debajo del min_balance. 
    #   Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.


class BankAccount:
    def __init__(self, balance):
        self.balance = balance


    def add_money(self, amount):
        self.balance += amount
        print(f"\n${amount} added to your account.")
        print(f"Current balance: ${self.balance}")



    def subtract_money(self, amount):
        if self.balance < amount:
            print("\nError: Insufficient funds.")

        elif self.balance >= amount:
            self.balance -= amount
            print(f"\n${amount} withdrawn successfully.")
            print(f"Current balance: ${self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance


    def subtract_money(self, amount):
        if (self.balance - amount) < self.min_balance:
            print(f"\nError: This withdraw would leave you below your ${self.min_balance} minimum.")

        else:
            self.balance -= amount
            print(f"\n${amount} withdrawn successfully.")
            print(f"Current balance: ${self.balance}")

regular_account = BankAccount(2000)
savings_account = SavingsAccount(1000, 500)

regular_account.subtract_money(800) # Current balance: $200
savings_account.subtract_money(800) # Error: This withdraw would leave you below your $500 minimum.