def max_crossing_sum(arr, l, mid, r):
    # Máxima suma en el lado izquierdo
    suma = 0
    izquierda_max = float('-inf')
    for i in range(mid, l-1, -1):
        suma += arr[i]
        izquierda_max = max(izquierda_max, suma)

    # Máxima suma en el lado derecho
    suma = 0
    derecha_max = float('-inf')
    for i in range(mid+1, r+1):
        suma += arr[i]
        derecha_max = max(derecha_max, suma)

    return izquierda_max + derecha_max


def max_subarray(arr, l, r):
    # Caso base: un solo elemento
    if l == r:
        return arr[l]

    mid = (l + r) // 2

    # Caso 1: subarray en el lado izquierdo
    max_izq = max_subarray(arr, l, mid)

    # Caso 2: subarray en el lado derecho
    max_der = max_subarray(arr, mid+1, r)

    # Caso 3: subarray que cruza el medio
    max_cruz = max_crossing_sum(arr, l, mid, r)

    return max(max_izq, max_der, max_cruz)


def maxima_subsecuencia(arr):
    return max_subarray(arr, 0, len(arr)-1)


# Ejemplo
arr = [3, -1, 4, 8, -2, 2, -7, 5]
print("Máxima subsecuencia =", maxima_subsecuencia(arr))

    
a = [3,-1,4,8,-2,2,-7,5]
a2 = [3,-1,4,8,-2,2,7,5]

print(maxima_subsecuencia(a))
print(maxima_subsecuencia(a2))
