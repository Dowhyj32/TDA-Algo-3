def desorden_sort(arr):
    # Caso base: si tiene 0 o 1 elemento, ya está ordenado
    if len(arr) <= 1:
        return arr, 0

    # DIVIDE
    mid = len(arr) // 2
    izq, inv_izq = desorden_sort(arr[:mid])
    der, inv_der = desorden_sort(arr[mid:])

    # COMBINE
    merged, inv_merge = merge(izq, der)

    # Total de inversiones = las de cada mitad + las cruzadas
    return merged, inv_izq + inv_der + inv_merge


def merge(izq, der):
    merged = []
    i = j = 0
    inv_count = 0

    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            merged.append(izq[i])
            i += 1
        else:
            merged.append(der[j])
            # Todas las posiciones restantes en izq forman inversión con der[j]
            inv_count += len(izq) - i
            j += 1

    # Agregar los elementos restantes
    merged.extend(izq[i:])
    merged.extend(der[j:])

    return merged, inv_count


# Ejemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
ordenado, inversiones = desorden_sort(arr)
print("Arreglo original:", arr)
print("Arreglo ordenado:", ordenado)
print("Cantidad de inversiones:", inversiones)
