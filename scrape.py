#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


def main():

    url = "https://books.toscrape.com/"

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        print("Top Books Available")
        print("-------------------")

        for book in books[:10]:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text

            print("Book:", title)
            print("Price:", price)
            print("-------------------")

    else:
        print("Unable to access website")


if __name__ == "__main__":
    main()
