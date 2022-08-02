# ↓↓↓↓ Модуль os  ↓↓↓↓
# https://pythonworld.ru/moduli/modul-os.html
# https://python-scripts.com/import-os-example
# https://docs-python.ru/standart-library/modul-os-python/

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

# ↑↑↑↑↑ подробно: https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-open/
                # https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html
                # https://pythonru.com/osnovy/fajly-v-python-vvod-vyvod
                # https://www.internet-technologies.ru/articles/chtenie-i-zapis-faylov-v-python.html





##############################
# ↓↓↓↓ Модуль os.path ↓↓↓↓
# https://pythonworld.ru/moduli/modul-os-path.html
# os.path является вложенным модулем в модуль os, и реализует некоторые полезные функции для работы с путями.
# os.path.abspath(path) - возвращает нормализованный абсолютный путь.
# os.path.basename(path) - базовое имя пути (эквивалентно os.path.split(path)[1]).
# os.path.commonprefix(list) - возвращает самый длинный префикс всех путей в списке.
# os.path.dirname(path) - возвращает имя директории пути path.
# os.path.exists(path) - возвращает True, если path указывает на существующий путь или дескриптор открытого файла.
# os.path.expanduser(path) - заменяет ~ или ~user на домашнюю директорию пользователя.
# os.path.expandvars(path) - возвращает аргумент с подставленными переменными окружения ($name или ${name} заменяются переменной окружения name). Несуществующие имена не заменяет. На Windows также заменяет %name%.
# os.path.getatime(path) - время последнего доступа к файлу, в секундах.
# os.path.getmtime(path) - время последнего изменения файла, в секундах.
# os.path.getctime(path) - время создания файла (Windows), время последнего изменения файла (Unix).
# os.path.getsize(path) - размер файла в байтах.
# os.path.isabs(path) - является ли путь абсолютным.
# os.path.isfile(path) - является ли путь файлом.
# os.path.isdir(path) - является ли путь директорией.
# os.path.islink(path) - является ли путь символической ссылкой.
# os.path.ismount(path) - является ли путь точкой монтирования.
# os.path.join(path1[, path2[, ...]]) - соединяет пути с учётом особенностей операционной системы.
# os.path.normcase(path) - нормализует регистр пути (на файловых системах, не учитывающих регистр, приводит путь к нижнему регистру).
# os.path.normpath(path) - нормализует путь, убирая избыточные разделители и ссылки на предыдущие директории. На Windows преобразует прямые слеши в обратные.
# os.path.realpath(path) - возвращает канонический путь, убирая все символические ссылки (если они поддерживаются).
# os.path.relpath(path, start=None) - вычисляет путь относительно директории start (по умолчанию - относительно текущей директории).
# os.path.samefile(path1, path2) - указывают ли path1 и path2 на один и тот же файл или директорию.
# os.path.sameopenfile(fp1, fp2) - указывают ли дескрипторы fp1 и fp2 на один и тот же открытый файл.
# os.path.split(path) - разбивает путь на кортеж (голова, хвост), где хвост - последний компонент пути, а голова - всё остальное. Хвост никогда не начинается со слеша (если путь заканчивается слешем, то хвост пустой). Если слешей в пути нет, то пустой будет голова.
# os.path.splitdrive(path) - разбивает путь на пару (привод, хвост).
# os.path.splitext(path) - разбивает путь на пару (root, ext), где ext начинается с точки и содержит не более одной точки.
# os.path.supports_unicode_filenames - поддерживает ли файловая система Unicode.


##############################
# ↓↓↓↓ Модуль pathlib ↓↓↓↓
# Использование модуля pathlib для манипуляции путями файловых систем в Python 3
# https://www.digitalocean.com/community/tutorials/how-to-use-the-pathlib-module-to-manipulate-filesystem-paths-in-python-3-ru



##############################
# Сериализация/десериализация объектов

# Модуль pickle

