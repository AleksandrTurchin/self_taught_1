str_1 = 'aaaaabbbaaaaaaaaaaaaaaa'
dict_1 = {}
for elem in str_1:
    dict_1[elem] = str_1.count(elem)
print(dict_1)
# {'a': 20, 'b': 3}
