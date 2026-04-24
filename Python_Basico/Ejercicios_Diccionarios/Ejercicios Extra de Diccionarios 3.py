#Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, 
# cree un diccionario que acumule el total por categoría.

sold_products = [
            {   "name": "Degreaser", 
                "category": "Cleaning", 
                "price": 2500
            },
            {   "name": "Carb cleaner", 
                "category": "Cleaning", 
                "price": 2800
            },
            {   "name": "Engine oil", 
                "category": "Lube", 
                "price": 10800
            },
            {   "name": "Fork oil", 
                "category": "Lube", 
                "price": 9875
            },
            {   "name": "Front break pads", 
                "category": "Maintenance", 
                "price": 15500
            },
            {   "name": "Rear break pads", 
                "category": "Maintenance", 
                "price": 17500
            },
]

category_list = {}

for product in sold_products:
    category = product['category']
    price_num = int(product['price'])
    total = product['price']
    

    if category in category_list:
       category_list[category] += price_num
    else:
        category_list[category] = price_num

for category, total in category_list.items():
    print(f"{category}: {total}")