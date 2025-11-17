import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

want1 = input("what movie do you want to search for?")
for movie in data:
    if movie["title"] == want1:
        print(movie["title"]) 
        print(movie["year"])