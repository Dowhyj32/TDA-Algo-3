from collections import deque

def BFS_bipartito(G, inicio, color, padre):
    
    color[inicio] = 0
    cola = deque([inicio])
    
    while cola:
        actual = cola.popleft()
        
        for vecino in G[actual]:
            if vecino not in color:
                color[vecino] = 1-color[actual]
                padre[vecino] = actual
                cola.append(vecino)
            
            elif color[vecino]==color[actual]:
                return ciclo_impar(actual, vecino, padre)
    
    return None
            
def ciclo_impar(u, v, padre):
    camino_u = []
    camino_v = []
    
    while u!=v:
        camino_u.append(u)
        camino_v.append(v)
        u = padre.get(u, u)
        v = padre.get(v, v)
        
    camino_u.append(u)
    
    ciclo = camino_u + camino_v[::-1]
    return ciclo

def es_bipartito_o_ciclo(grafo):
    color = {}
    padre = {}
    
    for nodo in grafo:
        if nodo not in color:
            ciclo = BFS_bipartito(grafo, nodo, color, padre)
            if ciclo:
                return False, ciclo  # No es bipartito, ciclo impar
    
    # Si terminamos sin conflicto, formar bipartición
    A = [v for v in color if color[v] == 0]
    B = [v for v in color if color[v] == 1]
    return True, (A, B)
