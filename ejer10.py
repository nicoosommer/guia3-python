#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 10:Crear un programa en el que el usuario introduzca números enteros hasta adivinar elnúmero aleatorio entre 0 y 100 generado al azar por el ordenador.El programa debe avisar si el número introducido por el usuario es más grande o más pequeño que el número generado aleatoriamente

import random
num=random.randrange(0,100)
while True:
    op=int(input("Ingrese un nume entero entre 0 y 100: "))
    if op<num:
        print("El numero aleatorio es mayor al numero que ingreso.")
    elif op>num:
        print("El numero aleatorio es menor al numero que ingreso.")
    else:
        print("Correcto! Adivino el numero")
        break