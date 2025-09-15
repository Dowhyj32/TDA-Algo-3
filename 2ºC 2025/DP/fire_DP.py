from functools import lru_cache

NEGINF = float('-inf')

def fire(tiempos, vida, valor):
    articulos = sorted(zip(vida, tiempos, valor))
    d_list, t_list, p_list = map(list, zip(*articulos))
    d, t, p = tuple(d_list), tuple(t_list), tuple(p_list)
    D = max(d)
    n = len(t)
    
    llamadas = 0
    
    @lru_cache(maxsize=None)
    def F(i, T):
        nonlocal llamadas
        llamadas +=1
        
        if i==0:
            return 0 if T==0 else NEGINF
        
        di, ti, pi = d[i-1], t[i-1], p[i-1]
                
        # El artículo ya no vale la pena salvarlo
        if T>di:
            return F(i-1, t)
        
        mejor = F(i-1, T)
        
        if T >= ti:
            prev = F(i-1, T-ti)
            if prev!=NEGINF:
                mejor = max(mejor, prev + pi) 
        
        return mejor
    
    best = max(F(n, T) for T in range(D + 1))
    stats = {"cache_info": F.cache_info(), "llamadas_reales": llamadas}
    return best, stats

t = [3,2,3]
d = [7,6,7]
p = [4,5,6]


best, stats = fire(t, d, p)
print("Valor óptimo:", best)
print("Stats:", stats)