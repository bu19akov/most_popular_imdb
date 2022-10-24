import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/moviemeter/?sort=rk,asc&mode=simple&page=1'

r = requests.get(url)
if r.status_code != 200:
    print(f"The URL returned {requests.get(url).status_code}!")
else:
    cont = r.content
    soup = BeautifulSoup(cont, "html.parser")
    names = soup.find_all("td", {"class": "titleColumn"})
    ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})
    films = dict()
    for i in range(len(names)):
        try:
            name = names[i].find("a", title=True).text
            rating = float(ratings[i].find("strong").text)
        except AttributeError:
            rating = 0.
        films[name] = rating
    if input("Do you want to sort result descending by rating? (yes/no)") == "yes":
        films_sorted = sorted(films.items(), key=lambda x:x[1], reverse=True)
        for films in films_sorted:
            print(f"Rating: {films[1]}, Title: {films[0]}")
    else:
        for film in films:
            print(f"Rating: {films[film]}, Title: {film}")
