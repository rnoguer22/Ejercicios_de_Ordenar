vector = [5,7,3,-4,8,12,9,2,8]

def segmentos(tabla):
    r = []
    for i in range(len(tabla)-1):
        if tabla[i] >= tabla[i+1]:
            r.append(tabla[i])
            if tabla[i+1] < tabla[i+2]:
                r.append(tabla[i+1])
                n = []
                for j in range(i+2, len(tabla)-1):
                    if tabla[j] >= tabla[j+1]:
                        n.append(tabla[j])
                        if tabla[j+1] < tabla[j+2]:
                            n.append(tabla[j+1])
                            return r, n
        else:
            pass

print (segmentos(vector))