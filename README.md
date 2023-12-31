# Трекер днів народження (Завдання 1)
Скрипт на Python для трекінгу та виведення списку майбутніх днів народження протягом наступного тижня з заданого списку юзерів.

## Можливості
- відстеження майбутніх днів народження протягом наступного тижня
- перенесення святкування днів народження на наступний понеділок, які припадають на вихідні

## Вимоги
- Python 3.x
- бібліотеки collections та datetime

## Встановлення
- клонуйте репозиторій або завантажте файли проекту

## Використання
- створіть список юзерів з датами днів народження
```
users = [
    {"name": "Ім'я Одне", "birthday": datetime(РРРР, ММ, ДД)},
    {"name": "Ім'я Два", "birthday": datetime(РРРР, ММ, ДД)},
    ...
]
```
- використовуйте функцію get_birthdays_per_week з вищевизначеним списком юзерів

# Бот асистент для управління контактами (Завдання 2)
Бот асистент на Python, що дозволяє зберігати та управляти контактними даними - імена та телефонні номери. 

## Можливості
- додавання нових контактів
- оновлення телефонних номерів у існуючих контаків
- пошук телефонних номерів за іменем контака
- відображення списку всіх збережених контактів
- взаємодія через командний рядок

## Вимоги
- Python 3.x

## Встановлення
- клонуйте репозиторій або завантажте файли проекту
- відкрийте термінал або командний рядок та перейдіть до директорії проекту
- запустіть бота, використовуючи команду python contact_assistant_bot.py

## Використання
Після запуску бота ви зможете взаємодіяти з ним через командний рядок. 
Використовуйте наступні команди:
```
hello: бот відповість привітанням та запитає про подальші дії.
add [ім'я] [номер телефону]: додати новий контакт.
change [ім'я] [новий номер телефону]: оновити номер телефону існуючого контакту.
phone [ім'я]: отримати номер телефону контакту.
all: показати всі збережені контакти.
close або exit: закрити бота.
```