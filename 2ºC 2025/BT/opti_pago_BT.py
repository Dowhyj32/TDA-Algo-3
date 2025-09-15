from functools import lru_cache

INF = float('inf')

def cc_FB(B, i, c):
    llamadas = 0
    def f(i, c):
        nonlocal llamadas
        llamadas += 1
        if c <= 0:        return (0, 0)
        if i < 0:         return (INF, INF)
        p_no, q_no = f(i-1, c)
        p_t,  q_t  = f(i-1, c - B[i]); tomar = (p_t + B[i], q_t + 1)
        return min(tomar, (p_no, q_no))
    res = f(i, c)
    return res, llamadas

def cc_BT(B, i, c):
    llamadas = 0
    # pref[i] = suma(B[0..i])
    pref, s = [0]*len(B), 0
    for t, v in enumerate(B):
        s += v; pref[t] = s
    def suma_rest(i): return pref[i] if i >= 0 else 0

    def f(i, c):
        nonlocal llamadas
        llamadas += 1
        if c <= 0:        return (0, 0)
        if i < 0:         return (INF, INF)
        if c > suma_rest(i):   # poda
            return (INF, INF)
        p_no, q_no = f(i-1, c)
        p_t,  q_t  = f(i-1, c - B[i]); tomar = (p_t + B[i], q_t + 1)
        return min(tomar, (p_no, q_no))
    res = f(i, c)
    return res, llamadas
    
    
B = [2, 3, 5, 10, 20, 20]
i_ult = len(B) - 1
c = int(input('Costo del prod: '))

(res_fb, calls_fb) = cc_FB(B, i_ult, c)
(res_bt, calls_bt) = cc_BT(B, i_ult, c)

print("FB  ->", res_fb, "llamadas:", calls_fb)
print("BT  ->", res_bt, "llamadas:", calls_bt)