vector = [5,7,3,-4,8,12,9,2,8]

def segmentos(tabla):
    def segmento(j):
        r = []
        for i in range(j, len(tabla)-1):
            if tabla[i] >= tabla[i+1]:
                r.append(tabla[i])
                if tabla[i+1] < tabla[i+2]:
                    r.append(tabla[i+1])
                    return r
            else:
                pass

print (segmentos(vector))