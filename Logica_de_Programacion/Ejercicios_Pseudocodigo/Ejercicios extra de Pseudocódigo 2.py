# Cree un algoritmo que le pida al usuario una velocidad en km/h 
# y la convierta a m/s. Recuerda que 1 km == 1000m y 1 hora == 60 minutos * 60 segundos.

# Ejemplos:

# 73 → 20.27
# 50 → 13.88
# 120 → 33.33

velocidad = int(input("Por favor ingrese la velocidad (km/h): "))
resultado = velocidad * 1000 / 3600
print(f"{velocidad} → {resultado}")

