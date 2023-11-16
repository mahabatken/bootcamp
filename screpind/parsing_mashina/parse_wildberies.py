from bs4 import BeautifulSoup
import requests
import csv

url = "https://lalafo.kg/"

def parsing_data():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', class_='main-feed__container')
    products = container.find_all('article', class_='adTile-wrap')
    result = []
    for prod in products:
        desc = prod.find('div', class_='adTile-title__wrap').find('a').text
        price = prod.find('p', class_='adTile-price').text
        image = prod.find('img')
        if image is not None:
            image = image.get('data-src')
        avatar = prod.find('img', class_='userAvatar-photo')
        if avatar is not None:
            avatar = avatar.get('data-src')
        data = {'desc': desc, 'price': price, 'image': image, 'avatar': avatar}
        result.append(data)
    
    write_to_csv(result)


def write_to_csv(data: list):
    with open('lalafo.csv', 'w') as file:
        count = 1
        fieldnames = ['№', 'desc', 'price', 'image', "avatar"]
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№',
            'desc': 'Description:',
            'price': 'Price:',
            'image': 'Image Url:',
            "avatar": "Avatar",
        })
        for prod in data:
            writer.writerow({
                '№': count,
                'desc': prod['desc'],
                'price': prod['price'],
                'image': prod['image'],
                "avatar": prod["avatar"]
            })
            count += 1


parsing_data()