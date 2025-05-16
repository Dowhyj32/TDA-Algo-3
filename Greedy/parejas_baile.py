def parejas_baile(A,B):
    i, j = 0, 0
    parejas = 0
    parejas_formadas = []
    
    while i<len(A) and j<len(B):    #O(n+m): n=len(A) m=len(B)
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
        

def parejas_baile_recursivo(A,B,i=0,j=0):
    if i>=len(A) or j>=len(B):
        return 0, []
    
    if abs(A[i]-B[i])<=1:
        parejas, lista = parejas_baile_recursivo(A,B,i+1,j+1)
        return 1 + parejas, [(i,j)]+lista
    
    elif A[i]<B[j]:
        return parejas_baile_recursivo(A,B,i+1,j)
    
    else:
        return parejas_baile_recursivo(A,B,i,j+1)        
        
        
A = [1,2,4,6]    
B = [1,5,5,7,9]
parejas, parejas_formadas = parejas_baile_recursivo(A,B)
print(f'Total de parejas: {parejas}') 
print(f'Parejas formadas: {parejas_formadas}')