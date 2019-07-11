#LISTS
fav_colours = ['black', 'turqouise', 'yellow']
family_ages = [25, 46, 34, 40, 41, 27]
coin_flip = ['tails', 'heads', 'tails', 'tails','tails']
fav_artists = ['Janelle Monae', 'Tush', 'Lizzo']

#DICTIONARIES 

dictionary = {
    'burgeon': 'to sprout, bloom, or flourish',
    'lionize': 'to treat with great importance',
    'flair':   'a natural talent or unique style'
}

fav_movies = {
    'The Lion King': 1994,
    'Akira': 1988, 
    'The Shining': 1980,
    'Us': 2019,
    'Paprika': 2006
}

cities = {
    'Toronto': 2930000,
    'Orleans': 116668,
    'Kingston': 666041
}

siblings = {
    'Andrew': 46,
    'Shawn': 41,
    'Jason': 40, 
    'Dustin': 34,
    'Ekua': 25
}

#Exercise 1

print(coin_flip)
print(fav_colours[0])
print(sorted(family_ages))
family_ages.append(0)
print(family_ages)
print(fav_movies['Akira'])

#Exercise 2

print(fav_colours[-1])
cities.update({'Fort Erie': 30710 })
print(cities)
coin_flip.reverse()
print(coin_flip)
print(cities['Toronto'])

for artist in fav_artists:
    print("I think {} is great.".format(artist))

#Exercise 3
#1
print(fav_artists[0:2])

#2
for movie, year in fav_movies.items():
    print("{} came out in {}.".format(movie, year))
#3
family_ages.sort()
family_ages.reverse()
print(family_ages)

#4 
fav_movies.update({'Beauty and the Beast': '1991 & 2017'})
print(fav_movies)

#Exercise 4

#1 
for member in family_ages:
    if member <=30:
        print(member)

#2
family_ages.sort()
print(family_ages[-1])

#3
print(coin_flip.count('heads'))

#4
fav_artists.pop(2)
print(fav_artists)

#5
print(cities['Toronto'])
cities['Toronto'] = 2930001
print(cities['Toronto'])

#Exercise 5 
#1 
total = 0

for population in cities:
    total

#2 
for sibling, age in siblings.items():
    if age <= 30:
        age = 'young'
    else:
        age = 'old'
    print("{} is {}.".format(sibling,age))
        

#3 
print(fav_colours[1:2+1])

#4 increase everyones' age 

for index, age in enumerate(family_ages):
    family_ages[index] = age + 1

print(family_ages)

#5 adding two new colours 
print(fav_colours)
fav_colours.append('pink')
fav_colours.append('lavender')
print(fav_colours)

#Exercise 6 

#1 
movie_archive = {
    1999: ['The Matrix', 'Star Wars: Episode 1', 'The Mummy'],
    2009: ['Avatar', 'Star Trek', 'District 9'],
    2019: ['How to Train Your Dragon 3', 'Toy Story 4', 'Star Wars: Episode 9']
}
#2
phone_buttons = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ['*',0, '#']
]

#3
countries = {
    'Canada': {'N_America', False},
    'Ghana': {'Africa', False},
    'Australia': {'Australia', True}
}

#Exercise 7

#1
message = 'I will not skateboard in the halls.'

print (message * 20)

#2 list with message 

detention = [message * 20]
print(detention)

#3 
numbers_list= []
for number in range(1,51):
    numbers_list.append(number)
print(numbers_list)


#4 
total = 0 
for number in numbers_list:
    total = total + number
print(total)

#5

new_numbers_list= []
for number in range(1,51):
    for triple_number in range(1,4):
        new_numbers_list.append(number)
        
print(new_numbers_list)

   

#6 
for country, island in countries:
    if island == False:
        print(country)
    if island == True:
        print(country)