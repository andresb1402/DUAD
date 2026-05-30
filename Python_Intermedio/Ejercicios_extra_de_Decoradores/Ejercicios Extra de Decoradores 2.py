# Cree un decorador @requires_login que:

#     Verifique si la variable global user_logged_in es True
#     Si no lo es, debe lanzar una excepción "Usuario no autenticado"
#     Si lo es, la función decorada se ejecuta normalmente

def requires_login(func):
    def wrapper(*args, **kwargs):
        if user_logged_in:
            return func(*args, **kwargs)
        else:
            raise PermissionError("User not found")

    return wrapper

user_logged_in = True
# user_logged_in = False

@requires_login
def view_profile():
    print("\nShowing user profile...")

view_profile()