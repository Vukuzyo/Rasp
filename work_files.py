import time
from PIL import Image      #установил = (Pyllow) для работы с изображениями
import os                  #ббиблиотека в которой есть функция которая возвращает список имен всех файлов и поддиректорий в указанной директории

def file_test_txt():                  #работа с файлами(текстовыми)
    file = open(r"test.txt",'r+')     #чтение + запись если будет полный путь то все робит

    #for i in range(0, 10):           #цикл
    #    file.write(f"Number {i}\n")  #запись в файл

    for line in file:                 #line = строка
        #if "2" in line:               #если в line есть 2
            #continue                  #пропустить
        print(line)#вывод
    file.close()

#работа с изображениями
def image():
    PIC = r"C:\Users\User\OneDrive\Рабочий стол\ЭВЭЛ\задание.jpg"              #full name
    with Image.open(PIC) as img:
        img.show()                                                              #вывод на экран
        img.save(r"C:\Users\User\OneDrive\Рабочий стол\алгоритмизация\test.png")#сохранение

#исключения
def exceptions():
    try:
        #В блоке try мы выполняем инструкцию, которая может породить исключение
        pass
    except:
        #в блоке except мы перехватываем их
        pass
    else:
        #если исключения не было
        pass
    finally:
        #Finally выполняет блок инструкций в любом случае, было ли исключение, или нет
        #(применима, когда нужно непременно что-то сделать, к примеру, закрыть файл)
        pass
def sort():
     directory = r"C:\Users\User\OneDrive\Изображения\Снимки экрана"     #Указываем путь к директории
     file_names = os.listdir(directory)                                   # Получаем список файлов

     #Эксперемент: вывод имени всех файлов(изображений созданных в 2024-11-05) и помещение их в новую директоию
     counter = 0  #cчетчик для ренейминга файлов
     for i in file_names:                         #i в списке файлов

         if "2024-11-05" in i:                   #условие

             f_n_s = fr"{directory}\{i}"         #полное имя файла
             img = Image.open(f_n_s)             #открытие файла
             img.save(fr"C:\Users\User\OneDrive\Рабочий стол\projekt_image\f2024-11-05 {counter}.png")#сохранение
             counter += 1  #счетчик +1
             print(f"файл {f_n_s} перемещен")    #оповещение
             img.close()                         #закрытие файла
             time.sleep(2)                       #сон на 1с
     print("все готово")

