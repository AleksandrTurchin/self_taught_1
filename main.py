#  Дан список. Необходимо найти сумму и произведение элементов списка. Результаты вывести на экран.
_list = [1, 2, 3, 4, 5]
print(sum(_list))

x = 1
for i in _list:
    x *= i
# print(x)

print([i * [i] for i in _list])

_list1 = ['cat', 'dog']
_list2 = ['wolf', 'chep']
_list1.append(_list2)
print(_list1)

print()
list_f = [30, 0.9, [8, 56, 22, ["a", "hello"]], [200, 3, [5, [89], 10]]]

def get_elements_of_nested_list(element):
    count = 0
    if isinstance(element, list):  # isinstance() проверяет, является ли element списком(list).
        # Первый элемент является целым числом 30, поэтому функция переходит к блоку else и
        # увеличивает счетчик на 1. Когда мы добираемся до [8, 56, 22, ["a", "hello"]],
        # функция распознает список и рекурсивно просматривает его, чтобы проверить наличие других списков.
        for each_element in element:  # выполняем цикл внутри списка и рекурсивно вызываем функцию до тех пор, пока не останутся вложенные списки. Все элементы, кроме списков (целые числа, строки и т.д.), увеличивают счетчик на 1
            count += get_elements_of_nested_list(each_element)
    else:
        count += 1
    return count

print("Total number of elements in the nested list: ", get_elements_of_nested_list(list_f))

print()
print()

count = 0
element = None

if isinstance(element, list):
    for each_element in element:  # each_element - "каждый_элемент"
        count += 1
    else:
        count += 1
print(count)
