# Greedy / deadlines.py

from typing import List, Tuple, Dict

def schedule_deadlines(D: List[int], start_time: int = 0
                      ) -> Tuple[int, List[int], List[Dict[str, int]]]:
    """
    Planifica para maximizar la cantidad de tareas completadas a tiempo.
    Todas las tareas duran 1 y están disponibles desde t=start_time.

    Parámetros
    ----------
    D : lista de int
        D[i] es el deadline (entero > 0) de la tarea i (0-indexada en D).
    start_time : int
        Instante inicial (por defecto 0).

    Retorna
    -------
    count : int
        Máximo número de tareas que pueden completarse en tiempo.
    order : List[int]
        Índices de las tareas (1-indexados para imprimir más cómodo) en el
        orden en que se ejecutan.
    plan : List[Dict[str,int]]
        Lista con dicts: {'task', 'deadline', 'start', 'finish'}.
    """
    n = len(D)
    # Ordenamos por deadline no decreciente. Guardamos (deadline, idx1based)
    tasks = sorted(((d, i+1) for i, d in enumerate(D)), key=lambda x: x[0])

    t = start_time
    order: List[int] = []
    plan: List[Dict[str, int]] = []

    for d, idx in tasks:
        # ¿Aún hay un slot libre antes de su deadline?
        if t < d:
            plan.append({'task': idx, 'deadline': d, 'start': t, 'finish': t+1})
            order.append(idx)
            t += 1           # ocupamos el siguiente slot
        # si t >= d, ya no llega: la descartamos

    return len(order), order, plan


# --- Ejemplos de uso ---
if __name__ == "__main__":
    T1 = [2, 1, 3, 2]           # ejemplo del enunciado
    c1, o1, p1 = schedule_deadlines(T1)
    print(f"T1 -> completadas: {c1}, orden: {o1}")
    

    T2 = [2, 4, 6, 1, 3, 4, 5, 2, 1, 5, 7, 9]
    c2, o2, p2 = schedule_deadlines(T2)
    print(f"\nT2 -> completadas: {c2}, orden: {o2}")
