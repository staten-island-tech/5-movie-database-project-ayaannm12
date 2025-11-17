import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

afteryear = int(input("what year would you like to see movies AFTER???"))
for movie in data:
    if movie["year"] > afteryear:
        print(movie["title"]) 
        print(movie["year"])