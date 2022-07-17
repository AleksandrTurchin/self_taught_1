
print(hash(1))
# 1

print(hash(True))
# 1

print(hash(False))
# 0

print(hash('python'))
# -8162270832320149206

print(hash([1, 2, 3, 4]))  # нельзя включить хэш от списка
# error

print({1:'asdad'})  # ключ справа, значение слева
# {1: 'asdad'}

print({1:'asdasd', 2:'kek', 3:[1, 2, 3, 4,]})  # словари включаются в фигурные скобки, значения разделяются запятой
# {1: 'asdasd', 2: 'kek', 3: [1, 2, 3, 4]}

print({1:'asdasd', 2:'kek', 'asd':4})
# {1: 'asdasd', 2: 'kek', 'asd': 4}

print({1:'asdasd', 2:'kek', [1, 2, 3, 4,]:4})  # нельзя ключам присваивать значения списков
# TypeError

# ↓↓↓ Создание словарей:  ↓↓↓

print(dict(b=4, c=3))  # можно, но так никто не пользуется
# {'b': 4, 'c': 3}

print(dict.fromkeys([1, 2, 3, 4, 5], 'asd'))  # classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None)
# {1: 'asd', 2: 'asd', 3: 'asd', 4: 'asd', 5: 'asd'}
print(dict.fromkeys([1, 2, 3, 4, 5], ['asd', 'qwe']))
# {1: ['asd', 'qwe'], 2: ['asd', 'qwe'], 3: ['asd', 'qwe'], 4: ['asd', 'qwe'], 5: ['asd', 'qwe']}
print(dict.fromkeys([1, 2, 3, 4, 5], ))  # если не присвоить значение ключам, будет None
# {1: None, 2: None, 3: None, 4: None, 5: None}

asd = {i: i**2 for i in range(10)}  # это генератор словарей, аналогичен генераторов списков
print(asd)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
asd = {i: 'asd' for i in range(10)}
print(asd)
# {0: 'asd', 1: 'asd', 2: 'asd', 3: 'asd', 4: 'asd', 5: 'asd', 6: 'asd', 7: 'asd', 8: 'asd', 9: 'asd'}

# Базовые оперции со словарями
# похожи на оперции со  списками ↓↓↓

_list = [1, 2, 3, 4]
print(_list[3])
# 4

_dict = {i: i**2 for i in range(10)}
print(_dict)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(_dict[3])  # выводит значение по ключу, а не по индексу
# 3

print(_dict[15])  # нет ключа в заданном словаре, то выведет ошибку
# KeyError: 15

# ↓↓↓ поэтому используем .get() ↓↓↓
print(_dict.get(3, 'No key'))  # dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None)
# 3
print(_dict.get(15, 'No key'))
# No key

a = _dict.get(15)  # нет ключа в заданном словаре, то выведет None
print(a)
# None

_dict[3] = 'asdadas'  # замена значений ключей
print(_dict)
# {0: 0, 1: 1, 2: 4, 3: 'asdadas', 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
_dict[6] = 'asdadas'
print(_dict)
# {0: 0, 1: 1, 2: 4, 3: 'asdadas', 4: 16, 5: 25, 6: 'asdadas', 7: 49, 8: 64, 9: 81}
_dict.update({1:5})  # dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
print(_dict)
# {0: 0, 1: 5, 2: 4, 3: 'asdadas', 4: 16, 5: 25, 6: 'asdadas', 7: 49, 8: 64, 9: 81}

_dict = {i: i**2 for i in range(10)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(len(_dict))  # выводит количество ключей в словаре
# 10

print(type(_dict))  # воводит тип функции
# <class 'dict'>

asd = {}  # создаем пустой словарь
print(type(asd))  # проверяем тип => словарь
# <class 'dict'>
print(all(asd))  #
# True
asd = dict.fromkeys([1, 2, 3, 4, 5, 6, ''], 0)
print(all(asd))  # выведет False, т.к. есть пустое значение ''
# False
asd = dict.fromkeys([1, 2, 3, 4, 5, 6,], 0)
print(all(asd))
# True

asd = {}
print(any({}))  # если словарь пустой, то вернет False
# False
print(any(asd))
# False
print(any({'', 123}))
# True

asd = dict.fromkeys([1, 2, 3, 4, 5, 6,], 0)  # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
print(sorted(asd))  # функция sorted вернет список с отсортированныйми ключами
# [1, 2, 3, 4, 5, 6]

asdf = dict.fromkeys([1, 6, 15, 123456, 123], 'value',)  # {1: 'value', 6: 'value', 15: 'value', 123456: 'value', 123: 'value'}
print(asdf)
print(1 in asdf)  # функция in выводит True, т.к. такой ключ есть в словаре
# True
print(2 in asdf)  # функция in выводит False, т.к. такого ключа нет в словаре
# False

# копирование словарей:
dict_1 = dict.fromkeys([1, 2, 3, 4, 5], 0)
dict_2 = dict_1
print(dict_1)
print(dict_2)
# {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
# {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
dict_2[3] = 8  # ключу 3 присвоим значение 8, причем изменятся значения в dict_1 и dict_2
print(dict_1)
print(dict_2)
# {1: 0, 2: 0, 3: 8, 4: 0, 5: 0}
# {1: 0, 2: 0, 3: 8, 4: 0, 5: 0}
print(id(dict_1))  # проверяем id двух словарей => они одинаковы, поэтому изменяются значения в dict_1 и dict_2
print(id(dict_2))
# 1339139245632
# 1339139245632

# при внесении изменений в словари с несколькими значениями надо быть внимательными и проверять вывод результата: ↓↓↓
dict_1 = dict.fromkeys([1, 2, 3, 4, 5], [1, 2, 3])  # {1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2, 3], 4: [1, 2, 3], 5: [1, 2, 3]}
dict_2 = dict_1.copy()  # создаем параметр dict_2 со значение копии dict_1
dict_2[4][2] = 9  # вносим изменение: ключу 4 по индексу 2 присваиваем значение 9
print(dict_1)
print(dict_2)
# {1: [1, 2, 9], 2: [1, 2, 9], 3: [1, 2, 9], 4: [1, 2, 9], 5: [1, 2, 9]}
# {1: [1, 2, 9], 2: [1, 2, 9], 3: [1, 2, 9], 4: [1, 2, 9], 5: [1, 2, 9]}
dict_2[4][1] = 7
print(dict_1)
print(dict_2)
# {1: [1, 7, 9], 2: [1, 7, 9], 3: [1, 7, 9], 4: [1, 7, 9], 5: [1, 7, 9]}
# {1: [1, 7, 9], 2: [1, 7, 9], 3: [1, 7, 9], 4: [1, 7, 9], 5: [1, 7, 9]}
dict_2[4][0] = 3
print(dict_1)
print(dict_2)
# {1: [3, 7, 9], 2: [3, 7, 9], 3: [3, 7, 9], 4: [3, 7, 9], 5: [3, 7, 9]}
# {1: [3, 7, 9], 2: [3, 7, 9], 3: [3, 7, 9], 4: [3, 7, 9], 5: [3, 7, 9]}
print(id(dict_1))  # проверяем id двух словарей => они разные
print(id(dict_2))
# 1282642385984
# 1282642029696

from copy import copy, deepcopy  # https://docs.python.org/3/library/copy.html
dict_1 = dict.fromkeys([1, 2, 3, 4, 5], 'VALUE')
dict_2 = copy(dict_1)
print(dict_1)  # print(dict_1, dict_2) => {1: 'VALUE', 2: 'VALUE', 3: 'VALUE', 4: 'VALUE', 5: 'VALUE'} {1: 'VALUE', 2: 'VALUE', 3: 'VALUE', 4: 'VALUE', 5: 'VALUE'}
print(dict_2)
# {1: 'VALUE', 2: 'VALUE', 3: 'VALUE', 4: 'VALUE', 5: 'VALUE'}
# {1: 'VALUE', 2: 'VALUE', 3: 'VALUE', 4: 'VALUE', 5: 'VALUE'}
dict_2[3] = 1  # ключу 3 присвоим значение 1
print(dict_2)
# {1: 'VALUE', 2: 'VALUE', 3: 1, 4: 'VALUE', 5: 'VALUE'}
print(dict_1)  # dict_1 не изменился ↓↓↓
# {1: 'VALUE', 2: 'VALUE', 3: 'VALUE', 4: 'VALUE', 5: 'VALUE'}

dict_1 = dict.fromkeys([1, 2, 3, 4, 5], ['val', 'val2', 'val3'])
dict_2 = copy(dict_1)  # с copy изменится dict_2 и dict_1
dict_2[3][2] = 'VALKIT'  # вносим изменение: ключу 3 по индексу 2 присваиваем значение 'VALKIT'
print(dict_1)
print(dict_2)
# {1: ['val', 'val2', 'VALKIT'], 2: ['val', 'val2', 'VALKIT'], 3: ['val', 'val2', 'VALKIT'], 4: ['val', 'val2', 'VALKIT'], 5: ['val', 'val2', 'VALKIT']}
# {1: ['val', 'val2', 'VALKIT'], 2: ['val', 'val2', 'VALKIT'], 3: ['val', 'val2', 'VALKIT'], 4: ['val', 'val2', 'VALKIT'], 5: ['val', 'val2', 'VALKIT']}
# при внесении изменений в словари с несколькими значениями надо быть внимательными и проверять вывод результата ↑↑↑

dict_1 = dict.fromkeys([1, 2, 3, 4, 5], ['val', 'val2', 'valkit'])  # {1: ['val', 'val2', 'valkit'], 2: ['val', 'val2', 'valkit'], 3: ['val', 'val2', 'valkit'], 4: ['val', 'val2', 'valkit'], 5: ['val', 'val2', 'valkit']}
dict_2 = deepcopy(dict_1)  # с deepcopy изменится dict_2 а dict_1 нет
dict_2[3][2] = 'VALKIT'
print(dict_1)
print(dict_2)
# {1: ['val', 'val2', 'valkit'], 2: ['val', 'val2', 'valkit'], 3: ['val', 'val2', 'valkit'], 4: ['val', 'val2', 'valkit'], 5: ['val', 'val2', 'valkit']}
# {1: ['val', 'val2', 'VALKIT'], 2: ['val', 'val2', 'VALKIT'], 3: ['val', 'val2', 'VALKIT'], 4: ['val', 'val2', 'VALKIT'], 5: ['val', 'val2', 'VALKIT']}


# Словари в циклах:

for key in dict_1:
    print(key)
# 1
# 2
# 3
# 4
# 5
dict_1 = dict.fromkeys([1, 2, 3, 4, 5], ['val', 'val2', 'valkit'])  # dict.keys() - возвращает ключи в словаре
print(dict_1.keys())
# dict_keys([1, 2, 3, 4, 5])
print(type(dict_1.keys()))
# <class 'dict_keys'>
print(list(dict_1.keys()))  # выводим ключи ввиде списка
# [1, 2, 3, 4, 5]

for vals in dict_1.values():  # dict.values() - возвращает значения в словаре
    print(vals)
# ['val', 'val2', 'valkit']
# ['val', 'val2', 'valkit']
# ['val', 'val2', 'valkit']
# ['val', 'val2', 'valkit']
# ['val', 'val2', 'valkit']
for vals in dict_1.values():  # dict.values() - возвращает значения в словаре
    if isinstance(vals, list):  # Функция isinstance() в Python, принадлежность экземпляра к классу => https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-isinstance/
        for val in vals:
            print(val)
# val
# val2
# valkit
# val
# val2
# valkit
# val
# val2
# valkit
# val
# val2
# valkit
# val
# val2
# valkit

for key, value in dict_1.items():  # dict.items() - возвращает пары (ключ, значение) => некий аналог enumerate()
    print(key, value)
# 1 ['val', 'val2', 'valkit']
# 2 ['val', 'val2', 'valkit']
# 3 ['val', 'val2', 'valkit']
# 4 ['val', 'val2', 'valkit']
# 5 ['val', 'val2', 'valkit']


dict_1 = dict.fromkeys([1, 2, 3, 4, 5], ['val', 'val2', 'valkit'])
del dict_1[3]  # удаление ключа 3
print(dict_1)
# {1: ['val', 'val2', 'valkit'], 2: ['val', 'val2', 'valkit'], 4: ['val', 'val2', 'valkit'], 5: ['val', 'val2', 'valkit']}
del dict_1[3]  # удаление ключа 3 еще раз вызовет ошибку
print(dict_1)
# KeyError

dict_1 = dict.fromkeys([1, 2, 3, 4, 5], ['val', 'val2', 'valkit'])
dict_1.clear()  # очищает словарь
print(dict_1)
# {}

dict_1 = dict.fromkeys([1, 2, 3, 4, 5], ['val', 'val2', 'valkit'])
dict_1.update({1: 2, 3: 4})  # dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
print(dict_1)
# {1: 2, 2: ['val', 'val2', 'valkit'], 3: 4, 4: ['val', 'val2', 'valkit'], 5: ['val', 'val2', 'valkit']}

dict_1 = dict.fromkeys([45, 4, 2, 76, -5, 0], [1, 2])
print(dict_1.keys())  # dict.keys() - возвращает ключи в словаре
# dict_keys([45, 4, 2, 76, -5, 0])


dict_1 = dict.fromkeys([45, 4, 2, 76, -5, 0], [1, 2])

print(dict_1.values())  # dict.values() - возвращает значения в словаре
# dict_values([[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]])

print(dict_1.items())  # dict.items() - возвращает пары (ключ, значение)
# dict_items([(45, [1, 2]), (4, [1, 2]), (2, [1, 2]), (76, [1, 2]), (-5, [1, 2]), (0, [1, 2])])
print(list(dict_1.items()))  # так нагляднее
# [(45, [1, 2]), (4, [1, 2]), (2, [1, 2]), (76, [1, 2]), (-5, [1, 2]), (0, [1, 2])] # список, который содержит кортеж. Каждый кортеж это пара ключ и пара значение

print(dict_1.setdefault(45, 'defaule_value'))  # dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None)
# [1, 2]
print(dict_1)
# {45: [1, 2], 4: [1, 2], 2: [1, 2], 76: [1, 2], -5: [1, 2], 0: [1, 2]}

print(dict_1.setdefault(15, 'defaule_value'))  # при отсутствии ключа 15, вернет значение defaule_value в словарь dict_1
# defaule_value
print(dict_1)
# {45: [1, 2], 4: [1, 2], 2: [1, 2], 76: [1, 2], -5: [1, 2], 0: [1, 2], 15: 'defaule_value'}

dict_1.pop(45)  # dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
# [1, 2]
print(dict_1)
# {4: [1, 2], 2: [1, 2], 76: [1, 2], -5: [1, 2], 0: [1, 2]}
dict_1.pop(45)  # если еще раз использовать этот метод по ключу 45, будет ошибка
print(dict_1)
# KeyError: 45
dict_1.pop(45, 'default_value')  # вернет словарь без KeyError: 45 и отсутвия ключа
# 'default_value'
print(dict_1)
# {4: [1, 2], 2: [1, 2], 76: [1, 2], -5: [1, 2], 0: [1, 2]}

dict_1 = dict.fromkeys([45, 4, 2, 76, -5, 0], [1, 2])
dict_1.popitem()  # dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены
print(dict_1)  #  вроде как удаляет пару начиная с конца
# {45: [1, 2], 4: [1, 2], 2: [1, 2], 76: [1, 2], -5: [1, 2]}


dict_1 = dict.fromkeys([1, 2, 3, 4], 'val')
print(dict_1)  # {1: 'val', 2: 'val', 3: 'val', 4: 'val'}
print(dict_1.get(3))  # dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None)
# val
print(dict_1.get(7))
# None
print(dict_1.get(7, 'default'))
# default


# ↓↓↓ методы словарей: ↓↓↓
# https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html

# Методы словарей
# dict.clear() - очищает словарь.
#
# dict.copy() - возвращает копию словаря.
#
# classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).
#
# dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение,
# а возвращает default (по умолчанию None).
#
# dict.items() - возвращает пары (ключ, значение).
#
# dict.keys() - возвращает ключи в словаре.
#
# dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет,
# возвращает default (по умолчанию бросает исключение).
#
# dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError.
# Помните, что словари неупорядочены.
#
# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение,
# а создает ключ со значением default (по умолчанию None).
#
# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other.
# Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
#
# dict.values() - возвращает значения в словаре.



# ↓↓↓ Задачи ↓↓↓
str_1 = 'pythonist'
dict_1 = {i: str_1.count(i) for i in str_1}
print(dict_1)
# {'p': 1, 'y': 1, 't': 2, 'h': 1, 'o': 1, 'n': 1, 'i': 1, 's': 1}
# каждая буква будет ключом, а их количество значением ключа

str_1 = 'aaaaabbbaaaaaaaaaaaaaaa'
dict_1 = {}
for elem in str_1:
    dict_1[elem] = str_1.count(elem)
print(dict_1)
# {'a': 20, 'b': 3}

