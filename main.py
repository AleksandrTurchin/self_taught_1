for i in range(5):
    print(i)
else:  # будет выводиться, если не ограничено условиями ранее
    print('Cycle is over')
# 0
# 1
# 2
# 3
# 4
# Cycle is over

for i in range(5):
    if i == 3:
        break  # c "break" "else" работать не будет так цикл прерван i=3
    print(i)
else:
    print('Cycle is over')
# 0
# 1
# 2

for i in range(5):
    if i == 3:
        continue   # c "continue" "else" будет работать
    print(i)
else:
    print('Cycle is over')
# 0
# 1
# 2
# 4
# Cycle is over

for i in range(5):
    if i == 3:
        pass   # c "pass" "else" будет работать
    print(i)
else:
    print('Cycle is over')
# 0
# 1
# 2
# 3
# 4
# Cycle is over
