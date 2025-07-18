import requests
from bs4 import BeautifulSoup

def get_courses(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    courses = set()
    for tag in soup.find_all(['td', 'li']):
        text = tag.get_text(strip=True)
        if len(text) > 10 and not any(x in text.lower() for x in ['часов', 'семестр']):
            courses.add(text)
    return list(courses)