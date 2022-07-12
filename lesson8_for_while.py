iterable = 'Python'
for element in iterable:
    print(element)
# P
# y
# t
# h
# o
# n

print(range(5))  # range - диапазон (англ.)
# range(0, 5)

print(list(range(5)))  # вывод диапазона 0-5 списком
# [0, 1, 2, 3, 4]

print(list(range(0, 5, 2)))  # range(start, stop, step)
# [0, 2, 4]  # диапазон от 0 до 5 с шагом (step) 2.

print(list(range(0, 5)))  # По умолчанию шаг (step) равен 1.
# [0, 1, 2, 3, 4]

print(list(range(5, 0, -1)))  # в убывающей последовательности
# [5, 4, 3, 2, 1]

print(list(range(-10, 5, 1)))  # старт (start) и стоп(stop) могут иметь отрицательные значения
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
print(list(range(-10, -5, 1)))
# [-10, -9, -8, -7, -6]
print(list(range(10, -5, 1)))
# [] # erorr

nums = range(10)
print(nums)
# range(0, 10)
print(list(nums))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(3 in range(0, 10))
# True
print(11 in range(0, 10))
# False
print(range(0, 10)[5])  # вывод по индексу
# 5
# print(range(0, 10)[11])
# IndexError: range object index out of range

for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(3):
    for k in range(2):  # внутренний цикл всегда выполняется первым
        print('i=', i, 'k=', k)
# i= 0 k= 0
# i= 0 k= 1
# i= 1 k= 0
# i= 1 k= 1
# i= 2 k= 0
# i= 2 k= 1

for i in range(3):
    for k in range(2):  # лучше не пользоваться большим количеством вложений, т.к. нагружает память => искать др. методы
        for j in range(1):
            print('i=', i, 'k=', k, 'j=', j)
# i= 0 k= 0
# i= 0 k= 1
# i= 1 k= 0
# i= 1 k= 1
# i= 2 k= 0
# i= 2 k= 1
# i= 0 k= 0 j= 0
# i= 0 k= 1 j= 0
# i= 1 k= 0 j= 0
# i= 1 k= 1 j= 0
# i= 2 k= 0 j= 0
# i= 2 k= 1 j= 0

i = 2
while 2 > 0:
    i = i ** 2
    print(i)  # приведет к зацикливанию программы, пока вся оперативная память не будет забита



# ↓↓↓Пример кода с циклом While↓↓↓:

username = input('Input username: ')
password = input('Input password: ')

password_correct = False

while not password_correct:
    if len(password) < 8:  # проверяем на длинну строки
        print('Too short')  # если не удовлетворяет условию, меньше 8, то вы водим ошибку
        password = input('Input password: ')  # и просим ввести корректный пароль
    elif username in password:
        print('Password contains username')  # Password contains username - пароль содержит имя пользователя
        password = input('Input password: ')  # и просим ввести корректный пароль
    else:
        print('Password set success')
        password_correct = True


for i in range(10):  # команда будет выводить диапазон от 0 до 10
    if i == 5:  # но достигнув значения 5
        break  # команда break выведет нас из цикла и дальнейшие значения напечатаны не будут
    else:
        print(i)
# 0
# 1
# 2
# 3
# 4

# ↓↓↓ То же самое, только с использованием цикла while ↓↓↓:
i = 0
while i < 10:
    if i == 5:
        break
    else:
        print(i)
        i += 1
# 0
# 1
# 2
# 3
# 4


# ↓↓↓ Пример кода расмотренного выше, только с применением break ↓↓↓:
username = input('Input username: ')
password = input('Input password: ')

while True:
    if len(password) < 8:  # проверяем на длинну строки
        print('Too short')  # если не удовлетворяет условию, меньше 8, то вы водим ошибку
        password = input('Input password: ')  # и просим ввести корректный пароль
    elif username in password:
        print('Password contains username')  # Password contains username - пароль содержит имя пользователя
        password = input('Input password: ')  # и просим ввести корректный пароль
    else:
        print('Password set success')
        break

for num in range(10):
    if num == 5:  # перепрыгивает пятерку '5' и идет дальше
        continue
    else:
        print(num)
# 0
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9

i = 0
while i < 6:
    i += 1
    if i == 3:
        print('propusk')
        continue
        print('not reachable code')  # после continue эта строка никогда не будет работать, надо про это не забывать
    else:
        print(i)
# 1
# 2
# propusk
# 4
# 5
# 6


i = 0
while i < 6:
    i += 1
    if i == 3:
        pass  # используется часто как заглушка, пропускает мимо себя значение => здесь это 3
    else:
        print(i)
# 1
# 2
# 4
# 5
# 6

# ↓↓↓ интересное использование enumerate ↓↓↓
a = ['Vova', 'Igor', 'Ivan']
names = a
for name in names:
    print(name)
# Vova
# Igor
# Ivan

for index, name in enumerate(names):
    print(index, name)
# 0 Vova
# 1 Igor
# 2 Ivan

# ↓↓↓ Про блок else ↓↓↓


for i in range(5):
    print(i)
else:  # будет выводиться, если не ограничено условиями ранее
    print('Cycle is over')
# 0
# 1
# 2
# 3
# 4
# Cycle is over

for i in range(5):
    if i == 3:
        break  # c "break" "else" работать не будет так цикл прерван i=3
    print(i)
else:
    print('Cycle is over')
# 0
# 1
# 2

for i in range(5):
    if i == 3:
        continue   # c "continue" "else" будет работать
    print(i)
else:
    print('Cycle is over')
# 0
# 1
# 2
# 4
# Cycle is over

for i in range(5):
    if i == 3:
        pass   # c "pass" "else" будет работать
    print(i)
else:
    print('Cycle is over')
# 0
# 1
# 2
# 3
# 4
# Cycle is over



#  ↓↓↓ https://pythonworld.ru/osnovy/cikly-for-i-while-operatory-break-i-continue-volshebnoe-slovo-else.html  ↓↓↓

# Цикл while
# While - один из самых универсальных циклов в Python, поэтому довольно медленный.
# Выполняет тело цикла до тех пор, пока условие цикла истинно. ↓↓↓

i = 5
while i < 15:
    print(i)
    i = i + 2
# 5
# 7
# 9
# 11
# 13


# Цикл for
# Цикл for уже чуточку сложнее, чуть менее универсальный, но выполняется гораздо быстрее цикла while.
# Этот цикл проходится по любому итерируемому объекту (например строке или списку), и во время каждого
# прохода выполняет тело цикла. ↓↓↓

for i in 'hello world':
    print(i * 2, end='')  # аргумент end с кавычками на экран выводит строки без пробела и переноса на новую строку. Подробно: https://dev-gang.ru/article/python-funkcija-print-i-parametr-end-uxnl9natxr/
# hheelllloo  wwoorrlldd


# Оператор continue
# Оператор continue начинает следующий проход цикла, минуя оставшееся тело цикла (for или while).

for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end='')
# hheellll  wwrrlldd


# Оператор break
# Оператор break досрочно прерывает цикл.

for i in 'hello world':
    if i == 'o':
        break
    print(i * 2, end='')
# hheellll


# Волшебное слово else
# Слово else, примененное в цикле for или while, проверяет, был ли произведен выход из цикла инструкцией break,
# или же "естественным" образом. Блок инструкций внутри else выполнится только в том случае, если выход из цикла
# произошел без помощи break.

for i in 'hello world':
    if i == 'a':
        break
else:
    print('Буквы a в строке нет')
# Буквы a в строке нет
