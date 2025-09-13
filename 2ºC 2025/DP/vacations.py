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
'''
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
print(f"Minima cantd de dias de descanso={vacations(N,0,'DESC')}")'''

#Problema resuelto con DP

# Convención para la última actividad
DESC, GYM, COMPE = 0, 1, 2

def min_descansos_TD(gym, compe):
    N = len(gym)
    memo = [[-1]*3 for _ in range(N)]

    # Contadores
    stats = {
        "calls_total": 0,
        "memo_hits": 0,
        "states_computed": 0,
    }

    def dp(i, last):
        stats["calls_total"] += 1

        if i == N:
            return 0
        if memo[i][last] != -1:
            stats["memo_hits"] += 1
            return memo[i][last]

        stats["states_computed"] += 1

        # Opción: descansar
        best = 1 + dp(i + 1, DESC)

        # Opción: gimnasio (si está disponible y no repito)
        if gym[i] == 1 and last != GYM:
            best = min(best, dp(i + 1, GYM))

        # Opción: competencia (si está disponible y no repito)
        if compe[i] == 1 and last != COMPE:
            best = min(best, dp(i + 1, COMPE))

        memo[i][last] = best
        return best

    ans = dp(0, DESC)
    return ans, stats


def min_descansos_BU(gym, compe):
    N = len(gym)
    INF = 10**9

    # Stats
    stats = {
        "iterations": 0,
        "transitions_considered": 0,
        "states_updated": 0,
    }

    # Día -1: solo válido DESC = 0
    prev_desc, prev_gym, prev_compe = 0, INF, INF

    for i in range(N):
        stats["iterations"] += 1

        # DESC hoy
        cur_desc = min(prev_desc, prev_gym, prev_compe) + 1
        stats["transitions_considered"] += 1   # transición de descansar
        stats["states_updated"] += 1

        # GYM hoy
        if gym[i] == 1:
            cur_gym = min(prev_desc, prev_compe)
            stats["transitions_considered"] += 1
        else:
            cur_gym = INF
            stats["transitions_considered"] += 0  # no sumo: no se consideró transición real
        stats["states_updated"] += 1

        # COMPE hoy
        if compe[i] == 1:
            cur_compe = min(prev_desc, prev_gym)
            stats["transitions_considered"] += 1
        else:
            cur_compe = INF
        stats["states_updated"] += 1

        prev_desc, prev_gym, prev_compe = cur_desc, cur_gym, cur_compe

    ans = min(prev_desc, prev_gym, prev_compe)
    return ans, stats


gym  = [0,0,1,1]
compe= [1,1,0,0]

ans_td, st_td = min_descansos_TD(gym, compe)
ans_bu, st_bu = min_descansos_BU(gym, compe)

print("Top-Down -> ans:", ans_td, "| stats:", st_td)
print("Bottom-Up -> ans:", ans_bu, "| stats:", st_bu)
