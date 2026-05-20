# Cree una clase de User que:

    # Tenga un atributo de date_of_birth.
    # Tenga un property de age.
    # Luego cree un decorador para funciones que acepten 
    #   un User como parámetro que se encargue de revisar 
    #   si el User es mayor de edad y arroje una excepción de no ser así.

from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
        
    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
            
        return age


def over_18(func):
    def wrapper(*args, **kwargs):
        user = args[0]
        print(f"\nVerifying user age... Current age: {user.age} years old.")
        
        if user.age < 18:
            raise PermissionError(f"Access Denied. User under 18. ({user.age} years old)")
        
        return func(*args, **kwargs)
        
    return wrapper


@over_18
def enter_to_place(user_obj):
    return f"¡Welcome, Born on {user_obj.date_of_birth.year}! Access granted."


adult_user = User(date(2000, 5, 15))
young_user  = User(date(2012, 10, 20))

print(enter_to_place(adult_user))
print(enter_to_place(young_user))