from itertools import permutations
from typing import List, Tuple

# ---------- Utilidades comunes ----------

def magic_number(n: int) -> int:
    # M = n(n^2+1)/2
    return n * (n*n + 1) // 2

def is_magic(mat: List[List[int]], M: int) -> bool:
    n = len(mat)
    # Filas
    for i in range(n):
        if sum(mat[i]) != M:
            return False
    # Columnas
    for j in range(n):
        if sum(mat[i][j] for i in range(n)) != M:
            return False
    # Diagonales
    if sum(mat[i][i] for i in range(n)) != M:
        return False
    if sum(mat[i][n-1-i] for i in range(n)) != M:
        return False
    return True

def pretty(mat: List[List[int]]) -> str:
    return "\n".join(" ".join(f"{x:2d}" for x in row) for row in mat)

# ---------- 1) Fuerza bruta (permutaciones) ----------

def magic_bruteforce(n: int) -> Tuple[List[List[List[int]]], int, int]:
    """
    Genera todas las permutaciones de 1..n^2 y chequea is_magic.
    Devuelve (soluciones, calls_total, full_mats_checked).
    Para fuerza bruta: calls_total == full_mats_checked == (n^2)!.
    """
    nums = list(range(1, n*n + 1))
    M = magic_number(n)
    calls_total = 0
    full_mats_checked = 0
    solutions = []

    for p in permutations(nums):
        calls_total += 1
        full_mats_checked += 1
        mat = [list(p[i*n:(i+1)*n]) for i in range(n)]
        if is_magic(mat, M):
            solutions.append([row[:] for row in mat])

    return solutions, calls_total, full_mats_checked

# ---------- 2) Backtracking con podas ----------

def magic_backtracking_pruned(n: int) -> Tuple[List[List[List[int]]], int, int]:
    """
    Podas:
      - cortar si suma parcial de fila/col/diag supera M
      - al completar una fila/col, exigir suma == M
      - al completar la diagonal principal/secundaria, exigir suma == M
    Devuelve (soluciones, calls_total, full_mats_checked).
    """
    M = magic_number(n)
    mat = [[0]*n for _ in range(n)]
    used = [False] * (n*n + 1)
    row_sum = [0]*n
    col_sum = [0]*n
    diag1 = 0  # i==j
    diag2 = 0  # i+j==n-1

    solutions = []
    calls_total = 0
    full_mats_checked = 0

    def place(pos: int):
        nonlocal diag1, diag2, calls_total, full_mats_checked
        calls_total += 1

        if pos == n*n:
            # matriz completa: verifico diagonales por seguridad
            full_mats_checked += 1
            if diag1 == M and diag2 == M:
                solutions.append([row[:] for row in mat])
            return

        r, c = divmod(pos, n)

        for v in range(1, n*n + 1):
            if used[v]:
                continue

            # Sumas parciales con v
            new_row = row_sum[r] + v
            new_col = col_sum[c] + v
            if new_row > M or new_col > M:
                continue

            inc_d1 = (r == c)
            inc_d2 = (r + c == n - 1)
            new_d1 = diag1 + (v if inc_d1 else 0)
            new_d2 = diag2 + (v if inc_d2 else 0)
            if new_d1 > M or new_d2 > M:
                continue

            # Colocar
            used[v] = True
            mat[r][c] = v
            prev_r, prev_c, prev_d1, prev_d2 = row_sum[r], col_sum[c], diag1, diag2
            row_sum[r], col_sum[c] = new_row, new_col
            if inc_d1: diag1 = new_d1
            if inc_d2: diag2 = new_d2

            # Chequeos “al completar”
            ok = True
            if c == n-1 and row_sum[r] != M:        # fila completa
                ok = False
            if ok and r == n-1 and col_sum[c] != M: # columna completa
                ok = False
            if ok and r == n-1 and c == n-1 and diag1 != M:  # diag principal completa
                ok = False
            if ok and r == n-1 and c == 0 and diag2 != M:    # diag secundaria completa
                ok = False

            if ok:
                place(pos + 1)

            # Deshacer
            row_sum[r], col_sum[c], diag1, diag2 = prev_r, prev_c, prev_d1, prev_d2
            mat[r][c] = 0
            used[v] = False

    place(0)
    return solutions, calls_total, full_mats_checked

# ---------- Demo mínima ----------

if __name__ == "__main__":
    n = 3  # bruta solo razonable para n=3
    M = magic_number(n)
    print(f"n={n}, número mágico M={M}\n")

    sols_bf, calls_bf, full_bf = magic_bruteforce(n)
    print(f"[Fuerza bruta] soluciones={len(sols_bf)}  calls_total={calls_bf}  full_mats_checked={full_bf}")

    sols_pr, calls_pr, full_pr = magic_backtracking_pruned(n)
    print(f"[BT con podas] soluciones={len(sols_pr)}  calls_total={calls_pr}  full_mats_checked={full_pr}")

    if sols_pr:
        print("\nEjemplo de solución (BT con podas):\n")
        print(pretty(sols_pr[0]))
