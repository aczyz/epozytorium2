
def dlugosc(lista):
    if lista == []:
        return 0
    else:
        return 1 + dlugosc(lista[1:])
    
lista = [1,3,4,2,5,11,8,33,1,2]
wynik = dlugosc(lista)
print(wynik)
