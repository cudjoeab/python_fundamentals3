#Exercise 9
#1
grocery_list = ['carrots','toilet paper','apples','salmon']

# for item in grocery_list:
#     print(" * {}.".format(item))

#2 add rice 

grocery_list.append('rice')
for item in grocery_list:
   print(" * {}.".format(item))

#3 length count
print(len(grocery_list))

#4 checking list items 
# # print('Is the item on the list?')
# # item  = input()
# grocery_list = ['carrots','toilet paper','apples','salmon']

# def checking(item): 
#     if grocery_list[item] == True:
#         return "You need to pick up bananas." 
#     elif grocery_list[item] == False:
#         return "You don't need to pick up bananas." 

# print(checking(item))

#4 display second item 
print('The second item is {}.'.format(grocery_list[1]))

#5 alpha order

# for item in grocery_list:
#     sorted(grocery_list)
#     print('* {}.'.format(item))

#6 

grocery_list.pop(3)
grocery_list.append('chicken')
print(grocery_list)





















