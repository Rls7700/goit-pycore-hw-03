# ЗАВДАННЯ  1
from datetime import datetime
import re
#оголошуємо функцію, повертає ціле число або нічого
def get_days_from_today(date:str) -> int | None:
    #пробуємо виконати код (неправильний формат або неіснуюча дата)
    try: 
        #Перетворюємо рядок у datetime
        given_datetime = datetime.strptime(date,"%Y-%m-%d") #date Це рядок, який передав користувач
        #Беремо тільки дату без часу
        given_date = given_datetime.date()
        #Беремо сьогоднішню дату без часу
        today_date = datetime.today().date()
        #Різниця між датами
        delta = today_date - given_date
        #Повертаємо кількість днів
        return delta.days
    except ValueError:
        return None
#Викликаємо функцію  
print("ЗАВДАННЯ 1:")  
print(get_days_from_today("1982-07-01"))
print(get_days_from_today("2030-01-01"))
print(get_days_from_today("2020/10/09"))
print()
#endregion ЗАВДАННЯ 1

# ЗАВДАННЯ 2
import random 
#Оголошуємо функцію, list фуеуція повертає список
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    
    #Перевірка корректності параметрів
    if min < 1 or max > 1000 or min >= max:
        #:min >= 1, max <= 1000, min < max, quantity не більша ніж кількість можливих чисел
        return[]
    if quantity > (max -min +1):
        
        return[]
    #Множина set для унікальних чисел
    numbers = set()
    #Генеруємо випадкові унікальні числа
    while len(numbers) < quantity:
        #випадкове число, додаємо в множину
        random_number = random.randint(min,max)
        numbers.add(random_number)
        
    #Повертаємо відсортований список
    return sorted(numbers)
#викликаємо функцію
print("ЗАВДАННЯ 2:")
print(get_numbers_ticket(1,49,6))
print(get_numbers_ticket(1,36,5))
print(get_numbers_ticket(1,10,20))
print()
#endregion ЗАВДАННЯ 2

#region ЗАВДАННЯ 3
import re 
#оголошуємо функцію
def normalize_phone(phone_number: str) -> str:
#phone_number вхідний рядок
    #Видаляємо всі символи крім цифр та +
    cleaned = re.sub(r"[^\d+]","",phone_number)
    #Якщо номер має міжнародний формат
    if cleaned.startswith("+"):
        return cleaned
    #Якщо номер починається з 380 + "+"
    if cleaned.startswith("380"):
        return "+" + cleaned
    # Якщо коду країни немає - додаємл +38
    return "+38" + cleaned

# Запуск
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("ЗАВДАННЯ 3:")
print(sanitized_numbers)
print()

#region ЗАВДАННЯ 4
from datetime import datetime, date, timedelta
#оголошення функції, приймає і повнртає список словників
def get_upcoming_birthdays (users: list[dict]) -> list[dict]:
    #отримаємо сьогоднішню дату(без часу)
    today = datetime.today().date()
    #задаємо межу +7днів
    end_date = today + timedelta(days=7)
    #створюємо список
    result = []
    #перебираємо людей
    for user in users:
        #дістаємо імя та дату народ.
        name = user.get("name")
        birthday_str = user.get("birthday")
        #Перевіряємо наявність даних
        if not name or not birthday_str:
            continue
        #Переводимо рядок у дату
        try:
            birthday = datetime.strptime(birthday_str, "%Y.%m.%d").date()
        except ValueError:
            #неправильний формат дати
            continue
        #Робимо день народження в цьому році, беремо місяць і день з birthday і ставимо поточний рік
        try:
            birthday_this_year = date(today.year, birthday.month, birthday.day)
        except ValueError:
            # випадок 29 лютого у невискосному році пропускаємо або вирішемо окремо
            continue
        #якщо др минув - беремо наступний рік
        if birthday_this_year < today:
            try:
                birthday_this_year = date(today.year + 1, birthday.month, birthday.day)
            except ValueError:
                continue
        # перевірка чи ДН в 7 днів включно
        if today <= birthday_this_year <= end_date:
            # створюємо привітання
            congrat_date = birthday_this_year
            # вихідний переносимо на понеділок
            if congrat_date.weekday() == 5: #субота
                congrat_date += timedelta(days=2)
            elif congrat_date.weekday() == 6: # неділя
                congrat_date +=timedelta(days=1)
            #додаємо людину у список
            result.append({
                "name": name,
                "congratulation_date": congrat_date.strftime("%Y.%m.%d")
            })        
    return result
#список
users = [
        {"name": "John Doe", "birthday": "1985.02.15"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        ]
print("ЗАВДАННЯ 4:")
print(get_upcoming_birthdays(users))
