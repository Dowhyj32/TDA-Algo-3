def corte(P, n):
    ganancias = [float('-inf')] * (n + 1)
    return corte_td(P, n, ganancias)

def corte_td(P, n, ganancias):
    if ganancias[n]>=0:              #Si ya lo tengo guardado, no hace falta que vuelva a calcularlo
        return ganancias[n]
    
    if n==0:
        q = 0
        
    else:
        q = float('-inf')
        for i in range(1,n+1):
            q = max(q, P[i-1]+corte_td(P,n-i,ganancias))
    
    ganancias[n]=q
    
    return q

P = [1,5,8,9,10,17,17,20,24,30]
print(corte(P,4)) 


