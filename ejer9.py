#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 9:Una familia va de vacaciones en auto desde Buenos Aires hasta Córdoba. La familiaconsta de los dos padres y de un hijo y de una niña. Durante el trayecto los niñospreguntan incesantes:¡¿Ya llegamos?! … a lo que los padres responden ¡No!Crear un programa que recree tal situación y que la consulta formulada por los niñosse detenga cuando la respuesta sea¡¡Sí!!

while True:
    print("¡¿Ya llegamos?!")
    rta=input("Ingrese la rta de los padres. SI llegaron ingrese  ¡¡Sí!!: ")
    if rta=="¡¡Sí!!":
        print("Porgrama finalizado. ")
        break