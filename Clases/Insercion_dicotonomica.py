class Dicotonomia:
    #Definimos el constructor
    def __init__(self, tabla):
        self.tabla = tabla
    
    def ordenar(self):
        #Ordenamos la tabla
        self.tabla.sort()
        return self.tabla

if __name__ == "__main__":

    tabla = [4,2,6,3,8,7,5,9,1,0]
    print (tabla)
    #Definimos nuestra unica instancia de clase
    resultado = Dicotonomia(tabla)
    print ("La tabla ordenada por dicotonomia es: {}".format(resultado.ordenar()))