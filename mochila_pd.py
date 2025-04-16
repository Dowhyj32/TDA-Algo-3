def mochila(p, v, C):
    
    n = len(p)
    dp = [[0 for _ in range(C+1)] for _ in range(n+1)]
    
    # Lleno la matriz
    for i in range(1, n+1):
        for j in range(1, C+1):
            if p[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], v[i-1] + dp[i-1][j - p[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
                
    # Reconstrucción de los objetos seleccionados
    objetos_seleccionados = []
    i, j = n, C
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            objetos_seleccionados.append(i-1)  # Guardo el índice del objeto
            j -= p[i-1]  # Reduzco la capacidad
        i -= 1

    objetos_seleccionados.reverse()  # Para que estén en orden original
    
    return dp[n][C], objetos_seleccionados
    
pesos = [1, 3, 4, 5]
valores = [1, 4, 5, 7]
capacidad = 7

resultado, seleccionados = mochila(pesos, valores, capacidad)

print("Valor máximo:", resultado)
print("Objetos seleccionados:", seleccionados)

for i in seleccionados:
    print(f" - Objeto {i} → peso: {pesos[i]}, valor: {valores[i]}")