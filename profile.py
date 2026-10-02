print("Возраст не больше 120 и не ноль! Часов занятий не может быть отрицательным!")

first_name = input("Имя: ")
second_name = input("Фамилия: ")
city_name = input("Город: ")
group_code = input("Код группы: ")
full_age = int(input("Полных лет (возраст): "))
fav_obj =  input("Любимый предмет: ")
hours_in_week = float(input("Количество часов подготовки в неделю: "))

age_plus_4 = int(full_age + 4)  # Считает возраст через 4 года
hours_4_weeks = float(hours_in_week * 4)  # Считает кол-во часов подготовки в 4 неделях
mid_time_per_7_days = (hours_in_week / 7)  # Считает среднее кол-во часов подготовки за 1 семидневную неделю

print(f'''---Карточка студента---
|Полное имя: {first_name} {second_name}
|Возраст через 4 года (лет): {age_plus_4} 
|Время подготовки за 4 недели (часов): {hours_4_weeks:.2f}
|Среднее время подготовки в день за 7-мидневную неделю (часов): {mid_time_per_7_days}''')
