def izq_dominante(arr):
    
    def DyC(i, j):
        #CB: arreglo de 1 solo elemento
        if i==j:
            return True, arr[i]
        
        medio = (i+j)//2
        
        okIzq, sumIzq = DyC(i, medio)
        okDer, sumDer = DyC(medio+1, j)
        
        ok = okIzq and okDer and (sumIzq>sumDer)        #Si los 3 valores son True, ok=True, cc: ok=False
        
        return ok, sumIzq+sumDer                        #Combine cuesta O(1)
    
    ok, _ = DyC(0, len(arr)-1)
    return ok

arr1 = [8,6,7,4,5,1,3,2]
print(f'Es izquierda dominante el arreglo {arr1}?   {izq_dominante(arr1)}')

arr2 = [8,4,7,6,5,1,3,2]
print(f'Es izquierda dominante el arreglo {arr2}?   {izq_dominante(arr2)}')

# T(n) = 2*T(n/2) + O(1)