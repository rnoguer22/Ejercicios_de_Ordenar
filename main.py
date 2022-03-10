def pedir_datos():
    while True:
        numero = input("Seleccione el ejercicio a ejecutar (1,2,3): ")
        try:
            numero == int(numero)
            return numero   
        except:
            print ("Introduzca un numero entero, por favor")
            pass

if __name__ == "__main__":