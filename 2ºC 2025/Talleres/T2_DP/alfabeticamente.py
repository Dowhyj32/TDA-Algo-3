import math

def alfabeticamente(cantd_palabras, Costos, palabras):

    invertidas = [p[::-1] for p in palabras]

    #Costo min hasta i si dejo la palabra normal
    dp_sin_invertir = [float('inf')]*cantd_palabras 

    #Costo min hasta i si dejo la palabra invertida
    dp_invirtiendo = [float('inf')]*cantd_palabras

    #Caso base
    dp_sin_invertir[0] = 0
    dp_invirtiendo[0] = Costos[0]

    for i in range(1,cantd_palabras):

        #Si quiero dejar la palabra normal
        #Puedo venir de una palabra normal
        if palabras[i-1]<=palabras[i]:
            dp_sin_invertir[i] = min(dp_sin_invertir[i],dp_sin_invertir[i-1])
        
        #Puedo venir de una palabra invertida
        if invertidas[i-1]<=palabras[i]:
            dp_sin_invertir[i] = min(dp_sin_invertir[i], dp_invirtiendo[i-1])

        #Quiero invertir la palabra
        #Puedo venir de una palabra normal
        if palabras[i-1]<=invertidas[i]:
            dp_invirtiendo[i] = min(dp_invirtiendo[i], dp_sin_invertir[i-1]+Costos[i])
        
        #Puedo venir de una palabra invertida
        if invertidas[i-1]<=invertidas[i]:
            dp_invirtiendo[i] = min(dp_invirtiendo[i], dp_invirtiendo[i-1]+Costos[i])

    res = min(dp_sin_invertir[-1], dp_invirtiendo[-1])

    return -1 if math.isinf(res) else res


C = [100, 200, 300]
p = ['za','yb','xc']
cantd_p = len(C)
print(f'Para ordenar las palabras ordenadas, gastaremos {alfabeticamente(cantd_p, C, p)}')