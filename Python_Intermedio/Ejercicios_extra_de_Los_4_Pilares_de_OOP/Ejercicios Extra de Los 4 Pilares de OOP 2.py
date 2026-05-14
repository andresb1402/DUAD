# Cree una clase abstracta User con los siguientes métodos abstractos:
#     get_role()
#     has_permission(permission)

# Luego cree dos clases que hereden de ella:

#     AdminUser
#     RegularUser

# Cada una debe implementar los métodos
# Por ejemplo:

#     AdminUser siempre tiene permisos
#     RegularUser solo tiene permisos limitados ("read", por ejemplo)

from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def get_role(self):
        pass


    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):
    def __init__(self, name):
        self.name = name

    
    def get_role(self):
        return 'Administrator'


    def has_permission(self, permission):
        permissions = ['Read', 'Write', 'Delete']
        return permission in permissions


class RegularUser(User):
    def __init__(self, name):
        self.name = name

    
    def get_role(self):
        return 'Regular User'


    def has_permission(self, permission):
        return permission == 'Read'


user1 = AdminUser("Jose")
user2 = RegularUser("Jaime")

print(user1.has_permission("delete".capitalize()))  # True
print(user2.has_permission("delete".capitalize()))  # False