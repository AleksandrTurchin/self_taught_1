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
# Синтаксис :
# fp = open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# Параметры:
# file - абсолютное или относительное значение пути к файлу или файловый дескриптор открываемого файла.
# mode - необязательно, строка, которая указывает режим, в котором открывается файл. По умолчанию 'r'.
# buffering - необязательно, целое число, используемое для установки политики буферизации.
# encoding - необязательно, кодировка, используемая для декодирования или кодирования файла.
# errors - необязательно, строка, которая указывает, как должны обрабатываться ошибки кодирования и декодирования. Не используется в -бинарном режиме
# newline - необязательно, режим перевода строк. Варианты: None, '\n', '\r' и '\r\n'. Следует использовать только для текстовых файлов.
# closefd - необязательно, bool, флаг закрытия файлового дескриптора.
# opener - необязательно, пользовательский объект, возвращающий открытый дескриптор файла.

# f = open(file, mode)  # обязательный синтаксис для работы с файлами
# где:
# file = имя открываемого файла
# mode = режим открытия файла. Он может быть: для чтения, записи и т. д.
# режимы открытия файла mode:
    # r	- Только для чтения. Указатель файла помещается в начале файла. Это режим "по умолчанию"
    # w	- Только для записи. Создаст новый файл, если не найдет с указанным именем.
    # rb - Только для чтения (бинарный). Указатель файла помещается в начале файла. Это режим "по умолчанию"
    # wb - Только для записи (бинарный). Создаст новый файл, если не найдет с указанным именем.
    # r+ - Для чтения и записи. Указатель файла помещается в начало файла
    # rb+ -	Для чтения и записи (бинарный).
    # w+ - Для чтения и записи. Создаст новый файл для записи, если не найдет с указанным именем.
    # wb+ - Для чтения и записи (бинарный). Создаст новый файл для записи, если не найдет с указанным именем.
    # a - Откроет для добавления нового содержимого. Создаст новый файл для записи, если не найдет с указанным именем. Указатель файла находится в конце файла, если файл существует. То есть файл находится в режиме добавления
    # a+ - Откроет для добавления нового содержимого. Создаст новый файл для чтения записи, если не найдет с указанным именем. Указатель файла находится в конце файла, если файл существует. То есть файл находится в режиме добавления
    # ab - Откроет для добавления нового содержимого (бинарный). Создаст новый файл для записи, если не найдет с указанным именем. Указатель файла находится в конце файла, если файл существует. То есть файл находится в режиме добавления
    # ab+ - Откроет для добавления нового содержимого (бинарный). Создаст новый файл для чтения записи, если не найдет с указанным именем. Указатель файла находится в конце файла, если файл существует. То есть файл находится в режиме добавления

# При работе с файлами в текстовом формате рекомендуется указывать тип кодировки:
f = open('file.txt', mode='r', encoding='utf-8')
# такой синтаксис тоже поддерживает:
f = open('file.txt', 'r')
f = open('file.txt', 'r', encoding='utf-8')

# после работы с файлом нужно обязательно произвести закрытие файлов, чтобы не было потери данных в файле:
f.close()  # Этот метод не полностью безопасен. Если при операции возникает исключение, выполнение будет прервано без закрытия файла.
# ↑↑↑↑↑ подробно: https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/metod-file-close/
# Более безопасный способ – использование блока try...finally:
try:
   f = open('file.txt',encoding = 'utf-8')
   # выполнение операций с файлом
finally:
   f.close()
# ↑↑ Это гарантирует правильное закрытие файла даже после возникновения исключения, прерывающего выполнения программы.

# Также для закрытия файла можно использовать конструкцию with. Оно гарантирует, что файл будет закрыт при выходе из блока with.
# При этом не нужно явно вызывать метод close(). Это будет сделано автоматически:
with open('file.txt',encoding = 'utf-8') as f:
   # выполнение операций с файлом

# проверить закрыт файл или нет можно сл.методом:
f.closed  # возвращает True, если файл закрыт, False - если открыт

# ↓↓ Запись в файл Python ↓↓
# Чтобы записать данные в файл в Python, нужно открыть его в режиме 'w', 'a' или 'x'.
# Но будьте осторожны с режимом 'w'. Он перезаписывает файл, если то уже существует. Все данные в этом случае стираются.

# ↓↓↓ подробно: https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/metod-file-write/  ↓↓↓
# Запись строки или последовательности байтов (для бинарных файлов) осуществляется методом write().
# Он возвращает количество символов, записанных в файл:
with open('file.txt','w',encoding='utf-8') as f:
   f.write('my first file\n')  # \n позволяет переносить на новую строку, иначе запись будет в одну строку
   f.write('This filen\n')
   f.write('contains three lines\n')

# Метод file.writelines() записывает список строк в файл:
text = ['This is 1st line\n', 'This is 2nd line\n', 'This is 3rd line\n']
with open('file.txt', 'w') as f:
    f.writelines(text)  # пишем
with open('file.txt', 'r') as f:
    print(f.read())  # читаем, что получилось
# This is 1st line
# This is 2nd line
# This is 3rd line
# ↑↑↑  подробно: https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/metod-file-writelines/  ↑↑↑

# ↓↓ Чтение из файла Python ↓↓
# подробно: https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/metod-file-read/
# Чтение из файла Python, нужно открыть его в режиме чтения.
# Использовать метод read(size), чтобы прочитать из файла данные в количестве, указанном в параметре size.
# Если параметр size не указан, метод читает и возвращает данные до конца файла:
f = open('file.txt', 'r', encoding = 'utf-8')
f.read(4)  # чтение первых 4 символов
# 'my f'
f.read(4)  # чтение следующих 4 символов
#'irst'
f.read()  # чтение остальных данных до конца файла
# 'my first filenThis filencontains three linesn'
f.read()  # дальнейшие попытки чтения возвращают пустую строку
# ''
# ↑↑ Метод read() возвращает новые строки как 'n'.
# Когда будет достигнут конец файла, при дальнейших попытках чтения мы получим пустые строки.

# Чтобы изменить позицию курсора в текущем файле, используется метод seek().
# Метод tell() возвращает текущую позицию курсора (в виде количества байтов).
# ↓↓↓ подробно: https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/metod-file-tell/  ↓↓↓
f.tell()  # получаем текущую позицию курсора в файле
# 10
# ↓↓↓ подробно: https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/metod-file-seek/  ↓↓↓
f.seek(0)   # возвращаем курсор в начальную позицию
# 0
print(f.read())  # читаем весь файл
# my first file
# This file
# contains three lines
# можем прочитать файл построчно в цикле for:
for line in f:
    print(line, end = '')  # Извлекаемые из файла строки включают в себя символ новой строки 'n'. Чтобы избежать вывода, используем пустой параметр end метода print(),.
    # my first file
    # This filen
    # contains three lines
# метод readline(), чтобы извлекать отдельные строки.
# ↓↓↓ подробно: https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/metod-file-readline/ ↓↓↓
# Он читает файл до символа новой строки:
f.readline()
# 'my first file\n'
f.readline()
# 'This filen\n'
f.readline()  # по порядку перебирает все строки файла
# 'contains three lines\n'
f.readline()  # дальнейшие попытки чтения возвращают пустую строку
# ''
# Метод readlines() возвращает список оставшихся строк.
# ↓↓↓ подробно: https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/metod-file-readlines/  ↓↓↓
f.readlines()
# ['my first file\n', 'This filen\n', 'contains three lines\n']


# Python работа с файлами - основные методы:
# close() -	Закрытие файла. Не делает ничего, если файл закрыт.
# detach() - Отделяет бинарный буфер от TextIOBase и возвращает его.
# fileno() - Возвращает целочисленный дескриптор файла.
# flush() - Вызывает сброс данных (запись на диск) из буфера записи файлового потока.
# isatty() - Возвращает значение True, если файловый поток интерактивный.
# read(n) - Читает максимум n символов из файла. Читает до конца файла, если значение отрицательное или None.
# readable() - Возвращает значение True, если из файлового потока можно осуществить чтение.
# readline(n=-1) - Читает и возвращает одну строку из файла. Читает максимум n байт, если указано соответствующее значение.
# readlines(n=-1) - Читает и возвращает список строк из файла. Читает максимум n байт/символов, если указано соответствующее значение.
# seek(offset,from=SEEK_SET) - Изменяет позицию курсора.
# seekable() - Возвращает значение True, если файловый поток поддерживает случайный доступ.
# tell() - Возвращает текущую позицию курсора в файле.
# truncate(size=None) - Изменяет размер файлового потока до size байт. Если значение size не указано, размер изменяется до текущего положения курсора.
# writable() - Возвращает значение True, если в файловый поток может производиться запись.
# write(s) - Записывает строки s в файл и возвращает количество записанных символов.
# writelines(lines) - Записывает список строк lines в файл.

# ↓↓↓ пример записи в файл списка: ↓↓↓
f = open('file.txt', 'w')  # откроем файл на запись
l = [str(i)+str(i-1) for i in range(20)]  # создаем список
# ['0-1', '10', '21', '32', '43', '54', '65', '76', '87', '98', '109', '1110', '1211', '1312', '1413', '1514', '1615', '1716', '1817', '1918']
for index in l:
    f.write(index + '\n')  # запись в файл осуществляется с помощью метода write
    # 0-1
    # 10
    # 21
    # 32
    # 43
    # 54
    # 65
    # 76
    # 87
    # 98
    # 109
    # 1110
    # 1211
    # 1312
    # 1413
    # 1514
    # 1615
    # 1716
    # 1817
    # 1918
f.close()  # после окончания работы с файлом его обязательно нужно закрыть с помощью метода close
# теперь пробуем воссоздать этот список из получившегося файла:
f = open('file.txt', 'r')  # открываем файл для чтения
l = [line.strip() for line in f]
print(l)
# # ['0-1', '10', '21', '32', '43', '54', '65', '76', '87', '98', '109', '1110', '1211', '1312', '1413', '1514', '1615', '1716', '1817', '1918']
f.close()  # после окончания работы с файлом его обязательно нужно закрыть с помощью метода close





##############################
# ↓↓↓↓ Модуль os.path ↓↓↓↓

# https://pythonworld.ru/moduli/modul-os-path.html
# https://docs-python.ru/standart-library/modul-os-path-python/

# os.path является вложенным модулем в модуль os, и реализует некоторые полезные функции для работы с путями.

# os.path.abspath(path) - возвращает нормализованный абсолютный путь.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-abspath-modulja-os-path/
import os.path
os.path.abspath('file.txt')
print(os.path.abspath('file.txt'))
# C:\Users\37529\PycharmProjects\self_taught_1\folder_for_files\file.txt

# os.path.basename(path) - базовое имя пути (эквивалентно os.path.split(path)[1]).
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-basename-modulja-os-path/
import os.path
os.path.basename('C:/Users/37529/PycharmProjects/self_taught_1/folder_for_files/file.txt')
print(os.path.basename('C:/Users/37529/PycharmProjects/self_taught_1/folder_for_files/file.txt'))
# 'file.txt'
os.path.basename('C:/Users/37529/PycharmProjects/self_taught_1/folder_for_files')
# 'folder_for_files'

# os.path.commonpath(paths) - возвращает самый длинный общий подпуть каждого пути в последовательности paths
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-commonpath-modulja-os-path/
import os.path
os.path.commonpath(['/Users/PycharmProjects/self_taught_1/folder_for_files', '/Users/37529/PycharmProjects/self_taught_1/folder_for_files'])
# '\Users'
#  Если последовательность paths содержит как абсолютные так и относительные пути,
#  пустые пути или пути находящиеся на разных дисках, то возникает исключение ValueError

# os.path.commonprefix(list) - возвращает самый длинный префикс всех путей в списке.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-commonprefix-modulja-os-path/
import os.path
os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
print(os.path.commonprefix(['/usr/lib', '/usr/local/lib']))
# '/usr/l'
print(os.path.commonpath(['/usr/lib', '/usr/local/lib']))
# '/usr'
#  Если список пуст, то вернет пустую строку ''

# os.path.dirname(path) - возвращает имя директории пути path.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-dirname-modulja-os-path/
import os.path
os.path.dirname('C:/Users/37529/PycharmProjects/self_taught_1/folder_for_files/file.txt')
print(os.path.dirname('C:/Users/37529/PycharmProjects/self_taught_1/folder_for_files/file.txt'))
# 'C:/Users/37529/PycharmProjects/self_taught_1/folder_for_files'
os.path.dirname('file.txt')
# ''
os.path.dirname('C:/Users/37529/PycharmProjects/self_taught_1/folder_for_files')
# 'C:/Users/37529/PycharmProjects/self_taught_1'

# os.path.exists(path) - возвращает True, если path указывает на существующий путь или дескриптор открытого файла.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-exists-modulja-os-path/
import os.path
os.path.exists('C:/Users/37529/PycharmProjects/self_taught_1/folder_for_files/file.txt')
# True
os.path.exists('C:/Users/PycharmProjects/self_taught_1/folder_for_files/file.txt')
# False

# os.path.expanduser(path) - заменяет ~ или ~user на домашнюю директорию пользователя.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-expanduser-modulja-os-path/
import os
os.path.expanduser(~/file.txt)
# '/home/docs-python/file.txt'
# Изменим переменную 'HOME' среды окружения
os.environ["HOME"] = '/home/testuser'
os.path.expanduser(~/file.txt)
# '/home/testuser/file.txt'
os.path.expanduser('~docs-python/file.txt')
# '/home/docs-python/file.txt'

# os.path.expandvars(path) - возвращает аргумент с подставленными переменными окружения ($name или ${name} заменяются переменной окружения name).
# Несуществующие имена не заменяет. На Windows также заменяет %name%.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-expandvars-modulja-os-path/
import os.path
os.path.expandvars("/home/${USER}/file.txt")
# '/home/docs-python/file.txt'
os.path.expandvars("${HOME}")
# '/home/docs-python'
os.path.expandvars(b"/home/${USER}/file.txt")
# b'/home/docs-python/file.txt'

# os.path.getatime(path) - время последнего доступа к файлу, в секундах.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-getatime-modulja-os-path/
import os.path
os.path.getatime('/home/docs-python/os.path.txt')
# 1585213409.8081393
atime = os.path.getatime('/home/docs-python/os.path.txt')
import time
time.ctime(atime)
# 'Thu Mar 26 12:03:29 2020'
atime = os.path.getatime('/home/docs-python')
time.ctime(atime)
# 'Thu Mar 26 15:07:01 2020'

# os.path.getmtime(path) - время последнего изменения файла, в секундах.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-getmtime-modulja-os-path/
import os.path
os.path.getmtime('/home/docs-python/os.path.txt')
# 1585212542.419274
mtime = os.path.getmtime('/home/docs-python/os.path.txt')
import time
time.ctime(mtime)
# 'Thu Mar 26 11:49:02 2020'
mtime = os.path.getmtime('/home/docs-python')
time.ctime(mtime)
# 'Thu Mar 26 15:07:01 2020'

# os.path.getctime(path) - время создания файла (Windows), время последнего изменения файла (Unix).
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-getctime-modulja-os-path/
import os.path
os.path.getctime('/home/docs-python/os.path.txt')
# 1585213403.6642175
ctime = os.path.getctime('/home/docs-python/os.path.txt')
import time
time.ctime(ctime)
'Thu Mar 26 12:03:23 2020'
ctime = os.path.getctime('/home/docs-python')
time.ctime(ctime)
'Thu Mar 26 15:07:01 2020'

# os.path.getsize(path) - размер файла в байтах.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-getsize-modulja-os-path/
import os.path
os.path.getsize('/home/docs-python/os.path.txt')
# 11828
os.path.getsize(b'/home/docs-python/os.path.txt')
# 11828
os.path.getsize('/home/docs-python')
# 4096

# os.path.isabs(path) - является ли путь абсолютным.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-isabs-modulja-os-path/
import os.path
os.path.isabs('/home/User/Documents')
# True
os.path.isabs('home/User/Documents')
# False
os.path.isabs('../User/Documents')
# False

# os.path.isfile(path) - является ли путь файлом.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-isfile-modulja-os-path/
import os.path
os.path.isfile('/home/User/Documents/file.txt')
# True
os.path.isfile('/home/User/Documents')
# False

# os.path.isdir(path) - является ли путь директорией.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-isdir-modulja-os-path/
import os.path
os.path.isdir('/home/User/Documents/file.txt')
# False
os.path.isdir('/home/User/Documents')
# True

# os.path.islink(path) - является ли путь символической ссылкой.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-islink-modulja-os-path/
import os, pathlib
# создадим файл
p = pathlib.Path('file.txt')
p.touch()
# создадим символьную ссылку
os.symlink(p, 'link')
# ПРОВЕРКА
os.path.islink('link')
# True
os.path.islink('file.txt')
# False
# Очистка
p.unlink()
os.unlink('link')

# os.path.ismount(path) - является ли путь точкой монтирования.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-ismount-modulja-os-path/
import os.path
os.path.ismount('/run')
# True
os.path.ismount('/dev')
# True
os.path.ismount('/home')
# False

# os.path.join(path1[, path2[, ...]]) - соединяет пути с учётом особенностей операционной системы.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-join-modulja-os-path/
import os.path
os.path.join('home', 'User', 'Desktop', 'file.txt')
# 'home/User/Desktop/file.txt'
os.path.join('/home', 'User/Desktop', 'file.txt')
# '/home/User/Desktop/file.txt'
os.path.join('/home', '/User/Desktop', 'file.txt')
# '/User/Desktop/file.txt'
os.path.join('User/Desktop', '/home', 'file.txt')
# '/home/file.txt'

# os.path.normcase(path) - нормализует регистр пути (на файловых системах, не учитывающих регистр, приводит путь к нижнему регистру).
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-normcase-modulja-os-path/
# Windows
import os.path
os.path.normcase('C:\User\admin\Documents')
# c:\\user\\admin\\documents
os.path.normcase('/hoMe/UseR/')
# \\home\\user
os.path.normcase(r'C:\Users/Desktop')
# c:\\users\\desktop

# os.path.normpath(path) - нормализует путь, убирая избыточные разделители и ссылки на предыдущие директории. На Windows преобразует прямые слеши в обратные.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-normpath-modulja-os-path/
import os.path
os.path.normpath('/home/./Documents')
# /home/Documents
os.path.normpath('/home/../Documents')
# '/Documents'
os.path.normpath('/home/user/temp/../Documents')
# '/home/user/Documents'

# os.path.realpath(path) - возвращает канонический путь, убирая все символические ссылки (если они поддерживаются).
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-realpath-modulja-os-path/
import os.path, pathlib
p = pathlib.Path('file.txt')
# создадим файл
p.touch()
# канонический путь
path = os.path.realpath(p)
path
# '/home/docs-python/file.txt'
# проверка символической ссылки
link = os.path.join(os.getcwd(), 'Desktop', 'link')
link
# '/home/docs-python/Desktop/link'
# создадим символическую ссылку
os.symlink(path, link)
# канонический путь по ссылке
os.path.realpath(link)
# '/home/docs-python/file.txt'

# os.path.relpath(path, start=None) - вычисляет путь относительно директории start (по умолчанию - относительно текущей директории).
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-relpath-modulja-os-path/
import os.path
path = "/home/User/Desktop/file.txt"
start = "/home/User/"
os.path.relpath(path, start)
# Desktop/file.txt
start = "/home/docs-python/"
os.path.relpath(path, start)
# '../User/Desktop/file.txt'
start = "/home/docs-python/Docs"
os.path.relpath(path, start)
# '../../User/Desktop/file.txt'

# os.path.samefile(path1, path2) - указывают ли path1 и path2 на один и тот же файл или директорию.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-samefile-modulja-os-path/
import os.path
path = '/home/docs-python/Desktop/file.txt'
link = '/home/docs-python/link.txt'
os.symlink(path, link)
os.path.samefile(path, link)
# True
path1 = os.path.join(os.getcwd(), 'Desktop', file.txt)
# True
os.path.samefile(path, path1)
# True

# os.path.sameopenfile(fp1, fp2) - указывают ли дескрипторы fp1 и fp2 на один и тот же открытый файл.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-sameopenfile-modulja-os-path/
import os.path
path = '/home/docs-python/Desktop/file.txt'
fd1 = os.open(path, os.O_RDONLY)
fp = open(path, mode ='r')
fd2 = fp.fileno()
os.path.sameopenfile(fd1, fd2)
# True
close(fd1)
close(fd2)

#  samestat(path) - возвращает True, если кортежи stat1 и stat2 ссылаются на один и тот же файл
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-samestat-modulja-os-path/
import os, pathlib
path1 = '/home/docs-python/Desktop/file.txt'
path2 = '/home/docs-python/Documents/file.txt'
stat1 = os.stat(path1)
fd = os.open(path1, os.O_RDONLY)
stat2 = os.fstat(fd)
os.path.samestat(stat1, stat2)
# True
p = pathlib.Path(path1)
stat3 = p.stat()
os.path.samestat(stat2, stat3)
# True
stat4 = os.stat(path2)
os.path.samestat(stat1, stat4)
# False

# os.path.split(path) - разбивает путь на кортеж (голова, хвост), где хвост - последний компонент пути, а голова - всё остальное.
# Хвост никогда не начинается со слеша (если путь заканчивается слешем, то хвост пустой). Если слешей в пути нет, то пустой будет голова.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-split-modulja-os-path/
import os.path
os.path.split('/home/User/Desktop/file.txt')
# ('/home/User/Desktop', 'file.txt')
os.path.split('/home/User/Desktop/')
# ('/home/User/Desktop', '')
os.path.split('/home/User/Desktop')
# ('/home/User', 'Desktop')

# os.path.splitdrive(path) - разбивает путь на пару (привод, хвост).
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-splitdrive-modulja-os-path/
import os.path
# UNIX
os.path.splitdrive('/home/User/Desktop/file.txt')
# ('', '/home/User/Desktop/file.txt')
# Windows
os.path.splitdrive('C:\User\Documents\file.txt')
# ('C:', '\User\Documents\file.txt')
os.path.splitdrive('\\host\computer\dir\file.txt')
# ('\\host\computer', '\dir\file.txt')

# os.path.splitext(path) - разбивает путь на пару (root, ext), где ext начинается с точки и содержит не более одной точки.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/funktsija-splitext-modulja-os-path/
import os.path
os.path.splitext('/home/User/Desktop/file.txt')
# ('/home/User/Desktop/file', '.txt')
os.path.splitext('/home/User/Desktop/')
# ('/home/User/Desktop/', '')
os.path.splitext('/home/User/Desktop')
# ('/home/User/Desktop', '')

# os.path.supports_unicode_filenames - поддерживает ли файловая система Unicode.
# подробно: https://docs-python.ru/standart-library/modul-os-path-python/svojstvo-supports-unicode-filenames-modulja-os-path/
import os.path
os.path.supports_unicode_filenames
# False


##############################
# ↓↓↓↓ Модуль pathlib ↓↓↓↓
# Использование модуля pathlib для манипуляции путями файловых систем в Python 3
# https://www.digitalocean.com/community/tutorials/how-to-use-the-pathlib-module-to-manipulate-filesystem-paths-in-python-3-ru
# https://docs-python.ru/standart-library/modul-pathlib-python/
# ↓↓↓ Модуль pathlib VS модулям os и os.path в Python ↓↓↓
# https://docs-python.ru/standart-library/modul-pathlib-python/modul-pathlib-vs-moduljam-os-os-path/
# Функции модулей os и os.path          Функции модуля pathlib
# os.path.abspath()                     Path.resolve()
# os.chmod()	                        Path.chmod()
# os.mkdir()	                        Path.mkdir()
# os.makedirs()	                        Path.mkdir()
# os.rename()	                        Path.rename()
# os.replace()	                        Path.replace()
# os.rmdir()	                        Path.rmdir()
# os.remove(), os.unlink()	            Path.unlink()
# os.getcwd()	                        Path.cwd()
# os.path.exists()	                    Path.exists()
# os.path.expanduser()	                Path.expanduser() и Path.home()
# os.listdir()	                        Path.iterdir()
# os.path.isdir()	                    Path.is_dir()
# os.path.isfile()	                    Path.is_file()
# os.path.islink()	                    Path.is_symlink()
# os.link()	                            Path.hardlink_to()
# os.symlink()	                        Path.symlink_to()
# os.readlink()	                        Path.readlink()
# os.path.relpath()	                    Path.relative_to()
# os.stat()	                            Path.stat(), Path.owner(), Path.group()
# os.path.isabs()	                    PurePath.is_absolute()
# os.path.join()	                    PurePath.joinpath()
# os.path.basename()	                PurePath.name
# os.path.dirname()	                    PurePath.parent
# os.path.samefile()	                Path.samefile()
# os.path.splitext()	                PurePath.suffix



##############################
# Сериализация/десериализация объектов

# Модуль pickle

