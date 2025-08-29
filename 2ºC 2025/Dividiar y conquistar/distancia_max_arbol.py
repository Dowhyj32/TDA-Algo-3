class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


def diam_y_altura(nodo):
    # Un árbol vacío tiene altura -1 y diámetro 0
    if nodo is None:
        return -1, 0
    
    # Obtener altura y diámetro del subárbol izquierdo
    alt_izq, diam_izq = diam_y_altura(nodo.izq)
    # Obtener altura y diámetro del subárbol derecho
    alt_der, diam_der = diam_y_altura(nodo.der)
    
    alt_actual = 1 + max(alt_izq, alt_der)
    
    # El diámetro puede estar:
    # - en el subárbol izquierdo
    # - en el subárbol derecho
    # - pasando por este nodo (izq + der + 2 aristas)
    
    diam_actual = max(diam_izq, diam_der, alt_izq+alt_der+2)
    
    return alt_actual, diam_actual

def diametro(arbol):
    _, d = diam_y_altura(arbol)
    return d

raiz = Nodo("A")
raiz.izq = Nodo("B")
raiz.der = Nodo("C")
raiz.izq.izq = Nodo("D")
raiz.izq.der = Nodo("E")

print("El diámetro del árbol es:", diametro(raiz))