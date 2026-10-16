#Целью проекта является создание программы, которая сможет определить является ли данная дата праздником
import holidays
ru_holidays = holidays.RU()
date_to_check = input("Введите дату в формате: ГГГГ-ММ-ДД")
holiday_name = ru_holidays.get(date_to_check)
if holiday_name:
    print(holiday_name)
else:
    print("Праздника в этот день нет.")