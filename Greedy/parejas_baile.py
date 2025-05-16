def parejas_baile(A,B):
    i, j = 0, 0
    parejas = 0
    parejas_formadas = []
    
    while i<len(A) and j<len(B):
        if abs(A[i]-B[i])<=1:
            parejas +=1
            parejas_formadas.append((i,j))
            i +=1
            j +=1
            
        elif A[i]<B[j]:
            i +=1
            
        else:
            j +=1
    
    
    return parejas, parejas_formadas
        

A = [1,2,4,6]    
B = [1,5,5,7,9]
parejas, parejas_formadas = parejas_baile(A,B)
print(f'Total de parejas: {parejas}') 
print(f'Parejas formadas: {parejas_formadas}')