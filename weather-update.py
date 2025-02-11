from bs4 import BeautifulSoup
import requests
import random

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'
]

headers = {
    'User-Agent': random.choice(user_agents),
    'Accept-Language': 'en-US,en;q=0.5'
}


def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers)
    print("Searching......\n")
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()
        print(location)
        print(time)
        print(info)
        print(weather + "°C")
    except IndexError:
        print("Weather information could not be retrieved. Please try again later.")


city = input("Enter the Name of Any City: ")
city = city + " weather"
weather(city)
