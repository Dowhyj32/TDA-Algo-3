def busqueda_binaria(arr, izq, der, objetivo):

    if izq>der:
        return -1
    
    medio = (izq+der)//2

    if arr[medio]==objetivo:
        return medio
    
    elif objetivo<arr[medio]:
        return busqueda_binaria(arr, izq, medio-1, objetivo)
    
    else:
        return busqueda_binaria(arr, medio+1, der, objetivo)
    
arr = [1, 3, 5, 7, 9, 11]
print(busqueda_binaria(arr, 0, len(arr)-1, 7))  # → 3
print(busqueda_binaria(arr, 0, len(arr)-1, 2))  # → -1
