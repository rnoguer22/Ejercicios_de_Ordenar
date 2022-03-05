lista = [5,7,3,-4,8,12,9,2,8]

class Lista:
    def __init__(self, lista):
        self.lista = lista
    
    def ordneacion_burbuja(self):
        for i in range(len(self.lista)-1):
            for j in range(len(self.lista)-1):
                if self.lista[j] > self.lista[j+1]:
                    #Intercambiamos los elementos mediante una asignacion multiple
                    self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j]
        return self.lista

print(lista)