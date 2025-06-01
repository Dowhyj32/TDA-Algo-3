def es_mas_a_la_izquierda(arr, l, r):
    # CASO BASE: si el subarreglo tiene un solo elemento, no hay más mitades
    if r - l == 1:
        return (True, arr[l])  # Un solo número se considera válido, y devuelve su suma

    # DIVIDIR: calculamos el punto medio
    mid = (l + r) // 2

    # RECURSIÓN: resolvemos cada mitad
    izq_ok, suma_izq = es_mas_a_la_izquierda(arr, l, mid)
    der_ok, suma_der = es_mas_a_la_izquierda(arr, mid, r)

    # COMBINAR: este subarreglo es "más a la izquierda" si:
    # - La suma izquierda > suma derecha
    # - Y cada mitad también es válida
    actual_ok = suma_izq > suma_der and izq_ok and der_ok

    # Retornamos si este tramo es válido y su suma total
    return (actual_ok, suma_izq + suma_der)


def arreglo_es_mas_a_la_izquierda(arr):
    ok, _ = es_mas_a_la_izquierda(arr, 0, len(arr))
    return ok

arr = [8, 6, 7, 4, 5, 1, 3, 2]
arreglo_es_mas_a_la_izquierda(arr)