import random
import time

import requests
from bs4 import BeautifulSoup
# from app.models import Serial

#
# def get_data(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
#     }
#     for item in range(0, 1620, 10):
#
#         req = requests.get(url + f"{item}&s=2&t=0", headers)
#
#         soup = BeautifulSoup(req.text, "lxml")
#         if soup.find(string='По Вашим критериям ничего не найдено :('):
#             print("Stop")
#             break
#
#         serial_list = soup.find_all('div', class_='row')
#         for serial in serial_list:
#             serial_url = "https://www.lostfilm.tv" + serial.find('a').get('href')
#             serial_img = "https:" + serial.find('img', class_='thumb').get('src')
#             serial_name_ru = serial.find('div', class_='name-ru').text
#             serial_name_en = serial.find('div', class_='name-en').text
#             serial_detail = serial.find('div', class_='details-pane').text.split('\n')[2].strip()
#             serial_status = False if 'Завершен' in serial_detail else True
#             print(serial_name_en)
#             s = Serial(
#                     name_en=serial_name_en,
#                     name_ru=serial_name_ru,
#                     serial_url=serial_url,
#                     serial_img=serial_img,
#                     serial_status=serial_status,
#                 )
#             s.save()
#         time.sleep(random.randrange(1, 3))


def pars_episodes(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
    }

    req_episode = requests.get(url + "/seasons", headers)
    req_news = requests.get(url + "/news", headers)

    soup_episodes = BeautifulSoup(req_episode.text, "lxml")
    soup_news = BeautifulSoup(req_news.text, "lxml")

    episode_data = soup_episodes.find('tr')
    if episode_data.get('class'):
        episode_data = episode_data.find_next('tr')
    last_episode = episode_data.find('td', class_='gamma').find('div').find('span').text
    last_episode_url = url + episode_data.find('td', class_='gamma').get('onclick').split("'")[1]

    news_data = soup_news.find('div', class_='news-box')
    last_news_url = url + news_data.find('a').get('href')
    last_news = news_data.find('div', class_='news-title').text

    # print(url.split('/')[-1])
    # print('Last episode      ', last_episode)
    # print('Last episode url', last_episode_url)
    # print('Last news url      ', last_news_url)
    # print('Last news name      ', last_news)
    return last_news, last_news_url, last_episode, last_episode_url

urls = [
    'https://www.lostfilm.tv/series/The_Rookie',
    'https://www.lostfilm.tv/series/Sex_Education',
    'https://www.lostfilm.tv/series/The_Last_of_Us',
]
