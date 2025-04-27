from FW import floyd_warshall
INF = float('inf')

def es_geodesico(grafo, D):
    """
    grafo: matriz de adyacencia del grafo
    D: conjunto (o lista) de vértices especiales
    Devuelve True si D es geodésico, False en caso contrario
    """
    n = len(grafo)
    dist = floyd_warshall(grafo)
    vertices_cubiertos = set()

    for v in D:
        for w in D:
            for u in range(n):
                if dist[v][u] + dist[u][w] == dist[v][w]:
                    vertices_cubiertos.add(u)

    return len(vertices_cubiertos) == n

# Ejemplo 1

grafo = [
    [0, 1, 2],
    [1, 0, 1],
    [2, 1, 0]
]
D = [0, 1, 2]

print(es_geodesico(grafo, D))  # Esperado: True

# Ejemplo 2

rafo = [
    [0, 2, INF, 5],
    [2, 0, 3, INF],
    [INF, 3, 0, 1],
    [5, INF, 1, 0]
]
D = [0, 1]  # Solo 2 vértices en D

print(es_geodesico(grafo, D))  # Esperado: False

# Ejemplo 3

grafo = [
    [0, 1, 2, 3],
    [1, 0, 1, 2],
    [2, 1, 0, 1],
    [3, 2, 1, 0]
]
D = [1, 2]  # Solo los del medio

print(es_geodesico(grafo, D))  # Esperado: True

# Ejemplo 4

grafo = [
    [0, 1, INF],
    [INF, 0, 1],
    [INF, INF, 0]
]
D = [0, 1]

print(es_geodesico(grafo, D))  # Esperado: False