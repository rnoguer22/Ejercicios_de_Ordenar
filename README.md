# Ejercicios_de_Ordenar

[Pincha aqui para acceder al link de este repositorio](https://github.com/rnoguer22/Ejercicios_de_Ordenar.git)

Hemos resuelto la tarea "Ejercicios de Ordenar", para la cual hemos creado una carpeta llamada "Clases" en la que se han introducido todas las clases para la correcta realizacion de la tarea. De la misma manera, hemos creado otra carpeta ("Introducir") con archivos para introducir datos (cadenas de texto, numeros y booleanos). Finalmente hemos intoducido los diagramas de flujo y UML correspondientes

## Main
```Python3
if __name__ == "__main__":

    from Clases.Insercion_dicotonomica import Dicotonomia_1, Dicotonomia_2
    print ("Ejercicio 1:")
    print ("Apartado 1")
    tabla = [4,2,6,3,8,7,5,9,1,0]
    print (tabla)
    #Definimos nuestra unica instancia de clase
    resultado = Dicotonomia_1(tabla)
    print ("La tabla ordenada por dicotonomia es: {}".format(resultado.ordenar()))

    print("Apartado 2")
    resultado_2 = Dicotonomia_2(tabla)
    print ("Ordenando a partir de una lista vacia, la lista es: {}".format(resultado_2.ordenar_lista_vacia()))
    print ("\n")

    from Clases.Ordenacion_topologica import Lista
    print ("Ejercicio 2")
    vector = [5,7,3,-4,8,12,9,2,8]
    #Definimos vector como una instancia de la clase Lista
    resultado = Lista(vector)
    #Mostramos el resultado por pantalla
    print ("El resultado tras la ordenacion es el siguiente: {}".format(resultado.ordenacion_burbuja()))
    print ("\n")

    from Clases.Explorar import Segmento
    print ("Ejercicio 3")
    vector = [5,7,3,-4,8,12,9,2,8]
    #Definimos vector como unica instancia de la clase Segmento
    resultado = Segmento(vector)
    #Mostramos por pantalla los segmentos de "vector"
    print ("Los segmentos de {} son: {}".format(vector, resultado.segmentos()))
    print("Tras aplicar la funcion explorar los segmentos quedan de la siguiente manera:")
    #Mostramos por pantalla los segmentos tras aplicar la funcion explorar
    print (resultado.explorar(resultado.segmentos()[0]), " - ", resultado.explorar(resultado.segmentos()[1]))
```

Su correspondiente diagrama de flujo es el siguiente:

![main drawio](https://user-images.githubusercontent.com/91721762/158055985-30ccf699-b95c-4a0a-98ff-d45dabdb5aaf.png)

Las clases utilizadas en el archivo main.py, con sus correspondientes diagramas UML son las siguientes:

### 1) Insercion Dicotonomica
```Python3
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
```
![Insercion_Dicotonomica_UML drawio](https://user-images.githubusercontent.com/91721762/158056064-fd0e6d8b-aa00-4343-b7a4-87c2271b8f08.png)

### 2) Ordenacion Topologica
```Python3
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
                    print ("Intercambiando {} con {}...".format(self.lista[j], self.lista[j+1]))
                    self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j]
        return self.lista
```
![Ordenacion_Topologica_UML drawio](https://user-images.githubusercontent.com/91721762/158056108-64e23223-e40d-4f59-a3a0-0699decd9591.png)

### 3) Explorar
```Python3
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
```
![Explorar_UML drawio](https://user-images.githubusercontent.com/91721762/158056133-20ebdb45-64bd-4a5f-b9a6-c4d5fa0d1910.png)

