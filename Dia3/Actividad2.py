#Modifiquen el código para generar una calculadora que reciba el parámetro por la linea de comandos y utilice funciones
# 1 = Suma
# 2 = Resta
# 3 = Multiplicación
# 4 = División

menu="Calculadora \n  Opción 1: Suma \n  Opción 2: Resta \n  Opción 3: Multiplcación \n  Opción 4: División "

def suma(x,y):return x+y
def resta(x,y):return x-y
def mult(x,y):return x*y
def div(x,y):return x/y

def calculadora(opcion):
        if (opcion==1):
            #Primer número
            num1 = float(input ("Ingresa el primer número: "))
            #Segundo numero
            num2= float(input("Ingresa el segundo número: "))
            print("El resultado de la suma es: " + str(suma(num1,num2)))
        elif (opcion==2):
            #Primer número
            num1 = float(input ("Ingresa el primer número: "))
            #Segundo numero
            num2= float(input("Ingresa el segundo número: "))
            print("El resultado de la resta es: " + str(resta(num1,num2)))
        elif (opcion==3):
            #Primer número
            num1 = float(input ("Ingresa el primer número: "))
            #Segundo numero
            num2= float(input("Ingresa el segundo número: "))
            print("El resultado de la multiplicación es: " + str(mult(num1,num2)))
        elif (opcion==4):
            #Primer número
            num1 = float(input ("Ingresa el primer número: "))
            #Segundo numero
            num2= float(input("Ingresa el segundo número: "))
            if(num2==0):
                print("No es posible realizar una división entre 0")
            else:
                print("El resultado de la división es: " + str(div(num1,num2)))
        else: 
            print("La opción es incorrecta")
            
        respuesta = int(input("¿Quieres realizar otra operación? Ingresa un 1 y para sí o 0 para no: "))
        
        if (respuesta==1):
            return True
        elif (respuesta==0):
            return False
        else:
            print("Opción incorrecta")
            return False
            
i=True
while(i==True):
    print(menu)
    #Opción seleccionada
    opcion = float(input("Ingresa una opción: "))
    i=calculadora(opcion)
    
print("Hasta luego")
