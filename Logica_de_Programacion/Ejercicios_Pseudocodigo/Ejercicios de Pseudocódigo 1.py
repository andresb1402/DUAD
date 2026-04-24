#1. Cree un pseudocódigo que le pida un precio de producto al usuario, 
# calcule su descuento y muestre el precio final tomando en cuenta que:

#Si el precio es menor a 100, el descuento es del 2%.
#Si el precio es mayor o igual a 100, el descuento es del 10%.
#Ejemplos:

#120 → 108
#40 → 39.2

product_price = int(input("Por favor ingrese el precio del producto: "))
if product_price < 100:
    discount = 0.02
else:
    discount = 0.10
final_price = product_price - (product_price * discount)
print(f"El precio final de su producto es: {final_price}")


