import time

def calcular_valores_maximos(matriz):
    valores = []
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i != j:
                valores.append(matriz[i][j])
    return sorted(valores, reverse=True)

def maxi_subconjunto_sin_poda(matriz, k, sub_conj, start, suma_actual, mejor_sum, mejor_sub_conj):
    if len(sub_conj) == k:
        if suma_actual > mejor_sum[0]:
            mejor_sum[0] = suma_actual
            mejor_sub_conj[0] = sub_conj[:]
        return
        
    for i in range(start, len(matriz)):
        nuevo_valor = 0
        for j in sub_conj:
            nuevo_valor += matriz[i][j] + matriz[j][i]

        sub_conj.append(i)
        maxi_subconjunto_sin_poda(matriz, k, sub_conj, i+1, suma_actual + nuevo_valor, mejor_sum, mejor_sub_conj)
        sub_conj.pop()

def maxi_subconjunto_con_poda(matriz, k, sub_conj, start, suma_actual, mejor_sum, mejor_sub_conj, valores_maximos):
    faltan = k - len(sub_conj)
    max_extra = sum(valores_maximos[:faltan*faltan])
    if suma_actual + max_extra <= mejor_sum[0]:
        return

    if len(sub_conj) == k:
        if suma_actual > mejor_sum[0]:
            mejor_sum[0] = suma_actual
            mejor_sub_conj[0] = sub_conj[:]
        return

    for i in range(start, len(matriz)):
        nuevo_valor = 0
        for j in sub_conj:
            nuevo_valor += matriz[i][j] + matriz[j][i]

        sub_conj.append(i)
        maxi_subconjunto_con_poda(matriz, k, sub_conj, i+1, suma_actual + nuevo_valor, mejor_sum, mejor_sub_conj, valores_maximos)
        sub_conj.pop()

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

# SIN PODA
mejor_sum_sin = [0]
mejor_subconj_sin = [[]]
start_time = time.time()
maxi_subconjunto_sin_poda(matriz, k, [], 0, 0, mejor_sum_sin, mejor_subconj_sin)
tiempo_sin = time.time() - start_time

# CON PODA
mejor_sum_con = [0]
mejor_subconj_con = [[]]
valores_maximos = calcular_valores_maximos(matriz)
start_time = time.time()
maxi_subconjunto_con_poda(matriz, k, [], 0, 0, mejor_sum_con, mejor_subconj_con, valores_maximos)
tiempo_con = time.time() - start_time


# ----------------- RESULTADOS ---------------------
print("\n----- Resultado SIN Poda -----")
print("Mejor subconjunto:", mejor_subconj_sin[0])
print("Suma máxima:", mejor_sum_sin[0])
print(f"Tiempo de ejecución: {tiempo_sin:.4f} segundos")

print("\n----- Resultado CON Poda -----")
print("Mejor subconjunto:", mejor_subconj_con[0])
print("Suma máxima:", mejor_sum_con[0])
print(f"Tiempo de ejecución: {tiempo_con:.4f} segundos")