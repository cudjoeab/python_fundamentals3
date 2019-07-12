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

#PizzaMaker
# ask user how many pizzas they want to order 
def get_pizzas():
    print('How many pizzas do you want to order?')
    return int(input())
print(get_pizzas())

def get_toppings(pizza):
    print('How many toppings do you want on pizza{}.'.format(pizza))
    return (int(input())) 




# # have their quantity set the list length 
# toppings = []
# for x in quantity: 
#     print ('How many toppings for pizza{}?'.format(x))
#     toppings.append(number)


# # for every pizza in the list, ask how many toppings 


# #confirm that they ordered a pizza with their amount of toppings 


# # pizzas = []
# # for pizza in pizzas:
# #     pizzas.append(pizza + 1)

# # print(pizzas)






