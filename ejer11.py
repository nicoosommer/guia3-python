#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 11:Crear un programa en el que el usuario introduzca una frase y el programa calcule el número de vocales de dicha frase.

frase=input("Ingrese una frase: ").lower()
vocales=0
for i in frase:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        vocales+=1
print(f"En su frase hay {vocales} vocales")