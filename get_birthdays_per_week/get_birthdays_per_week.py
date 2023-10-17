from collections import defaultdict
from datetime import datetime, timedelta
import calendar

def get_birthdays_per_week(users):
    # Поточна дата
    today = datetime.today().date()
    # Дата через тиждень
    week_ahead = today + timedelta(days=7)
    
    # Створюємо словник
    birthdays = defaultdict(list)
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        
        # Визначаємо дату народження
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження вже минув, тоді визначаємо для наступного року
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        # Перевіряємо, чи день народження на наступний тиждень
        if today <= birthday_this_year <= week_ahead:
            # Визначаємо день тижня (0 - понеділок)
            day_of_week = birthday_this_year.weekday()
            day_name = calendar.day_name[day_of_week]
            
            # Якщо день народження припадає на вихідні (5 - субота, 6 - неділя) - переносимо на понеділок
            if day_of_week == 5 or day_of_week == 6:
                day_name = 'Monday'
            
            birthdays[day_name].append(name)
    
    # Результат
    for day, users in birthdays.items():
        print(f'{day}: {", ".join(users)}')

def main():
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 30)}, # День народженння не в найближчі 7 днів
        {"name": "John Doe", "birthday": datetime(1988, 10, 22)},  # День народження в неділю
        {"name": "Jane Doe", "birthday": datetime(1990, 10, 18)},  # День народження в середу
        {"name": "Taylor Otwell", "birthday": datetime(1990, 10, 18)},  # День народження в середу
    ]

    get_birthdays_per_week(users)
    
# Точка входу
if __name__ == "__main__":
    main()
