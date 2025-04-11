def sum_fil(m, num_magico):
    
    for fila in m:
        if sum(fila) == num_magico:
            return True
        else:
            return False
    
def sum_col(m, num_magico):
    
    n = len(m)
    
    for col in range(n):
        suma = 0
        
        for fil in range(n):
            suma += m[fil][col]
        
        if suma != num_magico:
            return False
        
    return True    
    
def sum_diag(m, num_magico):

    n = len(m)
    
    diag1 = sum(m[i][i] for i in range(n))
    diag2 = sum(m[i][n-1-i] for i in range(n))
    
    return diag1==num_magico and diag2==num_magico

def es_magico(m, num_magico):
    
    if sum_fil(m, num_magico) and sum_col(m, num_magico) and sum_diag(m, num_magico):
        return True
    
    else:
        return False


def suma_parcial_fila(m, fil):
    return sum(m[fil])

def suma_parcial_col(m, col):
    return sum(m[i][col] for i in range(len(m)))

def cuadrado_magico(pos_actual, m, usados,n, num_magico):
    
    #Caso base
    if pos_actual==n**2:
        if es_magico(m, num_magico):
            print("Solución encontrada:")
            print(m) 
               
        return
    
    #Paso recursivo
    
    fil = pos_actual // n
    col = pos_actual % n
    
    for valor in range(1,n**2+1):
        if valor not in usados:
            m[fil][col] = valor
            usados.append(valor)
            
            #Podas
            if suma_parcial_fila(m, fil) > num_magico and suma_parcial_col(m, col) > num_magico:
                m[fil][col] = 0
                usados.pop()
                continue
            
            #Llamada recursiva
            cuadrado_magico(pos_actual+1, m, usados, n, num_magico)
            
            # Backtrack
            m[fil][col] = 0
            usados.pop()   
    
    
n = int(input('Ingrese el orden del cuadrado magico: '))
num_magico = ((n**3 + n)/2)
print('Su numero mágico será:',num_magico)
matriz = [[0 for _ in range(n)] for _ in range(n)]
usados = []

cuadrado_magico(0, matriz, usados,n, num_magico)