import sys


while True:
    numero_a_descomponer = input("Dime un número de máximo 4 dígitos el cual descompondremos en unidades, decenas, centenas y miles. ")
    numero_a_descomponer = int(numero_a_descomponer)
    if numero_a_descomponer >9999:
        print("NO es posible. ")
        continue
    elif numero_a_descomponer <0:
        print("NO es posible.  ")
    else:
        break

print("{:04n}".format(numero_a_descomponer))

