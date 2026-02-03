'''19. Days Until Birthday
Input: birthday = datetime.date(2025, 12, 25)
Output: Days left: 162'''
from datetime import date



from datetime import datetime, date

user_dob = input("Enter in MM-DD-YYYY format birthdate: ")

birthday_date = datetime.strptime(user_dob, "%m-%d-%Y").date()
today_day = date.today()

total_days = (birthday_date - today_day).days

print(f"Days left: {total_days}")
