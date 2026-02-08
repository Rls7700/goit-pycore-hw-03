# ЗАВДАННЯ  1
from datetime import datetime
import re
def get_days_from_today(date:str) -> int | None:#Повертає кількість днів між заданою та поточною датою.неправильний формат - ноне
    #оголосили функцію get_days.., (date)-змінна в яку передадуть параметри коли викличуть,:str - очікуємо рядок
    #стрілка означає що функція повертає ціле число int або нічого none
    try: #спробуй виконати код, бо перетворення рядка в дату може зламатися якщо неправильний формат або неіснуюча дата
        #1)Перетворюємо рядок у datetime
        given_datetime = datetime.strptime(date,"%Y-%m-%d") #Клас з модуля datetime, який працює з датою + часом.
        #strptime Розшифровується як: STRing Parse TIME Тобто:“перетворити рядок у дату за шаблоном”
        #date Це рядок, який передав користувач
        #2) Беремо тільки дату без часу
        given_date = given_datetime.date()
        #given_datetime → дата + час нам потрібна тільки дата .date() відкидає час.
        #3) Беремо сьогоднішню дату без часу
        today_date = datetime.today().date()
        #datetime.today() Повертає поточну дату і час,.date() Залишає тільки: 2026-02-01
        #Щоб ігнорувати години, хвилини, секунди, як вимагає умова.
        #4)Пізниця між датами
        delta = today_date - given_date
        # віднімання дат Python вміє віднімати дати результат — об’єкт timedelta
        #5) Повертаємо кількість днів
        return delta.days
    except ValueError:
        #Коли сюди потрапляє код? Якщо: формат неправильний дата не існує strptime не зміг розібрати рядок
        #Якщо рядок не відповідає формату "YYYY-MM-DD"
        return None
#Викликаємо функцію  
print("ЗАВДАННЯ 1:")  
print(get_days_from_today("1982-07-01"))
print(get_days_from_today("2030-01-01"))
print(get_days_from_today("2020/10/09"))
print()
#endregion ЗАВДАННЯ 1

# ЗАВДАННЯ 2
import random #Модуль random потрібен для випадкових чисел.
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    #оголошуємо функцію min — мінімальне число,max — максимальне число, quantity — скільки чисел потрібно-> list — функція повертає список
    
    #Перевірка корректності параметрів
    if min < 1 or max > 1000 or min >= max:
        #Ми повинні перевірити:min >= 1, max <= 1000, min < max, quantity не більша, ніж кількість можливих чисел
        return[]
    if quantity > (max -min +1):
        #Чому (max - min + 1)? від 1 до 5 → 5 чисел, а не 4, приклад: 1, 2, 3, 4, 5
        return[]
    
    #Множина для унікальних чисел
    numbers = set()
    #Створюємо множину (set) set НЕ допускає повторів, ідеально для “унікальних чисел”

    #Генеруємо випадкові унікальні числа
    while len(numbers) < quantity:
        random_number = random.randint(min,max)
        numbers.add(random_number)
        #random.randint(min, max) → випадкове число, add() → додаємо в множину, якщо число вже є → set просто ігнорує його
        # цикл працює, поки не наберемо потрібну кількість
        
    #Повертаємо відсортований список
    return sorted(numbers)
# Перетворюємо set у список і сортуємо, sorted() повертає відсортований список, це саме те, що вимагає завдання
#викликаємо функцію
print("ЗАВДАННЯ 2:")
print(get_numbers_ticket(1,49,6))
print(get_numbers_ticket(1,36,5))
print(get_numbers_ticket(1,10,20))
print()
#endregion ЗАВДАННЯ 2

#region ЗАВДАННЯ 3
import re 
#re - модуль для регулярних виразів, тобто для пошуку і очищення тексту

#оголошуємо функцію
def normalize_phone(phone_number: str) -> str:
#phone_number вхідний рядок будь який формат,-> str функція повертає рядок
    #Видаляємо всі символи крім цифр та +
    cleaned = re.sub(r"[^\d+]","",phone_number)
    # re.sub означає замінити(що шукаємо, на що міняємо,де шукаємо)
    #[^\d+] = все, що НЕ цифра і НЕ плюс, \d — будь-яка цифра (0–9),+ — символ +,^ всередині [] означає НЕ
    #Якщо номер має міжнародний формат
    if cleaned.startswith("+"):
        return cleaned
    
    #Якщо номер починається з 380 - додаємо +
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
