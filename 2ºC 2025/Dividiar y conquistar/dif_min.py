def diferencia_minima(A, B):
    n = len(A)
    
    def g(i):
        return A[i]-B[i]
    
    
    if g(0)>=0:
        return abs(g(0)), 0
    
    if g(n-1)<=0:
        return abs(g(n-1)), n-1
    
    l = 0
    h = n-1
    
    while h-l>1:
        medio = (l+h)//2
        
        if g(medio)==0:
            return 0, medio
        
        if g(medio)<0:
            l = medio
            
        else:
            h = medio
            
    cand1, cand2 = abs(g(l)), abs(g(h))
    return (cand1, l) if cand1 <= cand2 else (cand2, h)


A = [1,3,5,7,11]
B = [20,12,10,8,5]

difAB, indAB = diferencia_minima(A,B)

print(f'La difencia minima entre A y B es {difAB} y en el índice es {indAB}')

C = [1,2,3,4,5]
D = [5,4,3,2,1]

difCD, indCD = diferencia_minima(C,D)

print(f'La difencia minima entre C y D es {difCD} y en el índice es {indCD}')