#Exercise 9
#1
grocery_list = ['carrots','toilet paper','apples','salmon']

# for item in grocery_list:
#     print(" * {}.".format(item))

#2 add rice 

#new_item = input() --- can get user input 
grocery_list.append('rice')
for item in grocery_list:
   print(" * {}.".format(item))

# # # create a function where we return instead of print 
# def print_grocery_list(the_list):
#     to_print = '' 
#     for item in the_list:
#         to_print += f'* {item}\n'
#     return to_print 

# grocery_list = ['carrots','toilet paper','apples','salmon']
# print(grocery_list_display(grocery_list))
# grocery_list.append('rice')
# print(grocery_list_display(grocery_list))


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


# EXERCISE 10

students = {
  'cohort1': 34,
  'cohort2': 42,
  'cohort3': 22
}

#3
students.update({'cohort4': 43})

#4
print(students.keys())

#5 change classroom size 

for cohort, size in students.items():
    new_size = size * 0.95
    print('{} now has {} students.'.format(cohort,size))

#6 delete 

students.pop('cohort2')
print(students)

#7 total number of students 

total = 0 
for size in students:
    total = total + size 
    print('there are {} students.'.format(cohort,total))






















