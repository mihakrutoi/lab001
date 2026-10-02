print("Количество занятий не меньше нуля! Продолжительность занятия минимум 1 минута!")

subject_1 = input("Название 1 предмета?: ")
subject_2 = input("Название 2 предмета?: ")
number_classes_subject_1 = int(input("Количество занятий по 1 предмету за неделю?: "))
number_classes_subject_2 = int(input("Количество занятий по 2 предмету за неделю?: "))
time_minutes_of_one_class_subject_1 = int(input("Время одного занятия по 1 предмету в минутах?: "))
time_minutes_of_one_class_subject_2 = int(input("Время одного занятия по 2 предмету в минутах?: "))
max_time_in_week_in_hours = int(input("Доступное время на неделю в часах?: "))

minutes_for_subject_1 =  number_classes_subject_1 * time_minutes_of_one_class_subject_1  # Считает время занятий по 1 предмету в минутах
minutes_for_subject_2 =  number_classes_subject_2 * time_minutes_of_one_class_subject_2  # Считает время занятий по 2 предмету в минутах
all_classes_time_in_minutes =  minutes_for_subject_1 + minutes_for_subject_2  # Считает полное время всех занятий в минутах
all_classes_time_in_hours =  float(minutes_for_subject_1 + minutes_for_subject_2) / 60  # Считает полное время всех занятий в часах
remaining_time_in_hours =  max_time_in_week_in_hours - all_classes_time_in_hours  # Считает остаток времени в неделе (макс. минус время всех занятий) в часах
time_classes_for_4_weeks_in_hours = all_classes_time_in_hours * 4 # Считает время всех занятий за 4 одинаковые недели в часах

print(f"""  ---Учебная нагрузка---
    | Время занятий по {subject_1} (в минутах): {minutes_for_subject_1}
    | Время занятий по {subject_2} (в минутах): {minutes_for_subject_2}
    | Общая нагрузка (в минутах): {all_classes_time_in_minutes}
    | Общая нагрузка (в часах): {all_classes_time_in_hours:.2f}
    | Остаток свободного времени (в часах): {remaining_time_in_hours:.2f}
    | Нагрузка на 4 одинаковые недели (в часах): {time_classes_for_4_weeks_in_hours:.2f}""")