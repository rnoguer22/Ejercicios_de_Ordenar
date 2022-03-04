class Dicotonomia:
    #Definimos el constructor
    def __init__(self, tabla):
        self.tabla = tabla
        self.n = min(self.tabla)
        self.contador = 0
        #Definimos una lista vacia que contendra los elementos de "tabla" ordenados crecientemente
        self.r = []
    
    def ordenar(self):
        if self.n == min(self.tabla):
            self.r.append(self.n)
            self.n += 1
            self.contador += 1
            self.ordenar()
        else:
            if self.n in self.tabla:
                self.r.append(self.n)
                self.n += 1
                self.contador += 1
                self.ordenar()
            elif self.contador == len(self.tabla):
                return self.r

if __name__ == "__main__":

    tabla = [4,2,6,3,8,7,5,9,1,0]
    resultado = Dicotonomia(tabla)
    print ("La tabla ordenada por dicotonomia es: {}".format(resultado.ordenar()))