import random
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
print(f"Ticket numbers: {numbers_ticket}")

        

#Завдання 2 end