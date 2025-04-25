
def orientar_fuertemente_conexo(G):
    """
    G es un diccionario de listas de adyacencia de un grafo no dirigido.
    Devuelve un diccionario con la orientación de las aristas (u -> v).
    """
    n = len(G)
    visited = [False] * n
    in_time = [0] * n
    low = [0] * n
    timer = [0]
    orientadas = []
    parent = [-1] * n

    def dfs(v):
        visited[v] = True
        timer[0] += 1
        in_time[v] = low[v] = timer[0]

        for w in G[v]:
            if w == parent[v]:
                continue
            if visited[w]:
                # Back edge: orientar v → w si w fue antes que v
                low[v] = min(low[v], in_time[w])
                if in_time[w] < in_time[v]:
                    orientadas.append((v, w))
            else:
                parent[w] = v
                orientadas.append((v, w))  # Orientación hacia el hijo
                dfs(w)
                low[v] = min(low[v], low[w])
                # Chequeo de puente
                if low[w] > in_time[v]:
                    raise ValueError("El grafo tiene un puente ⇒ no se puede orientar fuertemente conexo")

    # Asumimos que el grafo es conexo (si no, agregar un chequeo antes)
    dfs(0)
    return orientadas

G = {
    0: [3, 4],
    1: [4, 5],
    2: [5, 6],
    3: [0, 7],
    4: [0, 1, 7, 8],
    5: [1, 2, 8, 9],
    6: [2, 9],
    7: [3, 4],
    8: [4, 5],
    9: [5, 6]
}


'''
G = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3]
}
'''

try:
    orientadas = orientar_fuertemente_conexo(G)
    for u, v in orientadas:
        print(f"{u} → {v}")
except ValueError as e:
    print(e)
