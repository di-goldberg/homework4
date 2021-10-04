try:
 r = int(input('Введите значение радиуса круга'))
except ValueError:
 print('Ошибка')
else:
    S = 3.14*r**2
print ('Площадь круга равна', S)