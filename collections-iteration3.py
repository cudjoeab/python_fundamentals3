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








