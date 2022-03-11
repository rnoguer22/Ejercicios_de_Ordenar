"Apartado 1"
class Dicotonomia_1:
    #Definimos el constructor
    def __init__(self, tabla):
        self.tabla = tabla
    
    def ordenar(self):
        #Ordenamos la tabla
        self.tabla.sort()
        return self.tabla

"Apartado 2"
class Dicotonomia_2:
    def __init__(self, tabla):
        #Heredamos el constructor de la clase Dicotonomia_1
        Dicotonomia_1.__init__(self, tabla)
        r = []
        self.r = r

    def ordenar_lista_vacia(self):
        #Heredamos la funcion ordenar de la clase Dicotonomia_1
        Dicotonomia_1.ordenar(self)
        #Bucle para añadir cada elemento de la lista ordenada a la lista vacia
        for i in self.tabla:
            self.r.append(i)
        return self.r

if __name__ == "__main__":

    "Apartado 1"
    tabla = [4,2,6,3,8,7,5,9,1,0]
    print (tabla)
    #Definimos nuestra unica instancia de clase
    resultado = Dicotonomia_1(tabla)
    print ("La tabla ordenada por dicotonomia es: {}".format(resultado.ordenar()))

    "Apartado 2"
    resultado_2 = Dicotonomia_2(tabla)
    print ("Ordenando a partir de una lista vacia, la lista es: {}".format(resultado_2.ordenar_lista_vacia()))