#    Dada una lista de ventas con la siguiente información:
#         date
#         customer_email
#         items

# Y cada item teniendo la siguiente información:

#     name
#     upc
#     unit_price

# Cree un diccionario que guarde el total de ventas de cada UPC.



fifteen_bday = {
    'name': '15 años',
    'upc': 'ITEM-002',
    'service_price': 180,
}

outdoors = {
    'name': 'Outdoors',
    'upc': 'ITEM-003',
    'service_price': 70,
}

christmas = {
    'name': 'Christmas',
    'upc': 'ITEM-004',
    'service_price': 50,
}

services = [fifteen_bday, outdoors, christmas]

sales = [
    {
        'date': '09/11/2025',
        'customer_email': 'nor18@gmail.com',
        'service': services[1],
    },
    {
        'date': '23/11/2025',
        'customer_email': 'mar.co@gmail.com',
        'service': services[0],
    },
    {
        'date': '29/11/2025',
        'customer_email': 'abi.25@gmail.com',
        'service': services[2],
    },
    {
        'date': '29/11/2025',
        'customer_email': 'abi.25@gmail.com',
        'service': services[2],
    },
    {
        'date': '29/11/2025',
        'customer_email': 'saenzm@outlook.com',
        'service': services[2],
    },
    
]

results = {}

for sale in sales:
    upc = sale['service']['upc']
    price = sale['service']['service_price']

    if upc in results:
        results[upc] += price
    else:
        results[upc] = price

for upc, price in results.items():
    print(f"UPC: {upc} | Ventas: {price}")

#Opcional para saber cual servicio fue el mas vendido.
top_upc = ""
max_price = 0

for upc, price in results.items():
    if price > max_price:
        max_price = price
        top_upc = upc
        pass

print(f"\nEl servicio más vendido fue {top_upc} con un total de ${max_price}")

