#SumaSubconjBT SIN PODA
def ss_BT(C, i, k):

    #La suma se puede lograr
    if k==0:
        return True
    
    #No tengo mas elementos que agregar o me pasé de la suma.
    elif i<0 or k<0:
        return False

    return ss_BT(C, i-1, k-C[i]) or ss_BT(C, i-1, k)

C = [6,12,6,2]
k = int(input('Ingrese un número natural:  '))
print(f'¿Es posible sumar {k} con el multiconjunto {C}?  {ss_BT(C,len(C)-1,k)}')


#SumaSubconj CON PODA

def ss_BT_Poda(C, i, k):

    #La suma se puede lograr
    if k==0:
        return True
    
    #No tengo mas elementos que agregar o me pasé de la suma.
    elif i<0 or k<0:
        return False
    
    agrego = False
    if C[i] <= k:  # poda: si tomar C[i] se pasa, ni lo intento
        agrego = ss_BT_Poda(C, i-1, k - C[i])
        if agrego:           # cortocircuito útil
            return True

    no_agrego = ss_BT_Poda(C, i-1, k)
    return no_agrego
    

C = [6,12,6]
k = int(input('Ingrese un número natural:  '))
print(f'¿Es posible sumar {k} con el multiconjunto {C}?  {ss_BT(C,len(C)-1,k)}')