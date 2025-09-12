#El rey Cambyses está interesado en armar ejércitos en una serie de días consecutivos. Mas aun,
#le interesa que el número de personas de su ejército en el dia di sea equivalente a la suma del
#número de personas del ejército que formó el dia i − 1 e i − 2. La excepción para esto es en
#el día 0 y 1, en cuyo caso la cantidad de personas en esos días va a ser siempre 1. Para el es
#muy complicado determinar este número, entonces nos pidió que lo ayudemos. Dado un dia N,
#tenemos que devolver el número de personas de su ejército.
#Pensar un algoritmo O(N) para resolver este problema y demostrar su correctitud y complejidad

#Basicamente es calcular fibonacci

#Top Down (memorizacion)
def fibo(N, memo={}):
    
    if N in memo.keys():
        return memo[N]
    
    if N<=1:
        memo[N]=N
        return N
    
    else:
        memo[N] = fibo(N-1)+fibo(N-2)
        return memo[N]


N = int(input('Ingrese un numero de dia: '))
print(f'El dia {N} hay {fibo(N)} personas en el ejército')

    