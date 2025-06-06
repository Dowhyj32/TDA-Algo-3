def indice_espejo(a, izq, der):
    if izq > der:
        return -1  # No existe
    
    medio = (izq + der) // 2
    
    if a[medio] == medio:
        return medio  # Encontrado
    elif a[medio] > medio:
        return indice_espejo(a, izq, medio - 1)  # Buscar a la izquierda
    else:
        return indice_espejo(a, medio + 1, der)  # Buscar a la derecha

a = [-4, -1, 2, 4, 7]
res = indice_espejo(a, 0, len(a)-1)
print(res)