print(list('asd'))
# ['a', 's', 'd']

print([i for i in range(5)])  # List comprehension - способ создания списка "не лету", т.е. возможность объявить содержимое списка прямо внутри списка
# [0, 1, 2, 3, 4]
# https://github.com/Faoxis/PythonBasicAndApplication/blob/master/week2/3.%20Iterators%20and%20generators.ipynb
# интересная инфа про List comprehension ↑↑↑

print([i ** 2 for i in range(5)])
# [0, 1, 4, 9, 16]

print([i ** 2 for i in range(5) if i % 2 == 0])
# [0, 4, 16]
# это был короткий вариант записи кода ↑:
lst = []
for i in range(5):
    if i % 2 == 0:
        lst.append(i ** 2)
print(lst)
# [0, 4, 16]


_list = [1,2,3,4,5]
print(_list[1])
# 2

_list = [1, 2, 3, 4, 5]
print(_list[-2])
# 4

_list = [1,2,34,56,]
_list1 = _list * 2
print(_list1)
# [1, 2, 34, 56, 1, 2, 34, 56]

_list = [1,2,3,4,5]
print(_list[:1])
# [1]

_list = [1,2,3,4,5]
print(_list[1:4])
# [2, 3, 4]

_list = [1,2,3,4,5,6]
_list[4], _list[2] = _list[2], _list[4]  # a, b = b, a
print(_list)
# [1, 2, 5, 4, 3, 6]

_list = [1,2,3,4,5]
print(max(_list))  # max - только с числами
# 5

_list = [1,2,33,4,5]
print(max(_list))
# 33

_list = ['1', '11', '1111', '11111111']
print(max(_list, key=len))  # по количеству символов
# 11111111

print(max([], default='EMPTY'))  # [] - пустой список
# EMPTY

_list = [1,2,3,4,5]
print(min(_list))  # min - работает также как max
# 1

_list = [1,2,3,4,5]
print(sum(_list))  # работает только с числами
# 15

_list = [1,2,3,4,5]
print(sum(_list, start=10))  # начало отсчета с 10
# 25

_list = [1,2,3,4,5]
print(len(_list))  # количество элементов в списке
# 5

_list = [1,5,4,3,2]
print(sorted(_list))
# [1, 2, 3, 4, 5]
print(sorted(_list, reverse=True))  # возвращает в обратном порядке
#  [5, 4, 3, 2, 1]

_list = ['1', '11', '1111', '11111111']
print(sorted(_list, key=len))  # по количеству символов
#  ['1', '11', '1111', '11111111']

_list = ['1', '11', '1111', '11111111']
print(sorted(_list, key=len, reverse=True))  # по количеству символов, возвращает в обратном порядке
#  ['11111111', '1111', '11', '1']


_list = [1,2,3,4,5]
print(all(_list))    #  аналог bool: print(bool(1)) - True   print(bool('')) - False
# True

_list = [1, 2, 3, 4, None]
print(all(_list))
#  False

_list = [1, 2, 3, 4, '']
print(all(_list))
#  False

_list = [1,2,3,4,5]
print(any(_list))
# True


_list = ['1', '2', 'asd', 'asdad', '4']
print(filter(str.isdigit, _list))
# <filter object at 0x000001F2D5C93D30>
# поэтому надо использовать list ↓↓↓
print(list(filter(str.isdigit, _list)))
# ['1', '2', '4']

_list = ['1', '2', 'asd', 'asdad', '4']
print(list(map(str.isdigit, _list)))
# [True, True, False, False, True]

#  начиная с пайтон 3.6 лучше записывать следующим образом:
print([i for i in _list if str.isdigit(i)])
# ['1', '2', '4']
print([i.isdigit() for i in _list])
# [True, True, False, False, True]


_list = [1, 2, 3, 4, 5]
_list.append('asd')  # используется для добавления элементов к списку.
print(_list)  # добавление нового элемента происходит в конец списка.
# [1, 2, 3, 4, 5, 'asd']
_list1 = [1, 2, 3, 4, 5]
_list2 = ['cat', 'dog']
_list1.append(_list2)
print(_list1)


_list = [1, 2, 3, 4, 4, 5]
print(_list.count(4))
# 2

_list = [1, 2, 3, 4, 4, 5]
_list2 = _list.copy()
_list2 = ['a', 'b', 's']
_list.extend(_list2)
print(_list)
# [1, 2, 3, 4, 4, 5, 'a', 'b', 's']

_list = [1, 2, 3, 4, 4, 5, 'a']
print(_list.index('a'))
# 6
print(_list.index(5))
# 5

_list = [1, 2, 3, 4, 4, 5]
print(_list.insert(1, 'asd'))  #  ?????????????????????
#

my_list = [12, 'USA', 'Sun', 14, 'Mars', 12, 'Mars']
# Передавая индекс как 2, чтобы удалить Sun:
name = my_list.pop(2)
print(name)
print(my_list)
# Sun
# [12, 'USA', 14, 'Mars', 12, 'Mars']
# метод pop() без индекса - возвращает последний элемент:
item = my_list.pop()
print(item)
print(my_list)
# Mars
# [12, 'USA', 14, 'Mars', 12]
# передача индекса за пределами списка:
item = my_list.pop(15)
print(item)
print(my_list)  # ошибка
# Метод pop() удаляет элемент на основе переданного индекса.
# Синтаксис: list.pop(index).
# Принимает лишь один аргумент — индекс.
# Для удаления элемента списка нужно передать его индекс. Индексы в списках стартуют с 0.
# Для получения первого передайте 0. Для удаления последнего передайте -1.
# Этот аргумент не является обязательным.
# Значение по умолчанию равно -1, поэтому по умолчанию будет удален последний элемент.
# Если этот индекс не найден или он вне диапазона, то метод выбросит исключение IndexError: pop index.
# Возвращает элемент, удаленный из списка по индексу. Сам же список обновляется и больше не содержит этот элемент.

_list = [1, 2, 3, 4, 4, 5]
_list.remove(4)  # удаляем первую 3 из списка
print(_list)
# [1, 2, 3, 4, 5]
my_list = [12, 'USA', 'Sun', 14, 'Mars', 12, 'Mars']
my_list.remove(12)  # удаляем элемент 12 в начале
print(my_list)
# ['USA', 'Sun', 14, 'Mars', 12, 'Mars']
my_list.remove('Mars')  # удаляем первый Mars из списка
print(my_list)
# ['USA', 'Sun', 14, 12, 'Mars']
my_list.remove(100)  # ошибка
print(my_list)
# Метод remove() — это встроенный метод, который удаляет первый совпадающий элемент из списка.
# Синтаксис: list.remove(element). Передается элемент, который нужно удалить из списка.
# Метод не возвращает значений.
# https://pythonru.com/osnovy/kak-udalit-element-iz-spiska-python

my_list = [12, 'USA', 'Sun', 14, 'Mars', 12, 'Mars']
element = my_list.clear()
print(element)  # None
print(my_list)  # []
# Метод clear() удаляет все элементы из списка.
# # Синтаксис: list.clear().
# # Нет ни параметров, ни возвращаемого значения.

my_list = list(range(7))
print("Исходный список", my_list)
#Исходный список [0, 1, 2, 3, 4, 5, 6]
# Чтобы удалить первый элемент:
del my_list[0]
print("После удаления первого элемента", my_list)
#После удаления первого элемента [1, 2, 3, 4, 5, 6]
# Чтобы удалить элемент по индексу:
del my_list[5]
print("После удаления элемента", my_list)
# После удаления элемента [1, 2, 3, 4, 5]
# Чтобы удалить несколько элементов:
del my_list[1:5]
print("После удаления нескольких элементов", my_list)
# После удаления нескольких элементов [1]
# Ключевое слово del
# Для удаления элемента из списка можно использовать ключевое слово del с названием списка после него.
# Также потребуется передать индекс того элемента, который нужно удалить.
# Синтаксис: del list[index].
# Также можно выбрать элементы в определенном диапазоне и удалить их с помощью del.
# Для этого нужно передать начальное и конечное значение диапазона. # Синтаксис: del list[start:stop].

_list = [1, 2, 3, 4, 5]
_list.reverse()  #  Перестраивает элементы списка в обратном порядке.
print(_list)  # Внимание: Данный метод модифицирует исходный объект на месте, возвращая при этом None.
# [5, 4, 3, 2, 1]

_list = [1, 5, 3, 2, 4, 6]
_list.sort()  # По умолчанию метод list.sort() в Python упорядочивает элементы списка в порядке возрастания. Это также естественный способ сортировки элементов. Источник: https://pythonim.ru/list/metod-sort-python
print(_list)
# [1, 2, 3, 4, 5, 6]
_list = ['a', 'c', 'd', 'b', 'B', 'C', '1']  # Элементы также могут быть символами ИЛИ числами, и метод sort() продолжит сортировку в порядке возрастания. Источник: https://pythonim.ru/list/metod-sort-python
_list.sort()  # Внимание: Данный метод модифицирует исходный объект на месте, возвращая при этом None.
print(_list)
# ['1', 'B', 'C', 'a', 'b', 'c', 'd']
_list = [1, 5, 3, 2, 4, 6]
_list.sort(reverse=True)  # Обратная сортировка списка
print(_list)
# [6, 5, 4, 3, 2, 1]
_list = ['123', '1234', '12', 'asdfg']
_list.sort(key=len)  # key=len только для строк
print(_list)
# ['12', '123', '1234', 'asdfg']


_list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(len(_list_))
# 3

from copy import copy  #  ????????????????????

from copy import deepcopy  #  ????????????????????


