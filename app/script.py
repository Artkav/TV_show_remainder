import random
import time
import requests
from bs4 import BeautifulSoup
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mass_mail, send_mail


# Return list of shows

def get_data(search_str=''):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.183 "
                      "Mobile Safari/537.36"
    }
    url = 'https://www.lostfilm.tv/search/?q=' + search_str

    req = requests.get(url, headers)

    soup = BeautifulSoup(req.text, 'lxml')

    show_search = soup.find('div', class_='serials-list').find_all('div', class_='row-search')
    show_list = []
    if len(show_search):
        for show in show_search:
            show_info = {'show_url': 'https://www.lostfilm.tv' + show.find("a").get("href"),
                         'img_url': 'https:' + show.find("img", class_="thumb").get("src"),
                         'name_ru': show.find("div", class_="name-ru").text,
                         }
            show_list.append(show_info)
    return show_list


# Return last episode and last news of show

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
    last_episode = episode_data.find('td', class_='gamma').find('div').text.strip().split('\n')[0]
    last_episode_url = 'https://www.lostfilm.tv' + episode_data.find('td', class_='gamma').get('onclick').split("'")[1]

    news_data = soup_news.find('div', class_='news-box')
    last_news_url = 'https://www.lostfilm.tv' + news_data.find('a').get('href')
    last_news = news_data.find('div', class_='news-title').text

    return last_news, last_news_url, last_episode, last_episode_url


# Sends an email to all users who are subscribed to the show

def send_subj_mail(show, subject, subj_name, url):
    message = f"В сериале {show} вышла новая {subject} - {subj_name}. Посмотреть можно по ссылке {url}"
    recipient_list = []
    for user in show.users.all():
        recipient_list.append(user.email)
    send_mail(f'Вышла новая {subject}.', message, EMAIL_HOST_USER, recipient_list)
