w = [19,7,5,6,1]
s = [15,13,7,8,2]
N = len(w)



def backtraking(i, peso_actual, soporte_actual):
    
    if i == N:
        return 0
    
    sin_i = backtraking(i+1, peso_actual, soporte_actual)
    
    con_i = 0
    if w[i] <= soporte_actual:
        nuevo_soporte = min(soporte_actual-w[i], s[i])
        con_i = 1 + backtraking(i+1, peso_actual + w[i], nuevo_soporte)
        
    return max(sin_i, con_i)

print(backtraking(0,0,float('inf')))