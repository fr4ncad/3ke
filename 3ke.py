"""
Imre:
"""

lista = []
with open("input.txt" , "r", encoding="utf8") as f:
    for i in f:
        lista.append(int(i))

#elso feladat:
print(len(lista))

#masodik feladat:
lista.reverse()

for i in range(len(lista)):
    if lista[i] % 3 == 0:
        print(f'{i}-edik elem: {lista[i]}')
        break

#harmadik feladat:
for i in range(len(lista)):
    if lista[i] % 3 == 0 and lista[i] % 5 == 0:
        print(f'{i}-edik elem: {lista[i]}')
        break
    
#negyedik feladat:
igaze = True
for i in lista:
    if i < -10 or i > 10:
        igaze = False
        break

print(igaze)
#ötötdik feladat:

szorzat = 2
for i in lista:
    szorzat*i

print(szorzat)

##hatodik feladat:
db = 0
for i in lista:
    if i % 18 == 0:
        db += 1

print(db)

#hetedik feladat:
for i in lista:
    if i % 18 == 0 or i % 17 == 0:
        print(i ** (1. / 3))

#nyolcadik feladat:
min = lista[0]
masodikMin = lista[1]
for i in lista:
    if i < min:
        masodikMin = min
        min = i
    else:
        if i < masodikMin and i != min:
            masodikMin = i

print(masodikMin)

"""
vége
"""
