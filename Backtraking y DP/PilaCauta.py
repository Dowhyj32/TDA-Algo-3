w = [19,7,5,6,1]
s = [15,13,7,8,2]
N = len(w)


'''
def backtraking(i, peso_actual, soporte_actual):
    
    if i == N:
        return 0
    
    sin_i = backtraking(i+1, peso_actual, soporte_actual)
    
    con_i = 0
    if w[i] <= soporte_actual:
        nuevo_soporte = min(soporte_actual-w[i], s[i])
        con_i = 1 + backtraking(i+1, peso_actual + w[i], nuevo_soporte)
        
    return max(sin_i, con_i)

print(backtraking(0,0,float('inf')))'''

memo = {}

def pila_td(i, soporte, memo):
    
    if i == N:
        return (0, [])
    
    if (i, soporte) in memo:
        return memo[(i, soporte)]
    
    sin_i_valor, sin_i_cajas = pila_td(i+1, soporte, memo)
    
    con_i_valor = 0
    con_i_cajas = []
    
    if w[i]<soporte:
        nuevo_soporte = min(soporte-w[i], s[i])
        sig_valor, sig_cajas = pila_td(i+1, nuevo_soporte, memo)
        con_i_valor = 1 + sig_valor
        con_i_cajas = [i] + sig_cajas
        
    if con_i_valor > sin_i_valor:
        memo[(i,soporte)] = (con_i_valor, con_i_cajas)
    
    else:
        memo[(i,soporte)] = (sin_i_valor, sin_i_cajas)
        
    return memo[(i, soporte)]
    
res, cajas_usadas = pila_td(0, float('inf'), memo)

print(f"Máximo número de cajas: {res}")
print(f"Índices de cajas utilizadas: {cajas_usadas}")
print(f"Pesos de cajas utilizadas: {[w[i] for i in cajas_usadas]}")