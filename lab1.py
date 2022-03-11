import math
from numpy import log as ln

#Zad1.
print("Zad1.")
a = 'Zmienna'
b = 'String'

c = 10
d = 20

e = 4.5
f = 6.7

g = 2+5j
h = 1+9j

print(a, b, c, d, e, f, g, h)

#Zad2.
print("Zad2.")
pierwsza = input("Podaj pierwsza liczbe: ")
druga = input("Podaj druga liczbe: ")

pierwsza = int(pierwsza)
druga = int(druga)

wynik = pierwsza + druga
print("Wynik dodawania to: "+str(wynik))
wynik = pierwsza - druga
print("Wynik odejmowania to: "+str(wynik))
wynik = pierwsza * druga
print("Wynik mnozenia to: "+str(wynik))
wynik = pierwsza / druga
print("Wynik dzielenia to: "+str(wynik))

#Zad3.
print ("Zad3.")
prz1 = 1
prz1 += 1

prz2 = 2
prz2 -= 1

prz3 = 3
prz3 *= 2

prz4 = 4
prz4 /= 2

prz5 = 5
prz5 **= 2

prz6 = 10
prz6 %= 3

print(prz1, prz2, prz3, prz4, prz5, prz6)


#Zad4.
print("Zad4.")
print(math.exp(10))
print((ln(5+(math.sin(8))**2))**(1/6))
print(math.floor(3.55))
print(math.ceil(4.8))

#Zad5.
print("Zad5.")
imie = "SEBASTIAN"
nazwisko = "GÓRSKI"

print(imie.capitalize())
print(nazwisko.capitalize())

#Zad6.
print("Zad6.")
tekst = "To jest moja piosenka -ka -ka -ka"
print(tekst.count("ka"))

#Zad7.
print("Zad7.")
tab = "Znaki w tablicy"

print(tab[1])
print(tab[len(tab)-1])

#Zad8.
print("Zad8.")
lista = tekst.split()

for x in lista:
    print(x)

#Zad9.
typString = "Typ string"
typFloat = 10.0
typHex = 0x8d

print('Zmienne to: {0:s}, {1:f}, {2:X}'.format(typString, typFloat, typHex))


