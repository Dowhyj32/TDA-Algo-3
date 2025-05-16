import heapq

def suma_golosa(C):
    
    heapq.heapify(C[:])

    costo = 0
    
    while len(C)>1:
        x = heapq.heappop(C)
        y = heapq.heappop(C)
        
        suma = x+y
        costo += suma
        heapq.heappush(C, suma)
        
    suma = C[0]
    return suma, costo

C = [1,2,5]
suma, costo = suma_golosa(C)
print(f'Suma total = {suma} con un costo de total de {costo}')