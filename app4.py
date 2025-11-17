import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

cuyear = int(input("what year would you like to see FOR?"))

for movie in data:
    if movie["year"] == cuyear:
        print(movie["title"]) 
        print(movie["year"])