import time

from bs4 import BeautifulSoup
import requests
import os.path


#https://codeby.net/threads/parsim-i-skachivaem-neskuchnye-oboi-s-ispolzovaniem-potokov-v-python.79770/ +вайб сайт где рассказал как скачивать
#https://ciur.ru/stmit/DocLib8/DocLib53/Forms/AllItems/%D0%A0%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%BD%D1%8F%D1%82%D0%B8%D0%B9%2017.12.2024.pdf
#полная ссылка вроде бы на страницу с фоточками

# def mainProg():
#     url_stmiit = "http://stmit.ru/wp-content/uploads/2025/01/Расписание-занятий-14.01.2025.pdf"
#
#     def stmiit_text(url):
#         # парсинг с альтернативки
#         request = requests.get(url).text  # запрос на получение кода
#         soup = BeautifulSoup(request, "lxml")  # htrml code
#         print(soup)
#
#     url_1488 = "http://stmit.ru/wp-content/uploads/2025/01/Расписание-занятий-14.01.2025.pdf"  # pdf file url
#
#     def imd_downlowand(Url_img):  # cкачивание
#         req = requests.get(url=Url_img)  # запрос на нее ???
#         # танец с бубном + скачивение ее в директорию
#         with open(os.path.join(Url_img, r'C:\Users\User\OneDrive\Рабочий стол\projekt_image\rasp.jpg'), 'wb') as file:
#             file.write(req.content)  # final dans s BUBNOM
#         time.sleep(5)
#
#         # image = Image.load(r'C:\Users\User\OneDrive\Рабочий стол\projekt_image\rasp.jpg')
#         # изменить размер изображения и сохранить изображение с измененным размером
#         # image.resize(300, 300)
#         # сохраните изображение с измененным размером
#         # image.save(r'C:\Users\User\OneDrive\Рабочий стол\projekt_image\rasp.jpg')
#
#     imd_downlowand(url_1488)
#
#     # парсинг с ссыылки с расширением PDF
#     def href_read(url):
#         request = requests.get(url).text  # запрос на получение кода
#         request = request.encode('utf-8').decode('cp1251')
#         soup = BeautifulSoup(request, "lxml")  # htrml code
#         print(soup.text)

#https://dict.fu-lab.ru/dict-p?id=129449&page={НОМЕР СТРАНИЦЫ}&letter1=%D0%B{НОМЕР БУКВЫ C 0}

#https://dict.fu-lab.ru/dict-p?id=129449&page=1&letter1=%D0%B{НОМЕР БУКВЫ C 0}

