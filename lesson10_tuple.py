# Кортежи
# https://pythonru.com/osnovy/kortezhi-python
# https://pythonchik.ru/osnovy/kortezhi-v-python
# https://www.bestprog.net/ru/2020/04/15/python-operations-on-tuples-bypass-of-tuple-methods-of-working-with-tuples-ru/

print(type((1, 2, 3, 4)))
# <class 'tuple'>

print(tuple('aasd'))
# ('a', 'a', 's', 'd')

_tuple = ('a', 1, 'b')
print(_tuple)
# ('a', 1, 'b')

print(_tuple[2])
# b

print(_tuple[-1])
# b

# _tuple[1] = 2  # Typeerror
# принимает не изменяемые значения

_tuple1 = (1, 2, 3)
_tuple2 = (4, 5, 6)
_tuple3 = _tuple1 + _tuple2
print(_tuple3)
# (1, 2, 3, 4, 5, 6)

_tuple3 *= 2
print(_tuple3)
# (1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)

print(_tuple3[:6])
#  (1, 2, 3, 4, 5, 6)


print(min(_tuple3))
# 1
print(max(_tuple3))
# 6
print(sum(_tuple3))
# 42
print(len(_tuple3))
# 12
print(sorted(_tuple3))
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]


_tuple10 = ('1', '2', 'asd', 'asd')
print(tuple(filter(str.isdigit, _tuple10)))
# '1', '2'

print()
_tiple5 = (1, 2, 3, 4, [5, 6])
_tiple5[4].append(7)
print(_tiple5)
# (1, 2, 3, 4, [5, 6, 7])

