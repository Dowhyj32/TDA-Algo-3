''' La programación dinámica (PD) es una técnica de diseño de algoritmos usada para resolver problemas que pueden dividirse en subproblemas más pequeños y solapados, aprovechando que estos se repiten.
En lugar de resolver el mismo subproblema varias veces (como hace la recursión simple), la PD guarda los resultados de los subproblemas ya resueltos y los reutiliza. 
Esto ahorra mucho tiempo y evita cálculos repetidos.'''

'''
El enfoque Top-Down:

- Comienza con el problema más grande y lo divide recursivamente en subproblemas.
- Usa memoización: se guarda el resultado de cada subproblema en una estructura auxiliar (como un diccionario o lista).
- Si un subproblema ya fue resuelto, se devuelve su resultado directamente en lugar de volver a calcularlo.

Se parece mucho a la recursión clásica, pero con memoria.
'''

'''
El enfoque Bottom-Up:

- Empieza resolviendo los subproblemas más pequeños de manera iterativa.
- Guarda los resultados en una estructura (por lo general una tabla).
- Con esos resultados, construye las soluciones a subproblemas más grandes hasta llegar al problema original.

No usa recursión, sino bucles.
'''


def fibonacci_td(n, memo):
        
    print(f"Calculando fibonacci_td({n})")
        
    if n<=1:
        return n
    
    if n in memo:
        print(f"Usando valor memoizado: memo[{n}] = {memo[n]}")
        return memo[n]
    
    memo[n] = fibonacci_td(n-1, memo) + fibonacci_td(n-2, memo)
    print(f"Guardando en memo[{n}]: {memo[n]}")
    return memo[n]

memo = {}
print('Resultado final:', fibonacci_td(5, memo))
print('Resultado final:', fibonacci_td(10, memo))
print('Resultado final:', fibonacci_td(15, memo))

# Complejidad temporal: O(n)
# Complejidad espacial: O(n)


def fibonacci_bu(n):
    
    if n<=1:
        return n
    
    fib = [0] * (n + 1)  # Crear lista para guardar resultados
    fib[0], fib[1] = 0, 1

    
    for i in range(2, n+1):
        fib[i] = fib[i - 1] + fib[i - 2]
        print(f"fib[{i}] = {fib[i]}")
    
    return fib[n]

print("Resultado final:", fibonacci_bu(10))

# Complejidad temporal: O(n)
# Complejidad espacial: O(n)