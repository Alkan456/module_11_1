from PIL import Image
import sys
import matplotlib.pyplot as plt
import requests
from requests.exceptions import HTTPError
import pandas as pd
import numpy as np

# Работа с изображениями с помощью библиотеки Pillow
# Поворот изображения
triangle = Image.open("апельсин.jpg")
rotated = triangle.rotate(90)
rotated.save('апельсин_rotated.jpg')

# Изменение размера
square = Image.open("яблоко.jpg")
square = square.resize((square.width//7, square.height//7))
square.save("яблоко_new.jpg")

# Наложение изображения
img = Image.open("апельсин.jpg")
img2 = Image.open("яблоко.jpg")
img.paste(img2)
img.save("яблоко_в_апельсине.jpg")


# Библиотека Matplotlib для построения графиков
# график в Matplotlib
x = [2015, 2016, 2017, 2018]
y = [30, 50, 20, 70]
plt.plot(x, y, color='red', marker='o', linewidth=2, markersize=14)
plt.xlabel('Годы')
plt.ylabel('Цена в рублях')
plt.title('Цены на морковь')
plt.show()

# Столбчатая диаграмма
x = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
y = [25, 30, 35, 15, 50, 80, 120]
plt.bar(x, y, color='green', label='Количество товаров')
plt.xlabel('Дни недели')
plt.ylabel('Количество товара')
plt.title('Продажа товара по дням недели')
plt.legend()
plt.show()

# Круговая диаграмма
vals = [70, 27, 3]
labels = ["Android", "Iphone", "Прочие"]
colors = ['tab:green', 'tab:blue', 'tab:grey']
plt.pie(vals, labels=labels, colors=colors)
plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title("Количество пользователей операционных систем")
plt.show()


# Создание Pandas DataFrame путем ввода значений вручную
data = {'ФИО': ['Каталова Алиса Игоревна', 'Ненахов Даниил Дмитриевич', 'Худоба Григорий Анатольевич'],
        'Личное мнение': ['недорабатываю', 'отлично работаю', 'работаю на исходе сил'],
        'Средняя успеваемость': ['отлично', 'хорошо', 'удовлетворительно']}
df = pd.DataFrame(data, index=['1', '2', '3'])
print(df)


# Создание массива NumPy
arr = np.array([1, 3, 4, 7, 9])
print(arr)

# Многомерный массив можно представить как одномерный, максимальной длины,
# нарезанный на фрагменты по длине самой последней части.
A = np.arange(60)
B = A.reshape(2, 30)
C = A.reshape(6, 5, 2)
print('B\n', B)
print('\nC\n', C)

