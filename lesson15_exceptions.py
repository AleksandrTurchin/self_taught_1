# Инфа по теме:
# https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
# https://pythonru.com/osnovy/znachenija-iskljuchenij-i-oshibok-v-python
# https://pythonchik.ru/osnovy/python-try-except
# https://devpractice.ru/python-lesson-11-work-with-exceptions/
# https://younglinux.info/python/exceptions

# Типы исключений:
# IOError — ошибка ввода/вывода;
# IndexError — не найден элемент с указанным индексом;
# KeyError — в словаре не найден ключ;
# NameError — не найдено имя;
# SyntaxError — синтаксическая ошибка в коде;
# TypeError — операция / функция применяется к неподходящему объекту;
# ValueError — аргумент функции / операции имеет неподходящее значение;
# ZeroDivisionError — в операции деления / нахождения остатка второй аргумент ноль.

# https://pythonist.ru/assert-v-python/  #

# 100 / 0

# ↓↓↓↓ результат операции ↓↓↓↓

# Traceback (most recent call last):
#   File "C:\Users\37529\PycharmProjects\self_taught_1\lesson15_exceptions.py", line 1, in <module>
#     100 / 0
# ZeroDivisionError: division by zero



# 2 + '1'

# ↓↓↓↓ результат операции ↓↓↓↓

# Traceback (most recent call last):
#   File "C:\Users\37529\PycharmProjects\self_taught_1\lesson15_exceptions.py", line 11, in <module>
#     2 + '1'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# int('qwerty')

# ↓↓↓↓ результат операции ↓↓↓↓

# Traceback (most recent call last):
#   File "C:\Users\37529\PycharmProjects\self_taught_1\lesson15_exceptions.py", line 18, in <module>
#     int('qwerty')
# ValueError: invalid literal for int() with base 10: 'qwerty'


a = 100
b = 0

try:
    c = a / b

except ZeroDivisionError as ex_obj:
    print('YOU HAVE AN ERROR')
          # YOU HAVE AN ERROR
    print(ex_obj)
    # division by zero

print('some code following')
# some code following





