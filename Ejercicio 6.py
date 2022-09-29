def lista_parimpar(lista):


    for i in range(lista):
        if i % 2 == 0:
            lista_par.append(i)

        else:
            lista_impar.append(i)

    return lista_par, lista_impar

lista_par = []
lista_impar = []
lista = [6, 5, 2, 1, 7]
lista.sort()
print(lista_parimpar(lista))