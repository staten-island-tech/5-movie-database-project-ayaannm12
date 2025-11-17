import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)


want2 = input("What genre movie are you looking for??? ")

for movie in data:
    if want2 in movie["genres"]:   # FIXED
        print(movie["title"])
        print(movie["year"])
        print(movie["genres"])