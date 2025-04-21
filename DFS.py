def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

dfs(graph, 'A', set())


def is_connected(graph):
    visited = set()
    dfs(graph, list(graph.keys())[0], visited)
    return len(visited) == len(graph)

grafo_conexo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
print(is_connected(grafo_conexo)) 

grafo_no_conexo = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C']
}
print(is_connected(grafo_no_conexo))


def count_components(graph):
    visited = set()
    components = 0
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
            components += 1
    return components

# Ejemplo 1
grafo = {
    '1': ['2', '3'],
    '2': ['1', '4'],
    '3': ['1'],
    '4': ['2']
}
print(count_components(grafo))  

# Ejemplo 2
grafo = {
    '1': ['2'],
    '2': ['1'],
    '3': [],
    '4': ['5'],
    '5': ['4']
}
print(count_components(grafo)) 

def has_cycle(graph):
    def dfs_cycle(node, parent, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs_cycle(neighbor, node, visited):
                    return True
            elif neighbor != parent:
                # Encontramos un ciclo
                return True
        return False

    visited = set()
    for node in graph:
        if node not in visited:
            if dfs_cycle(node, None, visited):
                return True
    return False

grafo_con_ciclo = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}
print(has_cycle(grafo_con_ciclo))  

grafo_sin_ciclo = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}
print(has_cycle(grafo_sin_ciclo))
