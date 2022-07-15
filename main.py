# Дан список. Проверить, все ли элементы в нем уникальные.
# Если найдены дубликаты, записать их в новый список. Результаты вывести на экран.
numbers = [20, 20, 30, 30, 40]

unique = []
for number in numbers:
    if number in unique:
        continue
    else:
        unique.append(number)
print(unique)
# [20, 30, 40]

# Для начала нужно создать пустой список, который будет включать уникальные числа.
# После этого можно задействовать цикл для итерации по каждому числу в переданном списке.
# Если число из него есть в уникальном, то можно переходить к следующему элементу.
# В противном случае — добавить это число.
# ↑↑↑ https://pythonru.com/primery/kak-poluchit-unikalnye-jelementy-spiska-python ↑↑↑
