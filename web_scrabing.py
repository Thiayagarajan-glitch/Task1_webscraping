
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

url = "https://books.toscrape.com/"

books_data = []

while url:

    print("Scraping:", url)

    response = requests.get(url, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        name = book.h3.a["title"]

        price = book.find(
            "p", class_="price_color"
        ).text

        rating = book.find(
            "p", class_="star-rating"
        )["class"][1]

        availability = book.find(
            "p", class_="availability"
        ).text.strip()

        books_data.append({
            "name": name,
            "price": price,
            "rating": rating,
            "availability": availability
        })

    next_page = soup.select_one("li.next a")

    if next_page:
        url = urljoin(url, next_page["href"])
    else:
        url = None
df = pd.DataFrame(books_data)
df.to_csv("books_dataset.csv", index=False)

print("\nFirst 5 records:")
print(df.head())

print("\nTotal books collected:", len(df))
print("Dataset saved successfully!")

import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

url = "https://books.toscrape.com/"

books_data = []

while url:

    print("Scraping:", url)

    response = requests.get(url, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        name = book.h3.a["title"]

        price = book.find(
            "p", class_="price_color"
        ).text

        rating = book.find(
            "p", class_="star-rating"
        )["class"][1]

        availability = book.find(
            "p", class_="availability"
        ).text.strip()

        books_data.append({
            "name": name,
            "price": price,
            "rating": rating,
            "availability": availability
        })

    next_page = soup.select_one("li.next a")

    if next_page:
        url = urljoin(url, next_page["href"])
    else:
        url = None
df = pd.DataFrame(books_data)
df.to_csv("books_dataset.csv", index=False)

print("\nFirst 5 records:")
print(df.head())

print("\nTotal books collected:", len(df))
print("Dataset saved successfully!")

