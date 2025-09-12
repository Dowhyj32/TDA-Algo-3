#Tomas tiene N días de vacaciones, donde puede hacer actividades:
#Se pueden hacer 2 actividades: gimnasio y competencias.
#Cada día puede tener disponible ninguna, alguna o ambas.
#Tomas cada dia puede
#Hacer una actividad que este disponible, siempre que no la haya hecho el día anterior
#Descansar.
#Tomas quiere minimizar los días de descanso.
#a) Diseñar un algoritmo O(N) que calcule la mínima cantidad de días de descanso.
#b) Probar la correctitud y complejidad del algoritmo.
#c) Indicar cómo se puede reconstruir la solución. Es decir, indicarle a Tomas qué hara cada
#día.
#Ayuda: Consideren el siguiente ejemplo:
#N = 4
#Días con gimnasio disponible: 2, 3
#Días con competencias disponibles: 1, 2
#Puede lograr tener solo 2 días de descanso.

#Descansar = ninguna actividad ese día


#Problema resuelto sin DP

def puedeGym(d):
    gym = [0,0,1,1]
    return gym[d] == 1

def puedeCompe(d):
    compe = [1,1,0,0]
    return compe[d] == 1

def vacations(N, d_actual, actv_ayer):
    # Caso base: no quedan días
    if d_actual == N:
        return 0

    # Opción 1: descansar
    mejor = 1 + vacations(N, d_actual + 1, 'DESC')

    # Opción 2: ir al gym si se puede y no se repite
    if puedeGym(d_actual) and actv_ayer != 'GYM':
        mejor = min(mejor, vacations(N, d_actual + 1, 'GYM'))

    # Opción 3: competir si se puede y no se repite
    if puedeCompe(d_actual) and actv_ayer != 'COMPE':
        mejor = min(mejor, vacations(N, d_actual + 1, 'COMPE'))

    return mejor

N = 4
print(f"Minima cantd de dias de descanso={vacations(N,0,'DESC')}")

#Problema resuelto con DP

# Convención para la última actividad
DESC, GYM, COMPE = 0, 1, 2

def min_descansos(gym, compe):
    N = len(gym)
    memo = [[-1]*3 for _ in range(N)]  # memo[i][last] = mínimo #descansos desde i si ayer fue 'last'

    def dp(i, last):
        if i == N:
            return 0
        if memo[i][last] != -1:
            return memo[i][last]

        # Opción: descansar hoy
        best = 1 + dp(i + 1, DESC)

        # Opción: gimnasio (si está disponible y no repito)
        if gym[i] == 1 and last != GYM:
            best = min(best, dp(i + 1, GYM))

        # Opción: competencia (si está disponible y no repito)
        if compe[i] == 1 and last != COMPE:
            best = min(best, dp(i + 1, COMPE))

        memo[i][last] = best
        return best

    return dp(0, DESC)