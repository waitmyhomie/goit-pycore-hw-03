import re
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
print(f"Clean phone numbers: {clean_phone_numbers}")

#Завдання 3 end