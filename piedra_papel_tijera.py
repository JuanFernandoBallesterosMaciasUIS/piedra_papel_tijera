#Piedra, papel o tijera.
import random
print("+------------------------------------+")
print("|-------PIEDRA-PAPEL-O-TIJERAS-------|")
print("+------------------------------------+\n")
print("+---------------OPCIONES-------------+")
print("|      1. Piedra                     |")
print("|      2. Tijeras                    |")
print("|      3. Papel                      |")
print("+---------------OPCIONES-------------+\n")

#input
opc = int(input("Ingresa uno de los tres dijitos: "))

#process
wind = random.randint(1,3)
def empate(opc1,wind1):
    return print("----------------EMPATE--------------\n>> Ingresaste",opc1,"y la maquina tambien eligio",wind1,"<<\n----------------EMPATE--------------")
     
if (opc == wind):
    if opc == 1:
        opc1 = "Piedra"
        wind1 = "Piedra"
        empate(opc1,wind1)
    if opc == 2:
        opc1 = "Tijeras"
        wind1 = "Tijeras"    
        empate(opc1,wind1)
    if opc == 3:
        opc1 = "Papel"
        wind1 = "Papel"    
        empate(opc1,wind1)
elif (opc == 1):
    if wind == 2:
        print("----------------GANASTE--------------\n>> Ingresaste piedra y la maquina eligio tijeras <<\n----------------GANASTE--------------")
    if wind == 3:
        print("----------------PERDISTE--------------\n>> Ingresaste piedra y la maquina eligio papel <<\n----------------PERDISTE--------------")
elif (opc == 2):
    if wind == 3:
        print("----------------GANASTE--------------\n>> Ingresaste tijeras y la maquina eligio papel <<\n----------------GANASTE--------------")
    if wind == 1:
        print("----------------PERDISTE--------------\n>> Ingresaste tijeras y la maquina eligio piedra <<\n----------------PERDISTE--------------")
elif (opc == 3):
    if wind == 1:
        print("----------------GANASTE--------------\n>> Ingresaste papel y la maquina eligio piedra <<\n----------------GANASTE--------------")
    if wind == 2:
        print("----------------PERDISTE--------------\n>> Ingresaste papel y la maquina eligio tijeras <<\n----------------PERDISTE--------------")
