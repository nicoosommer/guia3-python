#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 4: Leer 10 números enteros e imprimir el promedio, el mayor y menor ingresado.
i=1
suma=0
while (i<=10):
    num=int(input("ingrese un numero: "))
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