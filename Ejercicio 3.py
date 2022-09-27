##Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:##



lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a'] 

lista_3 = []

for values in lista_1:
    if values in lista_2:
        lista_3.append(values)
lista_3.pop(7)
print(lista_3)