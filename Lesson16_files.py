# ↓↓↓↓ Модуль os  ↓↓↓↓
# https://pythonworld.ru/moduli/modul-os.html
# https://python-scripts.com/import-os-example

import os
print(os.getcwd())
# C:\Users\37529\PycharmProjects\self_taught_1  # указывает путь файла, который сейчас исполняется интерпретатором пайтон

os.mkdir('test1')  # команда для создание папки

os.listdir()  # указывает список файлов на рабочем столе

os.mkdir('test3')
os.path.isdir('test4')  # проверяет на наличие файла в директории
# false

os.chdir('test2')

os.makedirs("nest1/nest2/nest3")

os.listdir()
# ['nest1]


# ↓↓↓↓ Модуль os  ↓↓↓↓
# https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html
# https://pythonru.com/osnovy/fajly-v-python-vvod-vyvod
# https://www.internet-technologies.ru/articles/chtenie-i-zapis-faylov-v-python.html



