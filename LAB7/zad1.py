import random

def quicksort(l, r, list):
    if l >= r:
        return

    v = list[r]
    p = l

    for j in range(l, r):
        if list[j] < v:
            list[p], list[j] = list[j], list[p]
            p += 1

    list[p], list[r] = list[r], list[p]

    quicksort(l, p - 1, list)
    quicksort(p + 1, r, list)
    return list

def binarysearch(lista,l,r,szukana):
    l=0
    r=n-1
    srodek=(l+r)//2
    while l<=r:
        srodek=(l+r)//2
        if lista[srodek] == szukana:
            return srodek
        elif lista[srodek] > szukana:
            r=srodek-1
        else:
            l=srodek+1
    return -1


while True:
    n = int(input('podaj ilość elemetów: '))
    if n>0:
        print('git')
        break
    else:
        print('proszę podać n>0')
while True:
    x = int(input('podaj x: '))
    y = int(input('podaj y: '))
    if x<=y:
        break
    else:
        print('Proszę podać ponownie ')

lista=[random.randint(x,y) for i in range(n)]
print(f'wygenerowana lista: {lista}')

#sortowanie szybkie

quicksort(0,n-1,lista)
print(f'posortowana lista: {lista}')
#trzeba dać duży przedział, żeby pozbyć się duplikatów

z=int(input('Jakiej liczby szukasz? '))
print(f'szukana liczba znajduję się na indeksie: {binarysearch(lista,0,n,z)}')
