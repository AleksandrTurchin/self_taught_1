# Метод join()
#
# Преобразование списка в строку
# Для этого также воспользуемся методом, а не циклом.
# Метод join() поможет нам в этом. Его синтаксис выглядит так:
# <sep>.join(<iterable>)
# Здесь <iterable> – любой итерируемый объект Python,
# содержащий подстроки. Это может быть, например, список или кортеж.
# <sep> – это разделитель, с помощью которого вы хотите объединить подстроки.

mylist = ['Я', 'научусь', 'программировать', 'на', 'Python']
mystr = ' '.join(mylist)
print(mystr)
