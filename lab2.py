import sys
import math

#Zad1.
print('Zad1.')
sporty = ['koszykówka', 'golf', 'szachy']
sporty.reverse()
sporty.append('siatkówka')
sporty.append('bieganie')
print(sporty)

#Zad2.
print('Zad2.')
slownik = {
    'itd.' : 'i tak dalej',
    'itp.' : 'i tym podobne',
    'np.'  : 'na przykład',
    'wg.'  : 'według'
}
print(slownik)

#Zad3.
print('Zad3.')
gry = {
    'najlepszy' : 'Wiedźmin 3',
    'lepszy' : 'Minecraft',
    'dobry' : 'Saper'
}
print('Ilość elementów w słowniku: ')
print(len(gry))

#Zad4.
zdanie = input('Wpisz zdanie: ')
print('W tym zdaniu wystąpiło: '+str(zdanie.count('a'))+' liter "a"')

#Zad5.
print('Zad5.')
liczba1 = int(sys.stdin.readline())
liczba2 = int(sys.stdin.readline())
liczba3 = int(sys.stdin.readline())

wynik = liczba1**liczba2 + liczba3
sys.stdout.write(str(wynik))

#Zad6.
print('')
print('Zad6.')

a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))

if a > b:
    if a > c:
        print('Liczba a jest największa')
if b > a:
    if b > c:
        print('Liczba b jest największa')
if c > a:
    if c > b:
        print('Liczba c jest największa')

#Zad7.
print('Zad7.')

liczby = [3, 6.4, 23, 12, 4.421, 5.3]

for i in liczby:
    print(math.pow(i, 2))

#Zad8.
print('Zad8.')

iloscLiczb = 0
pobraneLiczby = []
parzysteLiczby = []
while iloscLiczb < 10:
    l = int(input('Podaj '+str(iloscLiczb)+'. liczbę: '))
    pobraneLiczby.append(l)
    iloscLiczb += 1

for i in pobraneLiczby:
    if pobraneLiczby[i]%2 == 0:
        parzysteLiczby.append(pobraneLiczby[i])

print(parzysteLiczby)

#Zad9.
print('Zad9.')

zmienna = float(input('Podaj liczbę: '))

try:
    print(math.sqrt(zmienna))
except ValueError:
    print('Podano złą wartość!')









