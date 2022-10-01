

elementos = [1 , 5, -2]

def agregar_una_vez(lista, elemento):
    try:
        if elemento in lista:
            raise ValueError
        else:
            lista.append(elemento)
    except ValueError:
        print("Error: Imposible añadir elementos duplicados =>", elemento )
    

agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")
print(elementos)
    