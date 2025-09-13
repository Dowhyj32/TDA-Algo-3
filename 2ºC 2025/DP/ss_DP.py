def ss_DP(C, i, k, memo):

    #Caso base: logré la suma
    if k==0:
        return True
    
    #Sin elementos o me pasé
    if i<0 or k<0:
        return False
    
    if memo[i][k] != -1:
        return memo[i][k] == 1

    # Transiciones: tomar o no tomar C[i]
    tomar = False
    if C[i] <= k:                           # pequeña poda: sólo si no me paso
        tomar = ss_DP(C, i-1, k - C[i], memo)

    if tomar:
        memo[i][k] = 1
        return True

    no_tomar = ss_DP(C, i-1, k, memo)
    memo[i][k] = 1 if no_tomar else 0
    return no_tomar

C = [6,12,6]
n = len(C)
k = int(input('Ingrese un número natural:  '))
memo = [[-1]*(k+1) for _ in range(n)]
print(f'¿Es posible sumar {k} con el multiconjunto {C}?  {ss_DP(C,len(C)-1,k,memo)}')