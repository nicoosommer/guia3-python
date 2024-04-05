#NICOLAS SOMMER //// 6TOB //// nicosomer388@gmail.com
#Ejercicio 8:Cada cliente que va al banco Galicia, indica su número de documento y aguarda a ser atendido. Cuando finaliza la atención del día se ingresa -1 para indicar que no hay más clientes para ser atendidos. El banco desea saber quién fue el primer cliente atendido (DNI) y quién fue el último.

i=1
dni=0
while(dni!=-1):
    dni=int(input("Ingrese su documento y espere a ser atendido: "))
    if i==1:
        pc=dni
    if dni!=-1:
        ult=dni
    i+=1
print(f"El primer cliente fue {pc} y el utlimo es {ult}")