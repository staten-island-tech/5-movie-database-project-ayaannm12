import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
from time import *

bayear = int(input("what year would you like to see movies AFTER AND BEFORE???"))
for movie in data:
    sleep(0.01)
    if movie["year"] < bayear:
        print("movies before the year", bayear)
        print(movie["title"]) 
        print(movie["year"])
    elif movie["year"] > bayear:
        print("movie after the year", bayear)
        print(movie["title"]) 
        print(movie["year"])