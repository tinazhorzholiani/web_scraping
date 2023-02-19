import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_links(url, filename):
    f = open(filename, "w+")
    for i in range(1, 101):
        html_doc = requests.get(url + str(i)).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        data = soup.find_all('a', href=True, class_='styles__link--3QJ5N')
        for info in data:
            f.write(info.get('href') + '\n')
        print(f'page {i} is done')
        time.sleep(0.2)
    f.close()


def get_products(url):
    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    img = soup.find('img')['src']
    name = soup.find('h1',
                     class_='styles__box--2Ufmy styles__text--23E5U styles__display2--3HydH styles__display-block--3kWC4 styles__margin-none--3Ub2V styles__marginTop-xs--2KZR5').text
    price = soup.find('span',
                      class_='styles__box--2Ufmy styles__text--23E5U styles__display2--3HydH styles__display-block--3kWC4').text
    dict = {'name': name, 'image': img, 'price': price}
    return dict


def main(url, filename1):
    imgs = []
    names = []
    prices = []
    # get_links(url, filename1)
    with open(filename1, 'r') as f:
        my_list = [line.strip() for line in f]
    for info in my_list:
        diction = get_products(info)
        imgs.append(diction.get('image'))
        names.append(diction.get('name'))
        prices.append(diction.get('price'))
        time.sleep(0.2)
    dict = {'names': names, 'images': imgs, 'prices': prices}
    df = pd.DataFrame(dict)
    df.to_csv('table.csv', index=False)


if __name__ == '__main__':
    main('https://www.redbubble.com/shop/*?page=', 'redbubbleINFO')
