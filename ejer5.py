#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 5:Escribir un programa en Python que lea números enteros hasta que se ingrese un 0, y muestre el máximo, el mínimo y el promedio de todos ellos.
i=1
suma=0
mayor=0
menor=0
while(i!=0):
    num=int(input("ingrese un numero. si el numero es 0 se termina el programa: "))
    if num==0:
        break
    if i==1:
        mayor=num
        menor=num
    else:
        if num>mayor:
            mayor=num
        elif num<menor:
            menor=num
    suma+=num
    i+=1
print(f"el promedio es {suma/10}, el mayor es {mayor}, y el menor es {menor}")