#De la siguiente lista realizar las funciones que obtengan lo siguiente:
#Obtener el promedio
#La cantidad de aspirantes que reprobaron

a=[8,9,10,6,6,7,8,9,5,6,7,6,8,8,9,9,5,6,7,9,10,7,8,9,9]

def promedio(arreglo):
    tmp=0
    prom=0
    for i in a:
        tmp+=i
    prom =tmp/len(arreglo)
    return prom

def reprobaron(arreglo):
    reprobados=0
    for i in a:
        if(i<6):
            reprobados+=1
    return(reprobados)

print("El promedio de las calificaciones es: "+str(promedio(a)))
print("El número de reprobados es: "+str(reprobaron(a)))


            
