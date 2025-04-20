'''
mejor_exceso = float('inf')
mejor_usados = []

# Complejidad temporal: O(2^n)
# Complejidad espacial: O(n)

def opti_pago(i, B, c, suma, usados):
    global mejor_exceso, mejor_usados
    
    # Caso base
    if suma >= c:
        exceso = suma - c
        
        if (exceso < mejor_exceso) or (exceso == mejor_exceso and len(usados) < len(mejor_usados)):
            mejor_exceso = exceso
            mejor_usados = usados[:]
        
        return     

    if i >= len(B):
        return
    
    # Uso el billete en la posisción 'i'
    if usados.count(B[i]) < B.count(B[i]):
        usados.append(B[i])
        opti_pago(i+1, B, c, suma + B[i], usados)
        usados.pop()
    
    # No uso el billete en la posisición 'i'
    opti_pago(i+1, B, c, suma, usados)
    
    
billetes = [2, 3, 5, 10, 20]
costo = 14
suma = 0
usados = []
i = 0

opti_pago(i, billetes, costo, suma, usados)
print("Mejor exceso:", mejor_exceso)
print("Mejor conjunto de billetes usados:", mejor_usados)'''

# Funcion mas sencilla
'''
def cc(B, i, j):
    if j <= 0:
        return (0, 0)
    if i == 0:
        return (float('inf'), float('inf'))

    sin_bn = cc(B, i-1, j)
    con_bn = cc(B, i-1, j - B[i-1])
    con_bn = (con_bn[0] + B[i-1], con_bn[1] + 1)

    return min(sin_bn, con_bn)  # usando orden lexicográfico

B = [2, 3, 5, 10, 20]
costo = 14
resultado = cc(B, len(B), costo)
print("Pago mínimo posible:", resultado[0])
print("Cantidad mínima de billetes usados:", resultado[1])
'''

# Agrego memoización

memo = {}

def cc_prima(B, i, j, memo):
    if (i,j) in memo:
        print(f"Ya resuelto: ({i}, {j}) → {memo[(i, j)]}")
        return memo[(i,j)]
    
    print(f"Resolviendo: ({i}, {j})")
    
    if j <= 0:
        return (0,0)
    
    if i == 0:
        return (float('inf'), float('inf'))
    
    
    
    sin_bn = cc_prima(B, i-1, j, memo)
    con_bn = cc_prima(B, i-1, j-B[i-1], memo)
    con_bn = (con_bn[0]+B[i-1], con_bn[1]+1)
    
    memo[(i,j)] = min(sin_bn, con_bn)
    
    return memo[(i,j)]


B = [2, 3, 5]
costo = 7
memo = {}
print("\nEjemplo 1:")
print("Resultado:", cc_prima(B, len(B), costo, memo))


B = [1, 1, 1, 5]
costo = 6
memo = {}
print("\nEjemplo 2:")
print("Resultado:", cc_prima(B, len(B), costo, memo))

B = [4, 4, 4, 10]
costo = 8
memo = {}
print("\nEjemplo 3:")
print("Resultado:", cc_prima(B, len(B), costo, memo))

B = [5, 10, 20]
costo = 14
memo = {}
print("\nEjemplo 4:")
print("Resultado:", cc_prima(B, len(B), costo, memo))

B = [1, 2, 5, 10, 20]
costo = 23
memo = {}
print("\nEjemplo 5:")
print("Resultado:", cc_prima(B, len(B), costo, memo))


