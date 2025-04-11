def maxi_subconjunto(matriz, k, sub_conj):
    
    #Caso base
    if len(sub_conj)==k:
        for ind in sub_conj:
            
        
    #Paso recursivo
    
        
    
    
#Input
n = int(input('Ingrese el orden de la matriz: '))
matriz = []

for i in range(n):
    fila = list(map(int, input(f'Ingrese la fila {i+1} de la matriz: ').split()))
    matriz.append(fila)

k = int(input('Ingrese el valor de k: '))
sub_conj = []     #Lista donde voy a ir guardando los posibles indices

#LLamada principal
maxi_subconjunto(matriz, k, sub_conj)    