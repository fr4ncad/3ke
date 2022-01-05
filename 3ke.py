import math

lista=list()
with open("input.txt", "r", encoding="UTF-8") as f:
    for i in f:
        lista.append(int(i.strip()))



def ninth():
    van=False
    for i in lista:
        if i>0 and math.sqrt(i)%1==0:
            van=True
    print("Van a sorozatban négyzetszám" if van else "Nincs")

def tenth():
    van=False
    for index,value in enumerate(lista[1:-2]):
        if value<0 and lista[index-1]+lista[index+1]==0:
            van=True
            break
    print("Van a sorozatban olyan negatív szám, amelynek az összes szomszédja nulla" if van else "Nincs")

