# https://pythonchik.ru/osnovy/funkcii-v-python
# https://highload.today/funktsii-python/#2
# https://pythonru.com/osnovy/funkcii-v-python
# https://pythonworld.ru/tipy-dannyx-v-python/vse-o-funkciyax-i-ix-argumentax.html

def function_name():
    print('Hello World')
    # или
    # return None
function_name()
# Hello World

def function_2(positional_arg_1, positional_arg_2):
    print('arg 1:', positional_arg_1)
    print('arg 2:', positional_arg_2)
function_2(1, 'asd')
# arg 1: 1
# arg 2: asd

def function_2(positional_arg_1, positional_arg_2=2):
    print('arg 1:', positional_arg_1)
    print('arg 2:', positional_arg_2)
function_2(1,)

# def print(arc, arc2, arc3)
    # ????????????????????????????

def example_function_packed(*args, **kwargs):
    pass
# подробно https://py3dev.ru/types/function/#_2

def example(*args, **kwargs):
    print(type(args))
    print(type(kwargs))

