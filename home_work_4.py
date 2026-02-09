from __future__ import annotations

from datetime import datetime, date, timedelta
import re
import random


def get_days_from_today(date:str) -> int | None:
    """
    визначаємо кількість днів між заданою та поточною датою

    date_str:  дата у форматі YYYY-MM-DD

    Returns
    кількість днів (int), якщо дата у майбутньому - відємне сило
    неправильний формат - None.
    """
    try: 
        given_datetime = datetime.strptime(date,"%Y-%m-%d")
        given_date = given_datetime.date()
        today_date = datetime.today().date()
        delta = today_date - given_date
        return delta.days
    except ValueError:
        return None
    

def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list[int]:
    """
    генерує список унікальних випадковий чисел
    Args:
        min_nmu: не менше 1
        max_num: не більше 1000
        quantity: кількіть для відбору
    
    Returns:
        відстортований список унікальних чисел. Якщо некорректні - []
    """
    if min_num < 1 or max_num > 1000 or min_num >= max_num:
        return[]
    
    if quantity > (max_num -min_num +1):
        return[]
    
    numbers: set[int] = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_num, max_num))

    return sorted(numbers)


def normalize_phone(phone_number: str) -> str:
    """
    видаляє символи крім цифр та +
    додаєм +38
    якщо 380 присутнє додає тільки +

    Args:
        phone_number - номер у довільному форматі

    Returns:
        нормалізований номер
    """
    cleaned = re.sub(r"[^\d+]","",phone_number)
    

    if cleaned.startswith("+"):
        return cleaned
   

    if cleaned.startswith("380"):
        return "+" + cleaned
   
    return "+38" + cleaned


def get_upcoming_birthdays (users: list[dict]) -> list[dict]:
    """
    Повертає список користувачів в яких ДН в наступні 7 днів. Якщо припадає на 
    вихідні переносимо на понеділок.

    Args:
        users: список словників з ключами
            name (str)
            birthday (str) у форматі YYYY.MM.DD

    Returns:
        Список словників
        [{'name':..., 'congratulation_date': 'YYYY.MM.DD'},..]
    """
    
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
   
    result: list[dict] = []
    

    for user in users:
        name = user.get("name")
        birthday_str = user.get("birthday")
        

        if not name or not birthday_str:
            continue
        

        try:
            birthday = datetime.strptime(birthday_str, "%Y.%m.%d").date()
        except ValueError:
            continue
        

        try:
            birthday_this_year = date(today.year, birthday.month, birthday.day)
        except ValueError:
            # випадок 29 лютого у невискосному році пропускаємо або вирішемо окремо
            continue

        
        if birthday_this_year < today:
            try:
                birthday_this_year = date(today.year + 1, birthday.month, birthday.day)
            except ValueError:
                continue

        
        if today <= birthday_this_year <= end_date:
            congrat_date = birthday_this_year
            

            if congrat_date.weekday() == 5: #субота
                congrat_date += timedelta(days=2)
            elif congrat_date.weekday() == 6: # неділя
                congrat_date +=timedelta(days=1)
            

            result.append(
                {
                "name": name,
                "congratulation_date": congrat_date.strftime("%Y.%m.%d")
            }
        )   
                 
    return result


def main() -> None:
    """Запуск усіх завднаь"""
    print("ЗАВДАННЯ 1:")
    print(get_days_from_today("1982-07-01"))
    print(get_days_from_today("2030-01-01"))
    print(get_days_from_today("2020/10/09"))
    print()

    print("ЗАВДАННЯ 2:")
    print(get_numbers_ticket(1, 49, 6))
    print(get_numbers_ticket(1, 36, 5))
    print(get_numbers_ticket(1, 10, 20))
    print()

    print("ЗАВДАННЯ 3:")
    raw_numbers = [
        "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    ]
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print(sanitized_numbers)
    print()

    print("ЗАВДАННЯ 4:")
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Oleksii Test", "birthday": "1982.02.10"}
    ]
    print(get_upcoming_birthdays(users))

if __name__ == "__main__":
    main()