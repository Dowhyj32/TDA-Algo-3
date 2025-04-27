from FW import floyd_warshall

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