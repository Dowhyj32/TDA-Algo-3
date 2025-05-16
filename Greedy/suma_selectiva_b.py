def suma_selectiva(X,k):
    X.sort(reverse=True)    
    S = X[:k]
    suma = sum(S)
    return suma, S       


X = [1, 2, 3, 5, 6, 7, 9, 10, 12, 13, 14, 16]
k = int(input('Ingrese un entero positivo'))
res, S = suma_selectiva(X,k)
print(f'Suma: {res}')
print(f'Conjunto S={S}')