#Exercise 11 

#loop 1-100 

numbers_list= []
for number in range(1,101):
    numbers_list.append(number)
print(numbers_list)

#BitMaker's FizzBuzz 
for number in range(1,101):
    if number % 3 == 0:
        print('Bit')
    elif number % 5 == 0:
        print('Maker')
    elif number % 3 == 0 and number % 5 == 0:
        print ('BitMaker')
    else: 
        print(number)

# EXERCISE 12

print ('PIZZA MAKER ')
print('How many pizzas do you want to order?')
quantity = int(input()) 
quantity += 1 

for x in range(1, quantity): 
    print('How many toppings for pizza{}?'.format(x))
    toppings = int(input())
    print('You have ordered a pizza with {} toppings.'.format(toppings))
