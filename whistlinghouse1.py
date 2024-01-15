import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.reddit.com/r/nosleep/comments/dyqd5e/something_walks_whistling_past_my_house_every/')
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
elem1 = soup.find('h1', id='post-title-t3_dyqd5e')
elem2 = soup.find('div', id='t3_dyqd5e-post-rtjson-content')
print(elem1.text)
print(elem2.text)

# parses html content from a reddit story