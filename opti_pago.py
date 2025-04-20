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
print("Mejor conjunto de billetes usados:", mejor_usados)

