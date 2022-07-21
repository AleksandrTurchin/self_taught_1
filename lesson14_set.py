# подробно о множествах https://python-scripts.com/sets
# кратко об операциях с множествами https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html

# ===============================================================================================

# 4)* Дан список чисел. Реализовать сортировку пузырьком. Результаты вывести на экран.

_list = [6, 12, 4, 3, 8]

for i in range(len(_list) - 1):
    if _list[i] > _list[i + 1]:
        _list[i], _list[i + 1] = _list[i + 1], _list[i]
print(_list)
# ===============================================================================================

print(type({1, 2, 3, 4, 5, 6}))
# <class 'set'>
print(type({1: 2, 3: 4, 5: 6}))
# <class 'dict'>

# создание множества:
_set = {1, 2, 3, 4, 5}

_list = [1, 2, 3, 4, 5, 5, 5, 6]
_set1 = set(_list)
print(_set1)
# {1, 2, 3, 4, 5, 6}

k = {i ** 2 for i in range(5)}
print(k)
# {0, 1, 4, 9, 16}

m = {i ** 2 for i in _list}
print(m)
# {1, 4, 36, 9, 16, 25}

# множества нельзя брать по индексу и срезу

print(len(_set))
# 5
print(all(_set))
# True
print(any(_set))
# True
_set2 = sorted(_set)
print(_set2)
# [1, 2, 3, 4, 5]
print(sum(_set))
# 15
print(max(_set))
# 5
print(min(_set))
# 1

print(1 in _set)
# True
print('asd' in _set)
# False

# ************************************* ↓↓↓↓↓↓↓↓  ????????
from copy import copy, deepcopy
# set_1 = set([45, 4, 2, 76, -2,0])

#************************************* ↑↑↑↑↑↑↑↑


# по множествам можно итерироваться

for i in _set:
    print(i)
# 1
# 2
# 3
# 4
# 5
for i, v in enumerate(_set):
    print(i, v)
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5

# Методы множеств

_set_2 = {1, 2, 3, 4, 5}
a = _set_2.add(123)
print(a)
# None ?????
print(type(a))  # ????????????????
# <class 'NoneType'>

set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
set_3 = set_1.intersection(set_2)  # выводит пересекающиеся элементы
print(set_3)
# {3, 4}
print(set_1.intersection_update(set_2))  # ?????????
#

set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
print(set_1.isdisjoint(set_2))
# False
set_1 = {1, 2}
print(set_1.isdisjoint(set_2))
# True
set_3 = {1, 2, 3, 4}
print(set_1.issubset(set_3))
# True
set_2 = {3, 4, 5, 6}
print(set_2.issubset(set_3))
# False
print(set_3.issuperset(set_1))
# True
print(set_1.issuperset(set_3))
# False

a = set_1.pop()
print(a)
# 1
print(set_1)
# {2}
a = set_1.pop()  # ???????
# удалит все элементы

set_2.remove(3)  #??????????????????
# ???????????????????

set_2 = {4, 5, 6}
set_3 = {1, 2, 3, 4}
set_4 = set_3.symmetric_difference(set_2)
print(set_4)
# {1, 2, 3, 5, 6}

set_4 = set_3.symmetric_difference_update(set_2)
print(set_3)  # ???????????????????????????
# {1, 2, 3, 5, 6}

set_2 = {4, 5, 6}
set_3 = {1, 2, 3, 5, 6}

print(set_2.union(set_3))  # ???????????
# {1, 2, 3, 4, 5, 6}

set_2.update(set_3)  # ????????????
print(set_2)
# {1, 2, 3, 4, 5, 6}
#












# С множествами можно выполнять множество операций: находить объединение, пересечение... ↓↓↓↓↓↓↓↓
#
# len(s) - число элементов в множестве (размер множества).
# x in s - принадлежит ли x множеству s.
# set.isdisjoint(other) - истина, если set и other не имеют общих элементов.
# set == other - все элементы set принадлежат other, все элементы other принадлежат set.
# set.issubset(other) или set <= other - все элементы set принадлежат other.
# set.issuperset(other) или set >= other - аналогично.
# set.union(other, ...) или set | other | ... - объединение нескольких множеств.
# set.intersection(other, ...) или set & other & ... - пересечение.
# set.difference(other, ...) или set - other - ... - множество из всех элементов set, не принадлежащие ни одному из other.
# set.symmetric_difference(other); set ^ other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
# set.copy() - копия множества.
#
# И операции, непосредственно изменяющие множество: ↓↓↓↓↓↓↓↓
#
# set.update(other, ...); set |= other | ... - объединение.
# set.intersection_update(other, ...); set &= other & ... - пересечение.
# set.difference_update(other, ...); set -= other | ... - вычитание.
# set.symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
# set.add(elem) - добавляет элемент в множество.
# set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует.
# set.discard(elem) - удаляет элемент, если он находится в множестве.
# set.pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
# set.clear() - очистка множества.