#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 3:Mostrar las tablas de multiplicar (entre 1 y 10) del número 3.¿Qué cambios harías en el algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?
num=int(input("ingrese un numero: "))
for i in range(1,11):
    print(f"{num}*{i}={i*num}")