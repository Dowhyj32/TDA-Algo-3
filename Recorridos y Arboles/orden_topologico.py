def orden_topologico_dfs(grafo):
    visitados = set()
    pila = []
    
    def DFS(u):
        visitados.add(u)
        
        for v in grafo[u]:
            if v not in visitados:
                DFS(v)
        pila.append(u)
        
    for nodo in grafo:
        if nodo not in visitados:
            DFS(nodo)
            
    pila.reverse()
    return pila

plan = {
    #'CBC': ['CS Nat','Algebra I', 'Algo I', 'Analisis I'],
    'CS Nat': [],
    'Algebra I': ['Algo II', 'ALC', 'Analisis Avanzado'],
    'Algo I': ['Algo II', 'Labo de datos'],
    'Analisis I': ['Analisis II'],
    'Algo II': ['ALC', 'Algo III'],
    'ALC': ['Mod Continuo', 'Inv. Op y O', 'Estadistica y Cs de datos'],
    'Labo de datos': ['Estadistica y Cs de datos'],
    'Analisis II': ['Inv. Op y O', 'Analisis Avanzado'],
    'Analisis Avanzado': ['Probabilidad', 'Mod Continuo'],
    'Algo III': ['Inv. Op y O'],
    'Probabilidad': ['Estadistica y Cs de datos'],
    'Estadistica y Cs de datos': [],
    'Inv. Op y O': [],
    'Mod Continuo': []    
}

grafo = {
    'm': {'q','r','x'},
    'n': {'o','q','u'},
    'o': {'r','s','v'},
    'p': {'o','s','z'},
    'q': {'t'},
    'r': {'u','y'},
    's': {'r'},
    't': {},
    'u': {'t'},
    'v': {'w','x'},
    'w': {'z'},
    'x': {},
    'y': {'v'},
    'z': {}
}

print(f'Posible plan de estudios: {orden_topologico_dfs(plan)}')
print(f'Posible orden topologico del grafo: {orden_topologico_dfs(grafo)}')