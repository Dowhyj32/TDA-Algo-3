def floyd_warshall(grafo):
    """
    grafo: matriz de adyacencia donde grafo[i][j] es el peso de la arista i -> j
    Si no hay arista directa entre i y j, se asume grafo[i][j] = +inf.
    """

    n = len(grafo)
    # Inicializar la matriz de distancias
    dist = [fila[:] for fila in grafo]  # Copia profunda

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

M=[
    [0,1,0,0,0,0,0],
    [-1,0,1,0,1,0,1],
    [0,-1,0,1,0,0,0],
    [0,0,-1,0,-1,-1],
    [0,-1,0,0,0,1,0],
    [0,0,0,1,-1,0,0],
    [0,-1,0,1,0,0,0]
]