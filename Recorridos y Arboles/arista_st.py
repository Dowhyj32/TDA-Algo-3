from FW import floyd_warshall

def mejor_arista_st_eficiente(grafo):
    """
    grafo: matriz de adyacencia con pesos (float('inf') si no hay conexión directa).
    """

    n = len(grafo)
    dist = floyd_warshall(grafo)

    mejor_arista = None
    max_cantidad = -1

    # Probar cada arista v -> w
    for v in range(n):
        for w in range(n):
            if grafo[v][w] != float('inf') and v != w:
                cantidad = 0

                # Verificar para todos los pares (s, t)
                for s in range(n):
                    for t in range(n):
                        if dist[s][t] == dist[s][v] + grafo[v][w] + dist[w][t]:
                            cantidad += 1

                if cantidad > max_cantidad:
                    max_cantidad = cantidad
                    mejor_arista = (v, w)

    return mejor_arista
