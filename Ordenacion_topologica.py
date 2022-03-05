class Lista:
    def __init__(self, lista, i):
        self.lista = lista
        self.i = 0
        self.j = 0
    
    def ordenacion_burbuja(self):

        def recorrer_lista_2(j):
            if j == (len(self.lista)-1):
                recorrer_lista(self.i+1)
            else:
                if self.lista[j] > self.lista[j+1]:
                #Intercambiamos los elementos de la lista mediante una asignacion multiple
                    self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j]
                    print (self.lista)
            recorrer_lista_2(j+1)

        def recorrer_lista(i):
            if i == len(self.lista)-1:
                return self.lista
            else:
                recorrer_lista_2(self.j+i)
        
        recorrer_lista(self.i)

if __name__ == "__main__":
    
    vector = [5,7,3,-4,8,12,9,2,14]
    resultado = Lista(vector, 0)
    print (resultado.ordenacion_burbuja())