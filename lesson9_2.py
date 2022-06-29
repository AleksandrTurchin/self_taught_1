_List = [1, 2, 3, 7, 4, 5, 6, 7]

min_ind, max_ind = None, None

for ind, val in enumerate(_list):
    if val == 7:
        if min_ind is None: