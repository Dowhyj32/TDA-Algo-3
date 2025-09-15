from functools import lru_cache

INF = float('-inf')

def asteroides_TD(Asteroides):
    n = len(Asteroides)
    
    @lru_cache(maxsize=None)
    def f(a, d):
        
        #CB
        if d==0:
            return 0 if a==0 else INF
        
        #Casos inválidos
        if a<0 or a>d:
            return INF
        
        #Paso recursivo
        comprar = f(a-1, d-1) - Asteroides[d-1]
        vender = f(a+1, d-1) + Asteroides[d-1]
        no_operar = f(a, d-1)
        
        return max(comprar, vender, no_operar)
    
    return f(0, n)

a1 = [3, 6, 10]
a2 = [3, 2, 5, 6]
print(f'MGN de {a1} = {asteroides_TD(a1)}')
print(f'MGN de {a2} = {asteroides_TD(a2)}')

def asteroides_BU(Asteroides): 
    n = len(Asteroides)
    
    dp = [[INF]*(n+1) for _ in range(n+1)]
    dp[0][0] = 0 # 0 días, 0 asteroides -> mgn 0
    
    for d in range(1, n+1):
        precio = Asteroides[d-1]
        
        for a in range(0, d+1):     # a<=d
            mejor = dp[a][d-1]      # NO operar
            
            if a-1>=0:               # Comprar
                mejor = max(mejor, dp[a-1][d-1] - precio)
                
            if a+1<=d-1:            # Vender
                mejor = max(mejor, dp[a+1][d-1] + precio)
                
            dp[a][d] = mejor
    
    return dp[0][n]

a1 = [3, 6, 10]
a2 = [3, 2, 5, 6]
print(f'MGN de {a1} = {asteroides_BU(a1)}')
print(f'MGN de {a2} = {asteroides_BU(a2)}')