'''
def ordenar(i, j):
    
    if cajones[j] == 0:
        return 
    
    
    if juguetes[i] <= cajones[j]:
        cajones[j] -= juguetes[i]
        juguetes[i].pop()
        ordenar(0, 0)
        
    else:
        return ordenar(i+1, j)
            
             
altura_cajon = int(input('Altura del cajón: '))
juguetes = [2,6,7,8,5,1,2,10,12,3,1,4]
cajones = [altura_cajon for _ in range(len(juguetes))]
cajones_usados = ordenar(0, 0)
print(f'Se guardó todo en un total de', )'''

def ordenar(i, juguetes, cajones):
    if i == len(juguetes):
        # Logré ubicar todos los juguetes
        return True

    for j in range(len(cajones)):
        if cajones[j] >= juguetes[i]:
            # Intento poner el juguete i en el cajón j
            cajones[j] -= juguetes[i]
            if ordenar(i + 1, juguetes, cajones):
                return True
            # Backtracking: deshago la elección
            cajones[j] += juguetes[i]

    return False


altura_cajon = int(input("Altura del cajón: "))
juguetes = [2, 6, 7, 8, 5, 1, 2, 10, 12, 3, 1, 4]
c = len(juguetes)  # Podés ajustar c si se permite usar menos cajones
cajones = [altura_cajon for _ in range(c)]

if ordenar(0, juguetes, cajones):
    print("Se pudo ordenar todos los juguetes")
else:
    print("No se pudo")
