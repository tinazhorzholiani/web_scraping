import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd

product = []
categories = []
count = 1


def category(url):
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
    areas = soup.find_all('a', href=True, class_="ty-menu__submenu-link")
    for area in areas:
        link = area.get('href')
        if isIn(link):
            if useful_category(link):
                categories.append(link)


def products(url):
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
    areas = soup.find_all('a', href=True, class_=False)
    for area in areas:
        link = area.get('href')
        if isIn(link):
            if useful_product(link):
                product.append(link)


def info(href):
    response = requests.get(href).content
    soup = BeautifulSoup(response, 'html.parser')
    keys = []
    values = []
    for key in soup.find_all('span', class_='ty-product-feature__label'):
        keys.append(key.text)
    for value in soup.find_all('div', class_='ty-product-feature__value'):
        values.append(value.text)
    # forFile(keys, values)
    print(keys)
    print(values)
    time.sleep(0.25)


def forFile(keys, values):
    res = {}
    for key in keys:
        for value in values:
            res[key] = value
            values.remove(value)
    print(res)


def isIn(href):
    if href in product:
        return False
    else:
        return True


def useful_product(href):
    pattern = '^https://alta.ge/.+$'
    result = re.search(pattern, href)
    return result


def useful_category(href):
    pattern = '^https://alta.ge/[^/]*/[^/]+$'
    result = re.search(pattern, href)
    return result


if __name__ == '__main__':
    category('https://alta.ge/')
    for link in categories:
        products(link)
    for new in product:
        info(new)
