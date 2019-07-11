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


