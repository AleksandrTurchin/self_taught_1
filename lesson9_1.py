print(list('asd'))
# ['a', 's', 'd']

print([i for i in range(5)])
#[0, 1, 2, 3, 4]

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
# поэтому надо использовать list
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


_list = [1,2,3,4,5]
print(_list.append('asd'))  # ??

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
print(_list.insert(1, 'asd'))  #  ??
#

_list.pop()  # ??

_list = [1, 2, 3, 4, 4, 5]
print(_list.remove(3))  # ??


_list = [1, 2, 3, 4, 4, 5]
print(_list.reverse())  # ??


_list = [1, 5, 3, 2, 4, 6]
print(_list.sort())  # ??
print(_list.sort(reverse=True))  # ??
# print(_list.sort(key=len))   # ??


_list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(len(_list_))
# 3

from copy import copy  #  ??

from copy import deepcopy  #  ??


