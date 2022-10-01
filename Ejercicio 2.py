numero_magico = 12345679

while True:
    numero_usuario = input("Dime un número del 1 al 9. ")
    numero_usuario = int(numero_usuario)
    if numero_usuario <1:
        print("Un número del 1 al 9...")
        continue
    elif numero_usuario >9:
        print("Un número del 1 al 9...")
        continue
    else:
        print("Calculando...")
        break


numero_usariomult = numero_usuario * 9
numero_magico2 = numero_magico * numero_usariomult
print(numero_magico2)
print("Cálculo terminado.")
