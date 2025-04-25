def encontrar_puentes(G):
    """
    G: diccionario de listas de adyacencia (grafo no dirigido)
    Retorna una lista de aristas puente como pares (u, v)
    """
    n = len(G)
    visited = [False] * n
    in_time = [0] * n
    low = [0] * n
    timer = [0]
    parent = [-1] * n
    puentes = []

    def dfs(v):
        visited[v] = True
        timer[0] += 1
        in_time[v] = low[v] = timer[0]

        for w in G[v]:
            if w == parent[v]:
                continue
            if visited[w]:
                # Back edge
                low[v] = min(low[v], in_time[w])
            else:
                parent[w] = v
                dfs(w)
                low[v] = min(low[v], low[w])
                if low[w] > in_time[v]:
                    puentes.append((v, w))  # v → w es puente

    dfs(0)  # Asumimos que el grafo es conexo
    return puentes

G = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3]
}

print(encontrar_puentes(G))
# Salida esperada: [(3, 4), (2, 3)]
