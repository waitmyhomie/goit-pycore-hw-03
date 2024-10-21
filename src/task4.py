from datetime import datetime, timedelta
#Завдання 4 start

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.10.27"},
    {"name": "Ann Johnson", "birthday": "1980.11.27"},
    {"name": "Tommy Lee", "birthday": "1995.02.27"},
]

def get_upcoming_birthdays(users):
    #get today date
    today = datetime.today().date()
    #get upcoming birthdays
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
            
       #if birthday already passed this year, set next year birthday
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
        #get days difference from today to birthday
        days_difference = (birthday_this_year - today).days
        if 0 <= days_difference <= 7:
            congratulation_date = birthday_this_year
            #if birthday is on weekend, set it on monday
            if congratulation_date.weekday() in [5, 6]:
                days_to_monday = (7 - congratulation_date.weekday()) % 7
                congratulation_date += timedelta(days=days_to_monday)
                
                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                })
    
    return upcoming_birthdays


#initialaze function
upcoming_birthdays = get_upcoming_birthdays(users)
#output
print(f"Upcoming birthdays: {upcoming_birthdays}")
#Завдання 4 end