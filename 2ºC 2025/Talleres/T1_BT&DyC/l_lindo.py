def main(n, S):
    return l_lindo(S, 0, n-1, 'a')

def l_lindo(S, izq, der, letra):
    
    #CB
    if izq==der:
        if S[izq]==letra:
            return 0
        else:
            return 1
    
    mitad = (izq+der)//2
    
    #Cuento cuantos caracteres NO son letra en cada mitad
    noIgualesIzq = contarNoIguales(S, izq, mitad, letra)
    noIgualesDer = contarNoIguales(S, mitad+1, der, letra)
    
    #La izquierda ya tiene todo letra y quiero hacer derecha l-linda
    costo1 = noIgualesIzq + l_lindo(S, mitad+1, der, letraSiguiente(letra))
    
    #La derecha ya tiene todo letra y quiero hacer izquierda l-linda
    costo2 = noIgualesDer + l_lindo(S, izq, mitad, letraSiguiente(letra))
    
    return min(costo1, costo2)

def contarNoIguales(S, i, j, letra):
    total = 0
    for l in range(i,j+1):
        if S[l]!=letra:
            total+=1
    return total

def letraSiguiente(l):
    return chr(ord(l)+1)


pruebas = [[8,'aaaadcbb'],[8,'bbaaceaa'],[8,'jkghasdf'],[1,'x'],[2,'da'],[8,'ccddaabb']]
  
for i in range(len(pruebas)):
    print(f"Se necesitan {main(pruebas[i][0], pruebas[i][1])} movimientos para que {pruebas[i][1]} sea a-lindo")