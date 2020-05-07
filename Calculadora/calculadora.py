#Suma, resta, multiplicacion, division, raiz cuadrada y exponentes

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
# falta el try y catch
def suma():
    a = int(input("Introduce el primer numero:"))
    b = int(input("Introduce el segundo numero:"))
    print("Resultado:",a+b)
    input("Pulsa cualquier tecla para volver al menu.")
    print("--------------------------------------")
    menuPrincipal()

def resta():
    print("resta")
    menuPrincipal()

    



menuPrincipal()



