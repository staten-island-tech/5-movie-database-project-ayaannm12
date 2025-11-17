data = json.load(movies)
from time import *
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