from collections import deque

def BFS(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    res = []
    
    visitados.add(inicio)
    
    while cola:
        nodo = cola.popleft()
        res.append(nodo)
        
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
                
    return res
    
grafo = {
    1: [2,4],
    2: [1,3,5,7,8],
    3: [2,4,9,10],
    4: [1,3],
    5: [2,6,7,8],
    6: [5],
    7: [2,5,8],
    8: [2,5,7],
    9: [3],
    10: [3]
}

for i in range(1,len(grafo)+1):
    print(f'BFS (nodo inicial: {i}): {BFS(grafo, i)}')