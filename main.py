list_1 = [1, 2, 3]
list_2 = [10, 20, 30]
dictionary = dict(zip(list_1, list_2))
print(dictionary)

print()
dictionary = dict.fromkeys([])

for x in list_2:
    for i in list_1:
        dictionary = dict.fromkeys(list_1, x)
print(dictionary)
