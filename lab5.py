import numpy as np
import pandas as pd

# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
#
# c = a+b
# print(c)
#
# d = np.sqrt(b)
# print(d)
#
# e = d + c
# print(e)
#
# a = np.arange(12).reshape((3, 4))
# print(a)
# print(a.sum(axis = 0)) # kolumny
# print(a.sum(axis = 1)) # wiersze
# print(a.cumsum(axis = 1))


# a = np.arange(3)
# b = np.arange(3)
#
# print(np.dot(a, b))
# print(a.dot(b))
#
# c = np.arange(3)
# d = np.array([[0], [1], [2]])
# print(c.dot(d))
# e = np.array([[2, 4, 5], [5, 1, 7]])
# f = np.array([[2, 3], [4, 2], [6, 1]])
# print(np.dot(e, f))
#

# a = np.arange(6).reshape((3, 2))
# print(a)
# print(a.flat)
# for b in a.flat:
#     print(b)

# a = np.arange(12).reshape((3, 4))
# print(a)
#
# b = a.reshape((4, 3))
# print(b)
#
# c = b.ravel()
# print(c)
# print(b.T)
#
# # s = pd.Series([1, 3, 5, 'a', 5.5])
# # print(s)
# #
# s = pd.Series([10, 12, 14, 8], index=['a', 'b', 'c', 'd'])
# print(s)
#
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [11121321, 1232132132, 280123122]}
#
# df = pd.DataFrame(data)
# # print(df)
# #
# # daty = pd.date_range('20220507', periods=5)
# # print(daty)
# #
# # df2 = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# # print(df2)
# #
# # df3 = pd.read_csv('dane.csv', header = 0, sep = ';', decimal='.')
# # print(df3)
# #
# # xlsx = pd.ExcelFile('imiona.xlsx')
# # df = pd.read_excel(xlsx, header=0)
# #
# # print(df)
# # print(df.head(10))
# # print(df.tail(10))
# #
# # df3.to_csv('dane2.csv', index=False)
# # df.to_excel('imona2.xlsx', sheet_name='dane')
#
# print(s['a'])
# print(s.a)
# print(df[0:1])
# print(df.Kraj)
# print(df.iloc[[0], [0]])
# print(df.loc[[0], ['Kraj']])
# print(df.a[0, 'Kraj'])
#


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
from PIL import Image


# plt.plot([1, 2, 3, 4],[1, 4, 9, 16],'ro:',  label ='linia')
# plt.ylabel('wartosci z wektora')
# plt.show()
#
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r:')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')
#
# plt.axis([0, 6, 0, 20])
# plt.show()

# t = np.arange(0, 5, 0.1)
# plt.plot(t, t, 'r-', t, t**2, 'b:', t, t**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'sześcienna'], loc='center left')
# plt.show()
#

# x = np.linspace(0, 2, 100)
#
# plt.plot(x, x, label='liniowa')
# plt.plot(x, x**2, label='kwadratowa')
# plt.plot(x, x**3, label='szecienna')
#
# plt.xlabel('etykieta osi x')
# plt.ylabel('etykieta osi y')
# plt.title('Wykres trzech linii')
#
# plt.savefig('plot.jpg')
# plt.show()
#
# im1 = Image.open('plot.png')
# im1 = im1.convert('RGB')
# im1.save('plot.jpg')


# t = np.arange(0, 11, 0.1)
# print(t)
#
# plt.plot(t, np.sin(t), 'r', label='etykieta')
# plt.xlabel('wartosci x')
# plt.ylabel('wartosci y')
# plt.title('Tytul wykresu')
# plt.show()
#
#
#
#
# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
#
# y1 = np.sin(2*np.pi * x1)
# y2 = np.cos(2*np.pi * x2)

# plt.subplot(2, 1, 1)
# plt.plot(x1, y1)
#
# plt.ylabel('sin(x)')
# plt.title('wykres sin(x)')
#
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r-')
# plt.ylabel('cos(x)')
#
# plt.xlabel('x')
#
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# fig, axs = pl.subplots(3, 2)
# print(type(fig))
# print(type(axs))
#
#
# axs[0, 0].plot(x1, y1, 'g-')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
# axs[0, 0].set_title('wykres sin(x)')
#
# axs[1, 1].plot(x2, y2, 'r-')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
# axs[1, 1].set_title('Wykres cos(x)')
#
# axs[2, 0].plot(x2, y2, 'r-')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('cos(x)')
# axs[2, 0].set_title('Wykres cos(x)')
#
#
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
#
# plt.show()

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 51, 50),
#         'd': np.random.randn(50)}
#
# data['b'] = data['a'] + 10 * np.random.randn(50)
#
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter(data=data, x ='a', y='b', c='c', cmap ='plasma', s='d')
# plt.xlabel('wartości z klucza a')
# plt.ylabel('Wartości z klucza b')
#
# plt.show()


# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Populacja': [11190846, 1232132132, 207123122, 38674000],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}
#
# df = pd.DataFrame(data)
#
# grupa = df.groupby('Kontynent')
# etykiety = list(grupa.groups.keys())
# wartosci = list(grupa.agg('Populacja').sum())
#
# plt.bar(x = etykiety, height = wartosci, color = ['red', 'green', 'blue'])
#
# plt.show()
# print(etykiety)
# print(wartosci)


x = np.random.randn(10000)

plt.hist(x, bins=50, facecolor = 'g', alpha=0.75, density = True)

plt.xlabel('Wartosci')

plt.ylabel('Prawdopodobieństwa')
plt.title('Historgram')

plt.show()







