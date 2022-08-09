#string_input = input('Введите в случайной последовательности числа от 0 до 9: ')
#string_input = ('123456789012133288776655353535353441111')

#number_dict = {int(i): string_input.count(i) for i in string_input}
#sorted_num_dict = sorted(number_dict.items(), key=lambda e: e[1])
#print(dict(sorted_num_dict[-3:]))

dict1 = {1: 1, 2: 9, 3: 4, 4: 7, 5: 4}
sorted_values = sorted(dict1.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
       if dict1[k] == i:
            sorted_dict[k] = dict1[k]

print(dict(list(sorted_dict.items())[-3:]))
