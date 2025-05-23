def es_bipartito_DFS(grafo):
    color = {}  # Diccionario que asigna un color a cada nodo

    def dfs(nodo, c):
        color[nodo] = c
        for vecino in grafo[nodo]:
            if vecino not in color:
                if not dfs(vecino, 1 - c):  # Alternamos el color
                    return False
            elif color[vecino] == color[nodo]:
                return False  # Conflicto: no es bipartito
        return True

    for nodo in grafo:
        if nodo not in color:
            if not dfs(nodo, 0):
                return False

    return True

grafo_1 = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print(es_bipartito_DFS(grafo_1))  # True


grafo_2 = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}

print(es_bipartito_DFS(grafo_2))  # False
