from functools import lru_cache
INF = float('inf')

def cc_DP(B, i, c):
    llamadas = 0
    B = tuple(B)  # inmutable para seguridad de cache
    @lru_cache(maxsize=None)
    def f(i, c):
        nonlocal llamadas
        llamadas += 1       # se incrementa solo en MISS (en hits no se ejecuta)
        if c <= 0:        return (0, 0)
        if i < 0:         return (INF, INF)
        p_no, q_no = f(i-1, c)
        p_t,  q_t  = f(i-1, c - B[i]); tomar = (p_t + B[i], q_t + 1)
        return min(tomar, (p_no, q_no))
    res = f(i, c)
    info = f.cache_info()   # hits, misses, etc.
    return res, llamadas, (info.hits, info.misses)

B = [2, 3, 5, 10, 20, 20]
i_ult = len(B) - 1
c = int(input('Costo del prod: '))
(res_dp, calls_dp, (hits, misses)) = cc_DP(B, i_ult, c)
print("DP  ->", res_dp, "llamadas (misses):", calls_dp, "cache hits:", hits)