# Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, 
# ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.

# Ejemplos:

# 1, 1, 1, 2, 2, 2 → 50% mujeres y 50% hombres
# 1, 1, 2, 2, 2, 2 → 33.3% mujeres y 66.6% hombres
# 1, 1, 1, 1, 1, 2 → 83.3% mujeres y 16.6% hombres

sexo = 0
hombres = 0
mujeres = 0
entradas = []
for i in range(6):
    sexo = int(input("ingrese 1 si es mujer o 2 si es hombre: "))
    while sexo not in (1, 2):
        sexo = int(input("Numero invalido. ingrese 1 si es mujer o 2 si es hombre: "))
    entradas.append(sexo)
    if sexo == 1:
        mujeres += 1
    elif sexo == 2:
        hombres += 1
total = len(entradas)
porcentaje_h = (hombres / 6 * 100)
porcentaje_m = (mujeres / 6 * 100)
secuencia = ", ".join(str(x) for x in entradas)
print(f"{secuencia} → {porcentaje_m:.1f}% mujeres y {porcentaje_h:.1f}% hombres")