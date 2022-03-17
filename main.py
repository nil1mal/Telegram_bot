# coding=utf-8
import time

from selenium import webdriver
import bs4, sys
import urllib

driver = webdriver.Firefox(executable_path=r'/home/nil/Documents/Telegram_bot/geckodriver-v0.30.0-linux64/geckodriver')
driver.get("https://service.berlin.de/terminvereinbarung/termin/tag.php?termin=1&anliegen[]=120926&dienstleisterlist=122210,122217,122219,122227,122231,122238,122243,122252,122260,122262,122254,122271,122273,122277,122280,122282,122284,327539,122291,122285,122286,122296,150230,122301,122297,122294,122312,122314,122304,122311,122309,122281,122279,122276,122274,122267,122246,122251,122257,122208,122226&herkunft=http%3A%2F%2Fservice.berlin.de%2Fdienstleistung%2F120926%2F")
#driver.minimize_window()

html = driver.page_source
soup = bs4.BeautifulSoup(html)
print(soup)

found = False

while found is False:
    elements = soup.find_all("td", {"class": "buchbar"})

    if len(elements)<1:
        for th in soup.findAll('th', attrs={'class':'next'}):
            link = "https://service.berlin.de" + th.find('a')['href']

        driver.get(link)
        time.sleep(5)

    else:
        found = True

driver.close()