from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.chrome.options
from bs4 import BeautifulSoup as bs
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import threading


URL = 'https://lalafo.kg/kyrgyzstan/kvartiry/arenda-kvartir'


def get_html_with_selenium(url):
    options = selenium.webdriver.chrome.options.Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = selenium.webdriver.Chrome(options=options)
    driver.get(url)

    try:
        # Дождитесь загрузки кнопки
        button = WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="show-button"]'))
        )
        # Нажмите кнопку
        button.click()

        # Дождитесь загрузки контента после нажатия кнопки
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="phone-wrap"]'))
        )

        # Получите HTML после загрузки контента
        html = driver.page_source
    finally:
        driver.quit()

    return html


def get_html(url, params=''):
    return requests.get(url=url, params=params).text


def get_data(html, lst: list):
    a = html
    all_data = bs(a, 'html.parser')
    blocks = all_data.find_all('a', class_='lf-ad-tile__link')[:1]
    # detail_html_list = []

    def find_deposit(data):
        index = data.index('Депозит, сом:') if 'Депозит, сом:' in data else -1
        if index != -1:
            try:
                deposit = int(data[index + 1])
            except (IndexError, ValueError):
                deposit = 0
        else:
            deposit = 0
        return deposit

    def create_dop_info(data):
        text = ''
        for num, i in enumerate(data):
            if num != len(data)-1:
                text += f'{i}, '
            else:
                text += i
        return text

    for i in blocks:
        href = 'https://lalafo.kg' + i.attrs['href']
        detail_html = bs(get_html_with_selenium(href), 'html.parser')
        phone_number_element = detail_html.find('div', class_='phone-wrap')
        if phone_number_element:
            phone_number = phone_number_element.get_text().strip()
            if phone_number and '+' in phone_number and 'x' not in phone_number:
                lst.append({
                    'title': i.get_text(),
                    'price': detail_html.find('span', class_='price').get_text(),
                    'phone': phone_number,
                    'deposit': find_deposit([i.get_text() for i in
                                             detail_html.find('div', class_='main-content').find_all('p',
                                                                                                     class_='Paragraph secondary')]),
                    'dop_info': create_dop_info([i.get_text() for i in
                                                 detail_html.find('div', class_='main-content').find_all('a',
                                                                                                         class_='LinkText primary-black extra-small')]),
                    'img': [i.attrs['src'] for i in detail_html.find_all('img') if 'lalafo.com' in i.attrs['src']]
                })


def parser(count, frm='', to=''):
    info_list = []
    threads = []
    for _ in range(count):
        thread = threading.Thread(target=get_data, args=(get_html(url=URL, params={'price[from]': frm, 'price[to]': to}), info_list))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return info_list


print(parser(30))





