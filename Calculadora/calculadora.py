#Suma, resta, multiplicacion, division, raiz cuadrada y exponentes
from math import sqrt
def menuPrincipal():

    print("Calculadora:\n")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("5) Exponencial")
    print("6) Raiz cuadrada\n")
    print("0) Salir")

    while True:
        try:
            option = int(input("Elige una opcion:"))
            if option == 0:
                break
            elif option == 1:
                suma()
                break
            elif option == 2:
                resta()
                break
            elif option == 3:
                multi()
                break
            elif option == 4:
                divi()
                break
            elif option == 5:
                expo()
                break
            elif option == 6:
                raiz()
                break
            else:
                print("Elige una opcion entre 0 y 6.")
                menuPrincipal()
        except ValueError:
            print("Elige una opcion entre 0 y 6")
    exit

def primernumero():
    global n1
    try:
        n1 = int(input("Introduce un numero:"))
    except ValueError:
        print("El caracter introducido es invalido. Introduce un numero.")
        primernumero()
    return n1

def segundonumero():
    global n2
    try:
        n2 = int(input("Introduce el segundo numero:"))
    except ValueError:
        print("El caracter introducido es invalido. Introduce un numero.")
        segundonumero()
    return n2

def suma():
    print("Resultado:",primernumero()+segundonumero())
    input("Pulsa cualquier tecla para volver al menu.")
    print("--------------------------------------")
    menuPrincipal()

def resta():    
    print("Resultado:",primernumero()-segundonumero())
    input("Pulsa cualquier tecla para volver al menu.")
    print("--------------------------------------")
    menuPrincipal()   

def multi():
    print("Resultado:",primernumero()*segundonumero())
    input("Pulsa cualquier tecla para volver al menu.")
    print("--------------------------------------")
    menuPrincipal()

def divi():
    
    a = primernumero()
    b = segundonumero()
    if b==0:
        print("No se puede dividir entre 0.")
    else:
        print("Resultado:",a/b)
    input("Pulsa cualquier tecla para volver al menu.")
    print("--------------------------------------")
    menuPrincipal()

def expo():
    
    print("Resultado:",primernumero()**segundonumero())
    input("Pulsa cualquier tecla para volver al menu.")
    print("--------------------------------------")
    menuPrincipal()

def raiz():    
    print("Resultado:",sqrt(primernumero))
    input("Pulsa cualquier tecla para volver al menu.")
    print("--------------------------------------")
    menuPrincipal()


menuPrincipal()



