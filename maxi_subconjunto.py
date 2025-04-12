def maxi_subconjunto(matriz, k, sub_conj, start):
    
    #Caso base
    if len(sub_conj)==k:
        suma = 0
        
        for i in sub_conj:
            for j in sub_conj:
                suma += matriz[i][j]
        
        return suma, sub_conj[:]
    
    mejor_sum = 0
    mejor_sub_conj = []
        
    #Paso recursivo
    for i in range(start, len(matriz)):
        sub_conj.append(i)
        suma_actual, subconj_actual = maxi_subconjunto(matriz, k, sub_conj, i+1)

        if suma_actual > mejor_sum:
            mejor_sum = suma_actual
            mejor_sub_conj = subconj_actual[:]

        
        sub_conj.pop()        
    
    return mejor_sum, mejor_sub_conj
    
#Input
n = int(input('Ingrese el orden de la matriz: '))
matriz = []

for i in range(n):
    fila = list(map(int, input(f'Ingrese la fila {i+1} de la matriz: ').split()))
    matriz.append(fila)

k = int(input('Ingrese el valor de k: '))
sub_conj = []     #Lista donde voy a ir guardando los posibles indices

#LLamada principal
mejor_sum, mejor_sub_conj = maxi_subconjunto(matriz, k, sub_conj, 0)  

print("Mejor subconjunto:", mejor_sub_conj)
print("Suma máxima:", mejor_sum)