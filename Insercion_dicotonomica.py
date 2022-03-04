class Dicotonomia:
    #Definimos el constructor
    def __init__(self, tabla):
        self.tabla = tabla
        self.n = min(self.tabla)
        #Establecemos un contador para el correcto flujo de la funcion "ordenar"
        self.contador = 0
        #Definimos una lista vacia que contendra los elementos de "tabla" ordenados crecientemente
        self.r = []
    
    def ordenar(self):
        #Condicional para añadir el valor minimo de la tabla, y de ahi seguir hacia adelante
        if self.n == min(self.tabla):
            self.r.append(self.n)
            #Incrementamos en 1 el valor minimo, para ver si posteriormete este se encuentra en "tabla"
            self.n += 1
            self.contador += 1
            #Aplicamos recursividad para resolver el ejercicio
            self.ordenar()
        else:
            if self.n in self.tabla == False:
                #Si self.n no esta en la tabla, vamos incrementando en 1 hasta que este en "tabla"
                self.n += 1
                self.ordenar()
            if self.n in self.tabla:
                #Añadimos self.n a la futura tabla ordenada, ya que self.n esta en "tabla"
                self.r.append(self.n)
                self.n += 1
                self.contador += 1
                self.ordenar()
            #Cuando el contador sea igual a len(self.tabla), la tabla estara ordenada por completo
            elif self.contador == len(self.tabla):
                #Mostramos la tabla por pantalla
                print (self.r)
                return self.r

if __name__ == "__main__":

    tabla = [4,2,6,3,8,7,5,9,1,0]
    print (tabla)
    #Definimos nuestra unica instancia de clase
    resultado = Dicotonomia(tabla)
    print ("La tabla ordenada por dicotonomia es:")
    resultado.ordenar()