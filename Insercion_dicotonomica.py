tabla = [4,2,6,3,8,7,5,9,1,0]

class dicotonomia:
    #Definimos el constructor
    def __init__(self, tabla):
        self.tabla = tabla
        self.n = min(self.tabla)
        self.contador = 0
    
    def ordenar(self):
        #Definimos una lista vacia que contendra los elementos de "tabla" ordenados crecientemente
        r = []
        if self.n == min(self.tabla):
            r.append(self.n)
            self.n += 1
            self.contador += 1
            self.ordenar()
        else:
            if self.n in self.tabla:
                r.append(self.n)
                self.n += 1
                self.contador += 1
                self.ordenar()
            elif self.contador >= len(self.tabla):
                return r