#Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, 
# cree un diccionario que agrupe los empleados por su departamento:

employees_list = [
            {   "name": "Jose", 
                "email": "j.bar@jbs.com", 
                "department": "Jefatura"
            },
            {   "name": "Karla", 
                "email": "k.san@jbs.com", 
                "department": "Contabilidad"
            },
            {   "name": "Maria", 
                "email": "m.sae@jbs.com", 
                "department": "Ventas"
            },
            {   "name": "Belkys", 
                "email": "b.qui@jbs.com", 
                "department": "Ventas"
            },
            {   "name": "Jaime", 
                "email": "j.oba@jbs.com", 
                "department": "RRHH"
            },
]

dept_groups = {}

for employee in employees_list:
    department = employee['department']
    employee_name = employee['name']

    if department in dept_groups:
        dept_groups[department].append(employee_name)
    else:
        dept_groups[department] = [employee_name]

for department, employee_name in dept_groups.items():
    print(f"{department}: {employee_name}")