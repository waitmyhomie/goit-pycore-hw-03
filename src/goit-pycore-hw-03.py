from datetime import datetime, timedelta
import random
import re

##uncomment print function to see output of each task


#Завдання 1 start

# date in past which can be changed 
date_in_past = "09.10.2028"

#function which return days difference from today to date in past
def get_days_from_today(date_in_past):
    #parse text date to datetime
    date_in_past = datetime.strptime(date_in_past, "%d.%m.%Y")
    #return days difference (if date in past bigger and we not use '.days' we get mach minus value with time)
    return (datetime.today() - date_in_past).days

#initialaze function
days_difference = get_days_from_today(date_in_past)

#output
#print(f"Days from today:{days_difference}")


#Завдання 1 end


#Завдання 2 start

#min, max, quantity can be changed
min = 1
max = 1000
quantity =7

#function which return list of random numbers from min to max with quantity
def get_numbers_ticket(min, max, quantity):
    #check if min, max, quantity in range
    if min >= 1 and max <=1000 and quantity <= max and quantity >=min:
        #return sorted list of random numbers
        return sorted(random.sample(range(min, max), quantity))
    else:
        #return empty list if range is wrong
        return []
#initialaze function
numbers_ticket = get_numbers_ticket(min, max, quantity)
#output
# print(f"Ticket numbers: {numbers_ticket}")

        

#Завдання 2 end

#Завдання 3 start

#dirty phone numbers list
dirty_phone_numbers =[
"    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   ",
]
#function which return cleaned phone number
def normilze_phone_number(dirty_phone_number):
    #clean phone number pattern from spaces, tabs, new lines, brackets, minus, and dash
    pattern = r'[\s\t\n()\-]'
    #cleaned phone number
    cleaned_phone_number = re.sub(pattern, '', dirty_phone_number)
    #check if cleaned phone number starts with 0, 3, 8 and add +38, +, +3
    if cleaned_phone_number.startswith('0'):
        cleaned_phone_number = '+38' + cleaned_phone_number
    elif cleaned_phone_number.startswith('3'):
        cleaned_phone_number = '+' + cleaned_phone_number
    elif cleaned_phone_number.startswith('8'):
        cleaned_phone_number = '+3' + cleaned_phone_number
    return cleaned_phone_number

#initialaze function
clean_phone_numbers = [normilze_phone_number(dirty_phone_number) for dirty_phone_number in dirty_phone_numbers]
#output
#print(f"Clean phone numbers: {clean_phone_numbers}")

#Завдання 3 end

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