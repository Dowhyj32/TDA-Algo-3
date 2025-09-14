from collections import defaultdict

def main(n, S):
    if n == 0:
        return 0
    
    memo = [[-1]*n for _ in range(n)]

    posiciones_letras = defaultdict(list)

    
    
    for i, letra in enumerate(S):
        posiciones_letras[letra].append(i)

    def borrar(i, j):
        #Caso base: rango vacío
        if i>j: return 0

        #Caso base: un solo caracter
        if i==j:
            return 1
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        #Borro solo S[i]
        mejor = 1 + borrar(i+1, j)

        for k in posiciones_letras[S[i]]:
            if k<=i: 
                continue
            if k>j:
                break
            
            costo_medio = borrar(i+1, k-1)

            mejor = min(mejor, costo_medio + borrar(k,j))

            if mejor == 1:
                break

        memo[i][j] = mejor

        return mejor
    
    return borrar(0, n-1)

