class Lista:
    #Definimos el constructor
    def __init__(self, lista):
        self.lista = lista
    
    #Este ejercicio se puede solucionar facilmente con un algoritmo de burbuja
    def ordenacion_burbuja(self):
        #Bucle para recorrer la lista
        for i in range(len(self.lista)-1):
            #Bucle para recorrer todos los elementos de la lista
            for j in range(len(self.lista)-1):
                #Si el elemento de la lista es mayor que el que esta a su derecha
                if self.lista[j] > self.lista[j+1]:
                #Intercambiamos los elementos de la lista mediante una asignacion multiple
                    self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j]
        return self.lista

if __name__ == "__main__":
    
    vector = [5,7,3,-4,8,12,9,2,8]
    #Definimos vector como una instancia de la clase Lista
    resultado = Lista(vector)
    #Mostramos el resultado por pantalla
    print (resultado.ordenacion_burbuja())