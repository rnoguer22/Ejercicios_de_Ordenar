class Dicotonomia_1:
    #Definimos el constructor
    def __init__(self, tabla):
        self.tabla = tabla
    
    def ordenar(self):
        #Ordenamos la tabla
        self.tabla.sort()
        return self.tabla

class Dicotonomia_2:
    def __init__(self, tabla):
        #Heredamos el constructor de la clase Dicotonomia_1
        Dicotonomia_1.__init__(self, tabla)
    


if __name__ == "__main__":

    tabla = [4,2,6,3,8,7,5,9,1,0]
    print (tabla)
    #Definimos nuestra unica instancia de clase
    resultado = Dicotonomia_1(tabla)
    print ("La tabla ordenada por dicotonomia es: {}".format(resultado.ordenar()))