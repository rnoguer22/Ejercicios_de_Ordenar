vector = [5,7,3,-4,8,12,9,2,8]

#Funcion para hallar los segmentos de una tabla 
def segmentos(tabla):
    #En esta lista vacia se almacenaran los segmentos
    r = []
    for i in range(len(tabla)-1):
        #Si el elemento de la izquierda > derecha añadimos el numero a r (definicion de segmento)
        if tabla[i] >= tabla[i+1]:
            r.append(tabla[i])
            #Condicional para añadir el ultimo elemento del segmento
            if tabla[i+1] < tabla[i+2]:
                r.append(tabla[i+1])
                #Repetimos el mismo proceso para hallar el segundo segmento
                n = []
                #Con la diferencia de que partimos del indice del ultimo elemento del segmento
                for j in range(i+2, len(tabla)-1):
                    if tabla[j] >= tabla[j+1]:
                        n.append(tabla[j])
                        if tabla[j+1] < tabla[j+2]:
                            n.append(tabla[j+1])
                            #Devuelve una lista con ambos segmentos
                            return r, n
        else:
            pass

def explorar(segmento):
    #Hacemos copia de seguidad del maximo del segmento, tal y como nos dice el enunciado
    mi = segmento[0]
    #Desplazamos los elementos a la izquierda, concatenando dos sublistas de segmento
    segmento = segmento[1:] + segmento[:1]
    #Devolvemos el segmento ordenado
    return segmento

print (segmentos(vector))
segmento_1, segmento_2 = segmentos(vector)[0], segmentos(vector)[1]
print(segmento_1)
print(segmento_2)

print(explorar(segmento_1))