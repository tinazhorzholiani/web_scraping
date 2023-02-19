import re
import requests
from bs4 import BeautifulSoup
import webbrowser


def all(filename):
    needed = []
    file = open(filename, "r")
    data = file.read().split('{')
    for a in data:
        if re.search('^"id".*},$', a):
            needed.append(a.strip('},'))
    return needed


def each(string):
    keys = []
    values = []
    for some in string.split(','):
        keys.append(some.split(':')[0].strip('"'))
        values.append(some.split(':')[1].strip('"'))
    table = dict(zip(keys, values))
    return table


# url = 'https://www.cartune.ge/'
def scripter(url, filename):
    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    data = soup.find('script', defer=False)
    f = open(filename, "w+")
    f.write(str(data))
    return filename


if __name__ == '__main__':
    mechanics = []
    for one in all(scripter('https://www.cartune.ge/', "data.txt")):
        mechanics.append(each(one))
        print(each(one))
    # webbrowser.open('https://www.cartune.ge/mechanic/' + mechanics[0].get('id'))

