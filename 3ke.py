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

#ötötdik feladat:

szorzat = 2
for i in lista:
    szorzat*i

print(szorzat)

##hatodik feladat:
