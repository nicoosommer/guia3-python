#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 7: Leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e imprimir el resultado. Ejemplo: 4*3 = 4 + 4 + 4 (4 sumado 3 veces).

a=int(input("ingrese un numero: "))
b=int(input("ingrese un numero: "))
suma=0

for i in range(b+1):
    suma+=i
print(f"{a}*{b}={suma}")