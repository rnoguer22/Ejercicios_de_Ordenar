lista = [5,7,3,-4,8,12,9,2,8]

for i in range(len(lista)-1):
    for j in range(len(lista)-1):
        if lista[j] > lista[j+1]:
            #Intercambiamos los elementos mediante una asignacion multiple
            lista[j], lista[j+1] = lista[j+1], lista[j]

print(lista)