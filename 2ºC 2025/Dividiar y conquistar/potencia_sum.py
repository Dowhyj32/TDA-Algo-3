import numpy as np

def potencia_sum(A, n):
    
    if n==1:
        return A
    
    mitad = n//2
    S_n = potencia_sum(A,mitad)
    A_n = np.linalg.matrix_power(A, mitad)
    
    return S_n + A_n @ S_n


A = [[2,2],[2,2]]
n = int(input('Ingrese un numero natural que sea potencia de 2: '))
print(potencia_sum(A,n))