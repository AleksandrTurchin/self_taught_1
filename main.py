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