order_name = input("Введите название заказа: ")
client_name = input("Введите имя заказчика: ")
pos1_name = input("Введите название первой позиции: ")
pos2_name = input("Введите название второй позиции: ")
pos1_number = int(input("Введите количество 1-ых позиций (>= 0): "))
pos2_number = int(input("Введите количество 2-ых позиций (>= 0): "))
pos1_cost = float(input("Введите цену 1-ой позиции (>= 0): "))
pos2_cost = float(input("Введите цену 2-ой позиции (>= 0): "))
delivery_cost = float(input("Введите цену доставки (>= 0):  "))
client_payment = float(input("Введите внесённую сумму (не менее общей суммы заказа): "))

pos1_order_cost = pos1_cost * pos1_number  # Считает стоимость первых позиции
pos2_order_cost = pos2_cost * pos2_number  # Считает стоимость вторых позиций
order_cost_no_delivery = pos1_order_cost + pos2_order_cost  # Считает стоимость заказа без учёта доставки
order_cost_with_delivery = order_cost_no_delivery + delivery_cost  # Считает стоимость заказа с учётом доставки
number_of_positions = pos1_number + pos2_number  # Считает количество единиц позиций
change = client_payment - order_cost_with_delivery  # Считает сдачу 

print(f'''Название заказа: {order_name}  
Имя заказчика: {client_name}
{pos1_name} | {pos1_number} | {pos1_cost:.2f} | {pos1_order_cost:.2f}
{pos2_name} | {pos2_number} | {pos2_cost:.2f} | {pos2_order_cost:.2f}
Стоимость без доставки: {order_cost_no_delivery:.2f}
Стоимость с доставкой: {order_cost_with_delivery:.2f}
Количество единиц: {number_of_positions}
Сдача: {change:.2f}''')
