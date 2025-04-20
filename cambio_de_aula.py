
def cambio_de_aula(mapa):
    
    n = len(mapa)
    m = len(mapa[0])
    
    celdas_a_recorrer = n + m - 1
    
    if celdas_a_recorrer%2 != 0:
        return print('NO')
    
    dp = [[(float('inf'), float('-inf')) for _ in range(m)] for _ in range(n)]
    dp[0][0] = (mapa[0][0], mapa[0][0])
    
    for i in range(0,n):
        for j in range(0,m):
            if i==0 and j==0:
                continue

            min_val = float('inf')
            max_val = float('inf')
            
            # Si puedo venir desde arriba
            if i > 0:
                ant_min, ant_max = dp[i-1][j]
                min_val = min(min_val, ant_min + mapa[i][j])
                max_val = max(max_val, ant_max + mapa[i][j])

            # Si puedo venir desde la izquierda
            if j > 0:
                ant_min, ant_max = dp[i][j-1]
                min_val = min(min_val, ant_min + mapa[i][j])
                max_val = max(max_val, ant_max + mapa[i][j])
                
            dp[i][j] = (min_val, max_val)
            
    final_min, final_max = dp[n-1][m-1]
    
    if final_min <= 0 <= final_max:
        print('YES')
    else:
        print('NO')
            
            
mapa = [[1,-1,-1,-1],[-1,1,1,-1],[1,1,1,-1]]
cambio_de_aula(mapa)

mapa2 = [[1,1]]
cambio_de_aula(mapa2)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    mapa = [list(map(int, input().split())) for _ in range(n)]

    total_celdas = n + m - 1
    if total_celdas % 2 != 0:
        print("NO")
        continue

    dp = [[set() for _ in range(m)] for _ in range(n)]
    dp[0][0].add(mapa[0][0])

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            posibles_sumas = set()
            if i > 0:
                for s in dp[i - 1][j]:
                    posibles_sumas.add(s + mapa[i][j])
            if j > 0:
                for s in dp[i][j - 1]:
                    posibles_sumas.add(s + mapa[i][j])
            dp[i][j] = posibles_sumas

    print("YES" if 0 in dp[n - 1][m - 1] else "NO")



