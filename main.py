string = input()
symbol = input()

min_index, max_index = None, None

for i, v in enumerate(string):
     if v == symbol:
         if min_index is None:
                min_index = i
         max_index = i
print(min_index)
print(max_index)


_list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(len(_list_))

