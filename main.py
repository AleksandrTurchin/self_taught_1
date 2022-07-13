h = int(input('h = '))
m = int(input('m = '))
s = int(input('s = '))

result = (h * 3600000) + (m * 60000) + (s * 1000)

if 0 <= s <= 59:
    elif 0 <= m <= 59:lif 0 <= h <= 23:
    print('значение часов должно быть от 0 до 23')
else:
    print('миллисекунд: ', result)

