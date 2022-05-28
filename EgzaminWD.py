import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Zad1.
# etykiety = np.arange(0, 5)
#
# wartosciDuze = [101, 70, 75, 25, 50]
# wartosciMale = [20, 10, 30, 10, 0]
#
# linia = np.arange(0, 6)
# wartosc = np.full(6, 120)
#
# plt.title('Tytul')
# plt.bar(x=etykiety, height=wartosciDuze, color=['teal', 'darkgreen', 'greenyellow', 'pink', 'lawngreen'])
# plt.bar(x=etykiety, height=wartosciMale, color=['indigo', 'cyan', 'lime', 'blue', 'blue'])
# plt.plot(linia, wartosc, 'g')
# plt.axis([-0.60, 5.25, 0, 150])
# plt.savefig('1.pdf', format='pdf')
# plt.show()

#Zad2.
# xlsx = pd.ExcelFile('mieszkania1.xlsx')
# df = pd.read_excel(xlsx, header = 0)
#
# ind = df[df['Formy budownictwa'] == 'indywidualne']
# spo = df[df['Formy budownictwa'] == 'spółdzielcze']
# kom = df[df['Formy budownictwa'] == 'komunalne']
#
# lata = df.groupby('Rok').groups.keys()
#
# plt.axis([2014, 2019, 0, 90000])
# plt.bar(x = lata, height = ind['Wartość'], color = 'blue', label = 'indywidualne')
# plt.bar(x = lata, height = spo['Wartość'], color = 'gray', label = 'spółdzielcze')
# plt.bar(x = lata, height = kom['Wartość'], color = 'green', label = 'komunalne')
# plt.title('Wykres wartości mieszkań w latach w zależności od formy budownictwa')
# plt.ylabel('Wartość')
# plt.xlabel('Lata')
# plt.text(2014.1, 85000, '990624')
# plt.legend()
# plt.savefig('mieszkania.pdf', format='pdf')
# plt.show()

#Zad3.
# xlsx = pd.ExcelFile('turystyka1.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
# nowydf = df.transpose()
#
# nowydf = nowydf.reset_index()
#
#
# nowydf.columns = ['Kategoria', 'Rok', 'Ilość']
#
#
# print(nowydf.groupby('Kategoria').mean())
#
#
# # seria = nowydf.groupby('Kategoria')['Ilość'].sum()
# #
# # plt.pie(x = seria)
# # plt.show()
# # print(seria)
#
# # print(nowydf)











