
print(hash(1))
# 1

print(hash(True))
# 1

print(hash(False))
# 0

print(hash('python'))
# -8162270832320149206

# print(hash([1, 2, 3, 4]))  # нельзя включить хэш от списка
# error

# {1:'asdasd', 2:'kek', 3:[1, 2, 3, 4,]} словари включаются в фигурные скобки

# {1:'asdad'} ключ справа, значение слева

# Создание словарей:

print(dict(b=4, c=3))
# {'b': 4, 'c': 3}
print(dict.fromkeys([1, 2, 3, 4, 5], 'asd'))
# {1: 'asd', 2: 'asd', 3: 'asd', 4: 'asd', 5: 'asd'}
print(dict.fromkeys([1, 2, 3, 4, 5], ))
# {1: None, 2: None, 3: None, 4: None, 5: None}

asd = {i: i**2 for i in range(10)}
print(asd)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
asd = {i: 'asd' for i in range(10)}
print(asd)
# {0: 'asd', 1: 'asd', 2: 'asd', 3: 'asd', 4: 'asd', 5: 'asd', 6: 'asd', 7: 'asd', 8: 'asd', 9: 'asd'}

# Базовые оперции со словарями
# похожи на оперции со  списками

_list = [1, 2, 3, 4]
print(_list[3])
# 4

_dict = {i: i**2 for i in range(10)}
print(_dict)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(_dict[3])  # выводит значение по ключу, а не по индексу
# 3

# print(_dict[15])
# KeyError: 15

# ↓↓↓ поэтому используем .get() ↓↓↓
print(_dict.get(3, 'No key'))
# 3
print(_dict.get(15, 'No key'))
# No key

a = _dict.get(15)
print(a)
# None

_dict[3] = 'asdadas'  # замена значений ключей
print(_dict)
# {0: 0, 1: 1, 2: 4, 3: 'asdadas', 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
_dict[6] = 'asdadas'
print(_dict)
# {0: 0, 1: 1, 2: 4, 3: 'asdadas', 4: 16, 5: 25, 6: 'asdadas', 7: 49, 8: 64, 9: 81}
_dict.update({1:5})
print(_dict)
# {0: 0, 1: 5, 2: 4, 3: 'asdadas', 4: 16, 5: 25, 6: 'asdadas', 7: 49, 8: 64, 9: 81}

print(len(_dict))
# 10

print(type(_dict))
# <class 'dict'>

print(all(_dict))
# False

asd = {}
print(any({}))
#False
print(any(asd))
#False
print(any({'', 123}))
#True

#  ????? разобраться потом ↓↓↓
#  ????? не успел
#  ?????
#  ?????
#  ?????
#  ?????

dict_1 = dict.fromkeys([1, 2, 3, 4, 5], 0)
dict_2 = dict_1
print(dict_1)
print(dict_2)
# {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
# {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
dict_2[3] = 8
print(dict_1)
print(dict_2)
# {1: 0, 2: 0, 3: 8, 4: 0, 5: 0}
# {1: 0, 2: 0, 3: 8, 4: 0, 5: 0}
print(id(dict_1))
print(id(dict_2))
# 1339139245632
# 1339139245632


##############    ????  ↓↓↓ разобраться потом
# dict_1 = dict.fromkeys({[1, 2, 3, 4, 5], [1, 2, 3]})
# print(dict_1)






##################   ????  ↓↓↓↓  разобраться потом

# dict_1 = dict.fromkeys({[1, 2, 3, 4, 5], 1})
# dict_2 = dict



##################   ????  ↓↓↓↓   разобраться потом
from copy import copy, deepcopy
#dict_1 = dict.fromkeys([1, 2, 3, 4, 5, 6], 'VALUE')
#dict_2 = copy(dict_1)
#print(dict_2, dict_1)
# {1: 'VALUE',


# Словари в циклах

for key in dict_1:
    print(key)
# 1
# 2
# 3
# 4
# 5
print(dict_1.keys())
# dict_keys([1, 2, 3, 4, 5])
print(type(dict_1.keys()))
# <class 'dict_keys'>
#####################  не успел ↓↓↓↓
#
#
#
#




for key, value in dict_1.items():
    print(key, value)
# 1 0   ????
# 2 0   ????
# 3 8   ????
# 4 0   ????
# 5 0   ????

# print(dict_1[3])
# ????????????


dict_1.clear()
print(dict_1)
# {}

# ???????????????????????
# ???????????????????????
# ???????????????????????
# ???????????????????????
# ???????????????????????
# ???????????????????????


# ↓↓↓ методы словарей: ↓↓↓
# https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html










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









