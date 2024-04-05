#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 6: Crear un programa que permita ingresar números, hasta que la suma de los números pares supere 100. Mostrar Cuántos números en total se ingresaron.
i=0
suma=0
while(suma<=100):
    num=int(input("ingrese un numero: "))
    if num%2==0:
        suma+=num
    i+=1
print(f"La cantidad de numeros que se ingresaron fue: {i}")