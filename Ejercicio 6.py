def lista_parimpar(lista):


    for x in range(lista):
        if x % 2 == 0:
            lista_par.append(x)

        else:
            lista_impar.append(x)

    return lista_par, lista_impar

lista_par = []
lista_impar = []
lista = [6, 5, 2, 1, 7]

print(lista_parimpar(lista))