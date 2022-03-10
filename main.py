def pedir_datos():
    while True:
        numero = input("Seleccione el ejercicio a ejecutar (1,2,3): ")
        try:
            numero == int(numero)
            return numero   
        except:
            pass