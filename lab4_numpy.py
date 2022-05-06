import numpy as np

# #Zad1
print('Zadanie 1.')
a = np.arange(3, 48, 3)
print(a)

# #Zad2
print('Zadanie 2.')
lista1 = [0.23, 2.21, 3.321, 3.0, 87.4]
lista2 = np.int64(lista1)
lista2 = a.astype('int64')
print(lista1)
print(lista2)

# #Zad3
print('Zadanie 3.')
def funkcja(n):
    tab = np.arange(1, n*n+1, 1).reshape(n, n)
    return tab

print(funkcja(4))

#Zad4
print('Zadanie 4.')
def potegi(liczba, iloscpoteg):
    a = np.logspace(1, iloscpoteg, num = iloscpoteg, base = 2.0)
    return a

print(potegi(2, 6))

#Zad5
print('Zadanie 5.')
def generujWektor(dlugosc):
    a = np.array([x for x in range(dlugosc)])
    print(a)
    b = np.flip(a)
    print(b)
    c = np.diag(b)
    print(c)

generujWektor(10)

# #Zad6
# print('Zadanie 6.')
# lista1 = []
# lista2 = []
# lista3 = []
#
# wyraz1 = 'jedzie'
# wyraz2 = 'grzes'
# wyraz3 = 'rowerem'
#
# for i in wyraz1:
#     lista1.append(i)
#
# for i in wyraz2:
#     lista2.append(i)
#
# for i in wyraz3:
#     lista3.append(i)
#
# m1 = np.array(lista1)
# m2 = np.array(lista2)
# m3 = np.array(lista3)
#
# a = np.chararray((10, 10))
# a[:] = ' '
# np.diag(a, )
#
#
#
# print(a)


#Zad7
print('Zadanie 7.')
def wielokrotnoscDwa(n):
    a = np.zeros((n, n))
    np.fill_diagonal(a, 2)
    for i in range(1, n):
        np.fill_diagonal(a[i:], 2*(i+1))
        np.fill_diagonal(a[:, i:], 2*(i+1))
    print(a)

wielokrotnoscDwa(10)

#Zad8 (1 - kierunek pionowy, 0 - kierunek poziomy)
print('Zadanie 8.')
def dzielTablice(tab, kierunek):
    if (kierunek == 0 and np.shape(tab)[0] % 2 == 0) or (kierunek == 1 and np.shape(tab)[1] % 2 == 0):
        print(np.array_split(tab, 2, kierunek))
    else:
        print('Nie mozna podzielic tablicy na 2 rowne czesci!')

a = np.arange(25).reshape(5, 5)
print(a)
dzielTablice(a, 0)

#Zad9
print('Zadanie 9.')
def fib(n):
    if n in {0, 1}:
        return n
    return fib(n-1)+fib(n-2)

ciag = [fib(i) for i in range(25)]
print(ciag)
macierz = np.array(ciag).reshape((5, 5))
print(macierz)







