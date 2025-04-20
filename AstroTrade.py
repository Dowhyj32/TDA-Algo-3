memo = {}

def at(P, j, c, memo):
    
    if (j,c) in memo:
        return memo[(j,c)]
    
    if j == 0 and c == 0:
        return (0, [])
    
    if c < 0 or c > j:
        return (float('-inf'), [])
    
    # Acciones posibles:
    # 1. Comprar
    ganancia_compra, camino_compra = at(P, j-1, c-1, memo)
    ganancia_compra -= P[j-1]
    camino_compra = camino_compra + [(j-1, "compra", P[j-1])]

    # 2. Vender
    ganancia_venta, camino_venta = at(P, j-1, c+1, memo)
    ganancia_venta += P[j-1]
    camino_venta = camino_venta + [(j-1, "venta", P[j-1])]

    # 3. Nada
    ganancia_nada, camino_nada = at(P, j-1, c, memo)
    camino_nada = camino_nada + [(j-1, "nada", P[j-1])]

    # Elegimos la mejor acción
    opciones = [
        (ganancia_compra, camino_compra),
        (ganancia_venta, camino_venta),
        (ganancia_nada, camino_nada)
    ]
    mejor_opcion = max(opciones, key=lambda x: x[0])
    memo[(j, c)] = mejor_opcion
    return mejor_opcion

# Ejemplo 1
P = [3, 6, 10]
memo = {}
ganancia, camino = at(P, len(P), 0, memo)

print("Ganancia máxima:", ganancia)
print("Camino de decisiones:")
for dia, accion, precio in camino:
    print(f"Día {dia+1}: {accion} a ${precio}")


# Ejemplo 2
P = [5, 1, 3, 7, 4]
memo = {}
ganancia, camino = at(P, len(P), 0, memo)

print("Ganancia máxima:", ganancia)
print("Camino de decisiones:")
for dia, accion, precio in camino:
    print(f"Día {dia+1}: {accion} a ${precio}")


# Ejemplo 3
P = [10, 8, 5, 6, 9]
memo = {}
ganancia, camino = at(P, len(P), 0, memo)

print("Ganancia máxima:", ganancia)
print("Camino de decisiones:")
for dia, accion, precio in camino:
    print(f"Día {dia+1}: {accion} a ${precio}")
