from collections import defaultdict

class Grafo:
    def __init__(self, n):
        self.n = n
        self.grafo = defaultdict(list)
        self.tiempo = 0
        self.in_time = [-1] * n
        self.low = [-1] * n
        self.puentes = set()
        self.orientadas = []

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def dfs(self, v, padre):
        self.in_time[v] = self.low[v] = self.tiempo
        self.tiempo += 1

        for w in self.grafo[v]:
            if w == padre:
                continue
            if self.in_time[w] == -1:
                self.orientadas.append((v, w))  # Orientar árbol DFS
                self.dfs(w, v)
                self.low[v] = min(self.low[v], self.low[w])

                if self.low[w] > self.in_time[v]:
                    self.puentes.add((min(v, w), max(v, w)))
            else:
                self.low[v] = min(self.low[v], self.in_time[w])
                if self.in_time[w] < self.in_time[v]:
                    self.orientadas.append((v, w))  # Orientar back edge hacia arriba

    def orientar_grafo(self):
        self.dfs(0, -1)
        return self.orientadas, self.puentes

# ----------- Ejemplos de prueba -----------
def mostrar_resultado(grafo, n):
    g = Grafo(n)
    for u, vs in grafo.items():
        for v in vs:
            if u < v:  # Evitar duplicar aristas
                g.agregar_arista(u, v)
    orientadas, puentes = g.orientar_grafo()
    print("Orientadas:", orientadas)
    print("Puentes (mantener bidireccionales):", puentes)
    print("---")

# Ejemplo 1: ciclo simple
G1 = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}
mostrar_resultado(G1, 4)

# Ejemplo 2: un puente
G2 = {
    0: [1],
    1: [0, 2, 3],
    2: [1],
    3: [1, 4],
    4: [3]
}
mostrar_resultado(G2, 5)

# Ejemplo 3: grafo completamente conexo (sin puentes)
G3 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3, 0]
}
mostrar_resultado(G3, 5)

# Ejemplo 4: grafo con dos componentes que se unen por un puente
G4 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3]
}
mostrar_resultado(G4, 5)
