# ↓↓↓↓ Модуль os  ↓↓↓↓
# https://pythonworld.ru/moduli/modul-os.html
# https://python-scripts.com/import-os-example
# https://docs-python.ru/standart-library/modul-os-python/

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

##############################
# ↓↓ os.getcwd() ↓↓ — вывод текущей директории. Метод возвращает строку в Юникоде,представляющую текущий рабочий каталог.
# Вывод текущей директории:
import os
# вывести текущую директорию
print("Текущая деректория:", os.getcwd())
# Текущая деректория: C:\Users\37529\PycharmProjects\self_taught_1
# ↑↑↑↑ подробно: https://docs-python.ru/standart-library/modul-os-python/funktsija-getcwd-modulja-os/

##############################
# ↓↓ os.mkdir(<name>) ↓↓ — cоздание папки. Ошибка FileExistsError будет вызвана, потому что такая папка уже есть.
# Создание папки (каталога):

import os
os.mkdir("folder_for_files")
# После ее выполнения в текущем рабочем каталоге тут же появится новая папка с названием «folder_for_files».

# Если запустить ее еще раз, будет вызвана ошибка FileExistsError, потому что такая папка уже есть.
# Для решения проблемы нужно запускать команду только в том случае, если каталога с таким же именем нет.
# Этого можно добиться следующим образом:
# повторный запуск mkdir с тем же именем вызывает FileExistsError,
# вместо этого запустите:
import os
if not os.path.isdir("folder_for_files"):
     os.mkdir("folder_for_files")
# Функция os.path.isdir() вернет True, если переданное имя ссылается на существующий каталог.
# ↑↑↑↑ подробно: https://docs-python.ru/standart-library/modul-os-python/funktsija-mkdir-modulja-os/

##############################
# ↓↓ os.path.isdir(<name>) ↓↓ — вернет True, если переданное имя ссылается на существующий каталог.

import os
os.path.isdir("folder_for_files")
# True  # если папка уже создана
# False  # если папки нет в данной директории

##############################
# ↓↓ os.chdir(<name>) ↓↓ — изменение директории. Ошибка FileNotFoundError будет вызвана, потому что такая папка отсутствует.
# Изменение директории:

import os
# вернуться в предыдущую директорию
os.chdir("..")
# C:\Users\37529\PycharmProjects
os.chdir('C:\\Users\\37529\\PycharmProjects\\self_taught_1')  # переход в заданную директорию, очень важно обращать на использование \ /
# или так ↓↓
os.chdir('C:/Users/37529/PycharmProjects/self_taught_1')
# если будет так, то будет error ↓↓
os.chdir('C:\Users\37529\PycharmProjects\self_taught_1')  # из-за направления slash(/) backslash(\)
# ↑↑↑↑ подробно: https://docs-python.ru/standart-library/modul-os-python/funktsija-chdir-modulja-os/

##############################
# ↓↓ os.makedirs(<name>) ↓↓ — создание вложенных папок. Ошибка FileExists Error будет вызвана, потому что такая папка уже есть.
# Создание вложенных папок:
# Предположим, вы хотите создать не только одну папку, но и несколько вложенных:
import os
os.makedirs("nested1/nested2/nested3")
# результат: ↓↓
print(os.getcwd())
# C:\Users\37529\PycharmProjects\self_taught_1\nested1\nested2\nested3
# ↑↑↑↑ подробно: https://docs-python.ru/standart-library/modul-os-python/funktsija-makedirs-modulja-os/

##############################
# ↓↓ open(<filename>, <mode>) ↓↓ — создание файлов.
# создать новый текстовый файл:
text_file = open("text.txt", "w")  # import os для создания файлов не нужен. Можно использовать встроенную функцию open()
# запить текста в этот файл
text_file.write("This is a text file")  # добавляет строку с текстом в файл, а в консоли при вызове команды возвращает длину строки => 19
# СМОТРЕТЬ НИЖЕ. БУДЕТ РАССМОТРЕНО ОТДЕЛЬНО: РАБОТА С ФАЙЛАМИ

##############################
# ↓↓ os.rename(<old>, <new>) ↓↓ — переименование файлов. Ошибка FileNotFoundError будет вызвана, потому что такой файл отсутствует.
import os
# переименовать text.txt на file.txt.txt
os.rename("text.txt", "file.txt") # Функция os.rename() принимает 2 аргумента: имя файла (text.txt) или папки, которые нужно переименовать и новое имя(file.txt)
os.rename('nested3', 'nested4')
# предварительно заходим в директорию, где находится папка для переименования
# ↑↑↑↑↑ подробно: https://docs-python.ru/standart-library/modul-os-python/funktsija-rename-modulja-os/
os.renames()  # ↓↓↓↓↓↓↓
# os.renames() => рекурсивно переименовывает пустые директории или переименовывает конечный файл:
# https://docs-python.ru/standart-library/modul-os-python/funktsija-renames-modulja-os/

##############################
# ↓↓ os.replace(<old>, <new>) ↓↓ — перемещение файлов. Ошибка FileNotFoundError будет вызвана, потому что такой файл отсутствует.
# Если # в папке уже есть файл с таким же именем, он будет перезаписан.
import os
os.replace('text.txt', 'C:\\Users\\37529\\PycharmProjects\\self_taught_1\\text.txt')  # из текущей папки в папку self_taught_1
# ↑↑↑↑↑ подробно: https://docs-python.ru/standart-library/modul-os-python/funktsija-replace-modulja-os/

##############################
# os.listdir(<name>) — возвращает список, который содержит имена файлов в папке.
# Если в качестве аргумента не указывать ничего, вернется список файлов и папок текущего рабочего каталога.
# Ошибка FileNotFoundError будет вызвана, потому что такой файл отсутствует.

# распечатать все файлы и папки в текущем каталоге
print("Все папки и файлы:", os.listdir())
# ↑↑↑↑↑ подробно: https://docs-python.ru/standart-library/modul-os-python/funktsija-listdir-modulja-os/

##############################
# os.walk(<path>) — это генератор дерева каталогов. Он будет перебирать все переданные составляющие.
# распечатать все файлы и папки рекурсивно
import os
for dirpath, dirnames, filenames in os.walk("."):  # качестве аргумента передано значение «.», которое обозначает верхушку дерева
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))  # Метод os.path.join() был использован для объединения текущего пути с именем файла/папки
    # перебрать файлы
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))
# ↑↑↑↑↑ подробно: https://docs-python.ru/standart-library/modul-os-python/funktsija-walk-modulja-os/

##############################
# os.path.join(<path>, <path>) — используется для объединения текущего пути с именем файла/папки.
import os.path
os.path.join('home', 'User', 'Desktop', 'file.txt')
# 'home\\User\\Desktop\\file.txt'
os.path.join('/home', 'User/Desktop', 'file.txt')
# '/home\\User/Desktop\\file.txt'
os.path.join('\\home', 'User\\Desktop', 'file.txt')
# '\\home\\User\\Desktop\\file.txt'
os.path.join('/home', '/User/Desktop', 'file.txt')
# '/User/Desktop\\file.txt'
os.path.join('User/Desktop', '/home', 'file.txt')
# '/home\\file.txt'
# ↑↑↑↑↑ подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-join-modulja-os-path/

##############################
# os.remove(<filename>) — удаление файлов. Ошибка FileNotFoundError будет вызвана, потому что такой файл отсутствует.
# удалить этот файл
import os
os.remove('C:/Users/37529/PycharmProjects/self_taught_1/text.txt')  # удалит файл с указанным именем (не каталог)
# ↑↑↑↑↑ подробно: https://docs-python.ru/standart-library/modul-os-python/funktsija-remove-modulja-os/

##############################
# os.rmdir(<dirname>) — удаление папки. Ошибка FileNotFoundError будет вызвана, потому что такая папка отсутствует.
import os
os.rmdir("folder")
# ↑↑↑↑↑ подробно: https://docs-python.ru/standart-library/modul-os-python/funktsija-rmdir-modulja-os/

##############################
# os.removedirs(<dirname>) — удаление вложенных папок. Ошибка FileNotFoundError будет вызвана, потому что такая папка отсутствует.
# Удаляются только пустые каталоги.
import os
os.removedirs("nested1/nested2/nested4")  # удалит только пустые каталоги
# ↑↑↑↑↑ подробно: https://docs-python.ru/standart-library/modul-os-python/funktsija-removedirs-modulja-os/

##############################
# open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None) — создание файла.



# ↓↓↓↓ Модуль os.path ↓↓↓↓













# ↓↓↓↓ Модуль os  ↓↓↓↓
# https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html
# https://pythonru.com/osnovy/fajly-v-python-vvod-vyvod
# https://www.internet-technologies.ru/articles/chtenie-i-zapis-faylov-v-python.html



