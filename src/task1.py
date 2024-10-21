from datetime import datetime
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
print(f"Days from today:{days_difference}")


#Завдання 1 end