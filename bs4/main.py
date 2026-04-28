from bs4 import BeautifulSoup
import requests

res = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
)
page_content = res.content

soup = BeautifulSoup(page_content, "html.parser")

movie_titles = [
    f"{movie.string}\n" for movie in soup.find_all(name="h3", class_="title")
]


movie_titles.reverse()
# print(movie_titles)

with open("bs4/movies.txt", "w") as file:
    file.writelines(movie_titles)
