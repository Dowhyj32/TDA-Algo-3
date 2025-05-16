import heapq

def suma_selectiva_heap(X, k):
    # 1. Tomamos los primeros k elementos del conjunto
    heap = X[:k]

    # 2. Creamos un min-heap con esos k elementos
    heapq.heapify(heap)  # O(k)

    # 3. Recorremos el resto del conjunto
    for i in range(k, len(X)):
        # Si encontramos un elemento mayor que el menor del heap:
        if X[i] > heap[0]:
            # Reemplazamos el menor por este nuevo más grande
            heapq.heappushpop(heap, X[i])  # O(log k)

    # 4. Al final, el heap tiene los k elementos más grandes
    suma = sum(heap)
    return suma, list(heap)

X = [1, 2, 3, 5, 6, 7, 9, 10, 12, 13, 14, 16]
k = int(input('Ingrese un entero positivo'))
res, S = suma_selectiva_heap(X,k)
print(f'Suma: {res}')
print(f'Conjunto S={S}')