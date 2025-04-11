def maxi_subconjunto(matriz, k, sub_conj, mejor_sum, mejor_sub_conj):
    
    #Caso base
    if len(sub_conj)==k:
        suma = 0
        
        for i in sub_conj:
            for j in sub_conj:
                suma += matriz[i][j]
        
        if suma > mejor_sum:
            mejor_sum = suma
            mejor_sub_conj = sub_conj[:]
        
    #Paso recursivo
    
        
    
    
#Input
n = int(input('Ingrese el orden de la matriz: '))
matriz = []

for i in range(n):
    fila = list(map(int, input(f'Ingrese la fila {i+1} de la matriz: ').split()))
    matriz.append(fila)

k = int(input('Ingrese el valor de k: '))
sub_conj = []     #Lista donde voy a ir guardando los posibles indices

mejor_sum = 0
mejor_sub_conj = []

#LLamada principal
maxi_subconjunto(matriz, k, sub_conj, mejor_sum, mejor_sub_conj)    