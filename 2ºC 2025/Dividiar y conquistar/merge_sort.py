def merge_sort(arr):
    #Caso base: Si el arreglo tiene 0 o 1 elemento, ya está ordenado
    if len(arr)==1:
        return arr
    
    #DIVIDE
    mid = len(arr)//2
    izq = merge_sort(arr[:mid])
    der = merge_sort(arr[mid:])

    #COMBINE
    return merge(izq, der)


def merge(izq, der):
    res = []
    i = j = 0

    while i<len(izq) and j<len(der):
        if izq[i]<der[j]:
            res.append(izq[i])
            i+=1
        else:
            res.append(der[j])
            j+=1

    res.extend(izq[i:])
    res.extend(der[j:])

    return res

# Ejemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
print("Arreglo original:", arr)
print("Arreglo ordenado:", merge_sort(arr))