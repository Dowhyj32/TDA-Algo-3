'''def subset_sum(i, j, C):
    # Caso base: sin elementos, suma exacta lograda
    if i == 0:
        return j == 0 or j == C[0]

    # Regla de factibilidad: si la suma buscada ya es negativa, no seguir
    if j < 0:
        return False

    # Caso 1: no tomo el elemento C[i]
    sin_tomar = subset_sum(i - 1, j, C)

    # Caso 2: tomo el elemento C[i]
    con_tomar = subset_sum(i - 1, j - C[i], C)

    return sin_tomar or con_tomar


C = [6, 12, 6]
k = 12
resultado = subset_sum(len(C) - 1, k, C)
print(resultado)'''



def subset_sum_all(i, j, C, solucion_actual):
    if i == len(C):
        if j == 0:
            print(solucion_actual)
        return

    # Opción 1: no tomar C[i]
    subset_sum_all(i + 1, j, C, solucion_actual)

    # Opción 2: tomar C[i] si j - C[i] no se hace negativo (regla de factibilidad)
    if j - C[i] >= 0:
        subset_sum_all(i + 1, j - C[i], C, solucion_actual + [C[i]])


C = [6, 12, 6]
k = 12
subset_sum_all(0, k, C, [])
