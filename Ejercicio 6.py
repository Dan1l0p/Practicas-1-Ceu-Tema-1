def lista_parimpar(lista):
    lista_par = []
    lista_impar = []

    for i in lista:
        if i % 2 == 0:
            lista_par.append(i)
            lista_par.sort()

        else:
            lista_impar.append(i)
            lista_impar.sort()

    return lista_par, lista_impar


lista = [6, 5, 2, 1, 7]
listaseparada = lista_parimpar(lista)
print(lista_parimpar(lista))
