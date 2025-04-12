def calcular_valores_maximos(matriz):
    valores = []
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i != j:
                valores.append(matriz[i][j])
    return sorted(valores, reverse=True)

def maxi_subconjunto(matriz, k, sub_conj, start, suma_actual, mejor_sum, mejor_sub_conj, valores_maximos):
    
    # Poda
    faltan = k - len(sub_conj)
    max_extra = sum(valores_maximos[:faltan*faltan])
    if suma_actual + max_extra <= mejor_sum[0]:
        return

    # Caso base
    if len(sub_conj) == k:
        if suma_actual > mejor_sum[0]:
            mejor_sum[0] = suma_actual
            mejor_sub_conj[0] = sub_conj[:]
        return
        
    # Paso recursivo
    for i in range(start, len(matriz)):
        nuevo_valor = 0
        for j in sub_conj:
            nuevo_valor += matriz[i][j] + matriz[j][i]

        sub_conj.append(i)
        maxi_subconjunto(matriz, k, sub_conj, i+1, suma_actual + nuevo_valor, mejor_sum, mejor_sub_conj, valores_maximos)
        sub_conj.pop()  # Backtrack
    
#Input
n = int(input('Ingrese el orden de la matriz: '))
matriz = []

for i in range(n):
    fila = list(map(int, input(f'Ingrese la fila {i+1} de la matriz: ').split()))
    matriz.append(fila)

k = int(input('Ingrese el valor de k: '))
sub_conj = []     #Lista donde voy a ir guardando los posibles indices

mejor_sum = [0]
mejor_sub_conj = [[]]

valores_maximos = calcular_valores_maximos(matriz)

#LLamada principal
maxi_subconjunto(matriz, k, sub_conj, 0, 0, mejor_sum, mejor_sub_conj, valores_maximos)

print("Mejor subconjunto de índices:", mejor_sub_conj[0])
print("Suma máxima:", mejor_sum[0])