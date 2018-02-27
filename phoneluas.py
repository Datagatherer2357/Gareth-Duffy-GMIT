# Gareth Duffy 25-2-2018
# Phone balance and Luas ticket program

# Phone balance example 

phone_balance = 7.62
bank_balance = 104.39
# phone_balance = 12.34
# bank_balance = 25
if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10
print(phone_balance)
print(bank_balance)

# Odd/even example

# Change the number to experiment!
number = 2357141712
# number = 5 #3 sir
if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")

# Luas ticket example 

# change the age to experiment with the pricing
age = 36

# Set the age limits for Luas fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# Set Luas fares
concession_ticket = 1.25
adult_ticket = 2.45

# Ticket price logic
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
message = "A person who is {} years old will pay €{} to ride the Luas.".format(age,ticket_price)
print(message)
