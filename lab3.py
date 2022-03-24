from random import seed
from random import randint

from ciagi import *

#Zad1
A = [1-x for x in range(1, 11)]
B = [4**y for y in range(8)]
C = [x for x in B if x % 2 == 0]
print(A)
print(B)
print(C)

#Zad2
lista1 = [randint(0, 1000) for x in range(0, 10)]
lista2 = [x for x in lista1 if x % 2 == 0]
print(lista1)
print(lista2)

#Zad3
zakupy = {
    'banany' : 'kg',
    'maslo' : 'kg',
    'czajnik' : 'sztuki',
    'woda' : 'l',
    'lodowka' : 'sztuki',
    'worek' : 'sztuki',
    'kurczak' : 'sztuki'
}
sztuki = {k:v for (k, v) in zakupy.items() if v == 'sztuki'}
print(zakupy)
print(sztuki)

#Zad4
def czy_prostokatny(a, b, c):
    najdluzszy_bok = max(a, b, c)
    if najdluzszy_bok == a:
        wartosc = b**2 + c**2
    elif najdluzszy_bok == b:
        wartosc = a**2 + c**2
    elif najdluzszy_bok == c:
        wartosc = a**2 + b**2

    najdluzszy_bok_kwadrat = najdluzszy_bok**2

    if wartosc == najdluzszy_bok_kwadrat:
        print('Trójkąt jest prostokątny')
    else:
        print('Trójkąt nie jest prostokątny')

czy_prostokatny(9, 12, 15)

#Zad5
def pole_trapezu(a = 10, b = 20, h = 30):
    return ((a+b)*h)/2

print(pole_trapezu())

#Zad6
def iloczyn_ciagu(a = 1, b = 4, ile = 10):
    list = [x*b for x in range(a, ile+1)]
    iloczyn = 1
    for x in list:
        iloczyn *= x
    return iloczyn

print(iloczyn_ciagu())

#Zad7
def iloczyn_ciagu2(*argumenty):
    if len(argumenty) == 0:
        list = [x * 4 for x in range(1, 11)]
        iloczyn = 1
        for x in list:
            iloczyn *= x
        return iloczyn
    elif len(argumenty) == 1:
        list = [x * 4 for x in range(argumenty[0], 11)]
        iloczyn = 1
        for x in list:
            iloczyn *= x
        return iloczyn
    elif len(argumenty) == 2:
        list = [x * argumenty[1] for x in range(argumenty[0], 11)]
        iloczyn = 1
        for x in list:
            iloczyn *= x
        return iloczyn
    elif len(argumenty) == 3:
        list = [x * argumenty[1] for x in range(argumenty[0], argumenty[2])]
        iloczyn = 1
        for x in list:
            iloczyn *= x
        return iloczyn

print(iloczyn_ciagu2())

#Zad8
def produkty(**lista_produktow):
    ilosc_produktow = len(lista_produktow.keys())
    print('Ilosc produktów: '+str(ilosc_produktow))
    wartosc_produktow = 0
    for x in lista_produktow.keys():
        wartosc_produktow += lista_produktow[x]

    return wartosc_produktow

print(produkty(maslo = 6, chleb = 2, woda = 1))

#Zad9
print(ciagi_arytm.a_nty_wyraz(0, 5, 10))
print(ciagi_geo.g_nty_wyraz(1, 5, 10))

#Za10
plik = open('Zad10.txt', 'w+')
podz4 = [x for x in range(101) if x % 4 == 0]
print (podz4)
plik.write(str(podz4))
plik.close()

#Zad11
plik = open('Zad10.txt', 'r')
print('Odczytany plik:')
print(plik.read())
plik.close()












