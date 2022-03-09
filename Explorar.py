class Segmento:
    #Definimos el constructor
    def __init__(self, tabla):
        self.tabla = tabla

    #Funcion para hallar los segmentos de una tabla 
    def segmentos(self):
        #En esta lista vacia se almacenaran los segmentos
        r = []
        for i in range(len(self.tabla)-1):
            #Si el elemento de la izquierda > derecha añadimos el numero a r (definicion de segmento)
            if self.tabla[i] >= self.tabla[i+1]:
                r.append(self.tabla[i])
                #Condicional para añadir el ultimo elemento del segmento
                if self.tabla[i+1] < self.tabla[i+2]:
                    r.append(self.tabla[i+1])
                    #Repetimos el mismo proceso para hallar el segundo segmento
                    n = []
                    #Con la diferencia de que partimos del indice del ultimo elemento del segmento
                    for j in range(i+2, len(self.tabla)-1):
                        if self.tabla[j] >= self.tabla[j+1]:
                            n.append(self.tabla[j])
                            if self.tabla[j+1] < self.tabla[j+2]:
                                n.append(self.tabla[j+1])
                                #Devuelve una lista con ambos segmentos
                                return r, n
            else:
                pass

    def explorar(self, segmento):
        #Hacemos copia de seguidad del maximo del segmento, tal y como nos dice el enunciado
        mi = segmento[0]
        #Desplazamos los elementos a la izquierda, concatenando dos sublistas de segmento
        segmento = segmento[1:] + segmento[:1]
        #Devolvemos el segmento ordenado
        return segmento

if __name__ == "__main__":

    vector = [5,7,3,-4,8,12,9,2,8]
    resultado = Segmento(vector)
    print ("Los segmentos de {} son: {}".format(vector, resultado.segmentos()))
    print("Tras aplicar la funcion explorar los segmentos quedan de la siguiente manera:")
    print (resultado.explorar(resultado.segmentos()[0]), " - ", resultado.explorar(resultado.segmentos()[1]))