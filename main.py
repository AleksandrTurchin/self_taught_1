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
