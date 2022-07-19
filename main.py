print()

list_1 = [1, 2, 3]
list_2 = [10, 20, 30]

dictionary = {}
for i in range(len(list_1)):
    dictionary[list_1[i]] = list_2[i]
print(dictionary)

print()

list_1 = [1, 2, 3]
list_2 = [10, 20, 30]

x = 0
dictionary = {}
for i in list_1:
  dictionary[i] = dictionary.get(i, 0) + list_2[x]
  x += 1
print(dictionary)

print()

list_1 = [1, 2, 3]
list_2 = [10, 20, 30]

x = 0
dictionary = {}
for i in list_1:
  dictionary[i] = list_2[x]
  x += 1
print(dictionary)



# получить из строки словарь, где ключом будет слово, а значением - длина словаря
str = 'qwer asdf zxcv'
list_ = str.split()

a = {i: len(i) for i in list_}
print(a)

# находим минимальное значение ключа и значения
min_key = None
min_value = None

for key, value in a.items():
    if min_value is not None:
        if value < min_value:
            min_value = value
            min_key = key
    else:
        min_value = value
        min_key = key
print(min_key, min_value)


item_list = [
    {'item': 'chair', 'amount': 400}
    {'item': 'sofa', 'amount': 300}
    {'item': 'table', 'amount': 500}
]

_sum = 0
for item in item_list:
    _sum += item.get('amount', 0)
print(_sum)  # получить сумму всех значений 'amount'

max_val = 0
for item in item_list:
    count = item.get('count', 0)
    if max_val < count:
        max_val = count
print(max_val)   # получить максимальное значение 'count'


item_list = {
    'Alex': ['subj1', 'subj2',  'subj3'],
    'David': ['subj1', 'subj2'],
    'Marina': ['subj1', 'subj2',  'subj3']
}

_lst = []
for value in item_list.values():
    _lst += value
print(len(_lst))  # найти количество значений в словаре - #8